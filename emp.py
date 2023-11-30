# importing
import csv
import re
from tabulate import tabulate

# pattern for postal code
pattern = re.compile("^[A-Za-z][0-9][A-Za-z][0-9][A-Za-z][0-9]$")


class Employee:
    @staticmethod
    def verify_employee(emp_name, emp_id):
        with open("emp.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["name"] == emp_name and row["employee id"] == emp_id:
                    return row
            return False


class Clerk:
    @staticmethod
    def deposit(cx_name, cx_deposit_amt):
        dictionary_list = []
        with open("cx.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dictionary_list.append(row)
        headers = list(
            dictionary_list[0]
        )  # for extracting the headers from the list of dictionaries
        with open("cx.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in dictionary_list:
                if row["name"] == cx_name:
                    row["balance"] = int(row["balance"]) + cx_deposit_amt
                writer.writerow(row)
            return True

    @staticmethod
    def withdrawal(cx_name, cx_withdrawal_amt):
        dictionary_list = []
        with open("cx.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dictionary_list.append(row)
        headers = list(
            dictionary_list[0]
        )  # for extracting the headers from the list of dictionaries
        with open("cx.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in dictionary_list:
                if row["name"] == cx_name:
                    row["balance"] = int(row["balance"]) - cx_withdrawal_amt
                writer.writerow(row)
            return True


class Manager(Clerk):
    # changing status
    @staticmethod
    def change_account():
        dictionary_list = []
        cx_name = input("Enter the name of the customer: ").strip().capitalize()
        with open("cx.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                dictionary_list.append(row)
        headers = list(dictionary_list[0])
        with open("cx.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in dictionary_list:
                if row["name"] == cx_name:
                    row["status"] = "Active"
                writer.writerow(row)
        print("\nAccount status successfully changed\n")

    # adding new customer
    @staticmethod
    def add_cx():
        try:
            cx_name = input("Enter the name: ").strip().capitalize()
            cx_postal = input("Enter the postal code: ").upper().strip()
            if not pattern.fullmatch(cx_postal):
                print("\n❎ Invalid Postal Code ❎\n")
                return 1
            with open("cx.csv", "a", newline="") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["name", "postal code", "balance", "status"]
                )
                writer.writerow(
                    {
                        "name": cx_name,
                        "postal code": cx_postal,
                        "balance": "0",
                        "status": "Active",
                    }
                )
            print("\n✅ Account added successfully ✅\n")

        except (Exception, KeyboardInterrupt):
            print("\n⚠ Could not add the customer ⚠\n")


class Head(Manager):
    @staticmethod
    def display():
        print(
            tabulate(
                [["Employee"], ["Customer"]],
                headers=["Option Name"],
                tablefmt="pretty",
                showindex="always",
            )
        )
        head_choice = int(input("Which Records you want to see: "))
        if head_choice == 0:
            emp = []
            with open("emp.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp.append(row)
            header = list(emp[0])  # for getting the headers
            if emp:
                print(tabulate([], headers=header, tablefmt="pretty"))
                for row in emp:
                    print(tabulate([row.values()], tablefmt="pretty"))

        elif head_choice == 1:
            cx = []
            with open("cx.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cx.append(row)
            header = list(cx[0])  # for getting the headers
            if cx:
                print(tabulate([], headers=header, tablefmt="pretty"))
                for row in cx:
                    print(tabulate([row.values()], tablefmt="pretty"))
        else:
            print("\n😵 Invalid Choice 😵\n")
