#!/usr/bin/env python3
import sys

################# UNIQIFY ##################
try:
    input_file = sys.argv[1]
except:
    print('need to specify input fasta file name')
    sys.exit(1)
try:
    output_file = sys.argv[2]
except:
    print('specify file name for uniqified fasta sequences file')
    sys.exit(1)

holder=[]
with open(input_file,'r') as fo:
    record = fo.read().split('>')[1:]
    record = ['>'+i.strip()+'\n' for i in record]
holder.extend(record)

total='\n'.join(list(set(holder)))

with open(output_file,'w') as out:
    out.write(total)




