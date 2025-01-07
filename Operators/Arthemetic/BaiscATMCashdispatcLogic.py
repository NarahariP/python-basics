#write a Program which will accept a numerica value as rupees and decide and how many 500, 200 and 100 rupees note will be dispatched.
print("*"*40)
print('\t Calculate the (a^m/a^n) - Way1:')
print("*"*40)
amount = float(input('Enter withdrawal amount value(numeric only):'))
notes_500 = amount//500
amount = amount%500
notes_200 = amount//200
amount = amount%200
notes_100 = amount//100
amount = amount%100
print("-"*40)
print('\t Total dispatched 500 Rupees notes  is : {}'.format(notes_500))
print('\t Total dispatched 200 Rupees notes  is : {}'.format(notes_200))
print('\t Total dispatched 100 Rupees notes  is : {}'.format(notes_100))
print('\t Remaining Balance is : {}'.format(amount))
print("-"*40)