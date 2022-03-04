"""
Project Name: Rabbits Rabbits Rabbits
Author: Robbie Platt
Due Date: 2022-03-05
Course: CS1400



I learned how to use a while loop, write to a file, 
 using the fibonacci sequence and using f statements. 
This program will show a table of rabbits for the user to 
know when the cages will run out.

"""

def do_research(cages, adults, babies):
    """
    The function that runs everything. It will take parameters from run_rabbits.py.
    """
    month = 1
    total = adults + babies
    with open("rabbits.csv", "w") as out:
        out.write(f"# Table of rabbit pairs" + "\n")
        out.write(f"Month, Adults, Babies, Total" + "\n")
        adults_zero = 0
        while total < num_cages:
            babies = 
        out.write(f"Cages: {cages}\n")
        out.write(f"Adults: {adults}\n")
        out.write(f"Babies: {babies}\n")

