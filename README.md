# Data-Mining-Algo-Implementations

Naive Bayes:
Go to the destination folder and type
$ python nb.py
The current program takes into account the csv file. In order to test a tab delimited file please change row 128 of the program to:
reader = csv.DictReader(csvfile), delimiter=’/t’
The program takes any sample file and determines the attribute labels and values. It then prompts the user to choose the predictor label for which classificiation is to be done
For the remaining attributes it prompts the user to enter values and then perform frequency matrix and probability calculation and displays the output
