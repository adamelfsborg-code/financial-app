from financials import Activities, Food, Bills, Saveings
from currency import Currency
from salary import Salary


print('----take care of your financials----')
currency = str(input('Enter in what currency you want(ex."$"): '))
c = Currency(currency)
salary_in_bank = int(input(f'How manny {c} do you have in your bank right now?: '))
income = int(input('How much do you make per month?: '))
print(f'Your salary is {salary_in_bank}{c}')

run = True

while run:
    try:
        thingsToDo = int(input('1: add Activity \n2: add Food \n3: add Bills\n4: add savings \n5: convert your salary \n6: show all \n7: quit \nWhat do you want?: '))

        if thingsToDo == 1:
            try:
                A = True
                while A:
                    choice = int(input('1: add one activity\n2: go back\n What do you want to do?: '))
                    if choice == 1:
                        activity = str(input('Add one activity: '))
                        amount = int(input('How much did it cost?: '))
                        a = Activities(activity, amount)
                        print(f'{str(a)}: {int(a)} added')
                    else:
                        A = False
            except:
                print('something went wrong!!! try again later')
                run = False
            
            salary_after_activity = a.salaryAfterActivity(salary_in_bank)
            print(f'Your salary after this Activity is {salary_after_activity}')
            
        elif thingsToDo == 2:
            try:
                activity = str(input('Add food: '))
                amount = int(input('How much did it cost?: '))
                f = Food(activity, amount)
                print(f'{str(f)}: {int(f)}{c} added')
                salary_after_food = f.salaryAfterActivity(salary_in_bank)
                print(f'Your salary after this Activity is {salary_after_food}')
                F = True
                while F:
                    choice = int(input('1: add your food list\n2: go back\nWhat do you want to do?: '))
                    if choice == 1:
                        food = input(f'Add your food list and cost of item (ex. "tomato=3{c}, apple=2{c}"): ')
                        # food_list = food.split()
                        # print(food_list)
                        h = 'tomato'
                        f.food_list_items(h)
                        f.cart_item()
                        f.cart_price()
                    else:
                        F = False
                    

            except Exception as e:
                print(f'something whent wrong! {e}')
                run = False
        elif thingsToDo == 3:
            try:
                activity = str(input('Add bill: '))
                amount = int(input('How much did it cost?: '))
                b = Bills(activity, amount)
                print(f'{str(b)}: {int(b)}{c} added')
                salary_after_bill = b.salaryAfterBills(salary_in_bank)
                print(f'Your salary after the bill is {salary_after_bill}')
                B = True
                while True:
                    choice = int(input('1: add your bill list\n2: go back\nWhat do you want to do?'))
                    if choice == 1:
                        bill = input(f'Add your bill list and cost of every bill (ex. "Electricity=300{c}, Water=200{c}" ')
                        print(b.bill_list(bill))
                        b.bill_price()
                        print(b.bill_name())
                        print('hej')
                    else:
                        B = False
                    
            except Exception as e:
                run = False

        elif thingsToDo == 4:
            try:
                activity = str(input('Add Saveing: '))
                amount = int(input('How much will it cost?: '))
                s = Saveings(activity, amount)
                time_left = s.saveing_time(income)
                monney_left = s.saveing_amount(salary_in_bank)
                print(f'{time_left} months for your {activity} to come true')
                print(f' you will need: {monney_left}')
            except Exception as e:
                print(e)
                run = False
        elif thingsToDo == 5:
            try:
                working_months_per_y = int(input('How many months do you work per year?'))
                working_days_per_m = int(input('How many days do you work per month?: '))
                working_hours_per_d = int(input('How many hours do you work per dday?: '))
                sal = Salary(working_days_per_m,working_hours_per_d,working_months_per_y )
                year = sal.yearly_salary(income)
                month = sal.mounthly_salary(income)
                day = sal.daily_salary(income)
                hour = sal.hourly_salary(income)
                choice = int(input('Do you want to see what you make per year, month, day, hour or all?: '))
                if choice.lower() == 'year':
                    print(f'You make {year}{c} per year')
                elif choice.lower() == 'month':
                    print(f'You make {month}{c} per month')
                elif choice.lower() == 'day':
                    print(f'You make {day}{c} per day')
                elif choice.lower() == 'hour':
                    print(f'You make {hour}{c} per hour')
                elif choice.lower() == 'all':
                    print(f'You make {year}{c} per year')
                    print(f'You make {month}{c} per month')
                    print(f'You make {day}{c} per day')
                    print(f'You make {hour}{c} per hour')
                else:
                    print('something went wrong so were just gonna show you everything')
                    print(f'You make {year}{c} per year')
                    print(f'You make {month}{c} per month')
                    print(f'You make {day}{c} per day')
                    print(f'You make {hour}{c} per hour')
            except Exception as e:
                print(e)
                run = False

        elif thingsToDo == 6:
            try:
                A = True
                while A:
                    print(f'Your currency: {c}')
                    print(f'Your bank: {salary_in_bank}{c}')
                    print(f'You spent {int(a)}{c} on Activities last month')
                    print(f'You spent {int(f)}{c} on Food last month')
                    print(f'Your bills cost {int(b)}{c} last month')
                    print(f'You saved {int(s)}{c} for activities last month')
                    print('-----------------------------------------------')
                    if working_months_per_y != None and working_days_per_m != None and working_hours_per_d != None: 
                        print(f'You make {year}{c} per year')
                        print(f'You make {month}{c} per month')
                        print(f'You make {day}{c} per day')
                        print(f'You make {hour}{c} per hour')
                    exit = input('type exit if you want to exit: ')
                    if exit == 'exit':
                        A = False
            except Exception as e:
                print(e)
                run = False
        elif thingsToDo == 7:
            run = False
    except:
        print('something is wrong')
        run = False

