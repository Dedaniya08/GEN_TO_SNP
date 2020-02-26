print("Written by Akshay Dedaniya")
print("Project Scientist, CCMB")
print("Email to akshay@ccmb.res.in")


import pandas as pd
import numpy as np
import sys
import os

currentDirectory = os.getcwd()
filename = sys.argv[1]
Sample_name = sys.argv[2]
output_filename = sys.argv[3]

print("Inpute file name is :" +filename)
print("Sample file name is :" +Sample_name) 
print("Output file name is :" +output_filename) 

def test_argmax(np_array):
	if np.max(np_array) > 0:
		return np.argmax(np_array)
	else:
		return np.nan
		print(yyy)

def identify(row,columnss):
	swss=[];
	swss=np.split(row,columnss);
	yyy=np.apply_along_axis(test_argmax, 1, swss);
	yyy=yyy+1;
	return yyy;

def Process(filename,Sample_name,output_filename):		
	File_To_read = pd.read_csv(filename,compression='gzip',header=None,sep=' ',na_filter = True,skip_blank_lines=True)
	Only_genotype=File_To_read.drop([0,1,2,3,4],axis=1);
	Only_genotype_modified=Only_genotype.dropna(axis='columns');
	Only_genotype_modified_values=Only_genotype_modified.values;
	RSID_LIST=list(File_To_read.loc[:,1]);
	rowss = int(Only_genotype_modified.shape[0]);
	columnss=int((Only_genotype_modified.shape[1])/3);
	Sample_ID_LIST = pd.read_csv(Sample_name,header= 0,sep=' ')
	Sample_ID_LIST_modified=Sample_ID_LIST.drop(Sample_ID_LIST.index[0]);
	Sample_ID_LIST_modified=Sample_ID_LIST_modified['ID_1'];
	Sample_ID_LIST_modified_as_column=list(Sample_ID_LIST_modified.values.reshape((1,columnss)));
	final_file=np.zeros((rowss,columnss));
	for row,jj in zip(Only_genotype_modified_values,range(0,rowss)):
		final_file[jj,:]=np.array(identify(row,columnss));      
	FINAL = pd.DataFrame(final_file,columns=Sample_ID_LIST_modified_as_column,index=RSID_LIST,dtype=int)
	FINAL.to_csv(output_filename, sep=' ', mode='a')
 
Process(filename,Sample_name,output_filename)


print(" The process is done ")
