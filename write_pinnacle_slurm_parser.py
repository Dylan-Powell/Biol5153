#! /usr/bin/env python3

# importing the parser module
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='This script will assign job name and optional characters to a AHPCC job')

# add positional arguments
parser.add_argument('job_name', help='Defining the name of the job to be submitted', type=str)

# add optional arguments
parser.add_argument('--queue', help='assign the queue for the job', type=str)
parser.add_argument('--number_nodes', help='assign the number of nodes for the job', type=str)
parser.add_argument('--processors', help='assign the number of processors for the job', type=str)
parser.add_argument('--walltime', help='assign the amount of walltime needed for the job', type=str)


# parse the arguments
args=parser.parse_args()




print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition',args.queue)
print('#SBATCH --nodes=' + str(args.number_nodes))
print('#SBATCH --tasks-per-node=' + str(args.processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o assn4%j.out')
print('#SBATCH -e assn4%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=dtp006@uark.edu')

# cd $SLURM_SUBMIT_DIR

