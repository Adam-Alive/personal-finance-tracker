import os

global INCOME
global MONTHLY_EXPENDITURE
global RESTART

dict_keys = ['Rent or mortgage', 'Gas', 'Electricity', 'Phone', 'Food']
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

    print('> There are 10 expenditure fields and you will be able')
    print('> to enter expenditure items not already listed.\n')

    print('> The output applies to any currency and will provide')
    print('> a summary of your weekly, monthly and annual finances.\n')

    print('> We suggest you use your monthly bank statement for reference.\n')

    print('> You should round your figures to the nearest whole number and')
    print('> enter 0 (zero) if an expenditure item does not apply to you.\n')
    input('> Please press RETURN to begin...\n')
    clear()


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
    print('> Begin by entering your monthly income and press RETURN')
    print('> after each entry made:\n')
    global INCOME
    while True:
        try:
            INCOME = int(input('> Monthly income: \n'))
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0\n')
    # get_expenditure(finance_dict) ** CALLED IN MAIN BUT NEED HERE TOO?


def get_expenditure(data):
    '''
    Get expenditure data input by the user.
    Update the finance_dict with these values.
    '''
    print('> Enter the amount you spend each month on: \n')
    for key, value in finance_dict.items():
        while True:
            try:
                value = int(input(f'> {key}: \n'))
                finance_dict[key] = value
                clear()
                print('> Enter the amount you spend each month on: \n')
                break
            except ValueError:
                print('> Data is not valid, please enter a whole number or 0')
    clear()
    ask_user_item()


def ask_user_item():
    '''
    Ask user if they wish to enter more expenditure items.
    Validate input data for yes or no options.
    '''
    print('> Would you like to add any more expenditure items not covered?\n')
    answer = input('> Enter y or Y for yes, n or N for no\n')
    while True:
        try:
            if answer == 'y':
                get_user_item()
                break
            elif answer == 'Y':
                get_user_item()
                break
            elif answer == 'n':
                # ** I CALL THIS FUNCTION HERE - HAVE CALLED IN MAIN TOO?
                calculate_total_expenditure(finance_dict)
                clear()
                break
            elif answer == 'N':
                # ** I CALL THIS FUNCTION HERE - HAVE CALLED IN MAIN TOO?
                calculate_total_expenditure(finance_dict)
                clear()
                break
        except ValueError:
            # answer = input('> Enter y or Y for yes, n or N for no\n')
            print('> Enter y or Y for yes, n or N for no\n')


def get_user_item():
    '''
    Ask user to input name of expenditure item and amount.
    Update the finance_dict with this key and value.
    '''
    item_key = input('> Name of item: ')
    while True:
        try:
            item_value = int(input(f'> Enter the amount you spend each month on: {item_key}\n'))
            finance_dict.update({item_key: item_value})
            clear()
            break
        except ValueError:
            print('> Data is not valid, please enter a whole number or 0')
    ask_user_item()


def calculate_total_expenditure(data):
    '''
    Calculate total monthly expenditure.
    '''
    global MONTHLY_EXPENDITURE
    MONTHLY_EXPENDITURE = sum(data.values())


def item_list(data):
    '''
    Get finance_dict and print list of all expenditure items.
    Add a thousand comma separator to monthly expenditure output.
    Print monthly expenditure.
    '''
    print('> YOUR EXPENDITURE\n')
    for key, value in finance_dict.items():
        print(f'> {key.capitalize()}: {value}')
    print('\n')

    # Adds a thousand comma separator.
    global MONTHLY_EXPENDITURE
    convert = '{:,}'
    monthly_expenditure = convert.format(MONTHLY_EXPENDITURE)

    print(f'> MONTHLY EXPENDITURE: {monthly_expenditure}\n')
    input('> Please press RETURN to see your financial summary...\n')
    clear()


def calculate_monthly_surplus(income, expenditure):
    '''
    Subtract expenditure from income to calculate surplus.
    Add a thousand comma separator to output figures.
    Print out summary of financial data with messages.
    '''
    surplus = income - expenditure

    # Adds a thousand comma separator.
    convert = '{:,}'
    income = convert.format(income)
    expenditure = convert.format(expenditure)

    # Prints out first part of financial summary.
    print(f'> YOUR FINANCIAL SUMMARY\n')
    print(f'> Monthly income: {income}\n')
    print(f'> Monthly expenditure: {expenditure}\n')
    print(f'> Income less expenditure: {convert.format(surplus)}\n')
    if surplus > 0:
        print(f'> You have a monthly disposable income of {convert.format(surplus)} and')
        print(f'> can consider additional savings or expenditure.\n')
    elif surplus == 0:
        print(f'> Your expenditure matches your income exactly!\n')
    else:
        print(f'> You have a monthly deficit of {convert.format(surplus)} and')
        print(f'> should review your expenditure.\n')
    #  ** CALL THIS FUNCTION HERE OR STAY IN MAIN?
    # closing_summary()


def closing_summary():
    '''
    Calculate annual and weekly finance figures.
    Add a thousand comma separator to output figures.
    Print out summary of financial data with messages.
    Ask user to restart or exit.
    '''
    annual_income = INCOME * 12
    annual_expenditure = MONTHLY_EXPENDITURE * 12

    # Weekly figures are rounded down to nearest whole number.
    weekly_income = annual_income // 52
    weekly_expenditure = annual_expenditure // 52

    # Adds a thousand comma separator
    convert = '{:,}'
    annual_income = convert.format(annual_income)
    annual_expenditure = convert.format(annual_expenditure)
    weekly_income = convert.format(weekly_income)
    weekly_expenditure = convert.format(weekly_expenditure)

    # Prints out second part of financial summary.
    print(f'> Your annual income: {annual_income}\n')
    print(f'> Your annual expenditure: {annual_expenditure}\n')
    print(f'> Your weekly income: {weekly_income}\n')
    print(f'> Your weekly expenditure: {weekly_expenditure}\n')
    print('> DISCLAIMER: This app is for illustrative purposes only.\n')

    # Restart or exit.
    global RESTART
    RESTART = input('> Enter 1 to restart or 2 to exit.\n')
    restart_or_close()


def restart_or_close():
    '''
    Return to start if user enters 1.
    Print closing message if user enters 2.
    '''
    global RESTART
    if RESTART == '1':
        clear()
        # finance_dict.clear() ** EMPTIES DICT COMPLETELY
        # ** TEST PRINT SHOWS THAT DICT IS STILL POPULATED.
        print(finance_dict)
        get_income()
    elif RESTART == '2':
        clear()
        print('> Thank you for using the Personal Finance Tracker.\n')
        print('> Goodbye!')
    else:
        RESTART = input('> Enter 1 to restart or 2 to exit.\n')


if __name__ == '__main__':
    '''
    Run all program functions
    '''
    clear()
    start_app()
    get_income()
    item_cost = str_to_int(finance_dict)
    get_expenditure(finance_dict)
    item_list(finance_dict)
    calculate_total_expenditure(finance_dict)
    calculate_monthly_surplus(INCOME, MONTHLY_EXPENDITURE)
    closing_summary()
    restart_or_close()
