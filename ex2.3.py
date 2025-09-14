'''Q3.Compute the compound interest on an initial investment, for a defined
number of years and a fixed rate of interest. Print all of the values at the
end of each year in the form a table.'''
import math as m
p=int(input("Enter initial investment "))
roi=int(input("Enter rate of interest "))
n=int(input("Enter for how many years "))
for i in range(n):
    cy=int(input(f"Enter year {i+1}: "))

    am=p*(m.pow((1+(roi*0.01)),cy))
    print(f"Year {i+1}: ",am)
