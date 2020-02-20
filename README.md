# GEN_TO_SNP


This python script help you to convert the imputed gen file from IMPUTE2 to normal snp.txt format.

This snp.txt format can be used in GEM R-package for interaction of genotype and environment (GxE). 

Soon I will upload the Ped/bim format which can beused for further anaylsis.




# Inside the Folder.

The folder consist of a script gentosnp.py which is the main script, addition to that sample name format 

which is required by the script to perform convertion into sample file.
    
    - Impute.gen.gz
    - Sample_file_Impute.sample
    - gentosnp.py




# How to run the script.

This is a simple way to go, Make sure you convert the main Imputed Gen.gz(consist of all chromosome file)

into seperate gen file based on chromosome.

```
python ./gentosnp.py Impute.gen.gz Sample_file_Impute.sample snp.txt

```

The first argument after the gentosnp.py is gen file which you want to convert, it can be per chromosome gen file. 

The second argument is the sample format which consist of sample Id usually the Impute sample format And the third

argument is the name of the output file, which every you wish to keep.


PLease look at the Impute.gen.gz and Sample_file_Impute for format.




## Contributing

All comments and any kind of contribution is useful. The best way is to open an issue or make a pull request.
