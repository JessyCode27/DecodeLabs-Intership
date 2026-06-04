# ============================================
#   DecodeLabs - Python Project 3
#   Random Password Generator
#   Developer: Jessy
#   Batch: 2026
# ============================================

import string
import secrets

def generate_password(length, use_symbols):
    # Character pools
    letters = string.ascii_letters   # a-z and A-Z
    digits  = string.digits          # 0-9
    symbols = string.punctuation     # @#$%^&*

    # Build character set based on user choice
    if use_symbols:
        all_chars = letters + digits + symbols
    else:
        all_chars = letters + digits

    # Generate password using secrets (cryptographically secure)
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password

def check_strength(length):
    if length < 8:
        return "❌ Weak"
    elif length < 12:
        return "⚠️  Medium"
    elif length < 16:
        return "✅ Strong"
    else:
        return "🔒 Very Strong"

def main():
    print("\n" + "="*45)
    print("   🔐  DECODELABS PASSWORD GENERATOR")
    print("   Python Project 3 | Batch 2026")
    print("="*45)

    while True:
        print("\n  ┌──────────────────────────────┐")
        print("  │   1. 🔑  Generate Password    │")
        print("  │   2. ❌  Quit                 │")
        print("  └──────────────────────────────┘")

        choice = input("\n  Choose (1/2): ").strip()

        if choice == "1":
            try:
                length = int(input("\n  Enter password length (e.g. 12): "))

                if length < 4:
                    print("\n  ⚠️  Minimum length is 4!")
                    continue
                if length > 64:
                    print("\n  ⚠️  Maximum length is 64!")
                    continue

                sym = input("  Include symbols? (@#$%) (yes/no): ").strip().lower()
                use_symbols = sym == "yes"

                # Generate password
                password = generate_password(length, use_symbols)
                strength = check_strength(length)

                print("\n  " + "="*40)
                print("  🔑  YOUR GENERATED PASSWORD:")
                print(f"\n      {password}\n")
                print(f"  📏  Length   : {length} characters")
                print(f"  💪  Strength : {strength}")
                print("  " + "="*40)

            except ValueError:
                print("\n  ⚠️  Please enter a valid number!")

        elif choice == "2":
            print("\n  👋 Goodbye! Stay Secure!\n")
            break
        else:
            print("\n  ⚠️  Invalid choice! Enter 1 or 2 only.")

if __name__ == "__main__":
    main()
