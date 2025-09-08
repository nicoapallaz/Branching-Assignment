hour = int(input("Enter the KW hours used: "))
print()
if hour > 1000:
    amount = 7.633 * 1000
    hour -= 1000
    amount = amount + (9.259 * hour)
    amount /= 100
    total = round(amount, 2)
else:
    amount = 7.633 * hour
    amount /= 100
    total = round(amount, 2)
print("Amount owed is $" + str(total))
# hi