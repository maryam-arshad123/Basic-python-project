import re
import getpass

def check_password_strength(password):
    strength = 0

    remarks = "Very Weak"
    details = []

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[@$!%*?&#]", password))

    # Collect feedback based on criteria
    if length_criteria:
        strength += 1
        details.append("Meets length requirement (8+ characters)")
    else:
        details.append("Does not meet length requirement (8+ characters)")

    if uppercase_criteria:
        strength += 1
        details.append("Contains uppercase letters")
    else:
        details.append("Does not contain uppercase letters")

    if lowercase_criteria:
        strength += 1
        details.append("Contains lowercase letters")
    else:
        details.append("Does not contain lowercase letters")

    if number_criteria:
        strength += 1
        details.append("Contains numbers")
    else:
        details.append("Does not contain numbers")

    if special_char_criteria:
        strength += 1
        details.append("Contains special characters (@$!%*?&#)")
    else:
        details.append("Does not contain special characters (@$!%*?&#)")

    # Assign remarks based on strength
    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    return strength, remarks, details


# Test the function
if __name__ == "__main__":
    # This will hide the input behind dots in the terminal
    password = getpass.getpass("Enter your password: ")
    
    strength, remarks, details = check_password_strength(password)

    # Display the results
    print(f"Password Strength: {strength}/5 ({remarks})")
    print("\nPassword Analysis:")
    for detail in details:
        print(f"- {detail}")
