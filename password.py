import pickle
accounts = {}
code = "1234"


def account():
    writedict()
    readdict()
    print("Would you like to create an account, sign in, or exit?")
    print("Enter create account, sign in, or exit")
    sign = input()
    sign = f"{sign.lower()}"
    if sign == "sign in":
        signin()
    elif sign == "create account":
        createaccount()
    elif sign == "exit":
        exit()
    elif sign == "print":
        view()
    else:
        account()


def view():
    writedict()
    readdict()
    counter = 0
    check = input("Enter code:")
    if check == code:
        print(accounts)
        account()
    else:
        counter = counter + 1
        if counter >= 5:
            exit("Too many incorrect passwords")
        else:
            print("Incorrect code")
            view()


def signin():
    writedict()
    readdict()
    usr = input("Enter your username:")
    pas = input("Enter your password:")
    if pas == accounts[usr]:
        print("You have been signed in!")
        print("Would you like to delete your account, change password, or sign out?")
        a = input(" Enter delete, change pass, or sign out")
        a = f"{a.lower()}"
        if a == "delete":
            deleteaccount()
        elif a == "sign out":
            account()
        elif a == "change pass":
            userpass = input("Enter current password:")
            if userpass == pas:
                newpas = input("Enter your new password:")
                pascheck = input("Re-enter new password:")
                if newpas == pascheck:
                    accounts[usr] = newpas
                    writedict()
                    print(f"Changed password for: {usr}")
                    print("Please re-sign in with your new password")
                    signin()
                else:
                    signin()
            else:
                signin()
        else:
            signin()
    else:
        print("\nIncorrect Username or Password\n")
        signin()


def createaccount():
    readdict()
    tempusr = input("Enter a username:")
    temppas = input("Enter a password:")
    pascheck = input("Re-enter password:")
    if pascheck == temppas:
        usrget = accounts.get(tempusr, 'Account exists')
        if usrget != "Account exists":
            print("Account already exists")
            account()
        else:
            accounts[tempusr] = pascheck
            print("\nAccount created!")
            # print(f"Your site email is: {tempusr}@password.com\n")
            account()
            writedict()
    else:
        print("You typed a different password both times. Please try again")
        createaccount()


def deleteaccount():
    accountusr = input("Enter your username:")
    accountpsw = input("Enter your password:")
    if accountpsw == accounts[accountusr]:
        sure = input(f"Are you sure you want to delete your account: {accountusr}? Enter yes or no")
        sure = f"{sure.lower()}"
        if sure == "yes":
            print(f"Deleting account: {accountusr}")
            del accounts[accountusr]
            account()
            writedict()
        elif sure == "no":
            print(f"Not deleting your account: {accountusr}")
            account()
        else:
            deleteaccount()
    else:
        deleteaccount()


def writedict():
    output = open('password.pkl', 'wb')
    pickle.dump(accounts, output)
    output.close()


def readdict():
    global accounts
    pkl_file = open('password.pkl', 'rb')
    accounts = pickle.load(pkl_file)
    pkl_file.close()


try:
    readdict()
except FileNotFoundError:
    writedict()
writedict()
account()
