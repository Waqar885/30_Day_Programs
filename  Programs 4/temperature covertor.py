def kelvin(x):
    return x + 273

def celsius(x):
    return x - 273

def ferh(x):
    return x*1.8 + 32

def fcel(x):
    return (x-32)/1.8
b = input("Enter\n 1 for Kelvin to Celsius\n 2 for Celsius to kelvin\n 3 for Celsius to Fahrenheit\n 4 for Fahrenheit to Celsius\n 5 for kelvin to Fahrenheit\n 6 for Fahrenheit to kelvin: \n")
try:
    c = int(b)
    a = int(input("Enter the temperature: "))
    if (c == 1):
        print(celsius(a))
    elif(c == 2):
        print(kelvin(a))
    elif(c == 3):
        print(ferh(a))
    elif(c == 4):
        print(fcel(a))
    elif(c == 5):
        v = celsius(a)
        print(ferh(v))
    elif(c == 6):
        n = fcel(a)
        print(kelvin(n))


except:
    print("Input is not number try again and enter number")
