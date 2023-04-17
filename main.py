from predictor import predict_lifetime
from mega import Mega
import base64

def upload_to_mega(file):
    # This function will upload the file to mega.nz
    mega=Mega()
    mail=""
    #passw=base64.b64decode("J2NudncnZDkwY253cTljcG53cW5lamR3cHFjbm1qZXcnYzlu")
    passw=passw.decode("UTF-8")
    passw=""
    mega.login(mail, passw)
    upload=mega.upload(file)
    link=mega.get_upload_link(upload)
    print(link)

 
 
def default_file(output_file="sequences.csv"):
    '''
    Function to create a default file with the headers of the csv file

    Parameters:
    -output_file (str): Name of the output file. Default: sequences.csv
    '''
    with open(output_file,"w") as file:
        file.write("sequence,lifetime(hours)") 

def predictor(organism="yeast", upload_mega=True, output_file="sequences.csv", input_file="input.txt"):
    '''
    Function to predict the lifetime of a sequence of a given organism and save the results in a csv file

    Parameters:
    -organism (str): Name of the organism. Example: yeast
    -upload_mega (bool): If True, the file will be uploaded to mega.nz. Default: True
    -output_file (str): Name of the output file. Default: sequences.csv
    -input_file (str): Name of the input file. Default: input.txt
    
    '''
    default_file()
    sequences=[]
    lifetimes=[]
    with open(input_file,"r") as f:
        for sequence in f:
            sequence=sequence.replace("\n","")
            sequences.append(sequence)
            lifetime=predict_lifetime(organism, sequence)
            lifetimes.append(lifetime)
    results=list(zip(sequences,lifetimes))
    with open(output_file,"a", newline="") as f:
        for i in range(len(results)):
            f.write(f"\n{sequences[i]},{lifetimes[i]:.2f}")
    if upload_mega==True:
        upload_to_mega("sequences.csv")
    
predictor()