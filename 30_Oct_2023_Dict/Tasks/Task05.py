# Program 5:
# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

booking_data = {"bookingid": 2384,
                "booking": {
                    "firstname": "PRAMOD",
                    "lastname": "Dutta",
                    "totalprice": 432,
                    "depositpaid": False,
                    "bookingdates": {
                        "checkin": "2022-01-01",
                        "checkout": "2022-02-01"
                    },
                    "additionalneeds": "Lunch"
                }
                }

print("JSON response :", booking_data)
print("Booking ID: ", booking_data["bookingid"])
print("Checkin Date: ", booking_data["booking"]["bookingdates"]["checkin"])
print("Checkout Date: ", booking_data["booking"]["bookingdates"]["checkout"])
