greeting = input("Hello, possible pirate! What's the password?")
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")

#Line 1 added a close speach mark at the end 
#line 2 changed the curly bracket to a square bracket 
#line 5 indented as its apart of the else statement

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s" % author + " died in " + "%s." % date)
# line 16 move the close bracket to close the dictionary
# line 11 corrected the spelling misktake 
# line 18 added a "," after author and chamge the square brackets to curly bracket

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print ('Woah, thats the past!')
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
# line 24 changed "." to "(" to add int 
# line 30 indented the line as its apart of the else statement
exam_one = int(input("Input exam grade one:"))

exam_two = int(input("Input exam grade two:"))

exam_three = int(input("Input exam grade three:"))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print ("Student is passing.")


first_name = 'John'
last_name = 'Doe'

full_name = first_name + " " + last_name

print("The person's full name is:",  full_name)
# line 74 added a " " to add a space between john and Doe
