"""
    Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
hours = int(input("Enter the amount of hours you have done this week\n==>"))
rate = int(input("Rate per hours?\n==>"))

print(f"Weekly earn {hours * rate}")