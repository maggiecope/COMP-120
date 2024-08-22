"""
Module: dna_profiler

A program to use short tandem repeats (STRs) to identify a person using their
DNA.

Authors:
    1) Maggie Cope - mcope@sandiego.edu
"""

from typing import Tuple, List, Dict
import sys
from sys import argv

def read_dna_sequence(sequence_filename:str) -> str:
    """ 
    This function will open the DNA sequence file, read it in, and return it as a string.

    Parameters: 
    sequence_filename(str): The name of a file containing a DNA sequence 

    Return:
    line(str): returns the dna sequence as a string 

    >>> read_dna_sequence('alice.txt')
    'AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA'

    >>> read_dna_sequence('bob.txt')
    'AACCCTGCGCGCGCGCGATCTATCTATCTATCTATCCAGCATTAGCTAGCATCAAGATAGATAGATGAATTTCGAAATGAATGAATGAATGAATGAATGAATG'

    """
    f = open(sequence_filename, 'r')
    line = f.readline()
    line = line.strip('\n')
    return line 

def create_dna_profiles(profiles_filename:str) -> [list,dict]:
    """This function will read the STR data for each person listed in the DNA database file, 
    returning that data as a tuple of a list or strs, and a dictionary of the profiles


    Parameters:
    profiles_filename(str): The name of the file the information about the STRs for each person 

    Return:
    tuple of STR(list) and profiles(dict)
    STR(list): list of the STRS given in the file
    profiles(dict): dictionary that associates the name of each person with their amount of STR

    >>> create_dna_profiles('dna_database.csv')
    (['AGAT', 'AATG', 'TATC'], {'Alice': [5, 2, 8], 'Bob': [3, 7, 4], 'Charlie': [6, 1, 5]})
    """

    f = open(profiles_filename,'r')

    line = f.readline()
    line = line.strip('\n')
    line = line.split(',')
    #creates list of the STRS in the file
    STR = line[1:]


    #creates a dictionary that associates names to their respective amount of each str 
    profiles = {}
    for line in f:
        x = line.split(',')
        name = x[0]
        str_amount = x[1:]
        profiles[str(name)]= [int(i) for i in str_amount]
    
    return STR, profiles



def find_max_consecutive(dna:str,target:str) -> int:
    """This function will take in a DNA sequence and an STR and return the maximum number of times that STR appears consecutively in the sequence.


    Parameters:
    dna(str): The DNA strand to search for the STRs in
    target(str): The STR that you are searching for

    Returns: 
    max(int): maximum number of times the target STR shows up consecutively in the given DNA sequence. 

    >>> find_max_consecutive('ATAACACTT','AC')
    2
    >>> find_max_consecutive('AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA','AGAT')
    5

    """
    max_consecutive = 0 
    for i in range(len(dna)):
        #count is reset to 0 and consecutive is reset to true 
        count = 0
        consecutive = True
        while consecutive ==True:
            start = i + len(target) * count
            end = start + len(target) 
            if dna[start:end] == target:
                #counts each time the target appears in the dna consecutively 
                count +=1
                if count>max_consecutive:
                    max_consecutive=count
            else:
                #once the target does not appear, consecutive is set to false and the while loop comes to and end
               
                consecutive = False 

    return max_consecutive

def identify_dna(mystery_dna:str, STR:list ,profiles:dict) -> str:
    """This function will take in the DNA profile data (which you processed in create_dna_profiles) and the DNA sequence to identify, 
    and returns a string containing the person who matched that DNA sequence.

    Return:
    name(str):returns the name of the person that matches the given DNA sequence 

    >>> STR,profiles = create_dna_profiles('dna_database.csv')
    >>> identify_dna('AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA',STR,profiles)
    'Alice'

    """
    #creates a list of the max consecutive strs in mystery_dna
    mystery_strs = []
    for i in STR:
        mystery_strs.append(find_max_consecutive(mystery_dna,i))     
    #checks to see if the values of each name in the dictionary profule match the myster_str
    for name in profiles:
        if profiles[name]==mystery_strs:
            #if they do match, returns the name of the profile with the matchinh str values
            return name
    #if none of the profiles in the profiles dictionary match mystery_strs returns "No match"
    return "No match"

def main(sequence_filename:str,profiles_filename:str) -> None:
    """
     This is the function that orchestrates the whole process of going from inputs to printing the name of the individual that matched the given DNA sequence.

    This function should print out the name of the person whose DNA matches that given in the sequence_filename file. 

    Parameters: 
    sequence_filename(str): The name of the file containing a DNA sequence. 
    profiles_filename(str): The name of the file the information about the STRs for each person 

    Returns:
    None 

    >>> main('bob.txt','dna_database.csv')
    'Bob'
    >>> main('alice.txt','dna_database.csv')
    'Alice'
    >>> main('charlie.txt','dna_database.csv')
    'Charlie'
    >>> main('nomatch.txt','dna_database.csv')
    'No match'
    """
    #calls the function read_dna_sequence with the parameter sequence_filename and assigns it to sequence
    sequence = read_dna_sequence(sequence_filename)

    #calls the function create_dna_profiles with the parameter profiles_filename as assigns it to STR,profiles
    STR,profiles = create_dna_profiles(profiles_filename)

    #calls the function indentify_dna with the new variables the other functions just created(sequence, STR,profiles as paramters)
    #assigns to name
    name = identify_dna(sequence,STR,profiles)

    #prints out the name of the person whose DNA matches that given in the sequence_filename file.
    print(name)


# keep the following code at the END of your file, as per convention
if __name__ == "__main__":
    #Checks that the user specified two filenames when running the program. If not, it prints out an error message and exit.
    if len(sys.argv) != 3:
        sys.exit("Usage: python data.csv sequence.txt")

    #If given two filenames, calls the main function with those filenames as the parameters.
    else:
        main(str(sys.argv[1]), str(sys.argv[2]))


