elements_yeast={"M":1200, #Methionine
                   "G":1200, #Glycine
                   "A":1200, #Alanine
                   "S":1200, #Serine
                   "T":1200, #Threonine
                   "V":1200, #Valine
                   "P":1200, #Proline
                   "I":30, #Isoleucine
                   "E":30, #Glutamic acid
                   "Y":10, #Tyrosine
                   "Q":10, #Glutamine
                   "L":3, #Leucine
                   "F":3, #Phenylalanine
                   "D":3, #Aspartic acid
                   "K":3, #Lysine
                   "R":2} #Arginine

elements_mammals={"M":30, #Methionine
                   "G":30, #Glycine
                   "A":4.4, #Alanine
                   "S":1200, #Serine
                   "T":7.2, #Threonine
                   "V":100, #Valine
                   "P":20, #Proline
                   "I":20, #Isoleucine
                   "E":1, #Glutamic acid
                   "Y":2.8, #Tyrosine
                   "Q":10, #Glutamine
                   "L":5.5, #Leucine
                   "F":1.1, #Phenylalanine
                   "D":1.1, #Aspartic acid
                   "K":1.3, #Lysine
                   "R":1, #Arginine
                   "H":3.5, #Histidine
                   "W":2.8, #Tryptophan
                   "S":1.9, #Serine
                   "N":1.4, #Asparagine
                   "C":1.2, #Cysteine
                   "Q":0.8} #Glutamine

elements_bacteria={"V":600, #Valine
                   "M":600, #Methionine
                   "G":600, #Glycine
                   "P":600, #Proline
                   "I":600, #Isoleucine
                   "T":600, #Threonine
                   "L":2, #Leucine
                   "A":600, #Alanine
                   "H":600, #Histidine
                   "W":2, #Tryptophan
                   "Y":2, #Tyrosine
                   "S":600, #Serine
                   "N":600, #Asparagine
                   "K":2, #Lysine
                   "C":600, #Cysteine
                   "D":600, #Aspartic acid
                   "F":2, #Phenylalanine
                   "E":600, #Glutamic acid
                   "R":2, #Arginine
                   "Q":600} #Glutamine

def predict_lifetime(organism="", target=""):
    '''
    Function to predict the lifetime of a sequence of a given organism and save the results in a csv file

    Parameters:
    -organism (str): Name of the organism. Example: yeast.
    -target (str): Sequence of the protein to predict the lifetime in FASTA format. 
    
    '''
    organisms=["yeast","mammals","bacteria"]
    last_aa=target[-1]
    lifetime=0
    if organism.lower()==organisms[0]:
        for i in elements_yeast:
            if i==last_aa:
                lifetime=(elements_mammals[i]*2)/60
    elif organism.lower()==organisms[1]:
        for i in elements_mammals:
            if i==last_aa:
                lifetime=elements_mammals[i]*2
    elif organism.lower()==organisms[2]:
        for i in elements_bacteria:
            if i==last_aa:
                lifetime=(elements_bacteria[i]*2)/60
    
    elif organism.lower() not in organisms:
        print("Organism not found")
    return lifetime
    

predict_lifetime("yeast","SWDEFVDRSVQLFRADPESTRYVMKYRHCDGKLVLKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM")