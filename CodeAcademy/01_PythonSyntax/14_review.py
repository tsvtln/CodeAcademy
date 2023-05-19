"""
1.Let’s apply all of the concepts you have learned one more time!
Create a variable called skill_completed and set it equal to the string "Python Syntax".

2. Create a variable called exercises_completed and set it equal to 13.
Create another variable called points_per_exercise and set it equal to 5.

3. Create a variable called point_total and set it equal to 100.

4. Update point_total to be the original value plus the result of
multiplying exercises_completed and points_per_exercise.

5. Add a comment above your declaration of points_per_exercise that says:
The amount of points for each exercise may change, because points don't exist yet

6. Print a string to the console that says:
I got X points!
with the value of point_total where X is.
"""

skill_completed, exercises_completed, points_per_exercise, point_total = 'Python Syntax', 13, 5, 100
# The amount of points for each exercise may change, because points don't exist yet
point_total += exercises_completed * points_per_exercise
print(f'I got {point_total} points!')



# in python2:
# skill_completed = 'Python Syntax'
# exercises_completed = 13
# point_total = 100
# #The amount of points for each exercise may change, because points don't exist yet
# points_per_exercise = 5
#
# point_total += exercises_completed * points_per_exercise
# print(str('I got ') + str(point_total) + str(' points!'))
