import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_pareto_front(pareto_front):
    """Visualizes the Pareto front in 3D objective space."""
    if not pareto_front:
        print("Pareto front is empty. Nothing to plot.")
        return

    makespans = [ind.objs[0] for ind in pareto_front]
    costs = [ind.objs[1] for ind in pareto_front]
    load_balances = [ind.objs[2] for ind in pareto_front]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(
        makespans, costs, load_balances,
        c=load_balances, cmap='viridis', s=50, edgecolors='k'
    )
    ax.set_xlabel('Makespan (Time Units)', fontsize=12)
    ax.set_ylabel('Total Cost (Units)', fontsize=12)
    ax.set_zlabel('Load Balance (Std Dev)', fontsize=12)
    plt.title("Pareto-Optimal Solutions for Cloud Task Scheduling", pad=20)
    cbar = plt.colorbar(scatter, pad=0.1)
    cbar.set_label('Load Balance', rotation=270, labelpad=15)
    plt.tight_layout()
    plt.show()
