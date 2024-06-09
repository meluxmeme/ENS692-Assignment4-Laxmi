# calgary_dogs.py
# AUTHOR NAME: Laxmi Paudel
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.
import numpy as np
import pandas as pd
def main():

    dataFrame = pd.read_excel('CalgaryDogBreeds.xlsx')
    print("ENSF 692 Dogs of Calgary")
    dataFrame.set_index(['Breed','Year','Month'],inplace=True)

    #print(dataFrame)
    while True:
        try:
            userInputDog = input("Enter Dog breed name:  ")
            if (userInputDog in dataFrame.index.get_level_values('Breed')):
                print("Dog breed found in the database")
                break
            else:
                raise  ValueError("The dog breed is not found, enter again")
        
        except ValueError as e:
            print(e)

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
