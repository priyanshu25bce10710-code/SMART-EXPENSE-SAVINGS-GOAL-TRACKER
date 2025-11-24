from tracker import add_expense, view_expenses, add_saving_goal, view_goals
from storage import load_data, save_data

data = load_data()

def menu():
    while True:
        print("\n====== EXPENSE & GOAL TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Saving Goal")
        print("4. View Saving Goals")
        print("5. Save & Exit")
        print("6. Search expense by category")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            add_saving_goal(data)
        elif choice == "4":
            view_goals(data)
        elif choice == "6":
         category = input("Enter category to search: ") 
        
         print(f"\nExpenses under category '{category}':\n")
         found = False
         for item in data["expenses"]:
           if item["category"].lower() == category.lower():
            print(f"{item['amount']} - {item['category']}")
            found = True
         if not found:
           print("No expenses found in this category.")

        elif choice == "5":
            save_data(data)
            print("\nSaved successfully! Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()