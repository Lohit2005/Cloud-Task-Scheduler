import pytest
import random
import numpy as np
from scheduler.models import Task, VM, Individual
from scheduler.nsga2 import (
    evaluate_individual,
    create_initial_population,
    nsga2,
    extract_pareto_front
)

def test_individual_evaluation():
    # Minimal test: 2 tasks, 2 VMs
    tasks = [
        Task(0, 100, 50, 20, 1, 1, 1),
        Task(1, 200, 60, 30, 2, 2, 2)
    ]
    vms = [
        VM(0, 4, 4, 100, 1024, 0.005),
        VM(1, 8, 8, 200, 2048, 0.007)
    ]
    ind = Individual([0, 1])
    evaluate_individual(ind, tasks, vms)
    assert isinstance(ind.objs, tuple)
    assert len(ind.objs) == 3

def test_population_initialization():
    pop = create_initial_population(5, 3, 2)
    assert len(pop) == 5
    assert all(len(ind.schedule) == 3 for ind in pop)

def test_nsga2_runs():
    tasks = [Task(i, 100, 50, 20, 1, 1, 1) for i in range(5)]
    vms = [VM(j, 4, 4, 100, 1024, 0.005) for j in range(2)]
    result = nsga2(tasks, vms, pop_size=10, generations=5)
    assert isinstance(result, list)
    assert len(result) == 10

def test_extract_pareto_front():
    tasks = [Task(i, 100, 50, 20, 1, 1, 1) for i in range(3)]
    vms = [VM(j, 4, 4, 100, 1024, 0.005) for j in range(2)]
    pop = nsga2(tasks, vms, pop_size=6, generations=3)
    front = extract_pareto_front(pop)
    assert isinstance(front, list)
    assert len(front) > 0
