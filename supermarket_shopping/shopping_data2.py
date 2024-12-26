lists_dict = {'Milk':22, 'Curd': 24, 'Eggs': 5, 'Moong dal': 180, 'Green gram': 160 , 'Hair shampoo': 120, 'Hair oil': 110, 'Soap': 150, 'Tooth paste': 80, 'Carrot': 75, 'Peas': 115, 'Tomoto': 35, 'Onion': 180}
list_of_dict_tuples = ('Milk', 'Curd','Eggs','Moong dal','Green gram','Hair shampoo','Hair oil', 'Soap','Tooth paste','Carrot','Peas','Tomoto','Onion')

def select_an_item(user_input_select):
    for key, val in lists_dict.items():
        if user_input_select == key:
            return (key, val)
        

def add_measurement(Item):
    if Item == 'Milk' or Item == 'Curd' or Item == 'Hair shampoo' or Item == 'Hair oil':
        add_up = 'How many liters of {}'.format(Item)
    elif Item == 'Eggs' or Item == 'Tooth paste' or Item == 'Soap':
        add_up = 'How many {}'.format(Item)
    else:
        add_up = 'How many Kilogram of {}'.format(Item)
    return add_up   

def Add_price(Price, Mesaure):
    add_up_price = Price * Mesaure
    return add_up_price

def replay():
    reply = input("Do you want add more items (Y- yes / N- no)? ").capitalize()
    return reply

def print_out(dictionary, Measures):
    count = 0 - 1 
    for i, j in dictionary.items():
        count +=1 
        addP = j * Measures[count]
        print(count+1,'\t',i ,'\t\t', j ,'\t\t', Measures[count],'\t', addP )


#While loop area
ShoppingOn = True
count = 0
Total_cart = 0
dict = {}
list_addup = []

while ShoppingOn:
    count +=1
    user_input = input("Enter Items name: ").capitalize()
    if user_input not in list_of_dict_tuples:
        print("The item is not correct spelling, Try again to correct spelling")
        continue
    item_key, item_val = select_an_item(user_input)
    #print(item_key) 
    add_measurements = add_measurement(item_key)
    add_input_measurement = 'Enter {} do you want? '.format(add_measurements)#
    user_input_measure = int(input(add_input_measurement))
    Total_cart += Add_price(item_val, user_input_measure)
    dict[item_key] = item_val
    list_addup.append(user_input_measure)
    exit = replay()
    if exit == 'Y':
        continue
    else:
        break

print("\nWelcome to ABC Super Market: ")
print("---------------------------------------------------------------")
print("Sl no\tItems name\tItem Price\tQty\tTotal")
print_out(dict, list_addup)
print("---------------------------------------------------------------")
print("Total items:", count,"\t\t\t    Total price:",Total_cart)

