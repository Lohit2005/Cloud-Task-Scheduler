# Cloud Task Scheduler using NSGA-II

## Overview

This project implements a multi-objective task scheduling system for cloud computing environments using the NSGA-II (Non-dominated Sorting Genetic Algorithm II) algorithm. It simultaneously optimizes:
- **Makespan** (total execution time of all tasks)
- **Cost** (total resource usage cost)
- **Load Balance** (standard deviation of resource utilization across VMs)

Users can interactively define tasks, VMs, and algorithm parameters, and visualize the Pareto front of optimal solutions.

---

## Features

- **Interactive CLI:** Enter the number of tasks, VMs, and their properties at runtime.
- **Multi-objective Optimization:** Uses NSGA-II to optimize makespan, cost, and load balance.
- **Pareto Front Visualization:** 3D plot of Pareto-optimal solutions.
- **Modular Codebase:** Separated into models, algorithm, visualization, and CLI modules.
- **Unit Tests:** Includes basic tests for core functionality.
- **Industry-standard Structure:** Ready for collaborative development and CI/CD.

---

## Project Structure

cloud-scheduler/
├── src/
│ ├── scheduler/
│ │ ├── models.py
│ │ ├── nsga2.py
│ │ ├── visualization.py
│ │ └── init.py
│ ├── cli.py
│ └── init.py
├── tests/
│ └── test_nsga2.py
├── docs/
│ └── getting_started.md
├── .github/
│ └── workflows/
│ └── tests.yml
├── README.md
├── pyproject.toml
├── .gitignore
└── LICENSE

---

## Installation

1. **Clone the repository:**
git clone https://github.com/Lohit2005/cloud-scheduler.git
cd cloud-scheduler

2. **Install dependencies:**
pip install numpy matplotlib pytest

---

## Usage

Run the CLI from the project root:
python -m src.cli

You will be prompted to enter the number of tasks, VMs, and their properties, as well as algorithm parameters.


**Example session:**

=== Cloud Task Scheduling with NSGA-II ===
Enter number of tasks:
Enter number of VMs:
...
Pareto front solutions:
Schedule (task->VM): [2, 1, 0, ...]
Objectives: Makespan, Cost, LoadBalance = (3702.0, 140.996, 0.01116)
...
Show Pareto front 3D plot? (1=Yes, 0=No):

---

## Running Tests

To verify the implementation, run:
pytest tests/


---

## Contributing

Contributions are welcome! Please:
- Fork the repository
- Create a feature branch
- Commit your changes with clear messages
- Open a pull request

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [NSGA-II Algorithm Paper](https://ieeexplore.ieee.org/document/996017)
- [CloudSim Toolkit](https://cloudsim-plus.org/)
- [Matplotlib](https://matplotlib.org/) for visualization

---

## Contact

For questions or support, please contact [lohitsamantula@gmail.com](mailto:lohitsamantula@gmail.com).
