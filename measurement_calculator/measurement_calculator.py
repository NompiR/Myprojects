one_inch = 2.54 #1 inch to Cm
one_cm = 0.393701 #1 cm to Inches
one_puund = 0.45359237 #1 pound to Killogram(KG)
one_kg = 2.2046226218 #1kg to lbs

newLine = '\n'

def one_cm_to_inch(cm):
    return cm / one_inch

def one_Inches_to_cm(inches):
    return inches * one_inch

def one_kg_to_pound(kg):
    return kg / one_puund

def one_pound_to_kg(pound):
    return pound / one_kg

def user_input(val):
    return int(input(f"Please enter {val} value: "))

def user_choice():
    print('\033[1m' +"*****Welcome to Small measurement Calculator using Python***** " + '\033[0m'+ newLine )
    print("1. Centimeters(Cm) Converter to Inches: ")
    print("2. Inches(In) Converter to Centimeters(cm): ")
    print("3. kilograms(Kg) Converter to Pounds: ")
    print("4. Pounds Converter to kilograms(Kg): ")
    print("5. Exit ")
    ip= int(input("Enter choose the numbers (1 - 5): "))
    return ip


def switch(select):
    if select == 1:
        get_user_input_values= user_input('Centimeters')
        result_cm_to_inches = one_cm_to_inch(get_user_input_values)
        print(newLine)
        print(get_user_input_values, "Centimeters (cm) to Inches is: ", round(float(result_cm_to_inches), 4))
        print(newLine)

    elif select == 2:
        get_user_input_values = user_input('Inches')
        result_inches_to_cm = one_Inches_to_cm(get_user_input_values)
        print(newLine)
        print(get_user_input_values, "Inches to Centimeters (cm) is: ", round(result_inches_to_cm, 4))
        print(newLine)

    elif select == 3:
        get_user_input_values = user_input('kilograms')
        result_kilogram_to_pound = one_kg_to_pound(get_user_input_values)
        print(newLine)
        print(get_user_input_values, "kilograms(Kg) to Pounds: ", round(result_kilogram_to_pound, 4))
        print(newLine)

    elif select == 4:
        get_user_input_values = user_input('Pounds')
        result_pounds_to_kilogram = one_pound_to_kg(get_user_input_values)
        print(newLine)
        print(get_user_input_values, "Pounds to kilograms(Kg): ", round(result_pounds_to_kilogram, 4))
        print(newLine)

    else:
        pass


calculateon= True

while calculateon:
    numbers = user_choice()
    if numbers in range(6):
        switch(numbers)
        #print(newLine)
        if numbers == 5:
            print("Exited the Calculator")
            break
    else:
        print("That number should be within range 1 to 5")
        calculateon = False
