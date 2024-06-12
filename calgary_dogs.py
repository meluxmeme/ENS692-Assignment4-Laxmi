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
import re
class DogBreed:

    def user_input(userInputDog, breed):


        if (userInputDog.upper() in breed ):
            #print("Dog breed found in the database")
             return userInputDog.upper()
        else:
            raise  ValueError("Dog breed not found, please try again")


    def yearly_stat(userInputDog, dataFrame):
        idx = pd.IndexSlice
        SortedDog = dataFrame.loc[idx[userInputDog,:,:],:]
        year = SortedDog.index.get_level_values('Year').unique().tolist()
        print(f"The {userInputDog} was found in the top breeds for years: {", ".join(str(year) for year in year)}")
        total_userinputBreed_yearly = SortedDog.groupby('Year')['Total'].sum()

        totalBreed_yearly = dataFrame.groupby('Year')['Total'].sum()
        # totalMentionedBreed = dataFrame.groupby('Year')['Total'].sum()
        # total_year = dataFrame.groupby('Year')['Total'].sum()
        # total_year_bybreed = SortedDog.groupby('Year')['Total'].sum()
        total_accross_allYear = dataFrame['Total'].sum()
        total_InputBreed_accross_allYear = SortedDog['Total'].sum()
        print(f"There have been  {total_InputBreed_accross_allYear} {userInputDog} dogs registered total.")
        for year in year:
            yearly_total = totalBreed_yearly.get(year,0)
            yearly_total_UserinputBreed = total_userinputBreed_yearly.get(year)
            breed_percentage_yearly = yearly_total_UserinputBreed/yearly_total *100
            print(f"The {userInputDog} was {breed_percentage_yearly} of top breed in {year}.")

        breed_percentage = total_InputBreed_accross_allYear/total_accross_allYear*100
        print(f"The {userInputDog} was {breed_percentage} of top breed accross the year.")

    def popular_month(userInputDog, dataFrame):
        idx = pd.IndexSlice
        SortedDog = dataFrame.loc[idx[userInputDog,:,:],:]       
        popular_userinputBreed_months = SortedDog.index.get_level_values('Month').unique().tolist()
        print(f"Most popular month for the {userInputDog} is : {", " .join(str(popular_userinputBreed_months) for popular_userinputBreed_months in popular_userinputBreed_months)}")


def main():
    # DogBreed = DogBreed
    dataFrame = pd.read_excel('CalgaryDogBreeds.xlsx')
    print("ENSF 692 Dogs of Calgary")
    dataFrame.set_index(['Breed','Year','Month'],inplace=True)
    breed = dataFrame.index.get_level_values('Breed').unique().tolist()
    # print(dataFrame)
    while True:
        userInputDog = input("Please enter a Dog breed:  ")
        userInputDogCase = userInputDog.upper()
        try:
            DogBreed.user_input(userInputDog, breed )
            DogBreed.yearly_stat(userInputDogCase, dataFrame)
            DogBreed.popular_month(userInputDogCase, dataFrame)
            break
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
