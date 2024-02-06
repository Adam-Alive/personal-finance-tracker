import os
# Personal Finance Tracker
# Global variables 
dict_keys = ['rent_mortgage', 'gas', 'electric', 'phone', 'food', 'other']
dict_values = '0.00'
finance_dict = dict.fromkeys(dict_keys, dict_values)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Enable user to input finance data
def get_income():
    while True:
        try:
            income = int(input('Monthly income: '))
            clear()     
            break
        except ValueError:
            print('Data is not valid, please try again')
    get_rent_mortgage()


def get_rent_mortgage():
    print('Now enter the amount you spend each month on: ')
    while True:
        try:
            rent_mortgage = int(input('Rent or mortgage: '))           
            finance_dict['rent_mortgage'] = rent_mortgage
            clear()
            break
        except ValueError:
            print('Data is not valid, please try again')


clear()
gas = input('Gas: ')
electric = input('Electric: ')
phone = input('Phone: ')
food = input('Food: ')
other = input('Other item not listed: ')

print('Thank you for completing your entries… \n')
print('Your financial summary will soon follow… \n')

# Create dictionary from expenditure categories and input data
# Print dictionary for testing
print('Test: Dictionary initially has 0.00 for each value... \n')

print(finance_dict)


print('Test: Dictionary values are updated from input data... \n')
finance_dict['gas'] = gas
finance_dict['electric'] = electric
finance_dict['phone'] = phone
finance_dict['food'] = food
finance_dict['other'] = other
print(finance_dict)

# Test access to dictionary values
# Test convert values to int and multiply by 2
def str_to_int(data):
    '''
    Converts all string values to integers
    '''
    for value in finance_dict.values():
        item_cost = int(value)
        item_cost = item_cost * 2       
        print(item_cost)

#item_cost = str_to_int(finance_dict)

if __name__ == '__main__':
    '''
    Run all program functions  
    '''
    clear()
    get_income()    
    item_cost = str_to_int(finance_dict)
