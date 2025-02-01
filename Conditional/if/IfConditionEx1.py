#is number or not
a=input("Enter a value :")
msg = "\t{} is not a Number."
if (a.isdigit()):
    msg = "\t{} is a Number."
print(msg.format(a))