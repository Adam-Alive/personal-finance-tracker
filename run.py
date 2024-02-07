import os

global INCOME
global MONTHLY_EXPENDITURE

dict_keys = ['rent_mortgage', 'gas', 'electric', 'phone', 'food', 'other']
dict_values = '0'
finance_dict = dict.fromkeys(dict_keys, dict_values)


def start_app():
    '''
    Welcome messages and instructions
    '''
    print('> Welcome to your Personal Finance Tracker where you can')
    print('> calculate your monthly disposable income (or deficit)')
    print('> and so review and plan your finances.\n')

    print('> You will be asked to enter your monthly take-home pay')
    print('> (after tax and other deductions), followed by various')
    print('> costs for rent, utilities, food and leisure etc.\n')

    print('> There are 12 expenditure fields and 3 more blank fields')
    print('> where you can enter expenditure items not covered already.\n')

    print('> The output applies to any currency and will provide')
    print('> a summary of your weekly, monthly and annual finances.\n')

    print('> We suggest you use your monthly bank statement for reference.\n')

    print('> You should round your figures to the nearest whole number and')
    print('> enter 0 (zero) if an expenditure item does not apply to you.\n')
    print('> Begin by entering your monthly income and press return')
    print('> after each entry made:\n')


def clear():
    '''
    Clears the terminal window.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def str_to_int(data):
    '''
    Converts all string values to integers
    '''
    for value in finance_dict.values():
        item_cost = int(value)


def get_income():
    '''
    Get income data input by the user.
    Run a while loop to ensure input data is a whole
    number or 0.
    '''
    global INCOME
    while True:
        try:
            INCOME = int(input('> Monthly income: \n'))
            clear()
            print(INCOME)
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0\n')
    print(INCOME)
    get_rent_mortgage()


def get_rent_mortgage():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            rent_mortgage = int(input('> Rent or mortgage: '))
            finance_dict['rent_mortgage'] = rent_mortgage
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    get_gas()


def get_gas():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            gas = int(input('> Gas: '))
            finance_dict['gas'] = gas
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    get_electric()


def get_electric():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            electric = int(input('> Electric: '))
            finance_dict['electric'] = electric
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    get_phone()


def get_phone():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            phone = int(input('> Phone: '))
            finance_dict['phone'] = phone
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    get_food()


def get_food():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            food = int(input('> Food: '))
            finance_dict['food'] = food
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    get_other()


def get_other():
    '''
    Get expenditure data input by the user.
    Update the finance_dict with this value.
    '''
    print('> Enter the amount you spend each month on: \n')
    while True:
        try:
            other = int(input('> Other item not listed: '))
            finance_dict['other'] = other
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0 ')
    print(finance_dict)


def calculate_total_expenditure(data):
    '''
    Calculate total monthly expenditure.
    '''
    global MONTHLY_EXPENDITURE
    MONTHLY_EXPENDITURE = sum(data.values())
    print(MONTHLY_EXPENDITURE)
    #return monthly_expenditure


def calculate_monthly_surplus(income, expenditure):
    '''
    Subtract expenditure from income.
    '''
    surplus = income - expenditure
    print(surplus)
    if surplus > 0:
        print(f'> You have money to spare')
    elif surplus == 0:
        print(f'> Your expenditure matches your income exactly!')
    else:
        print(f'> You have a deficit')


print('> Thank you for completing your entries… \n')
print('> Your financial summary will soon follow… \n')

# Create dictionary from expenditure categories and input data
# Print dictionary for testing
print('Test: Dictionary initially has 0.00 for each value... \n')

# print(finance_dict)

print('Test: Dictionary values are updated from input data... \n')


if __name__ == '__main__':
    '''
    Run all program functions
    '''
    clear()
    start_app()
    # print(finance_dict)
    get_income()
    item_cost = str_to_int(finance_dict)
    calculate_total_expenditure(finance_dict)
    calculate_monthly_surplus(INCOME, MONTHLY_EXPENDITURE)
