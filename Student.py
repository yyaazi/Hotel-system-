class Guest:
    def __init__(self, first_name: str, last_name: str, email: str, phone: str, gender: str):
        # Initializing guest attributes
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._gender = gender

    # Getter and Setter Methods
    def get_first_name(self) -> str:
        # Return the first name of the guest
        return self._first_name

    def set_first_name(self, first_name: str):
        # Set the first name of the guest
        self._first_name = first_name

    def get_last_name(self) -> str:
        # Return the last name of the guest
        return self._last_name

    def set_last_name(self, last_name: str):
        # Set the last name of the guest
        self._last_name = last_name

    def get_email(self) -> str:
        # Return the email of the guest
        return self._email

    def set_email(self, email: str):
        # Set the email of the guest
        self._email = email

    def get_phone(self) -> str:
        # Return the phone number of the guest
        return self._phone

    def set_phone(self, phone: str):
        # Set the phone number of the guest
        self._phone = phone

    def get_gender(self) -> str:
        # Return the gender of the guest
        return self._gender

    def set_gender(self, gender: str):
        # Set the gender of the guest
        self._gender = gender


class Reservation:
    def __init__(self, reservation_id: int, guest: Guest, check_in: str, check_out: str, room_type: str, number_of_rooms: int):
        # Initializing reservation attributes
        self._reservation_id = reservation_id
        self._guest = guest
        self._check_in = check_in
        self._check_out = check_out
        self._room_type = room_type
        self._number_of_rooms = number_of_rooms

    # Getter and Setter Methods
    def get_reservation_id(self) -> int:
        # Return the reservation ID
        return self._reservation_id

    def set_reservation_id(self, reservation_id: int):
        # Set the reservation ID
        self._reservation_id = reservation_id

    def get_guest(self) -> Guest:
        # Return the guest associated with the reservation
        return self._guest

    def set_guest(self, guest: Guest):
        # Set the guest for the reservation
        self._guest = guest

    def get_check_in(self) -> str:
        # Return the check-in date
        return self._check_in

    def set_check_in(self, check_in: str):
        # Set the check-in date
        self._check_in = check_in

    def get_check_out(self) -> str:
        # Return the check-out date
        return self._check_out

    def set_check_out(self, check_out: str):
        # Set the check-out date
        self._check_out = check_out

    def get_room_type(self) -> str:
        # Return the room type
        return self._room_type

    def set_room_type(self, room_type: str):
        # Set the room type
        self._room_type = room_type

    def get_number_of_rooms(self) -> int:
        # Return the number of rooms booked
        return self._number_of_rooms

    def set_number_of_rooms(self, number_of_rooms: int):
        # Set the number of rooms booked
        self._number_of_rooms = number_of_rooms


class Payment:
    def __init__(self, payment_id: int, reservation: Reservation, amount: float, payment_date: str, status: str):
        # Initializing payment attributes
        self._payment_id = payment_id
        self._reservation = reservation
        self._amount = amount
        self._payment_date = payment_date
        self._status = status

    # Getter and Setter Methods
    def get_payment_id(self) -> int:
        # Return the payment ID
        return self._payment_id

    def set_payment_id(self, payment_id: int):
        # Set the payment ID
        self._payment_id = payment_id

    def get_reservation(self) -> Reservation:
        # Return the reservation associated with the payment
        return self._reservation

    def set_reservation(self, reservation: Reservation):
        # Set the reservation for the payment
        self._reservation = reservation

    def get_amount(self) -> float:
        # Return the amount of the payment
        return self._amount

    def set_amount(self, amount: float):
        # Set the payment amount
        self._amount = amount

    def get_payment_date(self) -> str:
        # Return the date of the payment
        return self._payment_date

    def set_payment_date(self, payment_date: str):
        # Set the date of the payment
        self._payment_date = payment_date

    def get_status(self) -> str:
        # Return the status of the payment
        return self._status

    def set_status(self, status: str):
        # Set the status of the payment
        self._status = status


class Staff:
    def __init__(self, staff_id: int, first_name: str, last_name: str, role: str, email: str):
        # Initializing staff attributes
        self._staff_id = staff_id
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._email = email

    # Getter and Setter Methods
    def get_staff_id(self) -> int:
        # Return the staff ID
        return self._staff_id

    def set_staff_id(self, staff_id: int):
        # Set the staff ID
        self._staff_id = staff_id

    def get_first_name(self) -> str:
        # Return the first name of the staff member
        return self._first_name

    def set_first_name(self, first_name: str):
        # Set the first name of the staff member
        self._first_name = first_name

    def get_last_name(self) -> str:
        # Return the last name of the staff member
        return self._last_name

    def set_last_name(self, last_name: str):
        # Set the last name of the staff member
        self._last_name = last_name

    def get_role(self) -> str:
        # Return the role of the staff member
        return self._role

    def set_role(self, role: str):
        # Set the role of the staff member
        self._role = role

    def get_email(self) -> str:
        # Return the email of the staff member
        return self._email

    def set_email(self, email: str):
        # Set the email of the staff member
        self._email = email


class Refund:
    def __init__(self, refund_id: int, payment: Payment, amount_refunded: float, refund_date: str):
        # Initializing refund attributes
        self._refund_id = refund_id
        self._payment = payment
        self._amount_refunded = amount_refunded
        self._refund_date = refund_date

    # Getter and Setter Methods
    def get_refund_id(self) -> int:
        # Return the refund ID
        return self._refund_id

    def set_refund_id(self, refund_id: int):
        # Set the refund ID
        self._refund_id = refund_id

    def get_payment(self) -> Payment:
        # Return the payment associated with the refund
        return self._payment

    def set_payment(self, payment: Payment):
        # Set the payment for the refund
        self._payment = payment

    def get_amount_refunded(self) -> float:
        # Return the amount refunded
        return self._amount_refunded

    def set_amount_refunded(self, amount_refunded: float):
        # Set the amount refunded
        self._amount_refunded = amount_refunded

    def get_refund_date(self) -> str:
        # Return the date of the refund
        return self._refund_date

    def set_refund_date(self, refund_date: str):
        # Set the date of the refund
        self._refund_date = refund_date

# Creating Objects of the Classes

# Creating a guest
guest = Guest("Ted", "Vera", "ledvera@mac.com", "505-661-1110", "Male")

# Creating a reservation
reservation = Reservation(52523687, guest, "Sun, Aug 22, 2010 - 03.00 PM", "Tue, Aug 24, 2010 - 12:00 PM", "2 Queen Beds / No Smoking", 1)

# Creating a payment
payment = Payment(15541050358, reservation, 201.48, "2024-09-30", "Completed")

# Creating staff
staff = Staff(1, "Sara", "Ali", "Receptionist", "receptionist@example.com")

# Creating a refund
refund = Refund(1, payment, 0.0, "N/A")  # No refund in this scenario

# Displaying Information
print(f"Guest: {guest.get_first_name()} {guest.get_last_name()}, Email: {guest.get_email()}, Phone: {guest.get_phone()}")
print(f"Reservation ID: {reservation.get_reservation_id()}, Check-in: {reservation.get_check_in()}, Check-out: {reservation.get_check_out()}, Room Type: {reservation.get_room_type()}")
print(f"Payment ID: {payment.get_payment_id()}, Amount: ${payment.get_amount()}, Status: {payment.get_status()}")
print(f"Staff: {staff.get_first_name()} {staff.get_last_name()}, Role: {staff.get_role()}")
print(f"Refund ID: {refund.get_refund_id()}, Amount Refunded: ${refund.get_amount_refunded()}, Refund Date: {refund.get_refund_date()}")
