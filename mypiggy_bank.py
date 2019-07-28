# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 08:14:17 2019

@author: JSM
"""
print("Welcome to the Piggy Bank!")

def StartApp(): 
    TrancInp = input("Add, Withdraw or Check: ").upper()
    
    if TrancInp == 'ADD':
        # that opens your bankledger.txt file in read mode
        Addvalue = open('BankLedger.txt', 'r+')
        #You should use the answer Bal_previous
        Bal_previous = Addvalue.read()
        #saves the file
        Addvalue.close() 
        #Bal_previous =0 
        Rupees_instance = input("How many rupees would you like to deposit?: ")
        Rupees_total = int(Rupees_instance) + int(Bal_previous) 
        print("There are %s Rupees in your bank"% (Rupees_total))
        # that opens your bankledger.txt file in write mode
        Addvalue = open('BankLedger.txt', 'r+')
        #You should use the answer Bal_previous
        Addvalue.write(str(Rupees_total))
        #saves the file
        Addvalue.close() 
        return transact()
    elif TrancInp == 'WITHDRAW':
        # that opens your bankledger.txt file in read mode
        Addvalue = open('BankLedger.txt', 'r+')
        #You should use the answer Bal_previous
        Bal_previous = Addvalue.read()
        #saves the file
        Addvalue.close() 
        #Bal_previous = Rupees_total
        Rupees_instance = input("How many rupees would you like to withdraw?: ")
        Rupees_total = int(Bal_previous) - int(Rupees_instance)  
        print("There are %s Rupees in your bank"% (Rupees_total))
        # that opens your bankledger.txt file in write mode
        Addvalue = open('BankLedger.txt', 'r+')
        #You should use the answer Bal_previous
        Addvalue.write(str(Rupees_total))
        #saves the file
        Addvalue.close()
        return transact()
    elif TrancInp == 'CHECK':
        # that opens your bankledger.txt file in read mode
        Addvalue = open('BankLedger.txt', 'r+')
        #You should use the answer Bal_previous
        Bal_previous = Addvalue.read()
        #saves the file
        Addvalue.close() 
        print("There are %s Rupees in your bank"% int(Bal_previous))
    else:
        return "Sorry. Please Type R for rupees."
def EndApp(): 
    #withdraw = input("what you would you like to widraw? (R: For Rupees):").upper() 

    print("Have a nice day!, Bye bye")

def transact():
    CustInp = input("Start or End: ").upper()

    if CustInp == 'S' or CustInp == 'START':
        return StartApp()                        

    elif CustInp == 'E' or CustInp == 'END':
        return EndApp()

    else:
        return "Sorry. Please type Start to Start App or End for End App features." 

print(transact())
