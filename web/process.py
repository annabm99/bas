
### PROCESS PASTED SEQUENCES
def process_sequences(sequence_string, clustal_input_file = "input.fasta"):
    with open (clustal_input_file, "w") as fd:
            print (sequence_string, file=fd)
    # Generates a file.fasta with the pasted sequences

### PROCESS PASTED UNIPROT IDs

def process_uniprot(ids, clustal_input_file = "input.fasta"):
    import requests as r
    from Bio import SeqIO
    from io import StringIO
    id_list = ids.split(", ")
    baseUrl="http://www.uniprot.org/uniprot/"
    fd = open (clustal_input_file, "w")
    
    for id in id_list:
        print(id)
        currentUrl=baseUrl+id+".fasta"
        response = r.post(currentUrl) # request to uniprot
        cData=''.join(response.text)
        print(cData, file=fd)
    fd.close()


### EXECUTE CLUSTALO

def execute_clustalo(output_format, input_file = "input.fasta"):
    from Bio.Align.Applications import ClustalOmegaCommandline
    import os
    clustalomega_cline = ClustalOmegaCommandline(infile = input_file, outfile = "outfile", outfmt = output_format, verbose = True, auto = False, force = True)
    o = str(clustalomega_cline)
    stream = os.popen(o)
    output = stream.read()
    output

# Generates an output file with the alignemnt in desired format