wybor = input(" * - mnożenie, / - dzielenie, + - dodawać, - - odejmować")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if (wybor == '*'):
    print(a * b)
elif (wybor == '/'):
    if (b == 0):
        print("Nie dziel przez zero")
    else:
        print(a / b)
elif (wybor == '+'):
    print(a + b)
elif (wybor == '-'):
    print(a - b)
else:
    print("nie wybrałeś dobrego wyboru")
        
        
