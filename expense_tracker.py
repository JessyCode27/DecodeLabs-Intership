# ============================================
#   DecodeLabs - Python Project 2
#   Expense Tracker Application
#   Developer: [Your Name]
#   Batch: 2026
# ============================================

expenses = []
total = 0  # Accumulator - initialized OUTSIDE the loop

def add_expense():
    global total
    try:
        amount = float(input("\n  Enter expense amount (e.g. 100): ₹"))
        if amount <= 0:
            print("\n  ⚠️  Amount must be greater than 0!")
            return
        description = input("  Enter description (e.g. Food): ")
        expenses.append({"amount": amount, "description": description})
        total += amount  # Accumulator pattern
        print(f"\n  ✅ Expense added: ₹{amount:.2f} for '{description}'")
        print(f"  💰 Running Total: ₹{total:.2f}")
    except ValueError:
        print("\n  ⚠️  Invalid input! Please enter a number only.")

def view_expenses():
    print("\n  " + "="*40)
    print("   📊  YOUR EXPENSE REPORT")
    print("  " + "="*40)
    if len(expenses) == 0:
        print("   No expenses recorded yet!")
    else:
        for i, exp in enumerate(expenses, 1):
            print(f"   {i}. ₹{exp['amount']:.2f}  →  {exp['description']}")
        print("  " + "-"*40)
        print(f"   💸 TOTAL SPENT: ₹{total:.2f}")
    print("  " + "="*40)

def main():
    print("\n" + "="*45)
    print("   💰  DECODELABS EXPENSE TRACKER APP")
    print("   Python Project 2 | Batch 2026")
    print("="*45)

    while True:
        print("\n  ┌──────────────────────────┐")
        print("  │   1. ➕  Add Expense      │")
        print("  │   2. 📊  View All Expenses│")
        print("  │   3. ❌  Quit             │")
        print("  └──────────────────────────┘")

        choice = input("\n  Choose (1/2/3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("\n  " + "="*40)
            print(f"   💸 FINAL TOTAL SPENT: ₹{total:.2f}")
            print("  " + "="*40)
            print("\n  👋 Goodbye! Keep tracking!\n")
            break
        else:
            print("\n  ⚠️  Invalid choice! Enter 1, 2, or 3 only.")

if __name__ == "__main__":
    main()
