# printing
print('The universe was born 13.8 billion years ago.'); enter1=input(' ')
print("Let's start with when you were born."); enter2=input(' ')
# variables: name = value
#UserInput
age = int(input("How many years old are you? Enter Age: "))
# strings
# double and single quotation marks are pretty much interchangeable

# if,elif, else statements 
if age <= 30:
    firstString="Wow, "
    secondString=" is really young! Now is probably a good time to take on some risk."
    additionString= firstString + str(age) + secondString #age must be converted to str(), a Type Conversion, you can also use int() to converst a string to an integer
    print(additionString)
elif age <= 40:
    print('That is pretty young, and you are probably finding that maturity is a beautiful thing.') 
elif age <= 50:
    print('Most people say their best years are in their mid forties.')
elif age <= 60:
    print('You must have a great sense of who you are.')
else:
    print ('You must be very wise.')

enter20=input('')

print("The average life expectancy in the United States is 79 years."); enter4=input(' ')

#Arithmetic Operations
yearsLeft=79-age #subtraction
soyou="So you have about "
yrsleft=" years left."
alltog=soyou + str(yearsLeft) + yrsleft
print(alltog); enter15=input('')

percentComplete=age/78.69*100 #division and multiplication
andyou='And your life is '
per=' percent complete.'
alltog2= andyou + str(percentComplete) + per
print(alltog2)

#Boolean Variables
# True | False ; these must be capital in first letter
print('But True or False? Life is what you make it.'); enter5=input(' ')
boolVariable = True
print(boolVariable)

#Lists
listVariable = [1,0,6.7,True]

print('So remember that...'); enter6=input(' ')
#Dictionary Variable
dictVariable = {"key":"Meaning in life is built through taking on responsibility.",
                "key2": "You Suck!",
                "key3": "Potatoes!"}
print(dictVariable["key"])

#Functions
# def name(inputVariable1,inputVariable2):
#   code
#   more code
#no longer in function

def addOne(x):
    y=x+1
    return y

nextNumber=addOne(age)
on="On your next birthday, you will be "
combString = on + str(nextNumber)
print(combString); enter7=input('')
print('You have lived quite a bit of years!'); enter8=input('')

#For Loops
# for loopingVariable in whatWeloopOver:
#   code
#   more code
start=0
stop = age+1
stepSize=1
for number in range(start,stop,stepSize):
    print(number)

#While Loops
#while booleanValue:
#   code
#   more code
print('And you have many more to go!'); enter9=input('')
startwhile = age
while startwhile < 79:
    print(startwhile)
    startwhile += 1 #start = start + 1.5

print('Now consider this...'); enter21=input('')
print('The Cosmic Calendar is a method to visualize the chronology of the universe, scaling its current age of 13.8 billion years to a single year.'); enter22=input('')
print('So sit tight for 5 seconds...I will count. (Do not press enter)')
#Module
import time
from time import sleep
sleep(5)

print("That is how long 2170 years feels."); enter31=input('')

print('We dont have a lot of time, but there is so much to do.'); enter30=input('')                                                 
print('So enjoy your time...'); enter10=input('')
print('Here...'); enter11=input('')
print('On planet Earth!'); enter12=input('')










