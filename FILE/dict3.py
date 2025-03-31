phone_dict = {
  "John": "555-1234",
  "Emily": "555-5678",
  "Michael": "555-9012",
  "Sarah": "555-3456",
  "David": "555-7890"
}
name = input("Enter a name: ")
if name in phone_dict:
  print(name + "'s phone number is " + phone_dict[name])
else:
  print("Sorry, that name is not in the phone book.")
