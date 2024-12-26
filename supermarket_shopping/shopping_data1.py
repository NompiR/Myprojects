add_items= {1: {'Milk':22, 'Curd': 24, 'Eggs': 5, 'Moong dal': 180, 'Green gram': 160}, 2: {'Hair shampoo': 120, 'Hair oil': 110, 'Soap': 150, 'Tooth paste': 80}, 3: {'Carrot': 75, 'Peas': 115, 'Tomoto': 35, 'Onion': 180}}

def select_items(select):
    return add_items[select]
    
def select_add_item(select_item_no, add_item):
    for key, val in select_item_no.items():
        if key == add_item:
            return (key, val)
        
def add_measurement(Item):
    if Item == 'Milk' or Item == 'Curd' or Item == 'Hair shampoo' or Item == 'Hair oil':
        add_up = 'How many liters of {}'.format(Item)
    elif Item == 'Eggs' or Item == 'Tooth paste' or Item == 'Soap':
        add_up = 'How many {}'.format(Item)
    else:
        add_up = 'How many Kilogram of {}'.format(Item)
    return add_up


def Add_Price(Price, Measure):
        add_up_price = Price * Measure
        return add_up_price

def replay():
    reply = input("Do you want add more items (Y- yes / N- no)? ").capitalize()
    return reply

print("\nWelcome to Super Market")
print("Items No -- Items Name -- Total Price")
#print(select_item_no)
count = 0
Total = 0
dict={}
dict1 = {}
add_bag = {}
ShoppingOn = True
while ShoppingOn:
    
    inp = int(input("Enter items no: "))
    select_item_no = select_items(inp)
    inp1 = input("Enter item select name: ").capitalize()
    Items, Price  = select_add_item(select_item_no, inp1)
    ad= add_measurement(Items)
    add_input = 'Enter {} do you want? '.format(ad)
    measure= int(input(add_input))
    Total += Add_Price(Price, measure)
    dict[Items]= Price
    exit = replay()
    if exit == 'Y':
        continue
    else:
        break
   
print(measure)
print("Items No ---- Items name ---- Item Price --- Qty ---- Price")
counter = 1
for i, j in dict.items():
    print(counter,'     ', i ,'     ', j)
    counter += 1
print('Total', count ,'Shopping Prices: ',Total)
