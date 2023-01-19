
# class for the initial budget information
class budget_information:
    def __init__(self, name, income, rent, car, insurance, fun):
        self.name = name
        self.income = income
        self.rent = rent
        self.car = car
        self.insurance = insurance
        self.fun = fun

# class for the calculated budget information
class calculated_budget_information:
    def __init__(self, name, income, needs_percentage, fun_percentage, remaining, remaining_percentage):
        self.name = name
        self.income = income
        self.needs_percentage = needs_percentage
        self.fun_percentage = fun_percentage
        self.remaining = remaining
        self.remaining_percentage = remaining_percentage
    def __str__(self):
        return f"\n{self.name}'s total income monthly is ${self.income}. Their/It needs percentage is %{self.needs_percentage}, " \
               f"their/it wants percentage is %{self.fun_percentage}. Their/It remaining money that goes into savings " \
               f"is ${self.remaining} or %{self.remaining_percentage}."

