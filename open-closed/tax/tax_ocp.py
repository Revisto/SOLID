from abc import ABC, abstractmethod

class CountryTaxCalculator(ABC):
    @abstractmethod
    def calculate_tax_amount(self):
        pass
    
class TaxCalculatorForUS(CountryTaxCalculator):
    def __init__(self, total_income, total_deduction):
        self.total_income = total_income
        self.total_deduction = total_deduction

    def calculate_tax_amount(self):
        taxable_income = self.total_income - self.total_deduction
        # calculation here 
        return taxable_income 


class TaxCalculatorForUK(CountryTaxCalculator):
    def __init__(self, total_income, total_deduction):
        self.total_income = total_income
        self.total_deduction = total_deduction

    def calculate_tax_amount(self):
        taxable_income = self.total_income - self.total_deduction
        # calculation here 
        return taxable_income