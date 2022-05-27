#1/usr/bin/python
##############

#program for printing patterns of numbers
rows=int(input("enter the number of row"))
for i in range(rows):
    for j in range (i+1):
        print(j+1,end=" ")
    print("\n")    
    