print("Electricity bill estimator 2.0")
tariff11 = 0.244618
tariff31 = 0.136928
price = int(input("Which tariff? 11 or 31:"))
if price == 11:
    price = tariff11
elif price == 31:
    price = tariff31
else:
    print("Invalid option")
daily_use = float(input("Enter daily use in kWh:"))
if daily_use < 0:
    print("Invalid option")
else:
    billing_days = int(input("enter number of billing days:"))
    if billing_days < 0:
        print("Invalid option")
    else:
        total = (price * daily_use * billing_days)
        print("Estimated bill: $", total)


