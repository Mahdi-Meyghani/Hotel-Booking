import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_security_card = pd.read_csv("card-security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel by changing the available column to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check the availability of the hotel"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        try:
            if availability == "yes":
                return True
            else:
                return False
        except ValueError:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def get(self):
        """Create a reservation ticket"""
        text = f"""
        Thanks for your reservation!
        Here are your reservation data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel_object.name}
        City: {self.hotel_object.city}
        """
        return text

    @property
    def the_customer_name(self):
        the_name = self.customer_name.title()
        return the_name


class CreditCard:
    def __init__(self, number, expiration, holder, cvc):
        self.number = number
        self.expiration = expiration
        self.holder = holder
        self.cvc = cvc

    def authenticate(self):
        """Check if card exists"""
        user_card = {"number": self.number, "expiration": self.expiration, "holder": self.holder, "cvc": self.cvc}
        if user_card in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def pass_validation(self, password):
        """validate password of the card"""
        correct_pass = df_security_card.loc[df_security_card["number"] == self.number, "password"].squeeze()
        if password == correct_pass:
            return True
        else:
            return False


print(df)
id_ = input("Enter hotel id: ")
hotel = Hotel(id_)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456", expiration="12/26", holder="John Smith".upper(), cvc="123")
    if credit_card.authenticate():
        if credit_card.pass_validation(password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.get())
        else:
            print("Credit card authentication failed.")
    else:
        print("There is a problem with your card payment !")
else:
    print("Hotel is not available.")
