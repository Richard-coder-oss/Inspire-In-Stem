
acc_bal=input("Enter your acc balance:")

if (int(acc_bal))> 100000 and int ((acc_bal)< 200000):
    acc_bal = acc_bal -25000
    print ("we have deducted ksh 15000 from your account")

elif (int(acc_bal) > 50000 and int (acc_bal) < 100000):
        acc_bal = acc_bal - (float(0.3)*acc_bal)
        print ("we have deducted 30 perecent from your account")

elif int (acc_bal) > 100000 :
        acc_bal = acc_bal - 15000
        print("we have deducted ksh 15000 from your account")
