import getpass

class Advocate:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Case:
    def __init__(self, case_number, client_name, original_suit_amount):
        self.case_number = case_number
        self.client_name = client_name
        self.original_suit_amount = original_suit_amount

class AdvocateAccountingSystem:
    def __init__(self):
        self.advocates = []
        self.cases = []

    def add_advocate(self, username, password):
        advocate = Advocate(username, password)
        self.advocates.append(advocate)

    def add_case(self, case_number, client_name, original_suit_amount):
        case = Case(case_number, client_name, original_suit_amount)
        self.cases.append(case)

    def list_advocates(self):
        for advocate in self.advocates:
            print(f"Advocate: {advocate.username}")

    def list_cases(self):
        for case in self.cases:
            print(f"Case Number: {case.case_number}, Client: {case.client_name}")

if __name__ == "__main__":
    accounting_system = AdvocateAccountingSystem()

    while True:
        print("\nAdvocate Accounting System")
        print("1. Add Advocate")
        print("2. Add Case")
        print("3. List Advocates")
        print("4. List Cases")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter advocate username: ")
            password = getpass.getpass("Enter advocate password: ")
            accounting_system.add_advocate(username, password)
        elif choice == '2':
            case_number = input("Enter case number: ")
            client_name = input("Enter client name: ")
            original_suit_amount = float(input("Enter original suit amount: "))
            accounting_system.add_case(case_number, client_name, original_suit_amount)
        elif choice == '3':
            accounting_system.list_advocates()
        elif choice == '4':
            accounting_system.list_cases()
        elif choice == '5':
            print("Exiting Advocate Accounting System.")
            break
        else:
            print("Invalid choice. Please try again.")
