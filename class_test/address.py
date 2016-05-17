# address.py

class Address():
    """ Hold all the fields for a mailing address. """
    def __init__(self):
        """ Set up the address fields. """
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""

def print_address(address):
    print(address.name)
    if len(address.line1) > 0:
        print(address.line1)
    if len(address.line2) > 0:
        print( address.line2)
    print(address.city + ", " + address.state + ", " + address.zip)


def main():
    """ Main function """
    # Create an address
    home_address = Address()

    # Set the fields in the address
    home_address.name = "John Smith"
    home_address.line1 = "701 N. C Street"
    home_address.line2 = "Carver Science Building"
    home_address.city = "Indianola"
    home_address.state = "IA"
    home_address.zip = "50125"

    # Create another address
    vacation_home_address = Address()

    # Set the fields in the address
    vacation_home_address.name = "John Smith"
    vacation_home_address.line1 = "1122 Main Street"
    vacation_home_address.line2 = ""
    vacation_home_address.city = "Panama City Beach"
    vacation_home_address.state = "FL"
    vacation_home_address.zip = "32407"

    print("The client's main home is in ", home_address.city)
    print("His vacation home is in ", vacation_home_address.city)

    print_address(home_address)
    print()
    print_address(vacation_home_address)

if __name__ == "__main__":
    main()
