class Person:
    # Attribute
    name = None
    age = None
    phone_no = None
    height = None
    weight = None
    gender = None
    prof = None

    # Methods
    def talk(self):
        print("talk")

    def sleep(self):
        print("sleep")

    def walk(self):
        return "I am walking"


amit = Person();
amit.name = "Amit"
amit.age = 59
amit.phone_no = "987654321"

print(amit)
