# importing libraries
import sys
import tabulate
from tabulate import tabulate

#importing classes from other programs
from cx import Customer

# lists for tabulate
welcome_msg = [["🏦Welcome to CS50 Bank🌐"]]  # welcome message
menu = [["Employee Login"], ["Customer Login"], ["Exit"]]  # main_menu
cx_menu = [['Account Summary'],['Exchange Rate of CAD'],['Address Change'],['Exit']]
while True:
    print(tabulate(welcome_msg, tablefmt="pretty"), "\n")  # welcome message + new_line
    print(tabulate(menu, headers=['Option Name'], tablefmt='pretty',showindex='always'),'\n')
    try:
      menu_choice = input(f'Which of the Options Best Suits You\nEnter Your Choice Here: ')
      #for employee
      if int(menu_choice) == 0:
          ...

      #for customer
      elif int(menu_choice) == 1:
        name = input('Name: ').strip().capitalize()
        postal_code = input('Postal Code: ').strip().capitalize()
      
        verified = Customer.verified(name,postal_code)
        if (verified): 
            while True:
              try:
                print(tabulate(cx_menu,headers=['Option Name'],showindex='always',tablefmt='pretty'),'\n')
                cx_choice = input('Enter the Number Corresponding to the Option💻: ')
                if int(cx_choice)==0:
                   account_summary=Customer.accountsummary(name,postal_code)
                elif int(cx_choice)==1: 
                  currency_rate = Customer.currency_rate(name,postal_code)
                elif int(cx_choice)==2:
                  confirmation = input('\nDo You Want To Change the Postal Code(y/n)🤔 ').lower().strip()
                  if (confirmation=='y'):
                      new_postal = input('\nEnter the New Postal Code🏠 ').strip().upper()
                      valid_postal = Customer.valid_postal(new_postal)
                      if valid_postal:
                        Customer.update_postal(name,postal_code,new_postal)
                        print('\nThe New Postal Code Has Been Updated✅\n')
                      else:
                        print('\n 🚫 Could Not Update The Postal Code 🚫\n')
                  else:
                     print('\n 🚫 Could Not Update The Postal Code 🚫\n')
                elif int(cx_choice)==3:
                   break
              except (Exception,KeyboardInterrupt):
                 continue
        else:
            ...     
          
      elif int(menu_choice) == 2: #exit
          print('\n',tabulate([['😊 Thank You For Visiting Us! 😊']],tablefmt='pretty'),'\n')
          break
      
    except (Exception,KeyboardInterrupt):
        continue
