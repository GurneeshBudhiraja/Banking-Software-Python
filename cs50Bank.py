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
        postal_code = input('Postal Code: ').strip().upper()
        verified = Customer.verified(name,postal_code)

        #for verification if the user exists
        if (verified=='active'): 
            while True:
              try:
                print('\n',tabulate(cx_menu,headers=['Option Name'],showindex='always',tablefmt='pretty'),'\n')
                cx_choice = int(input('Enter the Number Corresponding to the Option💻: '))
                if (cx_choice)==0:
                   #for account summary
                   account_summary=Customer.accountsummary(name,postal_code) 
                   print('\n',tabulate([account_summary],headers='keys',tablefmt='presto'),'\n')
                elif (cx_choice)==1: 
                  #for currency rate
                  currency_rate = round(int(Customer.currency_rate(name,postal_code)))
                  print(f'\n💵 1 GBP={currency_rate} CAD 💵\n')
                elif (cx_choice)==2:
                  #changing the postal code
                  confirmation = input('\nDo You Want To Change the Postal Code(y/n)🤔 ').lower().strip() #
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
        #checking the not active status
        elif (verified=='not_active'):
          print('\nAccount Status is Inactive🚫\nContact Your Assistant Manager👔 For Further Assistance📞\n')
        #if not found
        elif (verified=='not_found'):
            print(f'\nCustomer Not Found\n')

      #exit the program
      elif int(menu_choice) == 2: 
        print('\n',tabulate([['😊 Thank You For Visiting Us! 😊']],tablefmt='pretty'),'\n')
        sys.exit(1)

    except (Exception):
      continue 
    # KeyboardInterrupt
