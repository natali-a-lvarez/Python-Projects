import re

text = 'each The rain in Spain'
x = re.search("^each.*Spain", text)

if x:
    print("it IS a match")
else:
    print('it is NOT a match')