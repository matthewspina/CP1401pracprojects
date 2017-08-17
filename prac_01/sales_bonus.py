"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = 0
while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales >= 1000:
        sales = sales * 0.15
    else:
        sales = sales * 0.1
    print("Bonus: $", sales)

