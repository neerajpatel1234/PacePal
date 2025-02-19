import schedule
import time
import datetime
import random

def get_user_input():
    global target_pace, current_pace
    target_pace = float(input("Enter your target pace (minutes per mile): "))
    current_pace = float(input("Enter your current pace (minutes per mile): "))

def training_plan():
    days_to_marathon = (marathon_date - datetime.date.today()).days
    weeks_to_marathon = days_to_marathon // 7
    
    if weeks_to_marathon > 24:
        print("Start with base-building: easy runs, cross-training.")
    elif weeks_to_marathon > 16:
        print("Increase mileage, add tempo runs and intervals.")
    elif weeks_to_marathon > 8:
        print("Peak training: long runs, race pace workouts.")
    elif weeks_to_marathon > 4:
        print("Tapering phase: reduce mileage, maintain intensity.")
    else:
        print("Final prep: rest, carb-load, stay sharp!")

def nutrition_tip():
    tips = [
        "Stay hydrated – drink at least 2 liters of water daily.",
        "Eat a balanced diet rich in carbs, proteins, and fats.",
        "Try consuming electrolytes after long runs.",
        "Don't experiment with new foods close to race day.",
        "Refuel within 30 minutes post-run with protein and carbs."
    ]
    print(random.choice(tips))

def hydration_reminder():
    print("Hydration Reminder: Drink a glass of water!")

def motivation_boost():
    quotes = [
        "Your only limit is you!",
        "Pain is temporary, pride is forever.",
        "Run the mile you’re in.",
        "Believe in yourself and all that you are.",
        "The real race begins the moment you want to quit."
    ]
    print(random.choice(quotes))

# Get user input
get_user_input()

# Set the marathon date (YYYY, MM, DD)
marathon_date = datetime.date(2025, 4, 20)

# Schedule tasks
schedule.every().day.at("07:00").do(training_plan)
schedule.every().day.at("12:00").do(nutrition_tip)
schedule.every().hour.do(hydration_reminder)
schedule.every().day.at("18:00").do(motivation_boost)

print("Marathon Preparation Bot is running...\n")

# Keep the bot running
while True:
    schedule.run_pending()
    time.sleep(60)
