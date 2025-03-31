grade_dict = {
  "John": 85,
  "Emily": 92,
  "Michael": 78,
  "Sarah": 90,
  "David": 88
}

student = input("Enter a student name: ")
if student in grade_dict:
  print(student + "'s grade is " + str(grade_dict[student]))
else:
  print("Sorry, that student is not in the grade book.")
