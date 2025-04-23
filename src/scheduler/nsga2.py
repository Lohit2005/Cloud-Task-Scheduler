import random
import numpy as np
from typing import List
from .models import Task, VM, Individual

def evaluate_individual(ind: Individual, tasks: List[Task], vms: List[VM]):
    """Evaluates a single individual by computing three objectives."""
    n_vms = len(vms)
    vm_loads = [0.0] * n_vms
    vm_costs = [0.0] * n_vms
    vm_req_load = [0.0] * n_vms
    vm_capacities = [vm.cpu_cap + vm.ram_cap + vm.bw_cap for vm in vms]
    for task_idx, vm_idx in enumerate(ind.schedule):
        task = tasks[task_idx]
        vm = vms[vm_idx]
        vm_loads[vm_idx] += task.length
        vm_costs[vm_idx] += vm.cost * task.length
        vm_req_load[vm_idx] += (task.cpu_req + task.ram_req + task.bw_req)
    makespan = max(vm_loads)
    total_cost = sum(vm_costs)
    ratios = []
    for i in range(n_vms):
        ratio = vm_req_load[i] / vm_capacities[i] if vm_capacities[i] > 0 else 0
        ratios.append(ratio)
    load_balance = np.std(ratios)
    ind.objs = (makespan, total_cost, load_balance)

def dominates(ind1: Individual, ind2: Individual):
    """Check if ind1 dominates ind2."""
    better_in_all = True
    better_in_at_least_one = False
    for a, b in zip(ind1.objs, ind2.objs):
        if a > b:
            better_in_all = False
            break
        elif a < b:
            better_in_at_least_one = True
    return better_in_all and better_in_at_least_one

def fast_non_dominated_sort(population: List[Individual]):
    """Fast non-dominated sorting partitions the population into different Pareto fronts."""
    S = {}
    n = {}
    fronts = [[]]
    for p in population:
        S[p] = []
        n[p] = 0
        for q in population:
            if p is q:
                continue
            if dominates(p, q):
                S[p].append(q)
            elif dominates(q, p):
                n[p] += 1
        if n[p] == 0:
            p.rank = 0
            fronts[0].append(p)
    i = 0
    while fronts[i]:
        next_front = []
        for p in fronts[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    q.rank = i + 1
                    next_front.append(q)
        i += 1
        fronts.append(next_front)
    fronts.pop()
    return fronts

def crowding_distance_assignment(front: List[Individual]):
    """Computes the crowding distance for all individuals in a front."""
    l = len(front)
    if l == 0:
        return
    for ind in front:
        ind.crowding_distance = 0
    num_obj = len(front[0].objs)
    for m in range(num_obj):
        front.sort(key=lambda ind: ind.objs[m])
        front[0].crowding_distance = float('inf')
        front[-1].crowding_distance = float('inf')
        m_values = [ind.objs[m] for ind in front]
        m_min = min(m_values)
        m_max = max(m_values)
        if m_max == m_min:
            continue
        for i in range(1, l-1):
            front[i].crowding_distance += (front[i+1].objs[m] - front[i-1].objs[m]) / (m_max - m_min)

def tournament_selection(population: List[Individual], k=2):
    """Performs binary tournament selection."""
    candidates = random.sample(population, k)
    candidates.sort(key=lambda ind: (ind.rank, -ind.crowding_distance))
    return candidates[0]

def crossover(parent1: Individual, parent2: Individual, crossover_prob: float):
    """Performs a single-point crossover on the schedule of two parents."""
    child1 = parent1.copy()
    child2 = parent2.copy()
    if random.random() < crossover_prob:
        point = random.randint(1, len(parent1.schedule) - 1)
        child1.schedule = parent1.schedule[:point] + parent2.schedule[point:]
        child2.schedule = parent2.schedule[:point] + parent1.schedule[point:]
    return child1, child2

def mutation(individual: Individual, num_vms: int, mutation_prob: float):
    """Mutates an individual by randomly reassigning a task to a different VM."""
    for i in range(len(individual.schedule)):
        if random.random() < mutation_prob:
            individual.schedule[i] = random.randint(0, num_vms - 1)
    return individual

def create_initial_population(pop_size: int, num_tasks: int, num_vms: int):
    """Generates an initial population."""
    population = []
    for _ in range(pop_size):
        schedule = [random.randint(0, num_vms - 1) for _ in range(num_tasks)]
        individual = Individual(schedule)
        population.append(individual)
    return population

def nsga2(tasks, vms, pop_size=100, generations=100, crossover_prob=0.9, mutation_prob=0.1):
    num_tasks = len(tasks)
    num_vms = len(vms)
    population = create_initial_population(pop_size, num_tasks, num_vms)
    for ind in population:
        evaluate_individual(ind, tasks, vms)
    for gen in range(generations):
        if gen % 10 == 0:
            print(f"Generation {gen}")
        offspring = []
        while len(offspring) < pop_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2, crossover_prob)
            child1 = mutation(child1, num_vms, mutation_prob)
            child2 = mutation(child2, num_vms, mutation_prob)
            evaluate_individual(child1, tasks, vms)
            evaluate_individual(child2, tasks, vms)
            offspring.append(child1)
            if len(offspring) < pop_size:
                offspring.append(child2)
        combined_population = population + offspring
        fronts = fast_non_dominated_sort(combined_population)
        new_population = []
        for front in fronts:
            crowding_distance_assignment(front)
            if len(new_population) + len(front) <= pop_size:
                new_population.extend(front)
            else:
                front.sort(key=lambda ind: -ind.crowding_distance)
                remaining = pop_size - len(new_population)
                new_population.extend(front[:remaining])
                break
        population = new_population
    return population

def extract_pareto_front(population):
    """Returns the first Pareto front from the final population."""
    fronts = fast_non_dominated_sort(population)
    return fronts[0]
