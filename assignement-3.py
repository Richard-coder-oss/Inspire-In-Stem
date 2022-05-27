#write a program that gets user input for gender and age and add shs 0 to her account if she is btwn 25-30yrs
#age =input("what is your age")
#gender=input("what gender are you:male/female")
age =input("what is your age ?")
#gender =input("what geneder are you :male/female")

acc_bal =0

if(int(age)>25) and (int(age)<30):
    acc_bal = acc_bal + 10000
    print("confirmed you have received 10000")

else:
     print("sorry, no money for you") 
       