import time

MAX_CONFIRMED = 3
MAX_WAITLIST = 10

confirmed = []
waitlist = []

def get_priority(age, quota_type):
    priorities = {
        "V": 1,  # VIP
        "G": 2,  # General
        "S": 3,  # Senior Citizen
        "M": 4,  # Military
        "L": 5,  # Ladies
        "D": 6,  # Disabled
        "T": 7   # Tatkal
    }
    return priorities.get(quota_type.upper(), 8)

def book_ticket():
    try:
        id = int(input("Enter Passenger ID: "))
        if any(p['id'] == id for p in confirmed + waitlist):
            print("Passenger ID already exists!")
            return

        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        age = int(input("Enter Age: "))
        quota_type = input("Enter Quota Type (V/G/S/M/L/D/T): ").upper()
        if quota_type not in "VGSMTLD":
            print("Invalid quota type.")
            return

        timestamp = time.time()
        priority = get_priority(age, quota_type)

        passenger = {
            "id": id,
            "name": name,
            "age": age,
            "type": quota_type,
            "priority": priority,
            "timestamp": timestamp
        }

        if len(confirmed) < MAX_CONFIRMED:
            passenger["seatNumber"] = len(confirmed) + 1
            passenger["coach"] = "Sleeper Coach 1"
            confirmed.append(passenger)
            print(f"Ticket confirmed for {name}. Seat: {passenger['seatNumber']}, {passenger['coach']}")
        elif len(waitlist) < MAX_WAITLIST:
            waitlist.append(passenger)
            waitlist.sort(key=lambda p: (p['priority'], p['timestamp']))
            position = waitlist.index(passenger) + 1
            print(f"{name} added to Waiting List {position}")
        else:
            print("Waiting list full!")

    except ValueError:
        print("Invalid input. Please enter correct data.")

def cancel_ticket():
    try:
        id = int(input("Enter Passenger ID to cancel: "))
        index = next((i for i, p in enumerate(confirmed) if p['id'] == id), -1)

        if index != -1:
            removed = confirmed.pop(index)
            for i, p in enumerate(confirmed):
                p['seatNumber'] = i + 1

            if waitlist:
                promoted = waitlist.pop(0)
                promoted['seatNumber'] = len(confirmed) + 1
                promoted['coach'] = "Sleeper Coach 1"
                confirmed.append(promoted)
                print(f"Cancelled ticket of {removed['name']}. {promoted['name']} promoted to confirmed list.")
            else:
                print(f"Cancelled ticket of {removed['name']}.")
        else:
            print("Passenger ID not found in confirmed list.")
    except ValueError:
        print("Invalid ID entered.")

def display_lists():
    print("\n--- Confirmed Passengers ---")
    if not confirmed:
        print("No confirmed bookings.")
    else:
        for p in confirmed:
            print(f"{p['name']} (ID: {p['id']}) - Seat {p['seatNumber']}, {p['coach']}")

    print("\n--- Waiting List ---")
    if not waitlist:
        print("No passengers in waiting list.")
    else:
        for i, p in enumerate(waitlist, 1):
            print(f"Waiting List {i}: {p['name']} (ID: {p['id']})")

def main_menu():
    while True:
        print("\n==== Train Reservation System ====")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Show Passenger Lists")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            cancel_ticket()
        elif choice == "3":
            display_lists()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main_menu()
