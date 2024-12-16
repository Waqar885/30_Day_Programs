import time
import csv

def set_subject(period_no, days):
    with open('30_Programs/ Programs 21/school shedule.csv', mode='a', newline='') as data:
        file_address = csv.writer(data)
        if len(days) == 5:
            file_address.writerow(['Period', 'Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday'])
            
            for i in range(1, period_no +1):
                period_monday = input(f'Enter period {i} subject name on {days[0]}: ')
                period_tuesday = input(f'Enter period {i} subject name on {days[1]}: ')
                period_wednessday = input(f'Enter period {i} subject name on {days[2]}: ')
                period_thursday = input(f'Enter period {i} subject name on {days[3]}: ')
                period_friday = input(f'Enter period {i} subject name on {days[4]}: ')
                file_address.writerow([i, period_monday, period_tuesday, period_wednessday, period_thursday, period_friday])
                print(f'All {i} period done...Enter next')
        elif len(days) == 6:
            file_address.writerow(['Period', 'Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday', 'Saturday'])
            
            for i in range(1, period_no +1):
                period_monday = input(f'Enter period {i} subject name on {days[0]}: ')
                period_tuesday = input(f'Enter period {i} subject name on {days[1]}: ')
                period_wednessday = input(f'Enter period {i} subject name on {days[2]}: ')
                period_thursday = input(f'Enter period {i} subject name on {days[3]}: ')
                period_friday = input(f'Enter period {i} subject name on {days[4]}: ')
                period_saturday = input(f'Enter period {i} subject name on {days[5]}: ')
                file_address.writerow([i, period_monday, period_tuesday, period_wednessday, period_thursday, period_friday, period_saturday])
                print(f'All {i} period done...Enter next')
        
        else:
            print('Error....Please only entr 5 or 6 days')

days = input("Enter the number of days your school is open.\n Note: Sunday will be a holiday. And enter between 5-6: ")
period_no = int(input("Enter how much period your class have? :"))

five_days = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday']
six_days = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday', 'Saturday']

if days == '5':
    set_subject(period_no, five_days)

elif days == '6':
    set_subject(period_no, six_days)

else:
    print('Error....Please only entr 5 or 6 days')