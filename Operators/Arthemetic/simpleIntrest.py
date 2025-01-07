#write a Program to calculate the Simple Interest is i= ptr/100
from functools import total_ordering

print("*"*40)
print('\t Calculate the Simple Interest:')
print("*"*40)
p = float(input('Enter Principal Amount value(numeric only):'))
t = float(input('Enter term(time) value(numeric only):'))
r = float(input('Enter rate of interest value(numeric only):'))
si = (p*t*r)/100
total_amount = p + si
print("-"*40)
print('\t Calculated Simple interest is : {}'.format(si))
print('\t Calculated Total Amount is : {}'.format(total_amount))
print("-"*40)