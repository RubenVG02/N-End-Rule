from predictor import predict_lifetime
import mega

def upload_to_mega(file):
    # This function will upload the file to mega.nz
    mega=mega.Mega()
    mega.login()
    file=mega.upload(file)
    link=mega.get_upload_link(file)
    print(link)

 
 
def default_file(name_file="sequences.txt"):
    #Function to create a default file for the output
    with open(name_file,"w") as file:
        file.write("sequence,lifetime") 

def predictor(organism="", target="", upload_mega=True, name_file="sequences.txt"):
    # This function will call the predict_lifetime function from predictor.py
    # and will return the lifetime of the protein
    # It will also upload the file to mega.nz
    default_file()
    with open(name_file,"a") as f:
        for target in f:
            lifetime=predict_lifetime(organism, target)
            f.write(f"{target},{lifetime}")

    if upload_mega==True:
        upload_to_mega("results.csv")
    
    return lifetime

default_file()