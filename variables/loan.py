# determine if a staff can take a loan based on monthly spending
monthly_salary = 5000
monthly_spending = 5000
loan_range = 3000
eligibility = False

if monthly_spending < loan_range:
    eligibility = True

if eligibility:
    print('eligible to take a loan')
else:
    print('not eligible')
