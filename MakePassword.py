password = 'OpenSesame'

# three password attempts
for a in range(3):
    psw = input('Enter Password: ')
    b = 2
    if (psw == password):
        print("Access Granted")

    elif (b == 0):
        print("Password is incorrect!", a-b)
        break
    else:
        print("Wrong password")
        continue


print("Access Denied")