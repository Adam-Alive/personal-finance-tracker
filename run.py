# Personal Finance Tracker

# Enable user to input finance data
income = input('Monthly income: ')
print('Now enter the amount you spend each month on: ')
rent_mortgage  = input('Rent or mortgage: ')
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

dict_keys = ['rent_mortgage', 'gas', 'electric', 'phone', 'food', 'other']
dict_values = '0.00'
finance_dict = dict.fromkeys(dict_keys, dict_values)
print(finance_dict)


print('Test: Dictionary values are updated from input data... \n')
finance_dict['rent_mortgage'] = rent_mortgage
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

def main():
    '''
    Run all program functions  
    '''
    item_cost = str_to_int(finance_dict)

main()





