import security_tools


# Display the available tools and route each menu choice to its task.
def main():
    print("Welcome to the Security Tools Suite!")
    
    while True:
        print("\nSelect a task:")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Generate Strong Password")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            security_event_counter()
        elif choice == '2':
            brute_force_simulation()
        elif choice == '3':
            login_authentication()
        elif choice == '4':
            print(f"Generated password: {security_tools.generate_strong_password()}")
        elif choice == '5':
            print("Thank you for using the Security Tool!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Compare ten entered passwords with a fixed example and report failures.
def security_event_counter():
    correct_password = "password123"
    incorrect_count = 0
    
    for _ in range(10):
        user_password = input("Enter a password: ")
        if user_password == correct_password:
            print("Correct password!")
        else:
            incorrect_count += 1
            print("Incorrect password.")
    
    incorrect_percentage = (incorrect_count / 10) * 100
    print(f"Incorrect password percentage: {incorrect_percentage}%")
    
    if incorrect_percentage > 50:
        print("Alert: More than 50% of passwords were incorrect!")

# shows how a maximum attempt limit stops repeated password guess
def brute_force_simulation():
    correct_password = "password123"
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        user_password = input("Enter a password guess: ")
        if user_password == correct_password:
            print("Correct password!")
            break
        attempts += 1
    
    if attempts == max_attempts:
        print("Maximum number of attempts reached.")

# Allow three login attempts before reporting that the account is frozen.
def login_authentication():
    correct_username = "user"
    correct_password = "password123"
    max_failed_attempts = 3
    failed_attempts = 0
    
    while failed_attempts < max_failed_attempts:
        user_username = input("Enter username: ")
        user_password = input("Enter password: ")
        
        if user_username == correct_username and user_password == correct_password:
            print("Login successful!")
            break
        else:
            failed_attempts += 1
            if failed_attempts < max_failed_attempts:
                print(f"Login failed. {failed_attempts} attempts left.")
            else:
                print("Account frozen for 24 hours. Please try again later.")

# Start the interactive menu only when this file is run directly.
if __name__ == "__main__":
    main()
