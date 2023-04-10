#! /usr/bin/env python3

# importing the parser module
import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='This script will assign job name and optional characters to a AHPCC job')

# add positional arguments
parser.add_argument("gff", help='the name of the gff being parsed', type=str)
parser.add_argument("fasta", help='the name of the fasta file', type=str)


# parse the arguments
args = parser.parse_args()


# read the gff file
#gff_file = open(args.gff, "r")
#fasta_file = open(args.fasta, "r")

# open the gff file
with open(args.gff) as file:
	for line in file:
		print(line)
with open(args.fasta) as file_fasta:
	for line in file_fasta:
		print(line)
