
clustal_input_file = "input.fasta"

### PROCESS PASTED SEQUENCES
def process_sequences(sequence_string):
    with open (clustal_input_file, "w") as fd:
            print (sequences, file=fd)
    # Generates a file.fasta with the pasted sequences

### PROCESS PASTED UNIPROT IDs
import requests as r
from Bio import SeqIO
from io import StringIO

def process_uniprot(id_list):
    baseUrl="http://www.uniprot.org/uniprot/"
    fd = open (clustal_input_file, "w")
    for id in id_list:
        currentUrl=baseUrl+id+".fasta"
        response = r.post(currentUrl) # request to uniprot
        cData=''.join(response.text)
        print(cData, file=fd)
    fd.close()

id_list = ("P38398", "P51587")
process_uniprot(id_list)

### EXECUTE CLUSTALO
from Bio.Align.Applications import ClustalOmegaCommandline
import os

output_format = "fasta"

# a2m=fa[sta],clu[stal],msf,phy[lip],selex,st[ockholm],vie[nna]} MSA output file format (default: fasta)

def execute_clustalo(in_file):
    clustalomega_cline = ClustalOmegaCommandline(infile = in_file, outfile = "outfile", outfmt = output_format, verbose = True, auto = False)
    o = str(clustalomega_cline)
    stream = os.popen(o)
    output = stream.read()
    output

# Generates an output file with the alignemnt in desired format