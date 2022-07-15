master_pwd = input ("What will be your master password?")

def view():
    pass


def add():
    name = input('Account Name: ')
    pwd = input("Passowrd: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)

while True:
mode = input ("Would you like to add a new password or view existing  ones (view, add), press q to quiit?").lower()
if mode == "q":
    break

if mode == "view":
    view()

elif mode == "add":
    pass
else:
    print("Invalid mode.")
    continue