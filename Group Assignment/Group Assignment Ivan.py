# Group Assignment

import math


# growth rate calculator
# takes growth rate and social distancing % as input
def growth_rate(rate, SD):
    # use formula provided
    value = rate * (1 - (SD / 100))
    return value


# total positive tests for each state calculator
# takes initial positive test values, scaled growth rate, and number of days as input
def testing(initial, rate, days):
    # create empty list for each state
    tests = []
    # day counting value
    x = 0

    # calculate number of positive cases based on provided formula
    # this is rounded off to 0 decimal places, and then added to list
    while x < days:
        tests.append(format((initial * (rate ** x)), '.0f'))

        # other rounding methods (in order):
        # 1. round all case numbers up
        # 2. round case numbers 0.5 up and <0.5 down
        # 3. round all case numbers down
        # tests.append(math.ceil(initial * (rate ** x)))
        # tests.append(round(initial * (rate ** x)))
        # tests.append(math.floor(initial * (rate ** x)))
        x += 1
    return tests


def covid(answer=input('Calculate COVID-19 cases? (Y/N): ')):
    # open file
    try:
        data = open('data.txt', 'r')
    except ValueError:
        print('File not found.')
        return

    # import lines of data
    state_records = data.readlines()

    # strip \n from all lines
    clean_records = []
    for line in state_records:
        clean_records.append(line.strip())

    # create states and numbers list
    states = []
    numbers = []

    # create nested list containing lists for each state
    rows_list = []

    # loop creator
    if answer == 'Y' or answer == 'y':
        cont = True
    else:
        cont = False

    while cont:

        days = int(input('Enter days to calculate: '))
        growth = float(input('Enter growth rate: '))
        compliance_rate = int(input('Enter social distancing compliance %: '))

        # move state names into one list, and numbers into another
        for line in clean_records:
            if line.isdigit():
                numbers.append(line)
            elif line.isupper():
                states.append(line)

        # add day column
        day_column = []

        for i in range(days):
            day_column.append(i + 1)

        rows_list.append(day_column)

        # add test data
        for x in numbers:
            scaled_growth = growth_rate(growth, compliance_rate)
            positive_tests = testing(int(x), scaled_growth, days)

            rows_list.append(positive_tests)

        # add totals list to rows_list
        running_total = float(0)
        total = []

        for i in range(days):
            for x in rows_list:
                running_total += float(x[i])
            total.append(format(running_total, '.0f'))
            running_total = 0

        rows_list.append(total)

        # print labels
        print('COVID-19 POSITIVE RESULTS -', days, 'DAY PREDICTIONS')
        print('GROWTH RATE:', growth)
        print('SOCIAL DISTANCING COMPLIANCE:', compliance_rate, '%')
        print('DAY', *states, 'TOTAL')
        print('---------------------------------------')

        # print data out in table like format
        for i in range(days):
            for x in rows_list:
                print(x[i], end=' ')
            print()

        # alternate method of printing data out
        # for x, y, z, a, b, c, d, e in zip(*rows_list):
        #     print(x, y, z, a, b, c, d, e)

        answer = input('Calculate again? (Y/N): ')
        if answer == 'Y' or answer == 'y':
            cont = True
        else:
            cont = False


covid()
