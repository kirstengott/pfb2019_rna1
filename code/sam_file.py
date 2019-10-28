import sys
import os    #to interact with the unix shell
import subprocess   #run some tools as subprocess from the shell

# Funtion to read and split the sam content file into a list
# In: sam file
# out: py list
def sam_content(sam_file):
    sam_cont=[]
    # open - split and append to the sam_list

    with open(sam_file,"r") as file_object: #cleans up after exiting
        for line in file_object:
    	    line = line.rstrip()
  	    #print(line)
	    sam_cont.append(line)
	    return sam_cont # return the value to the code that called this function

try:
    
    # call sam_cont function

except:
    print("Something wrong")


# PRINT THE LIST RESULTS
for sam in sam_cont: # parse the sam list
    seqs = sam_cont[sam]	
    print(sam,seqs[0:10])
    print('Done')
