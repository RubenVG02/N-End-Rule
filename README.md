
# Protein Lifetime Predictor (N-End Rule)

The N-End Rule was firstly discovered by Alexander Varshavsky in 1986. This rule describe the relationship between the presence of an specific aminoacid at the end of the N-terminal region of a protein, and the time required to be degraded. These values vary depending on the organism, so one specific aminoacid might have an approximate half-life bigger in one organism than in another. Therefore, the stability of the protein depends on the organism, and the ending aminoacid in N-terminal.

# Usage

First of all, in order to make a good prediction, the proteins must be in FASTA sequences. 

In order to make predictions using multiple FASTA files, you have to copy them in the "input.txt" file, one line per sequence. Then, execute the "main.py" script, and it will automatically create an csv file where you will have your results. There's an example on "sequences.csv". If you want to upload your results to Mega, you have to write a valid email and password in the "upload_to_mega" function in "main.py". With this function, you will obtain a link that redirects to your file.







## Authors

- [@RubenVG02](https://www.github.com/RubenVG02)


## Features

- Prediction of protein lifetime in Bacteria, Yeast and Mammals
- Possibility to predict multiple proteins at once
- Results can be automatically uploaded to Mega.nz


