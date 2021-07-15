import math

class Loan:
    def __init__(self, loan_metadata):
        self.bank_name = loan_metadata["bank_name"]
        self.borrower_name = loan_metadata["borrower_name"]
        self.principal_amount = loan_metadata["principal_amount"]
        self.no_of_years = loan_metadata["no_of_years"]
        self.interest_rate = loan_metadata["interest_rate"]
        self.payments = {}
        self.amount = self.principal_amount* (1 + self.no_of_years*self.interest_rate/100)
        self.amount_left = self.principal_amount* (1 + self.no_of_years*self.interest_rate/100)
        self.emi_amount = math.ceil(self.amount_left/(self.no_of_years*12))
        self.no_of_emis = math.ceil(self.no_of_years*12)    
    
    def get_bank_name(self):
        return self.bank_name

    def get_borrower_name(self):
        return self.borrower_name

    def get_emi_amount(self):
        return self.emi_amount

    def get_amount_left(self):
        return self.amount_left

    def get_no_of_emis(self):
        return self.no_of_emis

    def get_amount(self):
        return self.amount

    def update_payment(self, key, value):
        self.payments[key] = value

    def get_lump_sum_payment(self, emi_no):
        amount_paid = 0
        for key in self.payments:
            if key <= emi_no:
                amount_paid += self.payments[key]
        return amount_paid


