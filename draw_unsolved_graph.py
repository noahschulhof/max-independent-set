import argparse
from draw_edges import *

# create argument parser object
argParser = argparse.ArgumentParser()

# add command line argument
argParser.add_argument('--edges_filepath', type = str, default = 'sample_edges.csv', help = 'Relative filepath to write/read edges csv file [default=edges.csv]')

# parse argument
args = argParser.parse_args()

# draw graph
graph = draw_graph(args.edges_filepath)
graph.show()