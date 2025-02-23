class Star_Cinema:
    _hall_list = []  # Protected class attribute to store all hall objects

    def entry_hall(self, hall):
        """Insert a Hall object into the hall_list."""
        Star_Cinema._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        """Initialize Hall instance with rows, cols, and hall number."""
        self.__rows = rows  # Private: Number of rows in the hall
        self.__cols = cols  # Private: Number of columns in the hall
        self.__hall_no = hall_no  # Private: Unique identifier for the hall
        self.__seats = {}  # Private: Dictionary to store seat information
        self.__show_list = []  # Private: List to store show information

        # Add this Hall object to the hall_list of Star_Cinema
        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        """Add a show to the show_list and allocate seats."""
        # Create a tuple of show details (id, movie_name, time)
        show_details = (show_id, movie_name, time)
        # Append the show details to the show_list
        self.__show_list.append(show_details)

        # Initialize a 2D list for the seats (all seats initially free)
        seat_arrangement = [['Free' for _ in range(self.__cols)] for _ in range(self.__rows)]
        # Map the 2D seat arrangement to the show ID in the seats dictionary
        self.__seats[show_id] = seat_arrangement

    def view_show_list(self):
        """View all shows currently running in the hall."""
        if not self.__show_list:
            print("No shows are currently running.")
        else:
            print(f"Shows running in {self.__hall_no}:")
            for show in self.__show_list:
                show_id, movie_name, time = show
                print(f"ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        """View available seats for a specific show."""
        if show_id not in self.__seats:
            print(f"No show found with ID '{show_id}'.")
            return

        seat_arrangement = self.__seats[show_id]
        print(f"Available seats for show ID '{show_id}' in {self.__hall_no}:")
        for row_idx, row in enumerate(seat_arrangement):
            available_seats = [f"{row_idx + 1}-{col_idx + 1}" for col_idx, seat in enumerate(row) if seat == 'Free']
            if available_seats:
                print(f"Row {row_idx + 1}: {', '.join(available_seats)}")
            else:
                print(f"Row {row_idx + 1}: No available seats")


class Counter:
    def __init__(self, hall):
        """Initialize the Counter with a specific Hall."""
        self.__hall = hall  # Private: Reference to the Hall object

    def view_shows(self):
        """View all shows running in the assigned hall."""
        self.__hall.view_show_list()

    def view_available_seats(self, show_id):
        """View available seats for a specific show."""
        self.__hall.view_available_seats(show_id)

    def book_ticket(self, show_id, seat):
        """Book a ticket for a specific seat in a show."""
        # Check if the show_id exists
        if show_id not in self.__hall._Hall__seats:
            print(f"Error: No show found with ID '{show_id}'.")
            return

        # Parse the seat input (e.g., "1-2")
        try:
            row, col = map(int, seat.split('-'))
            row_idx = row - 1  # Convert to 0-based index
            col_idx = col - 1  # Convert to 0-based index

            # Check if the seat is within the bounds
            if not (0 <= row_idx < self.__hall._Hall__rows) or not (0 <= col_idx < self.__hall._Hall__cols):
                print("Error: Invalid seat number. Please provide a seat in 'row-col' format within hall dimensions.")
                return

            # Check if the seat is available
            if self.__hall._Hall__seats[show_id][row_idx][col_idx] == 'Free':
                # Book the seat
                self.__hall._Hall__seats[show_id][row_idx][col_idx] = 'Booked'
                print(f"Ticket booked for show ID '{show_id}', seat {seat}.")
            else:
                print(f"Error: Seat {seat} is already booked.")

        except ValueError:
            print("Error: Invalid seat format. Please use 'row-col' format (e.g., '1-2').")


# Example usage
if __name__ == "__main__":
    # Create a Hall object
    hall1 = Hall(10, 15, "Hall 1")

    # Add some shows
    hall1.entry_show("101", "Movie A", "7:00 PM")
    hall1.entry_show("102", "Movie B", "9:00 PM")

    # Create a Counter object for the hall
    counter = Counter(hall1)

    while True:
        print("\nOptions:")
        print("1: View all Shows Today")
        print("2: View all Available Tickets")
        print("3: Book Ticket")
        print("4: Exit")
        option = input("Choose an option (1-4): ")

        if option == "1":
            # View all shows
            counter.view_shows()

        elif option == "2":
            # View available tickets
            show_id = input("Enter show ID to view available seats: ")
            counter.view_available_seats(show_id)

        elif option == "3":
            # Book a ticket
            show_id = input("Enter show ID to book a ticket: ")
            seat = input("Enter seat to book (format: row-col, e.g., '1-2'): ")
            counter.book_ticket(show_id, seat)

        elif option == "4":
            # Exit the program
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid option. Please choose a valid option (1-4).")
