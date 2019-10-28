#!/usr/bin/env python3

import sys
import os    #to interact with the unix shell
import subprocess   #run some tools as subprocess from the shell

def fastqc_process():
    x = 1/0


    #### FASTA FILE Path
    #    Raw files PATH: ~/../share/fastq  server_pwd:../projects/rna1/share/fastq
    raw_data_path='~/../share/fastq/'
    raw_data_path_cmd='ls ' + raw_data_path 
    print(raw_data_path)
    myCmd = os.popen(raw_data_path).read()
    print(myCmd)

##### Testing: reading files
#myFasta = 'head ~/pfb2019_rna1/reference/chr1/GCF_000001735.4_TAIR10.1_cds_chr1.fa'
#myCmd  = os.popen(myFasta).read()
#print(myCmd)


try:
    
    #### Create a directory for the fastqc results
    dir_name = fasta_R2=sys.argv[2]                 # Std name > 'fastqc_res'
    str_dir_name = 'rm -rf ' + dir_name
    myCmd2 = os.popen(str_dir_name).read()          # Delete the output directory if exists

    fasta_out='mkdir '+ dir_name                    # Create the fastqc output directory
    print(fasta_out)
    myCmd3 = os.popen(fasta_out).read()
    print(myCmd3)

    for _file in sys.argv[1:]:

    with open(_file,"r") as fin:
        print(_file)
        #### Fastqc cmd line in unix 
        #name=_file                                  # 'SRR9659514_pass_1_edit.fastq.gz'
        #fasta_cmd='zcat ' + raw_data_path + name +'| fastqc --outdir '+ dir_name +'/ --extract --threads 8 stdin'
        #print(fasta_cmd)
        #myCmd3 = os.popen(fasta_cmd).read()
        #print(myCmd3)

except:
    
    print("Please provide the fasta file and try again")
