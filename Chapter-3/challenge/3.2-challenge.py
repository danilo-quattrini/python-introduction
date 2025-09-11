"""
Write a program that:
	•	Reads a file data.txt where each line contains: name,age,city.
	•	Stores the data in a list of dictionaries.
	•	Prints the average age.
	•	Prints all unique cities (as a set).
	•	Saves the result into summary.json with structure:

	{
      "average_age": 28,
      "unique_cities": ["Rome", "Milan", "Naples"]
    }
"""
import  json # import the JSON module inside the script

def write_into_json(input_file, input_datas):
    """
    Function we use to write into a JSON file
    :param input_file:
    :param input_datas:
    :return: None
    """
    with open(input_file, "w") as f:
            json.dump(input_datas, f, indent=4)

def read_file(input_file):
    """
    Function where we read the file, and we return a list with the values
    of the file.
    :param input_file:
    :return:list
    """
    people_list = []
    # open the file in read mode with the "r" code
    with open(input_file, "r") as f:
        list_of_people = f.readlines() # save each line inside string data

        # Convert data read from a file into a list of divided elements
        for new_data in list_of_people:
            # new_data would be a new list with the formatted data
            new_data = new_data.replace("\n", "") # replace all the occurrences of "\n" with a blank space
            new_data = new_data.split(",") # with the split function we divide the string for each comma ","

            # we assign to each part of the list their specific value
            dict_value = {"name": new_data[0],"age": int(new_data[1]), "city": new_data[2]} # then we save each element inside the dict
            people_list.append(dict_value) # we add into the list of people the dict we updated before
    return people_list

def average_age(user_list):
    """
    Function where we give a list of users, and we return the avg of all of their ages,
    from each user inside the list of dicts.
    :param user_list:
    :return: age_average
    """
    age_average: int  = sum([user["age"] for user in user_list])
    return age_average / len(user_list)

def define_unique_cities(user_list):
    """
    Function where we take a list of user, and we save into a list, the uniques cities,
    we found inside the list.
    :param user_list:
    :return: unique_city_list
    """
    unique_city_list = []
    for user in user_list:
        unique_city_list.append(user["city"])

    set_of_city = set(unique_city_list)
    unique_city_list.clear()
    for i in set_of_city:
        unique_city_list.append(i)
    print(unique_city_list)

    return unique_city_list

file = "data.txt" # file where we read the raw data
result_file = "summary.json"

# Extract the data from the txt file we created
user_list = read_file(file)

# Calculate the avg of the ages of all the user inside the list
avg_of_age = average_age(user_list)

# Calculate the uniques cities for all the user inside the list
list_of_unique_cities = define_unique_cities(user_list)

user_info.update({"avg_age": avg_of_age, "unique_cities": list_of_unique_cities})
user_summary.append(user_info)
# dict where we save the info of the user
user_info = {"average_age": avg_of_age, "unique_cities": list_of_unique_cities}

write_into_json(result_file, user_info)