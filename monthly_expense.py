data = [
    {"January": 2000, "February": 2350, "March": 2600, "April": 2130, "May": 2190}
]

while True:
    x = int(input("Which data do you want?\n"
                  "Click 1 to know how many extra dollars you spent in February compared to January.\n"
                  "Click 2 to find out your total expense in the first quarter (first three months) of the year.\n"
                  "Click 3 to find out if you spent exactly 2000 dollars in any month.\n"
                  "Click 4 to add June's expense of 1980 dollars to your monthly list.\n"
                  "Click 5 to correct April's expense after a refund of 200 dollars.\n"
                  "Click 6 to exit.\n"))
    
    if x == 1:
        print(f"Extra spent in February compared to January: {data[0].get('February') - data[0].get('January')} dollars")
        
    elif x == 2:
        total_expense_q1 = data[0].get("January") + data[0].get("February") + data[0].get("March")
        print(f"Total expense in first quarter: {total_expense_q1} dollars")
        
    elif x == 3:
        found = any(expense == 2000 for expense in data[0].values())
        if found:
            print("You spent exactly 2000 dollars in one of the months.")
        else:
            print("You did not spend exactly 2000 dollars in any month.")
            
    elif x == 4:
        data[0].update({"June": 1980})
        print(f"Updated monthly expenses: {data}")
        
    elif x == 5:
        data[0].update({"April": data[0].get("April") - 200})
        print(f"Corrected April's expense after refund: {data}")
        
    elif x == 6:
        print("Exiting program.")
        break
        
    else:
        print("Not a valid number.")
