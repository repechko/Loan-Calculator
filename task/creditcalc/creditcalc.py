import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--payment')
parser.add_argument('--interest')
parser.add_argument('--periods')

args = parser.parse_args()
type = args.type
principal = args.principal
payment = args.payment
interest = args.interest
periods = args.periods

if type == 'diff':
    if principal and periods and interest:
        principal = float(principal)
        periods = int(periods)
        interest = float(interest)
        i = 1
        total_sum = 0
        while i <= periods:
            nominal_interest_rate = interest / (12 * 100)
            differentiated_payment = math.ceil(principal / periods + nominal_interest_rate *
                                               (principal - ((principal * (i - 1)) / periods)))
            print(f'Month {i}: payment is {differentiated_payment}')
            i += 1
            total_sum += differentiated_payment
        overpayment = total_sum - principal
        print(f'\nOverpayment = {int(overpayment)}')
    else:
        print('Incorrect parameters')
elif type == 'annuity':
    if principal and payment and interest:
        principal = float(principal)
        payment = float(payment)
        interest = float(interest)
        nominal_interest_rate = interest / (12 * 100)
        periods = math.ceil(math.log((payment / (payment - nominal_interest_rate * principal)), 1 + nominal_interest_rate))
        years = periods // 12
        months = periods % 12
        if not years and months:
            if months == 1:
                print(f'It will take 1 month to repay this loan!')
            else:
                print(f'It will take {months} months to repay this loan!')
        elif years and not months:
            if years == 1:
                print(f'It will take 1 year to repay this loan!')
            else:
                print(f'It will take {years} years to repay this loan!')
        else:
            if years == 1 and months != 1:
                print(f'It will take 1 year and {months} months to repay this loan!')
            elif years != 1 and months == 1:
                print(f'It will take {years} years and 1 month to repay this loan!')
            elif years == 1 and months == 1:
                print(f'It will take 1 year and 1 month to repay this loan!')
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')
        overpayment = payment * periods - principal
        print(f'Overpayment = {int(overpayment)}')
    elif principal and periods and interest:
        principal = float(principal)
        periods = int(periods)
        interest = float(interest)
        nominal_interest_rate = interest / (12 * 100)
        annuity_payment = math.ceil(principal *
                                    (nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods) /
                                     (math.pow((1 + nominal_interest_rate), periods) - 1)))
        overpayment = annuity_payment * periods - principal
        print(f'''Your annuity payment = {annuity_payment}!
Overpayment = {int(overpayment)}''')
    elif payment and periods and interest:
        payment = float(payment)
        periods = int(periods)
        interest = float(interest)
        nominal_interest_rate = interest / (12 * 100)
        principal = math.floor(payment /
                               ((nominal_interest_rate * math.pow((1 + nominal_interest_rate), periods)) /
                                (math.pow((1 + nominal_interest_rate), periods) - 1)))
        overpayment = periods * payment - principal
        print(f'''Your loan principal = {principal}!
Overpayment = {int(overpayment)}''')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
