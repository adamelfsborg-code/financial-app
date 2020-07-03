from financials import Activities, Food, Bills, Saveings
from currency import Currency
from salary import Salary


print('----take care of your financials----')
currency = str(input('Enter in what currency you want(ex."$"): '))
c = Currency(currency)
salary_in_bank = int(input('Enter your salary?: '))
print(f'Your salary is {salary_in_bank}{c}')

run = True

while run:
    try:
        thinsToDo = int(input('1: add Activity \n2: add Food \n3: add Bills\n4: add savings \n5: convert your salary \n6: show all \n7: quit \nWhat do you want?: '))

        if thinsToDo == 1:
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
            
        elif thinsToDo == 2:
            try:
                activity = str(input('Add one activity: '))
                amount = int(input('How much did it cost?: '))
                f = Food(activity, amount)
                print(f'{str(f)}: {int(f)} added')
                F = True
                while F:
                    choice = int(input('1: add your food list\n2: go back\n What do you want to do?: '))
                    if choice == 1:
                        food = input('Add your food list and cost of item (ex. "tomato=3"): ')
                        # food_list = food.split()
                        # print(food_list)
                        f.food_list_items(food)

                    else:
                        F = False
                    
                    salary_after_food = f.salaryAfterActivity(salary_in_bank)
                    print(f'Your salary after this Activity is {salary_after_food}')
                    
            except Exception as e:
                print(f'something whent wrong! {e}')
                run = False

        elif thinsToDo == 7:
            run = False
    except:
        print('something is wrong')
        run = False

