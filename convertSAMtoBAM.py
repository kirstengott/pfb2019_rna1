#!/usr/bin/env python3

###This script takes one user input (the SAM file of interest) and converts it into a BAM file.###

import subprocess
import pathlib
import sys
import os

samfile = sys.argv[1]
bamfile = (samfile+".bam")
print("sam file to convert:", samfile, "\n"+"bam file output:", bamfile)


samtobam = str("samtools view -S -b -@ 6 "+samfile+" > "+bamfile)
Cmdsambam = os.popen(samtobam).read()
print('convert sam to bam:' + Cmdsambam)
