import re
print("\nWelcome Aboard!\n\nEvery flight has a special experience and moment associated with it and we at SushiAir make it Remarkable for you!\n")
users_fullnames=[]
userpasswords=[]
useremails=[]
print("Before proceeding with the Booking process:\n\nSign Up if its your first time on our site or Login\n")
b=input('Press 1 for SignUp and 2 for login\n')
if b=='1':
    name=input('Enter your full name\n')
    users_fullnames.append(name)
    email=input('Enter your email id\n')
    useremails.append(email)
    print("Alright! Your account is almost ready let's secure it with a password\nThe password must contain:\n#Atleast one Special Character\n#Atleast one number\n#Atleast one UpperCase alphabet\n")
    j=0
    while j!=1:
        password=input('Password Please:\n')
        flag = 0
        if (len(password)<=8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]" , password):
            flag = -1
            break
        elif re.search("\s" , password):
            flag = -1
            break
        elif flag == -1:
            print("Not a Valid Password ")

        else:
            flag = 0
            print("Valid Password")
            j=1
            break
print("Your account has been created!") 
userpasswords.append(password)
b=input('Enter 2 to Login!')
if b=='2':
    name=input('Enter your email id')
    name.lower()
    if name in useremails:
        password=input('Enter you password')
        if password in userpasswords:
            print('Welcome Back!')

