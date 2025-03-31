"""s="string in python"
print(s.capitalize())
print(s.title())
s6=s.replace("in","data type")
print(s6)
""
word="work hard"
result= word.find('work')
print("substring,'work',found at index:",result)
result= word.find('har')
print("substring,'har',found at index:",result)
if(word.find('pawan') !=-1):
    print("yes")
else:
    print("no")
"""
mysubject="Computer Science"
print(mysubject[0:len(mysubject)])
print(mysubject[-7:-1])
print(mysubject[::2])
print(mysubject[len(mysubject)-1])
print(mysubject*2)
print(mysubject[::-2])
print(mysubject[:3]+mysubject[3:])
print(mysubject.swapcase())
print(mysubject.startswith('Comp'))
print(mysubject.isalpha())
