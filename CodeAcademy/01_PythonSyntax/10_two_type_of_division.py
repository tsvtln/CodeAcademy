# You have come home from the grocery store with 100 cucumbers to
# split amongst yourself and your 5 roommates (6 people total).
# Create a variable cucumbers that holds 100 and num_people that holds 6.

# Create a variable called whole_cucumbers_per_person that is the integer result of dividing cucumbers by num_people.
# Print whole_cucumbers_per_person to the console.

# You realize that the numbers don’t divide evenly. You don’t want to throw out the remaining cucumbers.
# Create a variable called float_cucumbers_per_person that holds the float result of dividing cucumbers by num_people.
# Print float_cucumbers_per_person to the console.

cucumbers, num_people = 100, 6
whole_cucumbers_per_person = int(cucumbers / num_people)
print(whole_cucumbers_per_person)
float_cucumbers_per_person = float(cucumbers / num_people)
print(float_cucumbers_per_person)

# in python 2:
# cucumbers, num_people = 100, 6
# whole_cucumbers_per_person = cucumbers / num_people
# print(whole_cucumbers_per_person)
# float_cucumbers_per_person = float(cucumbers) / float(num_people)
# print(float_cucumbers_per_person)

