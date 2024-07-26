import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, hotel_id):
        pass

    def book(self):
        pass

    def view(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def get(self):
        pass


print(df)
id_ = input("Enter hotel id: ")
hotel = Hotel(id_)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.get())
else:
    print("Hotel is not available.")
