import heapq

class Passenger:
    def __init__(self, name, pid, age, priority=0):
        self.name = name
        self.id = pid
        self.age = age
        self.priority = priority

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Age: {self.age})"

class TrainReservationSystem:
    def __init__(self, max_seats=3):
        self.max_seats = max_seats
        self.confirmed = []  # List of Passenger
        self.waiting_list = []  # Priority queue
        self.counter = 0

    def reserve(self, passenger):
        if len(self.confirmed) < self.max_seats:
            self.confirmed.append(passenger)
            print(f"{passenger} has been confirmed.")
        else:
            heapq.heappush(self.waiting_list, (-passenger.priority, self.counter, passenger))
            self.counter += 1
            print(f"{passenger} has been added to the waiting list.")

    def cancel(self, pid):
        for i, passenger in enumerate(self.confirmed):
            if passenger.id == pid:
                removed = self.confirmed.pop(i)
                print(f"Cancelled reservation for {removed}.")
                if self.waiting_list:
                    _, _, next_passenger = heapq.heappop(self.waiting_list)
                    self.confirmed.append(next_passenger)
                    print(f"{next_passenger} has been moved from waiting list to confirmed.")
                return
        print(f"No confirmed passenger found with ID: {pid}")

    def show_status(self):
        print("\nConfirmed Passengers:")
        for p in self.confirmed:
            print(f"  - {p}")
        print("Waiting List:")
        for _, _, p in self.waiting_list:
            print(f"  - {p}")
        print()

# Main loop
system = TrainReservationSystem()

while True:
    print("\n1. Reserve Seat\n2. Cancel Reservation\n3. Show Status\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter passenger name: ")
        pid = input("Enter passenger ID: ")
        age = int(input("Enter passenger age: "))
        priority = int(input("Enter priority (higher means more urgent): "))
        passenger = Passenger(name, pid, age, priority)
        system.reserve(passenger)

    elif choice == '2':
        pid = input("Enter passenger ID to cancel: ")
        system.cancel(pid)

    elif choice == '3':
        system.show_status()

    elif choice == '4':
        print("Exiting system.")
        break

    else:
        print("Invalid choice. Try again.")
