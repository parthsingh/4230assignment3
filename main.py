import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# 1.1 Reading in the twitter dataset and converting to undirected network
def read_twitter_dataset(filename):
    return nx.read_edgelist(filename, create_using=nx.DiGraph())

def convert_to_undirected(graph):
    return graph.to_undirected()

# 1.2 Generating histograms for degree, closeness, and betweenness centrality scores
def plot_histogram(data, title, xlabel, ylabel):
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def generate_centralities(graph):
    degree_centrality = nx.degree_centrality(graph)
    closeness_centrality = nx.closeness_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)

    plot_histogram(list(degree_centrality.values()), "Degree Centrality Histogram", "Degree Centrality", "Frequency")
    plot_histogram(list(closeness_centrality.values()), "Closeness Centrality Histogram", "Closeness Centrality", "Frequency")
    plot_histogram(list(betweenness_centrality.values()), "Betweenness Centrality Histogram", "Betweenness Centrality", "Frequency")

    return degree_centrality, closeness_centrality, betweenness_centrality

# 1.3 Analyzing nodes with highest degree centrality
def analyze_top_nodes(graph, degree_centrality, top_n=200):
    top_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:top_n]
    closeness_values = [nx.closeness_centrality(graph, u) for u in top_nodes]
    betweenness_values = [nx.betweenness_centrality(graph, u) for u in top_nodes]

    mean_closeness = np.mean(closeness_values)
    median_closeness = np.median(closeness_values)
    std_closeness = np.std(closeness_values)

    mean_betweenness = np.mean(betweenness_values)
    median_betweenness = np.median(betweenness_values)
    std_betweenness = np.std(betweenness_values)

    print("Mean Closeness Centrality:", mean_closeness)
    print("Median Closeness Centrality:", median_closeness)
    print("Standard Deviation of Closeness Centrality:", std_closeness)

    print("Mean Betweenness Centrality:", mean_betweenness)
    print("Median Betweenness Centrality:", median_betweenness)
    print("Standard Deviation of Betweenness Centrality:", std_betweenness)

# Main function
def main():
    # 1.1
    graph = read_twitter_dataset("twitter_combined.txt")
    undirected_graph = convert_to_undirected(graph)

    # Extracting largest connected component
    largest_cc = max(nx.connected_components(undirected_graph), key=len)
    graph_lcc = undirected_graph.subgraph(largest_cc)

    # 1.2
    degree_centrality, closeness_centrality, betweenness_centrality = generate_centralities(graph_lcc)

    # 1.3
    analyze_top_nodes(graph_lcc, degree_centrality)

if __name__ == "__main__":
    main()
