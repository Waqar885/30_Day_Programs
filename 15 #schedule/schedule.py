import time
from win10toast import ToastNotifier

class Schedule:
    def __init__(self, time, work):
        self.time = time
        self.work = work

    def store_data(self):
        with open("30_Programs/ Programs 15/Time.txt", 'a') as timing:
            timing.write(f"{self.time}\n")
        
        with open("30_Programs/ Programs 15/schedule.txt", "a") as works:
            works.write(f"{self.work}\n")
    @staticmethod
    def notify():
        toast = ToastNotifier()
        while True:
            local_time = time.strftime("%H:%M")
            with open("30_Programs/ Programs 15/schedule.txt", 'r') as read_work, open("30_Programs/ Programs 15/Time.txt", 'r') as read_time:
                tasks = read_work.readlines()
                times = read_time.readlines()
            
            for schedule_time, task in zip(times, tasks):
                scheduled_time = schedule_time.strip()
                task = task.strip()
                    
                if scheduled_time == local_time:
                    toast.show_toast("Schedule Alert", task, duration=10)
                else:
                    None
            time.sleep(30) # Check every minute
choice = input("Enter \n1 for Notify existing schedule\n2 for clear previous or/and make new schedule: ")
if choice=="1":
    Schedule.notify()

elif choice=="2":
    with open("30_Programs/ Programs 15/Time.txt", 'w') as time_clear, open("30_Programs/ Programs 15/schedule.txt", 'w') as schedule_clear:
        time_clear.write("Updated Times\n")
        schedule_clear.write("Updated Schedule\n")
    while True:
        print("Timing automatically starts with 0. The format of time is 0-23.")
        print("Please only enter schedule timing.")
        timing = input("Enter schedule start timing (HH:MM): ")
        work = input("Enter  'exit' to exit \nEnter your task: ").strip().lower()
        if 0 > int(timing[:2]) > 24:
            print("Error. please again enter between 0-23")
        else:
            if "exit" not in work:    
                task = Schedule(timing, work.capitalize())
                task.store_data()
                print("Task added add next")
            else:
                break