# open facebook
print("welcome to facebook")
fb=input("choose option 1.login, 2.create new fb account:")
if fb=="1":
    login=input("select your login process 1.7218142280 ,2.arpitalataye@123:")
    if login=="1" or login=="2":
            password=str(input("enter the password 1.sugakook97,2.forget password"))
            if password=="1":
                print("your acount is successfully login")
            elif fbpass=="2":
                way=int(input("choose a way to login 1.send code via sms 2. enter password to log in:"))
                if way=="1":
                    print("code will be send in your mo no")
                    code=int(input("enter code:"))
                    if code=="4321":
                        print("create new pass")
                        fb_new_pass=input("create pass:")
                        if fb_new_pass=="suga97":
                            print("your pass is successfuly created")
                        else:
                            print("incorrect password")
                    else:
                        print("invalid code")
                elif way==2:
                    pw=input("enter password:")
                    if pw=="sugakook97":
                        print("your login is successfuly") 
                    else:
                        print("incorrect pass")
            else:
                    print("another way to continue")
    else:
        print("invalid email please enter valid email or phone")
elif fb=="2":
    print("join facebook")
    name=input("enter the name you see in real life 1.miraya tiwari:")
    if name=="1":
        birth=input("what is your birthday?: 1.4 mar 2003")
        if birth=="1":
            gender=input("what is your gender 1.female ,2. male")
            if gender=="1":
                print("your gender added successfully")
                mobile_no=input("enter your mobile no 1.7218143980")
                if mobile_no=="1":
                    print("your mobile number link to facebook")
                    password=input("create your password 1.radhe")
                    if password=="1":
                        print("your account create sucessfully")
                    else:
                        print("repeat the process")
                else:
                    print("you enter wrong mobile number reenter it:")
            elif gender=="2":
                print("your gender added successfully")
                mobile_no=input("enter your mobile no 1.7218143980")
                if mobile_no=="1":
                    print("your mobile number link to facebook")
                    password=input("create your password 1.radhe")
                    if password=="1":
                        print("your account create sucessfully")
                    else:
                        print("repeat the process")
                else:
                    print("you enter wrong mobile number reenter it:")
    else:
        print("enter correct name to create fb:")