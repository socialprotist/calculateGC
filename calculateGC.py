"""
python calculateGC.py test.fas

This will output a tab delimited file (.tsv) which can be opened in Excel.
This calculates the GC% of each contig. 

(c) Matthew Brown, Ph.D | 4/30/2018

"""


import os, glob, sys

fastafile = sys.argv[1]

def oneline(input):
 infile = open(input, "r")
 lines = infile.readlines()
 infile.close()
 outfile = open(input,'w')
 for i,line in enumerate(lines):
	if line[0] == ('>'):
		if i>0:
			outfile.write("\n")
		outfile.write(line)
	else:
		line = line.strip()
		#line = line.replace('-','')  ######## Add if you want to remove gaps!!!
		outfile.write(line)
 outfile.close()


def content(input):
 infile = open(input,"r")
 lines = infile.readlines()
 infile.close()
 outfile= open("%s.ATGC.tsv" %(input),"w")
 outfile.write('SeqID\tA_count\tC_count\tG_count\tT_count\tContigLength\tGC_Percentage\n')
 for line in lines:
	if line[0]==">":
		seqid = line.split(">")[1]
		seqid = seqid.strip()	
	else:
		length = len(line)
		A_count = line.count('A')
		T_count = line.count('T')
		G_count = line.count('G')
		C_count = line.count('C')
		CG_percentage = float(C_count + G_count) / length
		outfile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(seqid, A_count, C_count, G_count, T_count, length, CG_percentage))
 outfile.close()

oneline(fastafile)
content(fastafile)