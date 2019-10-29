#!/usr/bin/env python3

#setting up interleaved files using scropt from BioPython
#https://news.open-bio.org/2009/12/14/interleaving-paired-fastq-files-with-biopython/

#I am adding the sys.argv arguments
#I'm updating the final print statement, to use the {} brackets instead of the modulous %

from Bio import SeqIO
import itertools
import sys

#set up variables and error messages
try:
    file_f = sys.argv[1] #if no input is provided, then go to except:
except:
    print('Need to enter forward fastq file')
    sys.exit(1) #the 1 returns an error code
try:
    file_r = sys.argv[2]
except:
    print('Need to enter reverse fastq file')
    sys.exit(1)
try:
    file_out = sys.argv[3]
except:
    print('Need to enter output file name for interleaved output, <file-out.fq>')
    sys.exit(1)

format = "fastq"

def interleave(iter1, iter2): #define function name as 'interleave', where input are iter1 and iter2
    for (forward, reverse) in zip(iter1,iter2): #going to zip in every pair of iter1:iter2 
        #assert forward.id == reverse.id #since I'm working with PE data, forward should equal reverse
        forward.id += "/1" #double check, but the input fastq file for forward should specify /1
        reverse.id += "/2"
        yield forward #Not sure what 'yield' means...
        yield reverse #when to use yield instead of return: 
        #Return sends a specified value back to its caller 
        #Yield can produce a sequence of values, and should be used to iterate over a sequence without storing the entire seq to memory

records_f = SeqIO.parse(open(file_f,'r'), format)  #Original code uses'rU' where U used to be the universal newlines. 
records_r = SeqIO.parse(open(file_r,'r'), format)  #usually, I specify 'r' for read, but I'm using implicit open mode
#with open(file_f,'r') as fo:
#    for line in fo:
#        line = line.strip('\n').split(' ')
#        records_f = SeqIO.parse(line, format)

handle = open(file_out,'w')
count = SeqIO.write(interleave(records_f,records_r), handle, format)
handle.close()
#print("{}i records written to {}s" % (count, file_out))




