
# Check if the given number is Even or Odd.

number = int(input("Enter the number to check is Even or Odd : "))
if (number % 2) == 0:
	print "The given number {0} is Even".format(number)
else :
	print "The given number {0} is Odd".format(number)
#----------------------------------------------------------------


# Check if the given numbers in the range are prime or Not. 

initialvalue = int(input("Enter initialvalue value : "))		
finalvalue = int(input("Enter finalvalue value : "))			

print "Prime numbers between given range are:"

for num in range(initialvalue,finalvalue + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
#---------------------------------------------------------


# Check if the given input is Strin or int or float

input = input("Please provide some input to the system :")

if type(input) == int:
    print "The given input is 'Integer' "
elif type(input) == float:
    print "The given input is 'Float' "
else:
	print "The given input is 'String' "

#---------------------------------------------------------