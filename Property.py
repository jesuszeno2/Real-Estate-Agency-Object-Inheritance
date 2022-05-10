"""
Jesus Zeno SIE 508 Assignment 3
We will make a parent property class that will have certain attributes. The initialize property method
will prompt the user for relevant info and be called in the constructor at object initiation time.
House and apartment will be children classes of property
"""


# Parent class to House and Apartment
class Property:
    def __init__(self):
        # Set initial object instance variables upon instantiation
        self._square_feet = None
        self._num_bedrooms = None
        self._num_bathrooms = None
        self._rent = None
        self._address = None
        self._property_name = None
        # Use protected method to initialize values for several variables. We are doing this in this
        # particular way to make it such that the variables in the method are available to every method
        # in the object.
        self._property_name, self._square_feet, self._num_bedrooms, self._num_bathrooms, self._rent, \
        self._address = self._InitializeProperty()

    # Used to run dialogue to initialize the object
    def _InitializeProperty(self):
        self._property_name = str(input("What do you want to name the property?"))
        self._square_feet = int(input("How many square feet is the {}?".format(self._property_name)))
        self._num_bedrooms = int(input("How many bedrooms are there?"))
        self._num_bathrooms = float(input("How many bathrooms does the property have?"))
        self._rent = int(input("How much does it cost to rent?"))
        self._address = str(input("What is the address?"))
        return self._property_name, self._square_feet, self._num_bedrooms, self._num_bathrooms, \
               self._rent, self._address

    # Display all the object instance variables
    def display(self):
        print("Info for property:")
        print("Square feet: {}sqft".format(self._square_feet))
        print("Number of bedrooms: {}".format(self._num_bedrooms))
        print("Number of bathrooms: {}".format(self._num_bathrooms))
        print("Cost of rent: ${}".format(self._rent))
        print("Address: {}".format(self._address))

    # More specific method to display object instance variables for a specific Real Estate Agent.
    def displayPropertyForAgent(self):
        print("Rent amount: {}".format(self._rent))
        print("Address:\n{}".format(self._address))


# Here we are making the House class which is a child of the property class.
class House(Property):
    def __init__(self):
        # Call the constructor for the parent class Property. Can also be done by writing:
        # Property().__init__()
        super().__init__()
        self._num_stories = None
        self._garage = None
        self._fenced_yard = None
        # Same concept as the parent class. We are just adding some more specific object instance
        # variables.
        self._num_stories, self._garage, self._fenced_yard = self._InitializeHouseProperty()

    # Method to initialize the class.
    def _InitializeHouseProperty(self):
        self._num_stories = int(input("How many stories is the house?"))
        self._garage = str(input("Does it have a garage?"))
        self._fenced_yard = str(input("Does it have a fenced yard?"))
        return self._num_stories, self._garage, self._fenced_yard

    # Display all house attributes.
    def displayHouse(self):
        print(self._property_name)
        super().display()
        print("Number of stories in the house: {}".format(self._num_stories))
        print("Garage status: {}".format(self._garage))
        print("Fence status: {}".format(self._fenced_yard))

    # More specific method to display house object instance variables for a specific Real Estate Agent.
    def displayHouseForAgent(self):
        print(self._property_name)
        print("Property type: House")
        super().displayPropertyForAgent()


# Here we are making an Apartment class which is a child of the property class.
class Apartment(Property):
    def __init__(self):
        # Call the constructor for the parent class Property. Can also be done by writing:
        # Property().__init__()
        super().__init__()
        self._balcony = None
        self._laundry = None
        # Same concept as the parent class. We are just adding some more specific object instance
        # variables.
        self._balcony, self._laundry = self._InitializeApartmentProperty()

    # Method to initialize the class.
    def _InitializeApartmentProperty(self):
        self._balcony = str(input("Does it have a balcony?"))
        self._laundry = str(input("Does it have a laundry rooom?"))
        return self._balcony, self._laundry

    # Display all apartment attributes.
    def displayApartment(self):
        print(self._property_name)
        super().display()
        print("Balcony status: {}".format(self._balcony))
        print("Laundry room status: {}".format(self._laundry))

    # More specific method to display apartment object instance variables for a specific Real Estate Agent.
    def displayApartmentForAgent(self):
        print(self._property_name)
        print("Property type: Apartment")
        super().displayPropertyForAgent()
