#(Rounding Numbers) Investigate built-in function round at
#https://docs.python.org/3/library/functions.html#round
#then use it to round the float value 13.56449 to the nearest integer, tenths, hundredths
#and thousandths positions.

num = 13.56449

print(round(num))          # nearest integer    =14
print(round(num, 1))       # tenths position    =13.6  
print(round(num, 2))       # hundredths position = 13.56
print(round(num, 3))       # thousandths position = 13.564
