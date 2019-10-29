#!/usr/bin/env python3
import sys
import os    #to interact with the unix shell
import subprocess   #run some tools as subprocess from the shell
import pathlib

########################################


# USAGE FOR FASTA: python3 preprocessing_data.py <../fastq-files/> <folder_to_save_the_fasqc_results>

# USAGE FOR BOWTIE2: python3 preprocessing_data.py <../fastq-files/> 


#### FASTA FILES #######################

#    Raw files PATH: 
#raw_data_path='../fastq-files'                     # This is the folder where are the fasta files
#raw_data_path_cmd='ls ' + raw_data_path 
#myCmd = os.popen(raw_data_path_cmd).read()
#print('Fasta directory:\n'+myCmd)

##### Testing: reading files
#myFasta = 'head ~/pfb2019_rna1/reference/chr1/GCF_000001735.4_TAIR10.1_cds_chr1.fa'
#myCmd  = os.popen(myFasta).read()
#print(myCmd)


# Function to trigger fastqc reports (read the full folder)
def fastaf_quality(dir_f):
    try:
        #### CREATE DIRECTORY for the fastqc results
        dir_name = sys.argv[2]                 # Std name > 'fastqc_res'
        str_dir_name = 'rm -rf ' + dir_name
        myCmd2 = os.popen(str_dir_name).read()          # Delete the out fastqc directory if exists
        fasta_out='mkdir '+ dir_name                    # Create the fastqc output directory
        #print(fasta_out)
        myCmd3 = os.popen(fasta_out).read()
        print('Directory for the fastqc output: ' + fasta_out)

        # Get the full list of fasta file (parameter sys.2) 
        str_dir_f = dir_f
        arr_fasta_f = os.listdir(str_dir_f)          # Real folder:'../fastq-files'; Test: 'fasta_test/'
        print(arr_fasta_f)

        # Parse the files into the directory to trigger the fastqc
        for fasta_f in (arr_fasta_f):
            f_file = str_dir_f+fasta_f
            #print(f_file)
            fastqc_cmd = "fastqc -f fastq " + f_file + " -- outdir " + dir_name       # It isn't saving in the --output dir.... just look in the fasta files folder  (...pending to review)
            print(fastqc_cmd)
            ######## Use this line for zip files    
            #       fastqc_cmd='zcat ' + name + ' | fastqc --outdir '+ dir_name +'/ --extract --threads 8 stdin'
            myCmd3 = os.popen(fastqc_cmd).read()
            #print(myCmd3)                          # output to the screen the process            
            
    except:
        print("Please provide the fasta file and try again")

    return(True)


# Function to triger alignments
def bowtie2_f(R1,R2,b_name):
    try:
        #cmd structure of bowtie2: "bowtie2 -p 8 --mm -t --end-to-end -x pfb2019_rna1/reference/full/bw2-ara-indx -1 ../share/fastq/SRR9659514_pass_1_edit.fastq.gz -2 ../share/fastq/SRR9659514_pass_2_edit.fastq.gz --un-conc-gz bw2-full-results-DONT-PUSH/bw2-R1-ara-un-conc.fq.gz --al-conc-gz bw2-full-results-DONT-PUSH/bw2-R1-ara-al-conc.fq.gz -S bw2-full-results-DONT-PUSH/bw2-R1-ara-alignments.sam 2> bw2-full-results-DONT-PUSH/bw2-R1-ara-output.stdout"
        
        un_conc = 'bw2-R1-ara-un-conc.fq.gz'
        al_conc = 'bw2-R1-ara-al-conc.fq.gz'
        sam_name = '../bowt2_res/bw2-R1-ara-alignments.sam'
        bwt_std_out='../bowt2_res/bw2-R1-ara-output.stdout'

        str_test = 'Read 1: '+ R1, 'Read 2: '+ R2, 'Base_Idx: '+ b_name 
        print(str_test)
        x = 1
    except:
        x = 0
    
    return(x)



# Function to parse the output of sam files
def bowtie2_read_std_out(dir_s):
    # Get the full list of sam.output file
    #str_dir_f = dir_s
    str_dir_f = '../bw2_results/'           # '~/../share/bw2-short-output/stdout-files/'
    print('Sam input path: ' + str_dir_f)
    arr_bwt2_f = os.listdir(str_dir_f)          # Real folder:'../fastq-files'; Test: 'fasta_test/'
    print(arr_bwt2_f)

    # Parse the files into the directory to trigger the fastqc
    samlist = [] 

    for bwt2_f in (arr_bwt2_f):
        f_file = bwt2_f              
        str_sam_file = str_dir_f + f_file 
        #print('Sam (ouput) file name: ' + str_sam_file)
   
        with open(str_sam_file,"r") as fn:            
            count_ln=0
            print('\n\nSam (ouput) file name: ' + f_file)
            samlist.append(f_file)
            for line in fn:
                count_ln+=1
                if (count_ln>6) & (count_ln<11):
                    ln=line.strip()
                    #ln_end = ln.find(')')
                    #ln_str = ln[1:ln_end+1]              
                    #ln_str2 = ln_str.spli(' ')
                    print(ln)
                    samlist.append(ln)
                        
    #print('fname:' , d.f_name , ' ' , 'Treads:' , d.reads, ' ' , 'Concor0:' , d.concor, 'Concor1:', d.concor1 )         
    #print(samlist)
    return(samlist)      # return the value to the code that called this function
           

#Get the path of the folder to parse
dir_f =sys.argv[1]


##################  HERE ARE CALL THE FUNCTIONS ################################


# FUNCTION TO RUN THE FASTA QUALITY PROCESS
#if fastaf_quality(dir_f): print("Fasta file process done")

# ASSUMING THE INDEX PROCESS WAS DONE PREVIOUSLY 

# FUNCTION TO RUN THE BOWTIE PROCESS with PE
fastaR1 = 'R1'
fastaR2 = 'R2'
idx_base = 'Base'
bow1 = bowtie2_f(fastaR1,fastaR2,idx_base) 
print(bow1)

# FUNCTION TO GET THE BOWTIE2 RESULTS
samlist = bowtie2_read_std_out(dir_f)
# Send the sam_list resume table to the screen
#for sam in samlist:
#  print(sam)







