import argparse
from draw_edges import *

# create argument parser object
argParser = argparse.ArgumentParser()

# add command line argument
argParser.add_argument('-e', '--edges_filepath', type = str, help = 'Filepath to existing edges csv file')

# parse argument
args = argParser.parse_args()

# draw graph
graph = draw_graph(args.edges_filepath)
graph.show()