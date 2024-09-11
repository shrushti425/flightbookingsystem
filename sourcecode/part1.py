import getpass
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
        while c!=1 and d!=1 and e!=1:
            passkey=getpass.getpass('Password Please:\n')
            l1=['0','1','2','3','4','5','6','7','8','9']
            l2=['!','@','#','$','%','^','&','*',')','(','-','_','+','=','{','}','[',']',':',';','"','?','/','.','>','<','~',',','`']
            l3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            for i in l1:
                if i in passkey:
                    c==1
                    break
            for i in l2:
                if i in passkey:
                    d==1
                    break
            for i in l3:
                if i in passkey:
                    e==1
                    break
         
            
        
        b=int(input(print('Enter 2 to Login!')))
    if b==2:
        name=input('Enter your email id')
        name=name.lower()
        if name in useremails:
            password=input('Enter you password')
            if password in userpasswords:
                print('Welcome Back!')

