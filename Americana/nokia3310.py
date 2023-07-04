class Nokia3310:
    def __init__(self):
        self.battery_life = 100
        self.contacts = {}
        self.messages = []

    def power_on(self):
        print("Nokia 3310 powered on.")

    def power_off(self):
        print("Nokia 3310 powered off.")

    def charge_battery(self, amount):
        self.battery_life += amount
        if self.battery_life > 100:
            self.battery_life = 100

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added.")

    def make_call(self, name):
        if name in self.contacts:
            number = self.contacts[name]
            print(f"Calling {name} ({number})...")
        else:
            print(f"Contact '{name}' not found.")

    def send_message(self, number, message):
        self.messages.append((number, message))
        print(f"Message sent to {number}: {message}")

    def read_messages(self):
        if len(self.messages) == 0:
            print("No messages.")
        else:
            for number, message in self.messages:
                print(f"From: {number}\nMessage: {message}")

    def show_menu(self):
        print("Nokia 3310 Menu:")
        print("1. Add Contact")
        print("2. Make Call")
        print("3. Send Message")
        print("4. Read Messages")
        print("5. Power Off")

    def run(self):
        self.power_on()
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                name = input("Enter contact name: ")
                number = input("Enter contact number: ")
                self.add_contact(name, number)
            elif choice == "2":
                name = input("Enter contact name: ")
                self.make_call(name)
            elif choice == "3":
                number = input("Enter recipient number: ")
                message = input("Enter message: ")
                self.send_message(number, message)
            elif choice == "4":
                self.read_messages()
            elif choice == "5":
                self.power_off()
                break
            else:
                print("Invalid choice. Please try again.")
phone = Nokia3310()
phone.run()