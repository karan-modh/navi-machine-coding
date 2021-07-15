from loan import Loan
from util import calculate_num_emis_left

class LoanManager():
    def __init__(self):
        self.loans = list()

    def addLoan(self, loan):
        self.loans.append(loan)
    
    def getLoans(self):
        return self.loans
    
    def processLoan(self, loan_metadata):
        loan = Loan(loan_metadata)
        self.loans.append(loan)

    def findLoanByNames(self, bank_name, borrower_name):
        for loan in self.loans:
            if loan.get_bank_name() == bank_name and loan.get_borrower_name() == borrower_name:
                return loan
        raise Exception("No Loans Exists")

    def updateLoan(self, updated_loan):
        index = 0
        for i in range(0,len(self.loans)):
            loan = self.loans[i]
            if loan.get_bank_name() == updated_loan.get_bank_name() and loan.get_borrower_name() == updated_loan.get_borrower_name():
                index = i
                break
        self.loans[index] = updated_loan
    
    def showBalance(self, balance_metadata):
        try:
            loan = self.findLoanByNames(balance_metadata["bank_name"], balance_metadata["borrower_name"])
        except Exception as e:
            print(e.args)
            return
        amount_paid = loan.get_emi_amount()*balance_metadata["emi_no"]
        amount_paid += loan.get_lump_sum_payment(balance_metadata["emi_no"])
        # amount_left = amount_left_after_emi_payment(loan.get_emi_amount(), loan.get_no_of_emis(), loan.get_amount_left())
        amount_left = loan.get_amount() - amount_paid
        num_emis_left = calculate_num_emis_left(amount_left, loan.get_emi_amount())

        response = [balance_metadata["bank_name"], balance_metadata["borrower_name"], amount_paid, num_emis_left]    
        return response

    def addPayment(self, payment_metadata):
        try:
            loan = self.findLoanByNames(payment_metadata["bank_name"], payment_metadata["borrower_name"])
        except Exception as e:
            print(e.args)
            return
        loan.update_payment(payment_metadata["emi_no"], payment_metadata["lump_sum_amount"])
        self.updateLoan(loan)
        