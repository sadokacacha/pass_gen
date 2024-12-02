import random
import string
import customtkinter as ctk

# Your original password generator function
def generatePassword(pwlength):
    lowercase = string.ascii_lowercase
    special = string.punctuation
    passwords = []

    for i in pwlength:
        password = ""
        for _ in range(i):
            next_letter_index = random.randrange(len(lowercase))
            password = password + lowercase[next_letter_index] + special[next_letter_index]

        num_replacements = random.randrange(1, 9)
        for _ in range(num_replacements):
            replace_index = random.randrange(len(password) // 2)
            password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]

        passwords.append(password)

    return passwords

# GUI: Function to handle password generation via GUI
def generate_passwords_from_gui():
    try:
        num_passwords = int(num_passwords_entry.get())
        password_lengths = [int(length) for length in lengths_entry.get().split(",")]

        if len(password_lengths) != num_passwords:
            result_label.configure(text="Error: Mismatch in number of passwords and lengths provided!")
            return

        for length in password_lengths:
            if length <= 3:
                result_label.configure(text="Error: Password length must be greater than 3!")
                return

        # Call your existing password generator function
        passwords = generatePassword(password_lengths)
        result_label.configure(text="\n".join(f"Password #{i+1}: {password}" for i, password in enumerate(passwords)))

    except ValueError:
        result_label.configure(text="Error: Please enter valid numbers!")

# GUI: Initialize the CustomTkinter app
def run_gui():
    app = ctk.CTk()
    app.title("Password Generator")
    app.geometry("500x400")

    # Number of passwords
    num_passwords_label = ctk.CTkLabel(app, text="Number of Passwords:")
    num_passwords_label.pack(pady=5)
    global num_passwords_entry
    num_passwords_entry = ctk.CTkEntry(app, width=300)
    num_passwords_entry.pack(pady=5)

    # Password lengths
    lengths_label = ctk.CTkLabel(app, text="Password Lengths (comma-separated):")
    lengths_label.pack(pady=5)
    global lengths_entry
    lengths_entry = ctk.CTkEntry(app, width=300)
    lengths_entry.pack(pady=5)

    # Generate button
    generate_button = ctk.CTkButton(app, text="Generate Passwords", command=generate_passwords_from_gui)
    generate_button.pack(pady=10)

    # Result display
    global result_label
    result_label = ctk.CTkLabel(app, text="", justify="left", wraplength=400)
    result_label.pack(pady=20)

    # Run the app
    app.mainloop()

# CLI: Original main function
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")

    passwordLengths = []

    for i in range(numPasswords):
        while True:
            length = int(input("Enter the length of Password, length must be more than 3 #" + str(i + 1) + " "))
            if length > 3:
                break
            print("Please enter a number greater than 3")

        passwordLengths.append(length)
        Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i + 1) + " = " + Password[i])

# Entry point for the program
if __name__ == "__main__":
    mode = input("Choose mode: 'cli' for command-line or 'gui' for graphical interface: ").strip().lower()
    if mode == "cli":
        main()
    elif mode == "gui":
        run_gui()
    else:
        print("Invalid mode! Please restart and choose 'cli' or 'gui'.")
