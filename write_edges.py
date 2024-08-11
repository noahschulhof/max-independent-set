import os

def remove_edge_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

def write_simple_edges(nodes_list, filepath):
    edges = []
    
    for i in range(len(nodes_list)):
        if i == len(nodes_list) - 1:
            edges.append([str(nodes_list[i]), str(nodes_list[0])])
            break
        edges.append([str(nodes_list[i]), str(nodes_list[i+1])])

    with open(filepath, 'a') as f:
        for edge in edges:
            f.write(','.join(edge) + '\n')
        f.close()

def write_edges(nodes_per_layer, num_layers, filepath, nodes_list = [], current_layer = 1):
    new_nodes_list = []
    current_nodes = []

    if current_layer > num_layers:
        return('Done')

    if current_layer == 1:
        nodes_list = [x for x in range(nodes_per_layer)]
        write_simple_edges(nodes_list, filepath)
        new_nodes_list = nodes_list
    else:
        for node in nodes_list:
            if len(current_nodes) == 0:
                current_nodes = [x for x in range(max(nodes_list) + 1, max(nodes_list) + nodes_per_layer)]
            else:
                max_node = max(current_nodes)
                current_nodes = [x for x in range(max_node + 1, max_node + nodes_per_layer)]
            new_nodes_list += current_nodes
            write_simple_edges([node] + current_nodes, filepath)

    return(write_edges(nodes_per_layer, num_layers, filepath, new_nodes_list, current_layer + 1))