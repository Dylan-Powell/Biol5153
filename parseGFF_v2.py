#! /usr/bin/env python3

# importing the parser module
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='This script will assign job name and optional characters to a AHPCC job')

# add positional arguments
parser.add_argument("gff", help='the name of the gff being parsed', type=str)
#parser.add_argument("fasta", help='the name of the fasta file', type=str)


# parse the arguments
args = parser.parse_args()


# open the gff file
gff_file = open(args.gff, "r")
#fasta_file = open(args.fasta, "r")

# read the gff file
#with open(args.gff) as file:
#	for line in file:
#		print(line.rstrip())
#with open(args.fasta) as file_fasta:
#	for line in file_fasta:
#		print(line.rstrip())

# feature type length
for line in gff_file:
	line = line.rstrip('\n')
	line_split = line.split('\t')
	len = int(line_split[4]) - int(line_split[3])
	len += 1
	print(line_split[2], str(len))
print('done!')
