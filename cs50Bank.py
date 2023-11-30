import sys
import tabulate
from tabulate import tabulate
import getpass

# importing classes
from cx import Customer
from emp import Employee, Clerk, Manager, Head

# lists for tabulate
welcome_msg = [["🏦Welcome to CS50 Bank🌐"]]  # welcome message
menu = [["Employee Login"], ["Customer Login"], ["Exit"]]  # main_menu
header = ["Option Name"]  # header
cx_menu = [["Account Summary"], ["Exchange Rate of CAD"], ["Address Change"], ["Exit"]]
clerk_menu = [["Deposit"], ["withdrawal"], ["Exit"]]  # clerk
assistant_menu = [
    ["Deposit"],
    ["withdrawal"],
    ["Change Account Status"],
    ["Add Customer"],
    ["Exit"],
]  # manager
head_menu = [
    ["Deposit"],
    ["withdrawal"],
    ["Change Account Status"],
    ["Add Customer"],
    ["Access Records"],
    ["Exit"],
]  # branch head


while True:
    print(tabulate(welcome_msg, tablefmt="pretty"), "\n")  # welcome message + new_line
    print(tabulate(menu, headers=header, tablefmt="pretty", showindex="always"), "\n")
    try:
        menu_choice = input(
            f"Which of the Options Best Suits You\nEnter Your Choice Here: "
        )
        # for employee
        if int(menu_choice) == 0:
            emp_name = input("\nEnter your name: ").strip().capitalize()
            emp_id = getpass.getpass("Enter the Id: ")
            emp_id = emp_id.upper()
            emp_detail = Employee.verify_employee(
                emp_name, emp_id
            )  # checking the employee is valid
            if not emp_detail:
                print(f"❌ Employee Not Found ❌")
            else:
                emp_pos = emp_detail["position"]

                # clerk
                if emp_pos == "Clerk":
                    while True:
                        try:
                            print(
                                f"\n",
                                tabulate(
                                    clerk_menu,
                                    headers=header,
                                    tablefmt="pretty",
                                    showindex="always",
                                ),
                                "\n",
                            )
                            clerk_choice = int(input("\nEnter the Choice: "))

                            # deposit
                            if clerk_choice == 0:
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_deposit_amt = int(
                                    input(
                                        "\nEnter the amount to be deopsited: "
                                    ).strip()
                                )
                                deposited = Clerk.deposit(cx_name, cx_deposit_amt)
                                if deposited:
                                    print("\nThe Amount Has Been Deposited\n")

                            # withdrawal
                            elif clerk_choice == 1:
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_withdrawal_amt = int(
                                    input(
                                        "\nEnter the amount to be withdrawal: "
                                    ).strip()
                                )
                                withdrawn = Clerk.withdrawal(cx_name, cx_withdrawal_amt)
                                if withdrawn:
                                    print("\nThe Amount Has Been Withdrawn\n")
                            elif clerk_choice == 2:
                                break
                            else:
                                continue
                        # exception handling
                        except (Exception, KeyboardInterrupt):
                            continue

                # manager
                elif emp_pos == "Assistant Manager":
                    while True:
                        try:
                            print(
                                "\n",
                                tabulate(
                                    assistant_menu,
                                    headers=header,
                                    tablefmt="pretty",
                                    showindex="always",
                                ),
                                "\n",
                            )
                            manager_choice = int(input("\nEnter the Choice: "))
                            # deposit
                            if manager_choice == 0:
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_deposit_amt = int(
                                    input(
                                        "\nEnter the amount to be deopsited: "
                                    ).strip()
                                )
                                deposited = Manager.deposit(cx_name, cx_deposit_amt)
                                if deposited:
                                    print("\nThe Amount Has Been Deposited\n")
                            # withdrawal
                            elif manager_choice == 1:
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_withdrawal_amt = int(
                                    input(
                                        "\nEnter the amount to be withdrawal: "
                                    ).strip()
                                )
                                withdrawn = Manager.withdrawal(
                                    cx_name, cx_withdrawal_amt
                                )
                                if withdrawn:
                                    print("\nThe Amount Has Been Withdrawn\n")
                            # account_change
                            elif manager_choice == 2:
                                Manager.change_account()
                            # adding cx
                            elif manager_choice == 3:
                                Manager.add_cx()
                            # exiting from the menu
                            elif manager_choice == 4:
                                break
                            else:
                                continue
                        # exception handling
                        except (Exception, KeyboardInterrupt):
                            continue

                # head_menu= [['Deposit'],['withdrawal'],['Change Account Status'],['Add Customer'],['Access Records'],['Exit']] #branch head

                elif emp_pos == "Branch Head":
                    while True:
                        try:
                            print(
                                "\n",
                                tabulate(
                                    head_menu,
                                    headers=header,
                                    tablefmt="pretty",
                                    showindex="always",
                                ),
                                "\n",
                            )
                            head_choice = int(input("\nEnter the choice: "))
                            # deposit
                            if head_choice == 0:  # will put in class for redundancy
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_deposit_amt = int(
                                    input(
                                        "\nEnter the amount to be deopsited: "
                                    ).strip()
                                )
                                deposited = Head.deposit(cx_name, cx_deposit_amt)
                                if deposited:
                                    print("\nThe Amount Has Been Deposited\n")

                            # withdrawal
                            elif head_choice == 1:
                                cx_name = (
                                    input("Enter the cusotmer name: ")
                                    .capitalize()
                                    .strip()
                                )
                                cx_withdrawal_amt = int(
                                    input(
                                        "\nEnter the amount to be withdrawal: "
                                    ).strip()
                                )
                                withdrawn = Head.withdrawal(cx_name, cx_withdrawal_amt)
                                if withdrawn:
                                    print("\nThe Amount Has Been Withdrawn\n")

                            # changing account status
                            elif head_choice == 2:
                                Head.change_account()

                            # adding cx
                            elif head_choice == 3:
                                Head.add_cx()
                            # displayin records
                            elif head_choice == 4:
                                Head.display()

                            elif head_choice == 5:
                                break
                            else:
                                continue
                        except (Exception, KeyboardInterrupt):
                            continue
                else:
                    # message for the cleaner
                    message = "\n🧽 Thank you for cleaning the premises 🧹\n"
                    print(message)

        # for customer
        elif int(menu_choice) == 1:
            name = input("Name: ").strip().capitalize()
            postal_code = input("Postal Code: ").strip().upper()
            verified = Customer.verified(name, postal_code)

            # for verification if the user exists
            if verified == "active":
                while True:
                    try:
                        print(
                            "\n",
                            tabulate(
                                cx_menu,
                                headers=["Option Name"],
                                showindex="always",
                                tablefmt="pretty",
                            ),
                            "\n",
                        )
                        cx_choice = int(
                            input("Enter the Number Corresponding to the Option💻: ")
                        )
                        if (cx_choice) == 0:
                            # for account summary
                            account_summary = Customer.accountsummary(name, postal_code)
                            print(
                                "\n",
                                tabulate(
                                    [account_summary], headers="keys", tablefmt="presto"
                                ),
                                "\n",
                            )
                        elif (cx_choice) == 1:
                            # for currency rate
                            currency_rate = round(int(Customer.currency_rate()))
                            print(f"\n💵 1 GBP={currency_rate} CAD 💵\n")
                        elif (cx_choice) == 2:
                            # changing the postal code
                            confirmation = (
                                input("\nDo You Want To Change the Postal Code(y/n)🤔 ")
                                .lower()
                                .strip()
                            )  #
                            if confirmation == "y":
                                new_postal = (
                                    input("\nEnter the New Postal Code🏠 ")
                                    .strip()
                                    .upper()
                                )
                                valid_postal = Customer.valid_postal(new_postal)
                                if valid_postal:
                                    # updating address in CSV file
                                    Customer.update_postal(
                                        name, postal_code, new_postal
                                    )
                                    print("\nThe New Postal Code Has Been Updated✅\n")
                                else:
                                    print("\n 🚫 Could Not Update The Postal Code 🚫\n")
                            else:
                                print("\n 🚫 Could Not Update The Postal Code 🚫\n")
                        elif int(cx_choice) == 3:
                            break
                    except (Exception, KeyboardInterrupt):
                        #  ,KeyboardInterrupt
                        continue
            # checking the not active status
            elif verified == "not_active":
                print(
                    "\nAccount Status is Inactive🚫\nContact Your Assistant Manager👔 For Further Assistance📞\n"
                )
            # if not found
            elif verified == "not_found":
                print(f"\nCustomer Not Found\n")

        # exit the program
        elif int(menu_choice) == 2:
            print(
                "\n",
                tabulate([["😊 Thank You For Visiting Us! 😊"]], tablefmt="pretty"),
                "\n",
            )
            sys.exit(1)
    except (Exception, KeyboardInterrupt):
        continue
