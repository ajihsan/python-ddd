class LoanRepository:
    def __init__(self):
        self.loans = {}

    def add(self, loan):
        self.loans[loan.loan_id] = loan

    def find_by_id(self, loan_id):
        return self.loans.get(loan_id)

    def get_all(self):
        return self.loans
