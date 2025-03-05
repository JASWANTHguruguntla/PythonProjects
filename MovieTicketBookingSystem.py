movies = {
    1: {"name": "RRR", "normal_price": 300, "vip_price": 500},
    2: {"name": "KGF: Chapter 2", "normal_price": 250, "vip_price": 450},
    3: {"name": "Pushpa: The Rise", "normal_price": 200, "vip_price": 400}
}

seating = [
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0]   
]

def display_movies():
    print("\nAvailable Movies:")
    for key, value in movies.items():
        print(f"{key}. {value['name']} - Normal: ₹{value['normal_price']}, VIP: ₹{value['vip_price']}")

def display_seats():
    print("\nScreen This Side 🎬")
    for i, row in enumerate(seating, start=1):
        seat_status = " ".join(["❌" if seat == 1 else "✅" for seat in row])
        print(f"Row {i}: {seat_status}")

def book_seat(movie):
    display_seats()
    try:
        row = int(input("Enter row number: ")) - 1
        seat = int(input("Enter seat number: ")) - 1

        if row < 0 or row >= len(seating) or seat < 0 or seat >= len(seating[0]):
            print("Invalid seat selection. Please try again.")
            return

        if seating[row][seat] == 1:
            print("Seat already booked. Please select another seat.")
            return

        seat_type = int(input("Choose Seat Type (1: Normal, 2: VIP): "))
        if seat_type not in [1, 2]:
            print("Invalid seat type. Please try again.")
            return

        price = movies[movie]["normal_price"] if seat_type == 1 else movies[movie]["vip_price"]
        confirm = input(f"Confirm booking for ₹{price}? (yes/no): ").lower()

        if confirm == "yes":
            seating[row][seat] = 1
            print("✅ Booking Successful!")
            generate_ticket(movie, row + 1, seat + 1, price)
        else:
            print("Booking cancelled.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def generate_ticket(movie, row, seat, price):
    print("\n🎟️ MOVIE TICKET 🎟️")
    print("===================")
    print(f"Movie : {movies[movie]['name']}")
    print(f"Seat  : Row {row}, Seat {seat}")
    print(f"Price : ₹{price}")
    print("===================")

def cancel_booking():
    display_seats()
    try:
        row = int(input("Enter row number to cancel: ")) - 1
        seat = int(input("Enter seat number to cancel: ")) - 1

        if row < 0 or row >= len(seating) or seat < 0 or seat >= len(seating[0]):
            print("Invalid seat selection. Please try again.")
            return

        if seating[row][seat] == 0:
            print("Seat is already available.")
            return

        seating[row][seat] = 0
        print("✅ Booking Cancelled.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def main():
    while True:
        print("\nMovie Ticket Booking System")
        print("1. View Movies")
        print("2. Book a Seat")
        print("3. Cancel Booking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies()
        elif choice == "2":
            display_movies()
            try:
                movie_choice = int(input("Enter the number of the movie you want to watch: "))
                if movie_choice in movies:
                    book_seat(movie_choice)
                else:
                    print("Invalid movie selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            print("Thank you for using the Movie Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()