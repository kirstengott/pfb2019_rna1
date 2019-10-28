#!/usr/bin/env python3
import sys

field_str = "QNAME FLAG RNAME POS MAPQ CIGAR RNEXT PNEXT TLEN SEQ QUAL TAG"
fields = field_str.split(' ')

hits_list = []

for hit_file in sys.argv[1:]:

    with open(hit_file,'r') as fo:
        for line in fo:
            if line.startswith('@'):
                continue
            hit_data = dict(zip(fields,line.strip('\n').split('\t')))
            hit_data['file'] = hit_file  #add a key:value pair to end to include the file name in the list
            hits_list.append(hit_data)
            break
print(hits_list)

            #if key in hits_list[8]:
                
             #   hits_list[8][key] = {'A':0, 'T':0, 'G':0, 'C':0}
                 #   print(hits_list)
            #else:    
             #   for nucleotide in hits_list[8][key]:
              #      hits_list[8][key][nucleotide] +=1
               #     print(hits_list)

for hit in hits_list:
    print('\t'.join([hit[x] for x in ('RNAME','SEQ')]))





