"""

    Write a script that prompts the user to enter number of years. Calculate
    the number of seconds a person can live. Assume a person can live hundred years
"""

years_to_live = int(input("Enter number of years you have lived: "))

years_into_second = 365 * 86400

print(f"You have lived for {years_to_live * years_into_second} seconds.")