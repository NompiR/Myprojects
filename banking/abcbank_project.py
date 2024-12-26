dict_cust_acc = {111: {'Name': 'Ajit', 'Address': 'Indira Nagar', 'Zip-code': 580012, 'Gender': 'Male', 'Account-type': 'Saving', 'Amt-balance': 500},115: {'Name': 'Arun', 'Address': 'Ashoka Nagar', 'Zip-code': 580052, 'Gender': 'Male', 'Account-type': 'Saving', 'Amt-balance': 1000}, 121: {'Name': 'Priya', 'Address': 'Jaya Nagar', 'Zip-code': 580082, 'Gender': 'Female', 'Account-type': 'Current' , 'Amt-balance': 500}, }
dict_lists = list(dict_cust_acc.keys())


def select_acc_no(i_acc):
    return dict_cust_acc[i_acc]


def is_dict_acc_no_avail(ip):
    dlen = len(dict_lists)
    for i in range(dlen):    
        if dict_lists[i] == ip:
            return True
        

def select_cust_acc_name(select_cust_acc_no):
    for key, val in select_cust_acc_no.items():
        if key == 'Name':
            return val
    
def select_cust_acc_address(select_cust_acc_no):
    for key, val in select_cust_acc_no.items():
        if key == 'Address':
            return val

def select_cust_acc_balance(select_cust_acc_no):
    for key, val in select_cust_acc_no.items():
        if key == 'Amt-balance':
            return val

        
def select_cust_acc_type(select_cust_acc_no):
    for key, val in select_cust_acc_no.items():
        if key == 'Account-type':
            return val
     
def deposite_amount(d_amount, cust_bal):
    total_c= cust_bal + d_amount
    return total_c

def withdraw_amount(amt, amt_withdraw):
    total_withdraw_amt = amt - amt_withdraw
    return total_withdraw_amt

def is_withdraw_amount_negative(amt, amt_withdraw):
    value = amt - amt_withdraw
    if -abs(value) == value:
        return True
    else:
        return False

def display(name, acc_no, acc_type, acc_amt):
    print("......................................................")
    print("\t\tMy account overview")
    print("......................................................")
    print("Name: ", name)
    print("My account number: ", acc_no)
    print("Account Type: ", acc_type)
    print("Amount Balance: ", acc_amt)
    print("......................................................")
    
def display_deposit(deposited_amt, deposit_amt):
    print("......................................................")
    print("\t\tMy account deposit")
    print("......................................................")
    print("Deposit amount: ", deposited_amt)
    print("Total Balance: ", deposit_amt)
    print("......................................................")

def display_balance(total_account_balance):
    print("......................................................")
    print("\t\tCheck my balance")
    print("......................................................")
    print('My Total balance: ', total_account_balance) 
    print("......................................................") 

def display_withdraw(cust_deposit_total_amount, input_withdrawal_amount):
    print("......................................................")
    print("\t\tMy Withdraw")
    print("......................................................")
    print("Withdrawal amount: ", input_withdrawal_amount)
    print('Remaining total amount', cust_deposit_total_amount)
    print("......................................................")
      



def customer_acc_bal_update_deposit(select_cust_acc_no, update_balance):
    dict_cust_acc[select_cust_acc_no]['Amt-balance'] += update_balance

def customer_acc_bal_update_withdraw(select_cust_acc_no, update_balance):
     dict_cust_acc[select_cust_acc_no]['Amt-balance'] -= update_balance

def customer_acc_bal_update_w(select_cust_acc_no, update_balance):
    dict_cust_acc[select_cust_acc_no]['Amt-balance'] = update_balance


print("......................................................")
print("\t\tWelcome to ABN Bank")
print("......................................................")

bankingOn = True

input_account_no = int(input("Enter Account number: "))
if is_dict_acc_no_avail(input_account_no):

    while bankingOn:
        
            select_input_account_no = select_acc_no(input_account_no)
            cust_acc_balance = select_cust_acc_balance(select_input_account_no)
            cust_acc_holder_name = select_cust_acc_name(select_input_account_no)
            cust_acc_type = select_cust_acc_type(select_input_account_no)
            
            print("1. My account overview")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Balance")
            print("5. Close")

            input_number = int(input("Enter the number of choice: "))    
            if input_number == 1:
                #My account overview

                display(cust_acc_holder_name, input_account_no, cust_acc_type, cust_acc_balance)           

            elif input_number == 2:
                #Deposite

                input_deposit_amount = int(input("Enter Deposit amount: "))
                customer_acc_bal_update_deposit(input_account_no, input_deposit_amount)
                customer_amount= select_cust_acc_balance(select_input_account_no)
                display_deposit(input_deposit_amount, customer_amount)
                
            elif input_number == 3:
                #Withdrawal

                input_withdraw_amount = int(input("Enter Withdraw amount: "))
                customer_amount_update_balance= select_cust_acc_balance(select_input_account_no)
                
                if customer_amount_update_balance <= 500:
                    print("You can not withdraw of minimum amount")
                else:
                    customer_amount_update_balance= select_cust_acc_balance(select_input_account_no)
                    #print('before', customer_amount_update_balance)
                    customer_acc_bal_update_withdraw(input_account_no, input_withdraw_amount)
                    customer_amount_update_balances = select_cust_acc_balance(select_input_account_no)
        
                    #print('after', customer_amount_update_balances)
                    totals = customer_amount_update_balances + input_withdraw_amount
                    if customer_amount_update_balances <= 500:
                        print("You can not withdraw of minimum amount")
                        customer_acc_bal_update_w(input_account_no, totals)
                        customer_amount_update_balances = select_cust_acc_balance(select_input_account_no)
                        print(customer_amount_update_balances)
                    else:
                        display_withdraw(customer_amount_update_balances, input_withdraw_amount)
                

            elif input_number == 4:
                #Balance

                display_balance(cust_acc_balance )

            else:
                break
    print("\t\tThank you for using ABC Bank")
    print("......................................................")
else:
    print('No account number existing')
    
