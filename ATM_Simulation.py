def ATM():
   amount=10000
   print("\nHi welcome to ATM Simulation using Python prograing")
   name=input("\nEnter your name: ")

   while True:
       print("\n------Enter your Choise------")
       
       choise=int(input("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit:\n\n"))
       
       if choise==1:
           print("")
           print(amount)
       
       elif choise==2:
           Depoist=int(input("\nEnter the amount to be Deposited: "))
           Depoist+=amount
           print("\nSucessfully Deposited the Cash\n")
           print(name,"your current balance amount is",Depoist)
           
       
       elif choise==3:
           withdraw=int(input("\nEnter the amount you want to withdraw: "))
           withdraw-=amount
           if withdraw <= amount:
               print("\nSucessfuly Withdraw the cash\n")
               print(name,"your current balance amount is",withdraw)
           elif withdraw >= amount:
               print(name,"your account has insufficent fund",withdraw)
       
       elif choise==4:
           print(name,"thank for using the ATM Simulation")
           break
           
       else:
           print(name,"you have choose an Invalid option")              
                        
        
ATM()
