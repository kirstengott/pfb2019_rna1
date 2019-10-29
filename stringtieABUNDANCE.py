#!/usr/bin/env python3

###Using the merged transcript file, next this takes one user input of a sorted bam file of interest and uses stringtie to estimate transcript abundances and create table counts.###

import subprocess
import pathlib
import sys
import os


sortedbam = sys.argv[1]
output = (sortedbam+".gtf")
abundance = ("stringtie -e -B -p 6 -G mergelist.gtf -o "+output+" "+sortedbam)
Cmdabundance = os.popen(abundance).read()

print('Provided sorted bam file:',sortedbam)
print('Determining abundance:', Cmdabundance)
