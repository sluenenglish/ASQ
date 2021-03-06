"""
Usage: run_simulation.py <dir_name>

Arguments
	dir_name    : name of the directory from which to read in parameters and write data files
    suff        : optional suffix to add to the data file name

Options
    -h          : displays this help file
"""
from __future__ import division
import os
import docopt
from asq import *

if __name__ == '__main__':
	arguments = docopt.docopt(__doc__)
	dirname = arguments['<dir_name>']
	P = load_parameters(dirname)
	Q = Simulation(P)
	Q.simulate_until_max_time()
	Q.write_records_to_file(dirname)