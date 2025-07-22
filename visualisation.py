import matplotlib.pyplot as plt

def plot_progress(profits):
    """
    Plot the best profit found over iterations.
    :param profits: List of best profits at each iteration
    """
    plt.figure(figsize=(8, 4))
    plt.plot(profits, marker='o')
    plt.title('Best Profit Over Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Best Profit')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_selection(selection, obj):
    """
    Visualize the selected objects in the knapsack.
    :param selection: List of 0/1 indicating selected objects
    :param obj: List of (size, profit) tuples
    """
    selected = [i for i, x in enumerate(selection) if x == 1]
    sizes = [obj[i][0] for i in selected]
    profits = [obj[i][1] for i in selected]
    labels = [f'Obj {i}' for i in selected]
    plt.figure(figsize=(8, 4))
    plt.bar(labels, profits, color='skyblue')
    plt.title('Profits of Selected Objects')
    plt.xlabel('Object')
    plt.ylabel('Profit')
    plt.tight_layout()
    plt.show() 