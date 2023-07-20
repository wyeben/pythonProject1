phone_book_entries = []
messages = []
call_register_entries = []
selected_tone = None
selected_settings = []

def show_menu():
    print("Welcome To AMeRIcANA Nokia 3310 Menu THaNK YoU:")
    print("1. Phone Book")
    print("2. Messages")
    print("3. Chat")
    print("4. Call Register")
    print("5. Tones")
    print("6. Settings")
    print("0. Exit")

def phone_book():
    while True:
        print("Phone Book")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("0. Go Back")
        option = input("Enter your choice (0-3): ")

        if option == '0':
            print("Going back to the main menu...")
            break
        elif option == '1':
            view_contacts()
        elif option == '2':
            add_contact()
        elif option == '3':
            remove_contact()
        else:
            print("Invalid choice. Please try again.")

def view_contacts():
    print("Phone Book - View Contacts:")
    if len(phone_book_entries) == 0:
        print("No contacts found.")
    else:
        for entry in phone_book_entries:
            print(f"Name: {entry['name']}, Number: {entry['number']}")

def add_contact():
    print("Phone Book - Add Contact:")
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    entry = {'name': name, 'number': number}
    phone_book_entries.append(entry)
    print("Contact added successfully.")

def remove_contact():
    print("Phone Book - Remove Contact:")
    if len(phone_book_entries) == 0:
        print("No contacts found.")
    else:
        name = input("Enter the name of the contact to remove: ")
        found = False
        for entry in phone_book_entries:
            if entry['name'] == name:
                phone_book_entries.remove(entry)
                found = True
                print("Contact removed successfully.")
                break
        if not found:
            print("Contact not found.")

def messages():
    while True:
        print("Messages")
        print("1. View Messages")
        print("2. Send Message")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the main menu...")
            break
        elif option == '1':
            view_messages()
        elif option == '2':
            send_message()
        else:
            print("Invalid choice. Please try again.")

def view_messages():
    while True:
        print("Can't view messages for now")
        print("work in progress...")
        option = input("Enter 0 to go back")
        if option == '0':
            break
def send_message():
    while True:
        print("Can't send message for now")
        print("work in progress...")
        option = input("Enter 0 to go back")
        if option == '0':
            break
def chat():
    while True:
        print("work in progress...")
        option = input("Enter 0 to go back")
        if option == '0':
            break

def call_register():
    while True:
        print("Call Register")
        print("1. View Call Register")
        print("2. Clear Call Register")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the main menu...")
            break
        elif option == '1':
            view_call_register()
        elif option == '2':
            clear_call_register()
        else:
            print("Invalid choice. Please try again.")

def view_call_register():
    print("Call Register - View Call Register:")
    if len(call_register_entries) == 0:
        print("No call records found.")
    else:
        for entry in call_register_entries:
            print(f"Number: {entry['number']}, Duration: {entry['duration']}s")

def clear_call_register():
    print("Call Register - Clear Call Register:")
    call_register_entries.clear()
    print("Call register cleared successfully.")

def tones():
    while True:
        print("Tones")
        print("1. Select Tone")
        print("2. Play Selected Tone")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the main menu...")
            break
        elif option == '1':
            select_tone()
        elif option == '2':
            play_selected_tone()
        else:
            print("Invalid choice. Please try again.")

def select_tone():
    global selected_tone
    print("Tones - Select Tone:")
    print("1. Tone 1")
    print("2. Tone 2")
    print("3. Tone 3")
    print("0. Go Back")
    option = input("Enter your choice (0-3): ")

    if option == '0':
        print("Going back to the Tones menu...")
    elif option == '1':
        selected_tone = "Tone 1"
        print("Tone 1 selected.")
    elif option == '2':
        selected_tone = "Tone 2"
        print("Tone 2 selected.")
    elif option == '3':
        selected_tone = "Tone 3"
        print("Tone 3 selected.")
    else:
        print("Invalid choice. Please try again.")

def play_selected_tone():
    print("Tones - Play Selected Tone:")
    if selected_tone:
        print(f"Playing {selected_tone}...")
    else:
        print("No tone selected.")

def settings():
    while True:
        print("Settings")
        print("1. Display Settings")
        print("2. Sound Settings")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the main menu...")
            break
        elif option == '1':
            display_settings()
        elif option == '2':
            sound_settings()
        else:
            print("Invalid choice. Please try again.")

def display_settings():
    while True:
        print("Settings - Display Settings")
        print("1. Change Wallpaper")
        print("2. Adjust Brightness")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the Settings menu...")
            break
        elif option == '1':
            change_wallpaper()
        elif option == '2':
            adjust_brightness()
        else:
            print("Invalid choice. Please try again.")

def change_wallpaper():
    while True:
        print("Settings - Display Settings - Change Wallpaper")
        print("1: Wyeben")
        print("2: roses")
        print("3: blue jean anna")
        option = input("Enter number (0-4): ")

        if option == '0':
            print("Going back to the settings menu...")
            break
        elif option == '1':
            Wyeben()
        elif option == '2':
            roses()
        elif option == '3':
            blue_jean_anna()
        else:
            print("Invalid choice: please try again")


def Wyeben():
    while True:
        print("wallpaper applied successfully")
        option = input("Enter 0 to go back")
        if option == '0':
            break


def roses():
    while True:
        print("wallpaper applied successfully")
        option = input("Enter 0 to go back")
        if option == '0':
            break


def blue_jean_anna():
    while True:
        print("wallpaper applied successfully")
        option = input("Enter 0 to go back")
        if option == '0':
            break


def adjust_brightness():
    while True:
        print("Settings - Display Settings - Adjust Brightness")
        print("wallpaper applied successfully")
        option = input("Enter 0 to go back")
        if option == '0':
            break

def sound_settings():
    while True:
        print("Settings - Sound Settings")
        print("1. Ringtone Volume")
        print("2. Keypad Tones")
        print("0. Go Back")
        option = input("Enter your choice (0-2): ")

        if option == '0':
            print("Going back to the Settings menu...")
            break
        elif option == '1':
            ringtone_volume()
        elif option == '2':
            keypad_tones()
        else:
            print("Invalid choice. Please try again.")

def ringtone_volume():
    while True:
        print("Settings - Sound Settings - Ringtone Volume")
        print("work in progress...")
        option = input("Enter 0 to go back")
        if option == '0':
            break
def keypad_tones():
    while True:
        print("Settings - Sound Settings - Keypad Tones")
        print("work in progress...")
        option = input("Enter 0 to go back")
        if option == '0':
            break

# Main program loop
while True:
    show_menu()
    option = input(f"Work in progress..."
                   f"Enter your choice (0-6) "
                   f"please don't forget to send me a mail "
                   f"on how you'd want me to improve (yila.benson@yahoo.com) "
                   f"THANK YOU: ")

    if option == '0':
        print("Your nokia is powered off Goodbye!")
        break
    elif option == '1':
        phone_book()
    elif option == '2':
        messages()
    elif option == '3':
        chat()
    elif option == '4':
        call_register()
    elif option == '5':
        tones()
    elif option == '6':
        settings()
    else:
        print("Invalid choice. Please try again.")
