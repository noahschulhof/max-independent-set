import gurobipy as gp
from gurobipy import GRB, quicksum
import pandas as pd
import argparse
from write_edges import *
from draw_edges import *

# create argument parser object
argParser = argparse.ArgumentParser()

# add command line arguments
argParser.add_argument('-n', '--nodes_per_layer', type = int, default = 3, help = 'Number of nodes per graph layer [default=3]')
argParser.add_argument('-l', '--num_layers', type = int, default = 3, help = 'Number of layers in the graph [default=3]')
argParser.add_argument('-m', '--max_num_sol', type = int, default = 100, help = 'Maximum number of optimal solutions returned by Gurobi [default=100]')
argParser.add_argument('-e', '--edges_filepath', type = str, default = None, help = 'Filepath from which to read edges')

# parse arguments
args = argParser.parse_args()

if args.edges_filepath:
    edges_fp = args.edges_filepath
else:
    edges_fp = 'edges.csv'

    # remove default edges csv file if it exists
    remove_edge_file(edges_fp)

    # write edges csv file
    write_edges(args.nodes_per_layer, args.num_layers, edges_fp)

# read edges csv file
df = pd.read_csv(edges_fp, header = None)

# get number of nodes in graph
num_nodes = int(df.values.max()) + 1

# maximum number of solutions returned
max_num_sol = args.max_num_sol

# create Gurobi model object
model = gp.Model()

# creates a dictionary object - keys are enumerations, values are model variable objects
x = model.addVars(num_nodes, vtype = GRB.BINARY, name = 'x')

# create a list of model variable objects
x_vars = x.values()

# create a list of sublists - each sublist contains the vertices forming an edge
edges = df.values.tolist()

# add constraint - adjacent vertices cannot be included in the independent set
for edge in edges:
    model.addConstr(x_vars[edge[0]] + x_vars[edge[1]] <= 1)

# limit size of solution pool
model.setParam(GRB.param.PoolSearchMode, 2)
model.setParam(GRB.param.PoolSolutions, max_num_sol)

# maximize sum of vertices
model.setObjective(quicksum(x for x in x_vars), GRB.MAXIMIZE)

# optimize the model
model.optimize()

# iterate through solutions in solution pool
# printing in this order guarantees that, if two solutions are the same, nodes are printed in the same order (simplifies string comparison)
if model.status == GRB.OPTIMAL:
    num_sols = model.SolCount # get number of solutions in pool
    independent_set_list = []
    for i in range(num_sols):
        model.setParam(GRB.Param.SolutionNumber, i) # set the current solution to the i-th solution of the pool
        independent_set_list.append([j for j, var in enumerate(x_vars) if var.xn == 1])
    max_independent_set_length = max([len(x) for x in independent_set_list])
    optimal_independent_set_list = [sublist for sublist in independent_set_list if len(sublist) == max_independent_set_length]
    for i, independent_set in enumerate(optimal_independent_set_list, 1):
        print(f'\nSOLUTION #{i}')
        print(f'Maximum Independent Set: {independent_set}')
        print(f'Number of nodes: {len(independent_set)}')
else:
    print('No solution found.')

# draw solved graph
solved_graph = draw_graph(edges_fp, independent_set)
solved_graph.show()