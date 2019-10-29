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
        dir_name_out = sys.argv[3]                          # Std name > 'fastqc_res'
        str_dir_name_out = 'rm -rf ' + dir_name_out
        myCmd2 = os.popen(str_dir_name_out).read()          # Delete the out fastqc directory if exists
        fasta_out='mkdir '+ dir_name_out                    # Create the fastqc output directory
        print(fasta_out)
        myCmd3 = os.popen(fasta_out).read()
        fasta_out=fasta_out
        print('Directory for the fastqc output: ' + fasta_out)

        # Get the full list of fasta file (parameter sys.2) 
        str_dir_f = 'fasta_test/'                    # dir_f
        #print('Aqui estoy')
        arr_fasta_f = os.listdir(str_dir_f)          # Real folder:'../fastq-files'; Test: 'fasta_test/'
        print(arr_fasta_f)
        
        # Parse the files into the directory to trigger the fastqc
        for fasta_f in (arr_fasta_f):
            f_file = str_dir_f+fasta_f
            #print(f_file)
            fastqc_cmd = "fastqc -f fastq " + f_file + " -- outdir " + dir_name_out     #dir_name       # It isn't saving in the --output dir.... just look in the fasta files folder  (...pending to review)
            print(fastqc_cmd)
            ######## Use this line for zip files    
            #       fastqc_cmd='zcat ' + name + ' | fastqc --outdir '+ dir_name +'/ --extract --threads 8 stdin'
            myCmd3 = os.popen(fastqc_cmd).read()
            print(myCmd3)                          # output to the screen the process
            #Note:Failed to send the results to the output folder... I do not know why... Need to be check, file results are send to the input folder 
    except:
        print("Please provide the fasta file and try again")
    return(True)


# Function to triger alignments
def bowtie2_f(R1='../share/fastq/SRR9659514_pass_1_edit.fastq.gz',R2='../share/fastq/SRR9659514_pass_2_edit.fastq.gz',idx_name='pfb2019_rna1/reference/full/bw2-ara-indx'):
    
    cmd_bt2 ="bowtie2 -p 8 --mm -t --end-to-end -x " + idx_name + " -1 " + R1 + " -2 " + R2 + " --un-conc-gz bw2-full-results-DONT-PUSH/bw2-R1-ara-un-conc.fq.gz --al-conc-gz bw2-full-results-DONT-PUSH/bw2-R1-ara-al-conc.fq.gz -S bw2-full-results-DONT-PUSH/bw2-R1-ara-alignments.sam 2> bw2-full-results-DONT-PUSH/bw2-R1-ara-output.stdout"
    myBwt2 = os.popen(cmd_bt2).read()
    print(myBwt2)
    
    return(True)



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
        print('You are reading the following files: ' + str_sam_file)
 
        with open(str_sam_file,"r") as fn:            
            count_ln=0
            #print('\n\nSam (ouput) file name: ' + f_file)
            #header = 'FILE_NAME Algn.Conc.0 Algn.Conc.1'
            #ln_str2 = header.split(' ')
            #samlist.append(ln_str2)
            for line in fn:
                count_ln+=1
                if (count_ln>6) & (count_ln<10):
                    ln=line.strip()
                    ln_end = ln.find(')')
                    ln_str = ln[1:ln_end+1]              
                    ln_str = f_file[0:10] + ' '  + ln_str 
                    #print(ln_str)
                    ln_str2 = ln_str.split(' ')
                    #print(ln_str2)
                    samlist.append(ln_str2)
                        
    #print('fname:' , d.f_name , ' ' , 'Treads:' , d.reads, ' ' , 'Concor0:' , d.concor, 'Concor1:', d.concor1 )         
    #print(samlist)
    print('\nComparative table of SAM output results\n')
    print('FILE_NAME\tAlgn.Conc.0\tAlgn.Conc.1\n')
    for i in samlist:
        print(i[0], i[1:])    



    return(samlist)      # return the value to the code that called this function
           

#Get the path of the folder to parse
dir_f =sys.argv[1]

#specify what process to run
#   1:Fastqc    2:Bowtie2   3:Parse Sam output
funct_to_execute = sys.argv[2]

#store the fastqc results 
dir_name = sys.argv[3] 

##################  HERE ARE CALL THE FUNCTIONS ################################

# FUNCTION TO RUN THE FASTA QUALITY PROCESS
 
if funct_to_execute=='1':
    print('You are running the FASTQC function:' + funct_to_execute)
    if fastaf_quality(dir_f): print("Fasta file process done")
elif funct_to_execute=='2':
    # ASSUMING THE INDEX PROCESS WAS DONE PREVIOUSLY 
    # FUNCTION TO RUN THE BOWTIE PROCESS with PE
    fastaR1 = 'R1'
    fastaR2 = 'R2'
    idx_base = 'Base'
    bow1 = bowtie2_f() 
    if bow1: print('Done bwt2')
elif funct_to_execute=='3':
    print('You are running the SAM cheking function:' + funct_to_execute)
    # FUNCTION TO GET THE BOWTIE2 RESULTS
    samlist = bowtie2_read_std_out(dir_f)
    # Send the sam_list resume table to the screen
    #for sam in samlist:
    #  print(sam)
else:
    print("Function not available, 1:Fastqc    2:Bowtie2   3:Parse Sam Output ")






