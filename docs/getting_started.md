# Getting Started with Cloud Task Scheduler

## Overview

This project implements a multi-objective task scheduling system for cloud computing environments using the NSGA-II algorithm. It optimizes three key objectives simultaneously:
- **Makespan** (total execution time)
- **Cost** (monetary cost of computation)
- **Load Balance** (fair distribution of workloads)

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. **Clone the repository**:
- git clone https://github.com/Lohit2005/Cloud-Task-Scheduler.git
- cd Cloud-Task-Scheduler

2. **Install dependencies**:
- pip install numpy matplotlib


## Usage

### Basic CLI Execution
`python -m src.cli`

### Interactive Workflow
1. You'll be prompted to enter:
   - Number of tasks and their properties (workload, resource requirements)
   - Number of VMs and their capabilities (CPU, RAM, bandwidth, cost)
   - Algorithm parameters (population size, generations, mutation/crossover rates)

2. Example session:
   === Cloud Task Scheduling with NSGA-II ===<br/>
   Enter number of tasks: 50<br/>
   Enter number of VMs: 10<br/>
   ...<br/>

3. After optimization, you'll see:
   - Pareto-optimal solutions with their schedules
   - Option to view the 3D Pareto front visualization


## Key Features

- **Interactive Configuration**: Set up tasks and VMs through intuitive prompts
- **Multi-objective Optimization**: Simultaneously optimizes time, cost, and balance
- **Visual Analytics**: 3D visualization of trade-offs between objectives
- **Reproducible Results**: Seed-based randomization for consistent outputs

## Running Tests

To verify the implementation, run:
pytest tests/

Sample test cases include:
- Individual evaluation checks
- Population initialization validation
- Algorithm convergence tests


## Contributing

We welcome contributions! Here's how to help:

1. **Report Issues**:  
   Open a GitHub issue for any bugs or feature requests.

2. **Submit Pull Requests**:  
   1. Fork the repository
   2. Create a feature branch (`git checkout -b feature/your-feature`)
   3. Commit your changes
   4. Push to the branch
   5. Open a pull request

3. **Development Guidelines**:
   - Follow PEP-8 style guide
   - Write unit tests for new features
   - Maintain 80%+ test coverage
   - Update documentation accordingly

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for full details.

## Acknowledgements

- **NSGA-II Algorithm**: Based on the work of Deb et al. (2002)
- **CloudSim Toolkit**: Inspiration from cloud simulation methodologies
- **Matplotlib**: Used for 3D visualization components

For academic references, please cite:
@article{deb2002,
title={A fast and elitist multiobjective genetic algorithm: NSGA-II},
author={Deb, Kalyanmoy and Pratap, Amrit and Agarwal, Sameer and Meyarivan, T},
journal={IEEE Transactions on Evolutionary Computation},
year={2002}
}

This documentation was last updated on April 23, 2025.  
For support, contact: [lohitsamantula@gmail.com](mailto:lohitsamantula@gmail.com)
