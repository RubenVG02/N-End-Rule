

elements_yeast={"M":1200,
                   "G":1200,
                   "A":1200,
                   "S":1200,
                   "T":1200,
                   "V":1200,
                   "P":1200,
                   "I":30,
                   "E":30,
                   "Y":10,
                   "Q":10,
                   "L":3,
                   "F":3,
                   "D":3,
                   "K":3,
                   "R":2}

elements_mammals={"M":30,
                   "G":30,
                   "A":4.4,
                   "S":1200,
                   "T":7.2,
                   "V":100,
                   "P":20,
                   "I":20,
                   "E":1,
                   "Y":2.8,
                   "Q":10,
                   "L":5.5,
                   "F":1.1,
                   "D":1.1,
                   "K":1.3,
                   "R":1,
                   "H":3.5,
                   "W":2.8,
                   "S":1.9,
                   "N":1.4,
                   "C":1.2,
                   "Q":0.8}

elements_bacteria={"V":600,
                   "M":600,
                   "G":600,
                   "P":600,
                   "I":600,
                   "T":600,
                   "L":2,
                   "A":600,
                   "H":600,
                   "W":2,
                   "Y":2,
                   "S":600,
                   "N":600,
                   "K":2,
                   "C":600,
                   "D":600,
                   "F":2,
                   "E":600,
                   "R":2,
                   "Q":600} 

def predict_lifetime(organism="", target=""):
    organisms=["yeast","mammals","bacteria"]
    last_aa=target[-1]
    lifetime=0
    if organism.lower()==organisms[0]:
        for i in elements_yeast:
            if i==last_aa:
                lifetime=(elements_mammals[i]*2)/60
    elif organism==organisms[1]:
        for i in elements_mammals:
            if i==last_aa:
                lifetime=elements_mammals[i]*2
    elif organism==organisms[2]:
        for i in elements_bacteria:
            if i==last_aa:
                lifetime=(elements_bacteria[i]*2)/60
    else:
        print("Organism not found")
        
    return lifetime
    

predict_lifetime("yeast","SWDEFVDRSVQLFRADPESTRYVMKYRHCDGKLVLKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM")