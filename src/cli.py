import random
import numpy as np
from scheduler.models import Task, VM
from scheduler.nsga2 import nsga2, extract_pareto_front
from scheduler.visualization import plot_pareto_front

def get_int(prompt, default=None, minval=None, maxval=None):
    while True:
        s = input(f"{prompt} [{default if default is not None else ''}]: ")
        if not s and default is not None:
            return default
        try:
            val = int(s)
            if minval is not None and val < minval:
                print(f"Value must be at least {minval}")
                continue
            if maxval is not None and val > maxval:
                print(f"Value must be at most {maxval}")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float(prompt, default=None, minval=None, maxval=None):
    while True:
        s = input(f"{prompt} [{default if default is not None else ''}]: ")
        if not s and default is not None:
            return default
        try:
            val = float(s)
            if minval is not None and val < minval:
                print(f"Value must be at least {minval}")
                continue
            if maxval is not None and val > maxval:
                print(f"Value must be at most {maxval}")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_tasks(num_tasks):
    print("\n--- Task Configuration ---")
    tasks = []
    for i in range(num_tasks):
        print(f"\nEnter details for Task {i+1}:")
        length = get_int("  Workload (length, 100-1000)", default=random.randint(100,1000), minval=1)
        filesize = get_int("  File size (50-200)", default=random.randint(50,200), minval=1)
        outputsize = get_int("  Output size (20-100)", default=random.randint(20,100), minval=1)
        cpu_req = get_int("  CPU requirement (1-4)", default=random.randint(1,4), minval=1)
        ram_req = get_int("  RAM requirement (1-4)", default=random.randint(1,4), minval=1)
        bw_req = get_int("  Bandwidth requirement (1-4)", default=random.randint(1,4), minval=1)
        tasks.append(Task(i, length, filesize, outputsize, cpu_req, ram_req, bw_req))
    return tasks

def input_vms(num_vms):
    print("\n--- VM Configuration ---")
    vms = []
    for j in range(num_vms):
        print(f"\nEnter details for VM {j+1}:")
        cpu_cap = get_int("  CPU capacity (4-16)", default=random.randint(4,16), minval=1)
        ram_cap = get_int("  RAM capacity (4-16)", default=random.randint(4,16), minval=1)
        bw_cap = get_int("  Bandwidth capacity (100-500)", default=random.randint(100,500), minval=1)
        storage = get_int("  Storage (1024-20480)", default=random.randint(1024,20480), minval=1)
        cost = get_float("  Cost per unit (0.001-0.01)", default=round(random.uniform(0.001,0.01),4), minval=0)
        vms.append(VM(j, cpu_cap, ram_cap, bw_cap, storage, cost))
    return vms

def input_algorithm_params():
    print("\n--- Algorithm Parameters ---")
    pop_size = get_int("Population size", default=100, minval=2)
    generations = get_int("Number of generations", default=100, minval=1)
    crossover_prob = get_float("Crossover probability (0.0-1.0)", default=0.9, minval=0.0, maxval=1.0)
    mutation_prob = get_float("Mutation probability (0.0-1.0)", default=0.1, minval=0.0, maxval=1.0)
    return pop_size, generations, crossover_prob, mutation_prob

def main():
    random.seed(42)
    np.random.seed(42)
    print("=== Cloud Task Scheduling with NSGA-II ===")
    num_tasks = get_int("Enter number of tasks", default=10, minval=1)
    num_vms = get_int("Enter number of VMs", default=5, minval=1)
    tasks = input_tasks(num_tasks)
    vms = input_vms(num_vms)
    pop_size, generations, crossover_prob, mutation_prob = input_algorithm_params()
    print("\nScheduling tasks using NSGA-II. Please wait...\n")
    final_population = nsga2(
        tasks, vms,
        pop_size=pop_size,
        generations=generations,
        crossover_prob=crossover_prob,
        mutation_prob=mutation_prob
    )
    pareto_front = extract_pareto_front(final_population)
    print("\nPareto front solutions:")
    for ind in pareto_front:
        print("Schedule (task->VM):", ind.schedule)
        print("Objectives: Makespan, Cost, LoadBalance =", ind.objs)
        print("-" * 40)
    show_plot = get_int("Show Pareto front 3D plot? (1=Yes, 0=No)", default=1)
    if show_plot:
        plot_pareto_front(pareto_front)

if __name__ == "__main__":
    main()
