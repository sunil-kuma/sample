# Fibonacci Series------------------------------------------------------

n1=0
n2=1
initial = int(input("Enter the initial value : "))
final=int(input("Enter the No of sequences : "))    
#print "%d ' ' %d"%(n1,n2)
#(i=2;i<final;++i)   
for a in range(initial, final):
	a=n1+n2
	print "%d "%(a)
	n1=n2
 	n2=a
#----------------------------------------------------------------------

# Even Numbers in a range ---------------------------------------------	
number1 = int(input("Enter the initail number to check is Even "))
number2 = int(input("Enter the final number to check is Even "))
for a in range(number1, number2):
	if (a % 2) == 0:
		print "The number {0} is Even".format(a)
	else :
		pass
#----------------------------------------------------------------------

# Odd Numbers in a range ---------------------------------------------	
number1 = int(input("Enter the initail number to check is Odd "))
number2 = int(input("Enter the final number to check is Odd "))
for a in range(number1, number2):
	if (a % 2) != 0:
		print "The number {0} is Odd".format(a)
	else :
		pass		
#---------------------------------------------------------------------

# Check if the given numbers in the range are prime or Not. ----------

x = int(input("Enter initialvalue value : "))		
y = int(input("Enter finalvalue value : "))			

print "Prime numbers between given range are:"

for num in range(x,y + 1):
  if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           break
   else:
       print(num)		
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
rows = int(input("Enther the number initial value of rows in which you want stars : "))
finalrows = int(input("Enther the number initial value of rows in which you want stars : "))
print "  "
for a in range(rows,finalrows):
	print "*"*a

#-------------------------------------------------------------------------------------------

for b in range (finalrows,rows,-1):
    print(b * ' ' + (finalrows-b) * '*') 	
#-------------------------------------------------------------------------------------------

for c in range(rows,finalrows+1):
	print (finalrows-c)*' '+c*'* '
#--------------------------------------------------------------------------------------------           