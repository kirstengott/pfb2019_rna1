#!/usr/bin/env python3
from Bio import SeqIO
import sys
import itertools

try:
    fastq = sys.argv[1]
except: 
    print('need to add input fastq file to commandline')
    sys.exit(1)
try:
    out_file = sys.argv[2]
except:
    print('need to include a name for the output file in fasta format')
    sys.exit(1)


#with open(fastq,'r') as infile, open(out_file,'w') as outfile:
#    line_ct = 0
#    for line in infile:
#        if (line_ct %4 == 0):
#            line_ct = 0
#        if (line_ct == 1):
#            print(line, end = "")
#        line_ct += 1

#converts fastq to fasta format
count = SeqIO.convert(fastq, 'fastq', out_file.rstrip(), 'fasta')
print(str(count) + " records converted")

################# UNIQIFY ##################


