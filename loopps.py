#1/usr/bin/python

#for loop
#while loop

#conditions
#if
#if else
        #if
        #elif
        #else
#and , or

#The syntax
#for numbers in range
#print(range(0,20))

for numbers in range(0,10):
 #print(numbers)
 #print(numbers%2)
 
 if(numbers%2==0):
  #print(numbers)

#Get the sum of all even numbers between 0,50
#Product of all even numbers between 0, 50

   sum_nums= 0 #sum of even numbers
prod_nums=1
for numbers in range (0,50):
    if(numbers %2==0):
        sum_nums= sum_nums + numbers
        prod_nums=prod_nums* numbers


#print(sum_nums)
print(prod_nums)

#calculate the factorial of 6
  #!6=6*5*4*3*2*1


  #while
  #operators
        #<less than
        #<=less than or equal to
        #> greater than
        #>= greater than or equal to
        #==equal to

        #boolen => True,false

num=0 #initialize the number
while num<10 :
     num=num+ 1
     #print(num)

     if(num%2==0):
       print(num)
           