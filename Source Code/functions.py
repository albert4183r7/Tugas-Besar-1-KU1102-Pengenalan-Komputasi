from os import access
import pickle
import sys
import time

pathEmail = r"Bin\email.bin"
pathPass = r"Bin\password.bin"
pathUsername = r"Bin\username.bin"




#Main Homepage
def home():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                WELCOME BACK!
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Home-Menu 
        1. Log In
        2. Sign up (First time use) 
        3. Exit
    """)
    ans = int(input('Choose : '))
    if ans == 1:
        login()
    elif ans == 2:
        signup()
    elif ans == 3:
        exit()
    else:
        print("Wrong input!")
        home()

#Load username, email, and password from bin
def load_username():
    with open(pathUsername,"rb") as h:
        try:
            return pickle.load(h)
        except:
            list3 = []
            with open(pathPass,"wb") as h:
                pickle.dump(list3, h)
            return []
def load_email():
    with open(pathEmail,"rb") as f:
        try:
            return pickle.load(f)
        except:
            list1 = []
            with open(pathEmail,"wb") as f:
                pickle.dump(list1, f)
            return []
def load_password():
    with open(pathPass,"rb") as g:
        try:
            return pickle.load(g)
        except:
            list2 = []
            with open(pathPass,"wb") as g:
                pickle.dump(list2, g)
            return []

#Reset function
def reset():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
            Resetting to Default...
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    clear = []
    with open(pathEmail,'wb') as f:
        pickle.dump(clear, f)
    with open(pathPass,'wb') as g:
        pickle.dump(clear, g)
    with open(pathUsername,'wb') as h:
        pickle.dump(clear, h)
    for i in range (5,0,-1):
        print(i," seconds remaining...")
        time.sleep(1)
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                  Success!
            Returning to Home-Menu...
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    time.sleep(1)
    login_home()

#Signup function
def signup ():
    load_username()
    load_email()
    load_password()
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
           Hello there! Who are you?
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    ls_email = load_email()
    ls_username = load_username()
    Name = input("Username: ")
    Email = input("Email address: ")
    sign = False
    for i in range(len(Email)):
            if Email[i] == "@":
                    for j in range(len(Email)):
                            if Email[j] == ".":
                                    sign = True
    if sign == False:
            print("Invalid email address!")
            signup()
    else:
        for i in range(len(load_username())):
            if Name == load_username()[i] or Email == load_password()[i]:
                print("User already exist!")
                print("Returning to home page...")
                time.sleep(0.5)
                home()
                break 
        ls_username.append(Name)
        with open(pathUsername, 'wb') as h:
            pickle.dump(ls_username, h)
        ls_email.append(Email)
        with open(pathEmail,"wb") as f:
            pickle.dump(ls_email, f)
        ls_password = load_password()
        Password = input("Password (minimum 6 character): ")
        if len(Password) < 6:
            print("Minimum of 6 character! Returning to homepage...")
            time.sleep(0.5)
            home()
        else:
            Verify = input("Rewrite Password: ")
            if Password != Verify:
                print("Wrong input! Returning to homepage...")
                time.sleep(0.5)
                home()
            else:
                print("Creating Account, please wait!")
                loading(0.2)
                print("Success!")
                ls_password.append(Password)
                with open(pathPass,"wb") as g:
                    pickle.dump(ls_password, g)
                print("Please log in your account.")
                time.sleep(0.5)
                home()    

#Login function
def login():
    load_username()
    load_email()
    load_password()
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                    Log In
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    User = input("Username: ")
    #Global username variable
    global Username
    Username = User
    Email_log = input("Email: ")
    Pass_log = input("Password: ")
    n=0
    while(n<2):
        if len(load_username()) == 0 and len(load_email()) == 0 and len(load_password()) == 0:#otentifikasi pertama kali (belum ada akun di bin)
            for i in range(3):
                if i != 2:
                    print("Invalid username or password!")
                    User = input("Username: ")
                    Email_log = input("Email: ")
                    Pass_log = input("Password: ")
                else:
                    print("Too many attempts! Returning to homepage...")
                    input("Press enter to continue...")
                    home()
        else:
            error = True
            for i in range(len(load_username())):
                if Email_log == load_email()[i] and Pass_log == load_password()[i] and User == load_username()[i]:
                    error = False
                    print("Logging in")
                    loading(0.2)
                    print("Success!")
                    time.sleep(0.5)
                    input("Press enter to continue...")
                    login_home()
                    break
            if error == True:
                print("Invalid username or password!")
                User = input("Username: ")
                Email_log = input("Email: ")
                Pass_log = input("Password: ")                                              
        n+=1
    if error ==  True:
        print("Too many attempts! Returning to homepage...")
        input("Press enter to continue...")
        home()

#Login homepage
def login_home():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
            WELCOME BACK """+str(Username)+""" !
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Home-Menu 
        1. Preset
        2. Reset
        3. Log out
        4. Exit 
    """)
    ans = int(input('Choose : '))
    if ans == 1:
        preset()
    elif ans == 2:
        reset()
    elif ans == 3:
        home()
    elif ans == 4:
        exit()
    else:
        print("Wrong input!")
        login_home()


#Preset function
def preset():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                 Preset Menu
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Preset-Menu 
        1. Defrost
        2. Grill Fry
        3. Set Timer
        4. Back to Home
        Press Enter to Exit 
    """)
    ans = int(input('Choose : '))
    if ans == 1:
        defrost()
    elif ans == 2:
        grill()
    elif ans == 3:
        home()
    elif ans == 4:
        login_home()
    elif ans == "":
        exit()
    else:
        print("Wrong input!")

#Defrost function
def defrost():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                   Defrost
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    """)
    max = True
    while (max):
        mass = float(input("Input total weight (kg [max 1.4kg]): "))
        if mass > 1.4 :
            print("Maximum 1.4kg ! Please reduce the size.")
        else:
            max = False
    t = round((10/0.45)*mass)*60
    timer(t)

#Grill function
def grill():
    print("""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
                  Grill Fry
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        Grill Fry 
        1. Ayam
        2. Sapi
        3. Kentang
        4. Ikan
        5. Back
    """)
    ans = int(input("Choose: "))
    if ans == 1:
        timer(180)
    elif ans == 2:
        timer(480)
    elif ans == 3:
        timer(180)
    elif ans == 4:
        timer(180)
    elif ans == 5:
        preset()
    else:
        print("Wrong input!")
        grill()











#Timer function
def timer(t):
    print("Initializing...")
    time.sleep(1)
    print("Starting...")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Done!")
    back = input("Press enter to return to Home-Menu")
    if back == "" :
        login_home()
    else:
        login_home()

#Loading function
def loading(seconds):
    animation = ["■■□□□□□□□□□□","■■■■□□□□□□□□", "■■■■■□□□□□□□", "■■■■■■□□□□□□", "■■■■■■■□□□□□", "■■■■■■■■□□□□", "■■■■■■■■■□□□", "■■■■■■■■■■□□", "■■■■■■■■■■■□", "■■■■■■■■■■■■"]
    for i in range (len(animation)):
        time.sleep(seconds)
        sys.stdout.write("\r"+ animation[i % len(animation)]+" "+str(i*10+10)+"%")
        sys.stdout.flush()
    print("\n")

    
    

