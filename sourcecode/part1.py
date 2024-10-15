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
    print("Alright! Your account is almost ready let's secure it with a password\nThe password must contain:\n#Atleast one Special Character\n#Atleast one number\n#Atleast one UpperCase alphabet\n#Atleast 8 characters\n#Atleast one lower case")
    j=0
    i=0
    while j!=1:
        password=input('Password Please:\n')
        while j!=1:
            flag = 0
            if (len(password)<=8):
                flag = -1
                s="Length is less than 8"
                break
            elif not re.search("[a-z]", password):
                flag = -1
                s="Lower case character missing"
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                s="Upper case character missing"
                break
            elif not re.search("[0-9]", password):
                flag = -1
                s="Digit missing"
                break
            elif not re.search("[_@$]" , password):
                flag = -1
                s="Special character missing"
                break
            elif re.search("\s" , password):
                flag = -1
                break
            else:
                flag = 0
                print("Valid Password")
                j=1
                break
        if flag == -1:
                print("Not a Valid Password ")
                print(s)

print("Your account has been created!") 
userpasswords.append(password)
b=input('Enter 2 to Login!\n')
if b=='2':
    n=0
    m=0
    while n==0 or m==0:
        n=0
        m=0
        name=input('Enter your email id\n')
        name.lower()
        password=input('Enter you password\n')
        i=0
        j=0
        k=0
        for i in useremails:
            if name==useremails[i]:
                for j in userpasswords:
                    if password==userpasswords[i]:
                        print("Welcome back")
                        k+=1
        if k==0:
            print('Invalid details!Recheck you details or sign up')
n=1
while n!=0:      
    location=input('Enter your location!\nPune\nMumbai\n')
    location.lower()
    if location=='pune':
        destination=input('Enter your destination\n')
        destination.lower()
        if destination=='dubai':
            month=input('Flights available for the month of January and February\nEnter month of travel')
            month.lower()
            if month=='january':
                date=int(input('Choose a date from 1-1-25 to 31-1-25'))
                tl=['2.00-5.00','13.00-15.00','6.00-11.00(2 hours halt at Delhi International airport']
                print(tl)
                if date in range(1,16):
                    sum=16000
                    print(sum)
                else:
                    sum=18000
                    print(sum)
                age=int(input('Enter you age'))
                if age>6:
                    pass
                else:
                    sum=sum/2
                    
        if destination=='singapore':
            singapore={'January':{1:{'02.00-5.00 Non-stop':16000,'12.30-7.30 Layover at Delhi international airport':10000,'23.55-2.55 Non Stop':15000},2:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],3:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],4:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],5:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55']},'February':{1:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],2:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],3:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],4:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55'],5:['02.00-5.00 Non-stop','12.30-7.30 Layover at Delhi international airport','23.55-2.55']}}
            print(singapore.keys())
            month=input('Enter your Month')
            print(singapore[month].keys())
            print(singapore[month].values())
            date=input("Choose a date") 
            print(f'Available flights on that day!{singapore[month][date].values()}')
            n=input('Which flight do you want to take? Enter the number:')
            final=singapore[month][date][n+1]
            print("Here are your final flight details:")
            print(f'Date:{month}{date}')
            print(f'Timings:{final}')
            sum=singapore[month][date][n+1].value()
    print('Switch to business class?')
    bus=input('y for YES and n for NO')
    if bus=='y':
        sum=sum+20000
    print('Almost there! Would you like to add some food items?')
    food=input('y for YES and n for NO')
    if food=='y':
        print('We serve one meal and a drink according to your flight timings!Book now to get one')
        ans=input('Enter y for Adding food and n for not adding it')
        if ans=='y':
            sum=sum+1500
    print('Total amount to be paid=',sum)
    

            
        

    
        

        




    

    
    




