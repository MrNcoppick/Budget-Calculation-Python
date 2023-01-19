
# ask user for amount of budgets to calculate
def budget_count():
    while True:
        try:
            count = int(input("How many budgets(people) do you want to calculate?"))
            if count <= 0:
                print("Entry must be a whole number greater than zero.")
                continue
            else:
                return count
        except:
            print("Entry must be a whole number greater than zero.")
            continue

# Method to convert the number from budget_count to have the proper suffix
def number_convert(x):
    if 10 <= x <= 20:
        ret_num = str(x + "th")
        return ret_num
    if x < 10 or x > 20:
        new_num = x % 10
        if new_num == 1:
            ret_num = str(x) + "st"
            return ret_num
        if new_num == 2:
            ret_num = str(x) + "nd"
            return ret_num
        if new_num == 3:
            ret_num = str(x) + "rd"
            return ret_num
        if new_num == 4 or new_num == 5 or new_num == 6 or new_num == 7 or new_num == 8 or new_num == 9:
            ret_num = str(x) + "th"
            return ret_num

# Method to ask the user how many insurances does this particular budget have, and then intake the information
# of those insurances, sum them, and output
def insurance_count():
    while True:
        try:
            ins_count = int(input("How many insurances does this budget have?"))
            if ins_count <= 0:
                print("Amount of insurances must be a whole number greater than zero.")
                continue
            else:
                break
        except:
            print("Amount of insurances must be a whole number greater than zero.")
            continue
    sum = 0
    for i in range(0,ins_count):
        x = number_convert(i + 1)
        amount = float(input(f"What is the {x} monthly insurance amount?"))
        sum = sum + amount
    return sum


# Method to collec the information of the budgets, to loop for the number entered in by the budget_count method
# put that information into the budget_information class and then the budget_collection dictionary
def collect_budget_info(x):
    from Classes import budget_information
    budget_collection = dict()
    y = 0
    for i in range(0,x):
        while True:
            try:
                name = str(input("What is the budgets name or name of person?"))
                income = float(input("What is the yearly income for this budget?"))
                if income <= 0:
                    print("Must be a number greater than zero. Try again.\n")
                    continue
                rent = float(input("What is the monthly rent/mortgage?"))
                if rent <= 0:
                    print("Must be a number greater than zero. Try again.\n")
                    continue
                car = float(input("What is the monthly car payment?"))
                if car < 0:
                    print("Must be a positive number or zero. Try again.\n")
                    continue
                insurance = float(insurance_count())
                if insurance < 0:
                    print("Must be a positive number or zero. Try again.\n")
                    continue
                fun = float(input("How much is spent on fun/entertainment monthly?"))
                if fun < 0:
                    print("Must be a positive number or zero. Try again.\n")
                    continue
                break
            except:
                print("Error, try again.\n")
                continue
        current_budget = budget_information(name, income, rent, car, insurance, fun)
        budget_collection[y] = current_budget
        y += 1
    return budget_collection


# Method to calculate the totals and percentages of each budget and put them into the
# calculated_budget_information class and insert them into the calculated_budget_collection dictionary
def calculate_budgets(x):
    from Classes import calculated_budget_information
    calculated_budget_collection = dict()
    for i in range(len(x)):
        name = x[i].name
        income = round((x[i].income / 12), 2)
        rent_percentage = (x[i].rent / income) * 100
        car_percentage = (x[i].car / income) * 100
        insurance_percentage = (x[i].insurance / income) * 100
        fun_percentage = round(((x[i].fun / income) * 100), 2)
        remaining = income - x[i].rent - x[i].car - x[i].insurance - x[i].fun
        remaining_percentage = round(((remaining / income) * 100), 2)
        needs_percentage = round((rent_percentage + car_percentage + insurance_percentage), 2)

        current_calculation = calculated_budget_information(name, income, needs_percentage, fun_percentage, remaining, remaining_percentage)
        calculated_budget_collection[i] = current_calculation
    return calculated_budget_collection

# Method to output to user the adjustments needed to match the 50-30-20 rule
def adjustment_calculations(x):
    name = x.name
    income = x.income
    needs = x.needs_percentage
    wants = x.fun_percentage
    savings = x.remaining_percentage
    if needs > 50:
        adj_needs = f'needs to go down by %{(needs - 50)} or ${round((((needs - 50)/100)*income), 2)}'
    if needs < 50:
        adj_needs = f'can stay the same, it has a surplus of %{(50 - needs)}, or ${round((((50-needs)/100)*income), 2)}'
    if wants > 30:
        adj_wants = f'needs to go down by %{(wants - 30)} or ${round((((wants - 30)/100)*income), 2)}'
    if wants < 30:
        adj_wants = f'can stay the same, it has a surplus of %{(30 - wants)}, or ${round((((30-wants)/100)*income), 2)}'
    if savings < 20:
        adj_savings = f'needs to go up by %{(savings - 20)} or ${round((((savings - 20)/100)*income), 2)}'
    if savings > 20:
        adj_savings = f'can stay the same, it has a surplus of %{(20 - savings)},' \
                      f' or ${round((((20-savings)/100)*income), 2)}'
    print(f"{name}'s needs usage {adj_needs}, wants usage {adj_wants}, and savings {adj_savings}.\n\n")




