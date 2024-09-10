import smtplib
while(1>0):
    print("\nWelcome Aboard!\n\nEvery flight has a special experience and moment associated with it and we at SushiAir make it Remarkable for you!\n")
    users_fullnames=[]
    userpasswords=[]
    useremails=[]
    print("Before proceeding with the Booking process:\n\nSign Up if its your first time on our site or Login\n")
    b=int(input('Press 1 for SignUp and 2 for login\n'))
    c=0
    d=0
    e=0
    a=0
    if b==1:
        name=input('Enter your full name\n')
        users_fullnames.append(name)
        print("Alright! Your account is almost ready let's secure it with a password\nThe password must contain:\n#Atleast one Special Character\n#Atleast one number\n#Atleast one UpperCase alphabet\n")
        passkey=getpass.getpass('Password Please:\n')

        if '!@#$%^&*-()_+=`~[]}{;:"?.><' in passkey:
            c=1
        elif '1234567890' in passkey:
            d=1
        elif 'QWERTYUIOPASDFGHJKLZXCVBNM' in passkey:
            e=1

        if c!=1:
            print('Add a SPECIAL CHARACTER to the password!\n')
        if d!=1:
            print('Add a NUMBER to the password!\n')
        if e!=1:
            print('Add an UPPER CASE ALPHABET to the password!\n')
        if c==1 and d==1 and e==1:
            print("Your account has been created!\n")
            userpasswords.append(passkey)
            a+=1
        b=int(input(print('Enter 2 to Login!')))
    if b==2:
        name=input('Enter your email id')
        name=name.lower()
        if name in useremails:
            password=input('Enter you password')
            if password in userpasswords:
                print('Welcome Back!')

