print("heloo how are you welcome to sbi atm machine")
restart=('y')
chance=3
balance=100000.500
while chance!=0:
    pin=int(input("enter the your 4 digit pin::\n"))
    if pin==1234:
        print("your pin is correct::\n")
        while restart not in ('n','N','NO','no'):
            print(":::::what you like to do:::::")
            print("1.withdraw money in your account\n ")
            print("2.credit money in your account\n")
            print("3.chek balance on your account\n")
            print("4. exit service\n")
            option=int(input("enter number what you like to  do::\n"))
            if option==1:
                
                print("your balnce is::",balance)
                withdraw=float(input("enter the amount which you like withdraw::\n"))
                if withdraw>200.00 and withdraw<=balance:
                    balance=balance-withdraw
                    print(':::::::you are sucessfully withdraw:::::::\n')
                    print("now your balance is",balance)
                    restart=input("whould you like to contiue our service\n")
                    if restart not in ('n','N','NO','no'):
                        break
                elif withdraw>balance:
                    print("sorry!! we  can not withdraw brcause you have not enough balance retry!!\n")
                    restart=('y')
                elif withdraw<200.00:
                    withdraw=float(input("you can not withdraw less than 200 try again\n"))
                    

            elif option==2:
                credit=float(input("enter the amount which you like to credit your account\n"))
                if credit>200.00:
                    balance=balance+credit
                    print(':::::::yor balance is sucessfully credit your account:::::::')
                    print('now your balance is',balance)
                    restart=input("whould you like to contiue our service::\n")
                    if restart not in ('n','N','NO','no'):
                        break
                elif credit<200.00:
                    credit=float(input("you can not credit less than 200 retry\n"))
                    
            elif option==3:
                print('your account balance is',balance )
                restart=input("whould you like to contiue our service::\n")
                if restart not in ('n','N','NO','no'):
                        break
            
            elif option==4:
                print('thank you for using our service')
                chance=0
                break
            else:
                print('please enter the correct number \n')
            chance=0
            print('thank you for using our service\n')
    elif pin!=1234:
        print('please is  incorrect\n')
        chance=chance-1
        if chance==0:
            print("sorry!! you don't have more time")



        

                