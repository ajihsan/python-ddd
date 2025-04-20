from datetime import datetime, timedelta


class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.due_date = datetime.now() + timedelta(days=14)  # 2-week loan period

    def return_book(self):
        self.book.mark_available()
