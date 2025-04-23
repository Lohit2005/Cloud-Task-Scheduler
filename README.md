# ☁️ Cloud Task Scheduler using NSGA-II

## 🧠 Overview

This project implements a **multi-objective task scheduling system** for cloud environments using the **NSGA-II (Non-dominated Sorting Genetic Algorithm II)**. It simultaneously optimizes:

- ⏱ **Makespan** (total execution time)
- 💰 **Cost** (resource usage cost)
- ⚖️ **Load Balance** (fair workload distribution)

Users can interactively define tasks, VMs, and algorithm parameters, and visualize the **Pareto front** of optimal solutions.

---

## ✨ Features

- 🖥️ **Interactive CLI** — Define tasks and VMs at runtime via simple prompts.
- 🎯 **Multi-objective Optimization** — Optimize time, cost, and load balance.
- 📊 **Pareto Front Visualization** — View 3D plot of trade-offs between objectives.
- 🧩 **Modular Codebase** — Separated into models, algorithm, CLI, and visualization.
- 🧪 **Unit Testing** — Basic tests for population handling and objective calculations.
- 🏗️ **Developer-Friendly Structure** — Ideal for CI/CD integration and contributions.

---

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Lohit2005/Cloud-Task-Scheduler.git
   cd Cloud-Task-Scheduler

2. **Install dependencies:**
   ```bash
   pip install numpy matplotlib pytest

---

## 🚀 Usage

Run the CLI from the project root:
`python -m src.cli`

You will be prompted to enter the number of tasks, VMs, and their properties, as well as algorithm parameters.


** 🧾 Example Session**

=== Cloud Task Scheduling with NSGA-II ===<br/>
Enter number of tasks:<br/>
Enter number of VMs:<br/>
...<br/>
Pareto front solutions:<br/>
Schedule (task->VM): [2, 1, 0, ...]<br/>
Objectives: Makespan, Cost, LoadBalance = (3702.0, 140.996, 0.01116)<br/>
...<br/>
Show Pareto front 3D plot? (1=Yes, 0=No):<br/>

---

## ✅ Running Tests

To verify the implementation, run:
pytest tests/


---

## 🤝 Contributing

Contributions are welcome! Please:
- Fork the repository
- Create a feature branch
- Commit your changes with clear messages
- Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- 📚 [NSGA-II Algorithm Paper](https://ieeexplore.ieee.org/document/996017)
- ☁️ [CloudSim Toolkit](https://cloudsim-plus.org/)
- 📈 [Matplotlib](https://matplotlib.org/) for visualization

---

## 📬 Contact

For questions or support, please contact [lohitsamantula@gmail.com](mailto:lohitsamantula@gmail.com).
