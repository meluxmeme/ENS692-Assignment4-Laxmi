"""
calgary_dogs.py

A terminal-based application for computing and printing detailes of dog breed based on user input breed.
Detailed specifications are provided via the Assignment 4 README file.

Author: Laxmi Paudel
"""
import numpy as np
import pandas as pd
import re
class DogBreed:

    def user_input(userInputDog, breed):
        """
        Validate user input against the breed names in the dataframe.

        Parameters:
        - user_input_dog (str): The dog breed entered by the user.
        - breed (list): List of all valid dog breed names.

        Returns:
        - str: The validated and normalized dog breed name in uppercase.

        Raises:
        - ValueError: If the dog breed is not found in the list of valid breeds.
        """
        if (userInputDog.upper() in breed ):

             return userInputDog.upper()
        else:
            raise  ValueError("Dog breed not found, please try again")


    def yearly_stat(userInputDog, dataFrame):
        """
        Compute and print yearly and across all year statistics for the given dog breed.

        Parameters:
        - user_input_dog (str): The dog breed that user entered in uppercase.
        - data_frame (DataFrame): The pandas DataFrame containing dog breed data.
        """
        idx = pd.IndexSlice
        #slicing only the user input dog breed data.
        SortedDog = dataFrame.loc[idx[userInputDog,:,:],:]
        #list out the years that given dog breed data has
        year = SortedDog.index.get_level_values('Year').unique().tolist()
        print(f"The {userInputDog} was found in the top breeds for years: {", ".join(str(year) for year in year)}")

        #sum the total user input dog breed yearly.
        total_userinputBreed_yearly = SortedDog.groupby('Year')['Total'].sum()
        #sum the total dog breed yearly.
        totalBreed_yearly = dataFrame.groupby('Year')['Total'].sum()
         #sum  all dog breed in all year.       
        total_accross_allYear = dataFrame['Total'].sum()
         #sum  only user input dog breed in all year.         
        total_InputBreed_accross_allYear = SortedDog['Total'].sum()
        print(f"There have been  {total_InputBreed_accross_allYear} {userInputDog} dogs registered total.")

        #print and calculate percentage of user input dog breed based on total dog breedd yearly using loop through out the given year.
        for year in year:
            yearly_total = totalBreed_yearly.get(year,0)
            yearly_total_UserinputBreed = total_userinputBreed_yearly.get(year)
            breed_percentage_yearly = yearly_total_UserinputBreed/yearly_total *100
            print(f"The {userInputDog} was {breed_percentage_yearly} of top breed in {year}.")

        breed_percentage = total_InputBreed_accross_allYear/total_accross_allYear*100
        print(f"The {userInputDog} was {breed_percentage} of top breed accross the year.")

    def popular_month(userInputDog, dataFrame):
        """
        Find and print the most popular months for the given dog breed.

        Parameters:
        - user_input_dog (str): The dog breed.
        - data_frame (DataFrame): The pandas DataFrame containing dog breed data.
        """
        idx = pd.IndexSlice
        #slicing only the user input dog breed data.
        SortedDog = dataFrame.loc[idx[userInputDog,:,:],:]  
         #list out and print the months that given dog breed data has.    
        popular_months = SortedDog.index.get_level_values('Month').value_counts()
        max_occurrence = popular_months.max()

        most_popular_months = popular_months[popular_months == max_occurrence].index.tolist()
        most_popular_months.sort()
        print(f"Most popular month for the {userInputDog} is : {" ".join(most_popular_months)}")
            #   {", " .join(str(i) for i in popular_userinputBreed_months)}")


def main():

    dataFrame = pd.read_excel('CalgaryDogBreeds.xlsx')
    print("ENSF 692 Dogs of Calgary")
    dataFrame.set_index(['Breed','Year','Month'],inplace=True)
    breed = dataFrame.index.get_level_values('Breed').unique().tolist()
    #Prompt the user until the user enter correct dog breed, case does not matter
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
