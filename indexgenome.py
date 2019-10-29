##############################
#First index the genome using the following format:
#--runThreadN NumberOfThreads
#--runMode genomeGenerate
#--genomeDir /path/to/genomeDir
#--genomeFastaFiles /path/to/genome/fasta1 /path/to/genome/fasta2 ...
#--sjdbGTFfile /path/to/annotations.gtf

import subprocess
import pathlib

Cmdindex = os.popen("STAR --runThreadN 4 --runMode genomeGenerate --genomeDir ~/pfb2019_rna1/reference/chr1/indexedchr1 --genomeFastaFiles ~/pfb2019_rna1/reference/chr1/GCF_000001735.4_TAIR10.1_genomic_chr1.fa --sjdbGTFtagExonParentTranscript ~/pfb2019_rna1/reference/chr1/GCF_000001735.4_TAIR10.1_genomic_chr1.gff").read()
print('Indexed: ' + Cmdindex)

