import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check the length of the password
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should have at least one number.")

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1
    else:
        feedback.append("At least one special character should be included in your password.")

    # Determine password strength
    if strength == 5:
        return "Strong Password", feedback
    elif strength >= 3:
        return "Medium Strength", feedback
    else:
        return "Weak Password", feedback

def main():
    while True:
        password = input("Enter your password: ")
        strength, feedback = assess_password_strength(password)
        print(f"\nPassword strength: {strength}")
        for item in feedback:
            print(f"- {item}")

        # give users permission if they'll like to try again or end the process
        retry = input("\nWould you like to try another password? (yes to continue, no to exit): ").strip().lower()
        if retry != 'yes':
            print("End of process. Thank you!")
            break

# Run the main function
main()
