print(".....THE SMART MED INTELLIGENCE SYSTEM.....")

def med_manager():
    my_meds = {}

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add New Medicine/Vaccine")
        print("2. View All Reminders")
        print("3. Check Inventory Status")
        print("4. Exit & Save")
        
        choice = input("\nWhat would you like to do? (1-4): ")

        if choice == '1':
            # User inputs the medicine details
            name = input("Enter Medicine Name: ").title()
            qty = int(input(f"How many doses of {name} do you have? "))
            time = input(f"What time should you take {name}? (e.g., 08:00 AM): ")
            
            my_meds[name] = [qty, time]
            print(f"\nSUCCESS: {name} added to your schedule!")

        elif choice == '2':
            print("\n--- YOUR DAILY REMINDERS ---")
            if not my_meds:
                print("No medicines added yet.")
            else:
                for name, info in my_meds.items():
                    print(f"🔔 {info[1]} -> Take {name}")

        elif choice == '3':
            print("\n--- INVENTORY & DOSE TRACKER ---")
            if not my_meds:
                print("No data available.")
            else:
                print(f"{'Medicine':<15} | {'Doses':<10} | {'Status'}")
                print("-" * 40)
                for name, info in my_meds.items():
                    status = "Safe"
                    if info[0] <= 3:
                        status = "REORDER SOON!"
                    print(f"{name:<15} | {info[0]:<10} | {status}")

        elif choice == '4':
            print("\n Stay healthy, stay safe!")
            break

        else:
            print("\nInvalid input! Please choose 1, 2, 3, or 4.")
            
med_manager()
