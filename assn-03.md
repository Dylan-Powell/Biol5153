1. rsync -r mt_genomes/ dtp006@hpc-portal2.hpc.uark.edu:/storage/dtp006/mt_genomes
 
2. scp unknown.fa dtp006@hpc-portal2.hpc.uark.edu:/storage/dtp006/
Enter passphrase for key '/home/dtpowell/.ssh/id_rsa':
unknown.fa                                                                            100% 1615    54.7KB/s   00:00

3. #!/bin/bash

#SBATCH --job-name=assn_3
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH -o assn_3_%j.out
#SBATCH -e assn_3_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=dtp006@uark.edu

export OMP_NUM_THREADS=32

module purge
module load blast/2.3.0+

cd $SLURM_SUBMIT_DIR
cat *.fasta > genomes.fas
makeblastdb -in genomes.fas -dbtype nucl
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn

4. rsync -azv dtp006@hpc-portal2.hpc.uark.edu:/storage/dtp006/mt_genomes .

5. The email says the job took 2 seconds. Slurm Job_id=1443227 Name=assn_3 Ended, Run time 00:00:02, COMPLETED, ExitCode 0

The closest match in the database is Cucurbita with a percent identity of 1566/1584 (99%) and a score of 2826 bits. 

