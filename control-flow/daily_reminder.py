task = str(input("Enter your task: "))
time_bound = str(input("Is it time-bound? (yes/no): "))
priority = str(input("Priority (high/medium/low): "))
match priority:
    case "high":
     if time_bound == "yes":
      print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
     else:
       print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that should be completed soon.")
        else:
            print(f"Note: {task} is a medium priority task. You can complete it when convenient.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task, but it is time_bound. Please complete it soon.")
        else:
            print(f"Note: {task} is a low priority task. You can complete it at your leisure.")

