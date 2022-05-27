#1/usr/bin/python
#calculate the factorial of 6

number=int(input("enter the number"))
factorial =1
if number <0:
    print ("factorioal of number does not exist")

elif number==0:
     print("factorile of 0=1")

else:
    for i in range(1,number+1):
       factorial=factorial*i 
print ("factorial of number:",factorial)