#write a Program to achieve the (a+b)^2
print("*"*40)
print('\t Calculate the (a+b)^2 - Way1:')
print("*"*40)
a = float(input('Enter \'a\' value(numeric only):'))
b = float(input('Enter \'b\' value(numeric only):'))
r1 = (a**2) + (2*a*b) + (b**2)
print("-"*40)
print('\t Calculate value of (a+b)^2 is : {}'.format(r1))
print("-"*40)
print('\t Calculate the (a+b)^2 - Way2:')
r2 = (a+b)*(a+b)
print("-"*40)
print('\t Calculate value of (a+b)^2 is : {}'.format(r2))
print("-"*40)