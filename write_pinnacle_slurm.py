#! /usr/bin/env python3

job_name = "assn4"
queue = "bird"
number_nodes = "snake"
processors = "infinite"
walltime = "eternal"

print('#SBATCH --job-name=',job_name)
print('#SBATCH --partition',queue)
print('#SBATCH --nodes=',number_nodes)
print('#SBATCH --tasks-per-node=',processors)
print('#SBATCH --time=',walltime)
print('#SBATCH -o assn4%j.out')
print('#SBATCH -e assn4%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=dtp006@uark.edu')

# cd $SLURM_SUBMIT_DIR

