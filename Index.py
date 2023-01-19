# Created by:
# Nicholas Coppick
#
# Created: 1/18/2023
# Last Updated: 1/19/2023
# Total Time: ~4hrs
#
#
# This program was created to show my proficiency in using python.
# It includes the use of loops, classes, lists, methods, and dictionaries.
#
# This program is a  budget calculation project.
# It will intake information by the user and calculate individual budget plans for each entry
# following the 50-30-20 rule, where 50% goes into needs(bills, payments, ect..)
# 30% goes into wants(entertainment)
# and 20% goes into savings accounts.


import Methods

y = Methods.calculate_budgets(Methods.collect_budget_info(Methods.budget_count()))
for i in range(0,len(y)):
    print(str(y[i]))
    Methods.adjustment_calculations(y[i])
