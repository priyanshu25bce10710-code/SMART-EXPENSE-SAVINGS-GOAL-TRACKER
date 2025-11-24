def add_expense(data):
    try:
        amount = float(input("Enter amount: "))
        category = input("Category (Food/Travel/Bills/Other): ")
        note = input("Note: ")

        data["expenses"].append({
            "amount": amount,
            "category": category,
            "note": note
        })

        print("\nExpense added!\n")

    except:
        print("Invalid input!\n")


def view_expenses(data):
    expenses = data["expenses"]

    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n------ Expense List ------")
    total = 0

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ₹{e['amount']} - {e['category']} ({e['note']})")
        total += e["amount"]

    print(f"Total Spent: ₹{total}\n")


def add_saving_goal(data):
    try:
        goal = input("Goal name: ")
        target = float(input("Target amount: "))
        saved = float(input("Amount already saved: "))

        data["goals"].append({
            "goal": goal,
            "target": target,
            "saved": saved
        })

        print("\nSaving goal added!\n")

    except:
        print("Invalid input!\n")


def view_goals(data):
    goals = data["goals"]

    if not goals:
        print("\nNo saving goals added.\n")
        return

    print("\n------ Saving Goals ------")

    for g in goals:
        remaining = g["target"] - g["saved"]
        percent = (g["saved"] / g["target"]) * 100

        print(f"\nGoal: {g['goal']}")
        print(f"Target: ₹{g['target']}")
        print(f"Saved: ₹{g['saved']} ({percent:.1f}%)")
        print(f"Remaining: ₹{remaining}")

print()
