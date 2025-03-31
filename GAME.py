import random
import pyttsx3
def speak(s):
    ts=pyttsx3.init()
    ts.say(s)
    ts.runAndWait()
def bat():
    v1="it's your batting"
    speak(v1)
    sum1=0
    while True:
        i=random.randint(0,10)
        j=int(input("enter a number b/w (0,10)"))
        print(i)
        if j==0 and j!=i and j<=10 and j>=0:
            sum1+=i
        elif j!=0 and j!=i and j<=10 and j>=0:
            sum1+=j
        elif j==i and j<=10 and j>=0:
            speak("out's that ")
            print("total is", sum1)
            break
    v3="it's my batting"
    speak(v3)
    sum2=0
    while True:
        y=random.randint(0,10)
        x=int(input("enter a number b/w (0,10)"))
        print(y)
        if y==0 and x!=y and x<=10 and x>=0:
            sum2+=x
        elif y!=0 and x!=y and x<=10 and x>=0:
            sum2+=y
        elif x==y and x<=10 and x>=0:
            print("total is", sum2)
            break
        if sum2>sum1:
            break
    if sum1>sum2:
        c=sum1-sum2
        print("you won by",c,"runs")
    elif sum1==sum2:
        print("draw")
    elif sum1<sum2:
        d=sum2-sum1
        print("you lost by",d,"runs")
def ball():
    print ("it's my batting")
    sum2=0
    while True:
        y=random.randint(0,10)
        x=int(input("enter a number b/w (0,10)"))
        print(y)
        if y==0 and x!=y and x<=10 and x>=0:
            sum2+=x
        elif y!=0 and x!=y and x<=10 and x>=0:
            sum2+=y
        elif x==y and x<=10 and x>=0:
            print("total is", sum2)
            break
    print ("it's your batting")
    sum1=0
    while True:
        i=random.randint(0,10)
        j=int(input("enter a number b/w (0,10)"))
        print(i)
        if j==0 and j!=i and j<=10 and j>=0:
            sum1+=i
        elif j!=0 and j!=i and j<=10 and j>=0:
            sum1+=j
        elif j==i and j<=10 and j>=0:
            print("total is", sum1)
            break
        if sum1>sum2:
            break
    if sum1>sum2:
        c=sum1-sum2
        print("you won by",c,"runs")
    elif sum1==sum2:
        print("draw")
    elif sum1<sum2:
        d=sum2-sum1
        print("you lost by",d,"runs")

    
k=random.randint(0,1)
h=int(input("toss enter 0 or 1 :"))
if k==h:
    print ("you won the toss")
    p=int(input("enter 0 for batting and 1 for balling:"))
    if p==0:
        bat()
    elif p==1:
        ball()
else:
    g=["batting","balling"]
    m=random.choice(g)
    print("you lost i choose",m)
    if m=="batting":
        ball()
    if m=="balling":
        bat()
