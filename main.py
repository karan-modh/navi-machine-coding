from loan_manager import LoanManager
import sys
from loan_manager import LoanManager

def main():
    input_file = sys.argv[1]
    input_data = open(input_file, 'r').readlines()
    input_data = [x.strip() for x in input_data]
    loan_manager = LoanManager()
    for command in input_data:
        command = command.split(" ")
        command_type = command[0]
        if command_type == "LOAN":
            loan_metadata = {
                "bank_name": command[1],
                "borrower_name": command[2],
                "principal_amount": int(command[3]),
                "no_of_years": int(command[4]),
                "interest_rate": int(command[5])
            }
            loan_manager.processLoan(loan_metadata)
        elif command_type == "PAYMENT":
            payment_metadata = {
                "bank_name": command[1],
                "borrower_name": command[2],
                "lump_sum_amount": int(command[3]),
                "emi_no": int(command[4])
            }
            loan_manager.addPayment(payment_metadata)
        else:
            balance_metadata = {
                "bank_name": command[1],
                "borrower_name": command[2],
                "emi_no": int(command[3])
            }
            print(loan_manager.showBalance(balance_metadata))

if __name__ == "__main__":
    main()
