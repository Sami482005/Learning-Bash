'''
This script aims to:
1. Search NCBI for complete Klebsiella Pneumoniae plasmids
2. Write the accession keys in a text file
3. Extract each fasta file from each accession key and save the fasta files in data/genomes
'''

# Importing libraries
import os
from Bio import Entrez, SeqIO

def Retrieving_Accession_Keys(species, output_path):
    '''
    This function retrieves the accession keys from NCBI for a given species.

    param:
    -------
    species: str
        The species to search for in NCBI
    output_path: str
        The path of the text file to save the accession keys
    '''
    # Setting the email
    Entrez.email = "samielsalibi9@gmail.com"
    search_term = f'({species}[Organism]) AND plasmid[filter] AND (ddbj_embl_genbank[filter]) AND ("complete sequence"[Title])'
    handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=9000)
    record = Entrez.read(handle)
    handle.close()
    accession_keys = record['IdList']
    with open(output_path, 'w') as file:
        for key in accession_keys:
            file.write(key + '\n')
    print(f'{len(accession_keys)} accession keys have been saved in {output_path}')
    return accession_keys


def Extracting_Fasta(accession_keys):
    '''
    This function extracts the fasta files from NCBI for a given list of accession keys.

    param:
    -------
    accession_keys: list
        The list of accession keys to extract the fasta files from
    
    '''
    # Setting the email
    Entrez.email = "samielsalibi9@gmail.com"
    for key in accession_keys:
        handle = Entrez.efetch(db="nucleotide", id=key, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        with open(f'data/genomes/{key}.fasta', 'w') as file: #did not take output path because it is fixed
            file.write(f'>{record.id}\n{record.seq}')
        print(f'{key} fasta file has been saved in data/genomes')


