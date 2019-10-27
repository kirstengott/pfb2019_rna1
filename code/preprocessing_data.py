#!/usr/bin/env python3

import sys
import os    #to interact with the unix shell
import subprocess   #run some tools as subprocess from the shell

def fastqc_process():
    x = 1/0

##### Getting the path of the files
myCmd = os.popen('pwd').read()
chr1_path='ls ~/pfb2019_rna1/reference/chr1/'
print(chr1_path)
myCmd = os.popen(chr1_path).read()
print(myCmd)

##### Testing: reading files
#myFasta = 'head '+chr1_path+'GCF_000001735.4_TAIR10.1_cds_chr1.fa'
#myCmd  = os.popen(myFasta).read()
#print(myCmd)


try:

    #### FASTA FILE PROCESS
    #    Raw files in: ~/../share/fastq  server_pwd:../projects/rna1/share/fastq
    raw_data_path='cd ~/../share/fastq'
    print(raw_data_path)
    myCmd = os.popen(raw_data_path).read()
    myCmd = os.popen('ls -lhg').read()
    print(myCmd)

    #fasta_R1=sys.argv[1]
    #fasta_R2=sys.argv[2]
    #fastqc_cmd = 'fastqc -help xxxxxx '
    #myCmd  = os.popen(fastqc_cmd).read()
    #print(myCmd)


except:
    
    print("Please provide the fasta file and try again")
