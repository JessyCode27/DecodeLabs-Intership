# ============================================
#   DecodeLabs - Python Project 1
#   To-Do List Application
#   Developer: [Your Name]
#   Batch: 2026
# ============================================

my_tasks = []

def add_task():
    task = input("\n  Enter task: ").strip()
    if task == "":
        print("\n  ⚠️  Task cannot be empty!")
    else:
        my_tasks.append(task)
        print(f"\n  ✅ Task added: '{task}'")

def view_tasks():
    print("\n  " + "="*35)
    print("   📋  YOUR TO-DO LIST")
    print("  " + "="*35)
    if len(my_tasks) == 0:
        print("   No tasks yet. Add some tasks!")
    else:
        for i, task in enumerate(my_tasks, 1):
            print(f"   {i}. {task}")
    print("  " + "="*35)

def main():
    print("\n" + "="*40)
    print("   🚀  DECODELABS TO-DO LIST APP")
    print("   Python Project 1 | Batch 2026")
    print("="*40)

    while True:
        print("\n  ┌─────────────────────┐")
        print("  │   1. ➕  Add Task    │")
        print("  │   2. 📋  View Tasks  │")
        print("  │   3. ❌  Quit        │")
        print("  └─────────────────────┘")

        choice = input("\n  Choose (1/2/3): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("\n  👋 Goodbye! Keep coding!\n")
            break
        else:
            print("\n  ⚠️  Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()