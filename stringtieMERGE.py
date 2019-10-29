#!/usr/bin/env python3

###This script takes one user input and uses stringtie to generate merged transcript file.###

import subprocess
import pathlib
import sys
import os

sortedbamfile = sys.argv[1]
referencegenome = sys.argv[2]
outputgtf = (sortedbamfile+".gtf")

print("sorted bam file provided: ",sortedbamfile, "\n"+"pathway to reference genome: ",referencegenome )


mergetranscriptfiles = ("stringtie -p 6 -G "+referencegenome+" -o "+outputgtf+" "+sortedbamfile)

Cmdmergetranscriptfiles = os.popen(mergetranscriptfiles).read()

print('merge:',Cmdmergetranscriptfiles)

#collect each output file and append to mergelist.txt to be used in stringtie merge

mergelist= open("mergelist.txt","a+")
mergelist.write(outputgtf)


