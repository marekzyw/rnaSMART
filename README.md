# rnaSMART - tool for identification of Structural Motifs Across RNA Transcripts

## Installation

rnaSMART require Python 3.5 or higher and following Python3 libraries:
+ matplotlib 
+ pybedtools    
+ fastcluster    
+ scipy    

Also, following software should be installed on your system:
+ BEDTools
+ java 

On Debian-based systems (e.g. Ubuntu) you can simply follow the instructions:

 1. Make sure you have Python 3.5 or higher on your system:
 
	 ```python3 --version```
	 
 3. Install python dependencies:
 
	 ```pip3 install matplotlib pybedtools fastcluster scipy```
	 
 4. Install bedtools and java:
 
 	 ```sudo apt-get install bedtools java```

 5. Download latest version of rnaSMART by clonning this repository:
 
	 ```git clone https://github.com/marekzyw/rnaSMART.git```
	 
	 or download a .zip package and unpack it:
   
	 ```wget https://github.com/marekzyw/rnaSMART/archive/master.zip```
	 
	 ```unzip rnaSMART-master.zip```
 
 &nbsp;

## Quick start

The main file of rnaSMART program is *rnaSMART*. To run rnaSMART on provided example file with default parameters and using your system's default python3 interpreter, enter the *sample* directory and type:

```../rnaSMART -i RNASTRAND.fasta```
	 
To show full list of available  options type:

```rnaSMART -h```

&nbsp;

## Detailed usage
### Options
#### Required

-i, --input 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input file in FASTA format, containing sequences and secondary structures in dot-bracket notation (see below for details)
#### Optional

-h, --help  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show help message and exit

-o, --output  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output file name. Default: rnaSMART_result_sst_sqt.txt

-t, --threads 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of threads to use. Default: 1

-sst, --secondary_structure_threshold  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clustering threshold for structural similarity. Default: 50

-sqt, --sequence_threshold   

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clustering threshold for sequence similarity. Default: 50

-sh, --single_hairpin  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include single hairpin motifs in analysis. May significantly increase analysis time. Default: false

-a, --alignment  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Produce structural alignment of motif members. May significantly increase analysis time. Default: unaligned fasta format 

-r, --save_redundancy  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do not remove redundant motifs. Useful when looking for small motifs

### Input

rnaSMART requires input file in fasta-like format, containing both sequences and secondary structures in dot-bracket format.:

    >PDB_00866_synthetic
    AGACAUGUCAGACAGUGUC
    .(((..))).((((.))))
    >PDB_00965_synthetic
    UGUCUAAGACUGGUCUAAGAC
    .(((...)))..(((...)))

Sample input file is provided in "sample" folder. *RNASTRAND.fasta* consists of 401 RNA sequences obtained from [RNA STRAND](http://www.rnasoft.ca/strand/) database. Sequences were pre-filtered. Pseudoknots, non-canonical base pairs, single hairpins and incomplete sequences were removed.

### Output file

rnaSMART saves one output file with all motifs that were found, using a following format:

    @ID: 23; Shape: [][][[][]]; Parent: self; Count: 2; Length: 134.5; Distance_str: 9.38; Distance_seq: 18.47
    >CRW_00749_GII|52-180
    GAGGUGAAAGUCCUCCUCCCGAAUCGUUCAUGGGAGAGUCUAUCCAGACUUGCGUAGCGAGUAAUCGCUAGGUGAGAAGCUCUGGAGACAAUGUACCUGCCCUUCAAUUGGAGGUGCCAGGGCUAGGCU
    ((((.......))))((((((.........))))))((((((.((((((((((.((((((....)))))).)))))....))))).............(((((...............)))))))))))
    >CRW_00726_GII|80-219
    GUAGUUUAAGGUACUACUCUGUAAGAUAACACAGAAAACAGCCAACCUAACCGAAAAGCGAAAGCUGAUACGGGAACAGAGCACGGUUGGAAAGCGAUGAGUUACCUAAAGACAAUCGGGUACGACUGAGUCGCAAUGUU
    (((((.......)))))(((((........))))).((((.((((((...(((...(((....)))....)))...........))))))...(((((....(((((..........))))).......)))))..))))
Sample output file *rnaSMART_results_50_50_CIO0U.txt* in fasta format is provided in "sample" folder.

The file structure is as follows:
1. Line with each motif definition starts with "@" sign. It contains such informations as:
+ order number, e.g. *ID: 33;*
+ motif abstract shape, e.g. *Shape: [[][][]];*
+ IDs of parent motifs - motifs with overlapping structures, e.g. *Parent: 0, 1, 2, 4, 19, 23, 25;*
+ number of RNAs within motif, e.g. *Count: 15;*
+ median of motif members lengths, e.g. *Length: 100.0;*
+ median of structure distance within RNAs in motif, e.g. *Distance_str: 34,86;*
+ median of sequence distance within RNAs in motif, e.g. *Distance_seq: 21,56;*
2. Next lines contains RNAs in motif:
+ id that starts with *>*
+ RNA sequence
+ RNA structure



If user adds *-a, --alignent* option, the additional result file will be generated where sequences and structures of motif members will be aligned using *4sale* tool:

    @ID: 22; Shape: [][][[][]]; Parent: self; Count: 2; Length: 134.5; Distance_str: 9.38; Distance_seq: 18.47
    >CRW_00749_GII|52-180 G-AGGUGAAAGUCCU-CCUCCCGAAUCGUUCAUG-GGAGAGUCUAUCCAGACUUG--CGU--AGCGAGUAAUCGCUA-GGUGAGA-AGC-U--CUGGAGA-CAAUGUACCUGCCCUU---CAAUUGGAGGUG-CC-AGG-GCUAGGCU
    (-(((.......)))-)((((((.........))-))))((((((.(((((((((--(.(--(((((....))))))-.))))).-...-)--))))...-..........(((((.---............-..-)))-))))))))
    >CRW_00726_GII|80-219 GUAGUUUAAGGUACUAC-UCU-GUAA-GAUAACACAGAAAA-C-AGCCA-ACCUAACCGAAAAGCGAA-AGCUGAUACGGGAACAGAGCACGGUUGGAAAGCGAUG-AGUUACCUAAAGACAAUCGGGUACGACUGAGUCGCAAUGUU
    (((((.......)))))-(((-((..-......))))).((-(-(.(((-(((...(((...(((...-.)))....)))...........))))))...(((((.-...(((((..........))))).......)))))..))))

 Sample output file *rnaSMART_results_50_50_4HM09.txt* in alignment format is provided in "sample" folder.

### Commands used to generate sample output files
Fasta format result

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```rnaSMART -i RNASTRAND.fasta -sst 50 -ssq 50``` 

Aligned format result:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```rnaSMART -i RNASTRAND.fasta -sst 50 -ssq 50 -a``` 

### Contribute

If you notice any errors and mistakes, or would like to suggest some new features, please use Github's issue tracking system to report it. You are also welcome to send a pull request with your corrections and suggestions.

### Licence

This project is licensed under the terms of the GNU General Public License v3.0 license.

