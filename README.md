# rnaSMART - tool for identification of Structural Motifs Across Transcripts

### Requirements

Python 3.5 required.

+ matplotlib 
+ pybedtools    
+ fastcluster    
+ scipy    
+ BEDTools    
+ java
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install matplotlib```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install pybedtools```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install fastcluster```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install scipy```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```sudo apt-get install bedtools```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```sudo apt-get install java```
  

Additionally you need to give permisions to aligning program clustalw2:   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```chmod +x clustalw2```

### Usage

The main file of rnaSMART program is *rnaSMART.py* file. To show program help type:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python3 rnaSMART.py -h```

### Options
#### Required

-i, --input 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input file in FASTA format, requires seqence and structure
#### Optional

-h, --help  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show help message and exit

-o, --output  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output file name. Default: rnaSMART_result_sst_sqt.txt

-t, --threads 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of threads to use. Default: 1

-sst, --secondary_structure_threshold  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clustering threshold for RNAs sequences. Default: 50

-sqt, --sequence_threshold   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clustering threshold for RNAs sequences. Default: 50

-sh, --single_hairpin  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include single hairpin motifs in analysis. Significantly increases analysis time. Default: false

-a, --alignment  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The result motifs are presented as alignment with 4sale tool. Default: fasta format result

-r, --save_redundancy  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Not removing redundant motifs. Useful when looking for small motifs

### Input

rnaSMART requires input file in fasta-like format, containing both sequences and secondary structures in dot-bracket format.
Sample input file is provided in "sample" folder.

"RNASTRAND.fasta" consists of 401 RNA sequences obtained from [RNA STRAND](http://www.rnasoft.ca/strand/) database.
Sequences were pre-filtered. Pseudoknots, non-canonical base pairs, single hairpins and uncomplete sequences were removed.

### Output file

rnaSMART saves one output file with all motifs that were found. The file structure is as follows:
1. Line with each motif definition starts with "@" sign. It contains such informations as:
+ order number, e.g. *ID: 33;*
+ motif abstract shape, e.g. *Shape: [[][][]];*
+ number of motif parents - motifs with overlapping structures, e.g. *Parent: 0, 1, 2, 4, 19, 23, 25;*
+ number of RNAs within motif, e.g. *Count: 15;*
+ motif length median, e.g. *Length: 100.0;*
+ median of structure distance within RNAs in motif, e.g. *Distance_str: 34,86;*
+ median of sequence distance within RNAs in motif, e.g. *Distance_seq: 21,56;*
2. Next lines contains RNAs in motif:
+ id that starts with *>*
+ RNA sequence
+ RNA structure

Sample output file *rnaSMART_results_50_50_CIO0U.txt* in fasta format is provided in "sample" folder.

If user adds -a, --alignent option, the result RNAs will be aligned within the motif. Sample output file *rnaSMART_results_50_50_4HM09.txt* in alignment format is provided in "sample" folder.

### Commands used to generate sample output files
Fasta format result

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python3 rnaSMART.py -i RNASTRAND.fasta -sst 50 -ssq 50``` 

Aligned format result:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python3 rnaSMART.py -i RNASTRAND.fasta -sst 50 -ssq 50 -a``` 

### Contribute

If you notice any mistakes in content or formatting, please send a pull request with your correction.

### Licence

This project is licensed under the terms of the GNU General Public License v3.0 license.
