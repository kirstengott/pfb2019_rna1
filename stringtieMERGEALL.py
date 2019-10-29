#!/usr/bin/env python3

#Next, merge all the transcripts to one file. This creates one set of transcripts for all samples so the anaysis for differential expression can be performed.

###This script takes the mergelist.txt and creates one set of transc    ripts for all samples.

import subprocess
import pathlib
import sys
import os

referencegenome = sys.argv[1]
mergedgtf = (sortedbamfile+".gtf")

mergelist = open("mergelist.txt","r")

mergeall = ("stringtie --merge -p 6 -G",referencegenome,"-o mergelist.gtf",mergelist)
Cmdmergeall = os.popen(mergeall).read()
print('final merge:', Cmdmergeall)

