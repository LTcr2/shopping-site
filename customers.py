"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Customer: {}, {}, {}>".format(self.email, self.password)

def read_customers_from_file(filepath):
    """ get customers info from file"""

    customers = {}

    with open (filepath) as opened_file:
        for line in opened_file:
            (firstname,
             lastname,
             email,
             password) = line.strip().split("|")

            customers[email] = Customer(firstname, lastname, email, password)

    return customers


def get_by_email(email):
    """ get customer object given email"""
    
    if email in customers.keys():
        return customers[email]


    # TODO: need to implement this
customers = read_customers_from_file("customers.txt")