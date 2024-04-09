import networkx as nx
import matplotlib.pyplot as plt

from data_generation.set_generator import *
from mathematical_model.arc_model import *

def plot_result_arcs():
    result_dict = {}
    #arcs for all days
    for arc in result_arcs:
        parts = arc.split("_")[1:]
        variable_indices = [int(part) for part in parts]
        last_number = variable_indices[-1]
        #arcs sortert etter dag som key
        if last_number not in result_dict:
            result_dict[last_number] = []
        result_dict[last_number].append(variable_indices)
    #arcs for each day
    arcs_ij = {}
    arcs_employees = {}
    for key, value in result_dict.items():
        arcs_ij_list = [(item[0], item[1]) for item in value]
        arcs_employees_list = [(item[2]) for item in value]
        arcs_ij[key] = arcs_ij_list
        arcs_employees[key] = arcs_employees_list
    for day in arcs_ij:
        G = nx.DiGraph()
        # Nodes for each day
        nodes_one_day = ACTIVITIES
        G.add_nodes_from(nodes_one_day, node_type='activities_depot')
        # Arcs for each day
        print(f'dag {day}: ', arcs_ij[day])
        print(f'dag {day}: ', arcs_employees[day])
        chosen_arcs = arcs_ij[day]
        #chosen_arcs = arcs_employees[day]
        chosen_nodes = set() #ny og må testes. 
        for arc in chosen_arcs: #ny
            chosen_nodes.update(arc)

        G.add_nodes_from(chosen_nodes, node_type='activity') #ny

        G.add_edges_from(chosen_arcs, edge_type='valgt')
        #G.add_weighted_edges_from(chosen_arcs, edge_type='valgt', weight='weight')

        # Få en liste over kanter som er valgt
        chosen_edges = [(u, v) for u, v, data in G.edges(data=True) if data.get('edge_type') == 'valgt']

        # Visualiser grafen
        pos = nx.spring_layout(G, k=2)  # Bestemmer layout
        node_colors = ['blue' if node_type == 'depot' else 'red' for node_type in
                       nx.get_node_attributes(G, 'node_type')]
        edge_colors = ['green' if kant in chosen_edges else 'gray' for kant in G.edges()]

        nx.draw(G, pos, with_labels=True, node_color='red', edge_color=edge_colors)
        plt.show()


#Testing
#result_arcs = ["x_0_24_1_1", "x_21_23_1_1", "x_23_21_1_1", "x_24_0_1_1","x_0_24_1_2", "x_21_23_1_2", "x_23_21_1_2", "x_24_0_1_2"]
result_arcs = run_model()
plot_result_arcs(result_arcs)
