#Open Close Principle

#Problem
class PersonalLoanValidator:
    
    def is_valid_user_for_personal_loan(self, user:User) -> bool:
        #Do validation
        pass

class MortgageValidator:

    def is_valid_user_for_mortgage_loan(self, user:User) -> bool:
        #Do validation
        pass


class LoanHandler:

    #Esta clase no esta cerrada para modificaciones, ni abierta para la extension

    def __init__(self) -> None:
        self.personal_loan_validator = PersonalLoanValidator()
        self.mortgage_validator = MortgageValidator()

    def approve_personal(self, user:User) -> None:
        if self.personal_loan_validator.is_valid_user_for_personal_loan(user):
            pass

    def approve_mortgage(self, user:User) -> None:
        if self.mortgage_validator.is_valid_user_for_mortgage_loan(user):
            pass


if __name__ == "__main__":
    loan_handler = LoanHandler()
    user = user

    loan_handler.approve_mortgage(user)
    loan_handler.approve_personal(user)


#Solution

from abc import ABC, classmethod

class LoanValidator(ABC):
    @classmethod
    def is_valid_user_for_loan(cls, user:User) -> bool:
        pass

class PersonalLoanValidator(LoanValidator):
    def is_valid_user_for_loan(cls, user:User) -> bool:
        pass

class MortgageLoanValidator(LoanValidator):
    def is_valid_user_for_loan(cls, user:User) -> bool:
        pass


if __name__ == '__main__' :
    user = User()
    personal_loan_validator = PersonalLoanValidator()
    mortgage_loan_validator = MortgageLoanValidator()

    personal_loan_validator.is_valid_user_for_loan(user)
    mortgage_loan_validator.is_valid_user_for_loan(user)
        

