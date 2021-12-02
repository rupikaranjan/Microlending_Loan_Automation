# coding: utf-8
import csv
from pathlib import Path
import pprint

# Part 1: Automate the Calculations.
loan_costs = [500, 600, 200, 1000, 450]

# Calculating and printing the total number of loans in the list(loan_costs)
total_number_loans = len(loan_costs)
print("\nTotal number of loans : " , total_number_loans)

# Calculating and printing the sum of all loans in the list(loan_costs)
sum_of_loans = sum(loan_costs)
print("Sum of all loans : " , sum_of_loans)

# Calculating and printing the average of all loans in the list(loan_costs)
average_of_loan = sum_of_loans / total_number_loans
print("The average value of loans : " , average_of_loan)

# Part 2: Analyze Loan Data.

# loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extracting and printing the Future Value and Remaining Months on the loan from the loan data dictionary
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print("\nThe future value of the loan is : ",future_value)
print("The number of remaining months for the loan is : ",remaining_months)

# Calculating and Printing Present Value of the loan using the below formula and  minimum required return of 20%(.20) as discount rate.
#  Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate = .2
present_value = future_value / (1 + discount_rate / 12) ** remaining_months
print("\nThe present value of the loan is : ",present_value)

# Deciding if the present value represents the loan's fair value by comparing the present value to the loan's cost.
if present_value >= loan.get("loan_price"):
    print("\nThe loan is worthy to buy!")
else:
    print("\nThe loan is too expensive and not worth to buy for the cost")


# Part 3: Financial Calculations.

# new loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Function calculate_present_value calculates present value of the any given loan data
# Input parameters : `future_value`, `remaining_months`, and the `annual_discount_rate`
# Output :  `present_value` for the loan
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + discount_rate / 12) ** remaining_months
    return present_value

# Calling calculate_present_value to calculate present value for new loan data and `discount rate` as 0.2
present_value = calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),0.2)
print(f"The present value of the loan is: {present_value}")


# Part 4: Conditionally filtering lists of loans.

# Loan list
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creating an empty list called `inexpensive_loans`
inexpensive_loans = []

# Looping through all the loans and appending any loans that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)


# Printing the `inexpensive_loans` list
print("\nThe inexpensive loans are :\n")
pprint.pprint(inexpensive_loans)


# Part 5: Saving the results.


# Output header variable
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Output file path
output_path = Path("inexpensive_loans.csv")


# Writing header row and all values in `inexpensive_loans` to a csv file named `inexpensive_loans.csv`
with open(output_path, 'w', newline='') as csv_outputfile:
    csv_writer = csv.writer(csv_outputfile)
    csv_writer.writerow(header)
    for loan in inexpensive_loans:
        invidual_loan_values = loan.values()
        csv_writer.writerow(invidual_loan_values)
