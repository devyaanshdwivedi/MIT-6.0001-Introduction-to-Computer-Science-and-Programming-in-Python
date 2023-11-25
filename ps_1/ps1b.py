# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:57:15 2023

@author: Dell
"""

annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion salary saved: "))
cost_dream_house = float(input("Enter cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25 * cost_dream_house
current_savings = 0
months = 0
while (current_savings < portion_down_payment):
    if months % 6 == 0 and months != 0:
        annual_salary += annual_salary * semi_annual_raise
    current_savings += portion_saved * (annual_salary / 12) + current_savings * 0.04 / 12
    months += 1
print("Number of Months: ", months)
