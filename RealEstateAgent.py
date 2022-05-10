"""
Jesus Zeno
This class holds a list of real estate agents and can print that list. We can also use the methods to
assign certain properties to a specific agent. These properties can then be viewed in relation to the agent.
"""

from Property import Property, House, Apartment

class RealEstateAgent:

    # Make global variable and initiate empty list to use later
    global list_agents
    list_agents = []

    def __init__(self, name):
        # Set initial object instance variables upon instantiation
        self._properties_list = None
        self._properties_names_list = None
        self._name = name
        properties_list = []
        properties_names_list = []
        self._properties_list = properties_list
        self._properties_names_list = properties_names_list
        list_agents.append(self._name)

    # Method to help print the list of real estate agents
    def printAgentList(self):
        print("These are all the real estate agents: {}".format(list_agents))

    # Method to list out all the properties for the real estate agent
    def ListProperties(self):
        print("{} is responsible for the following properties:\n".format(self._name))
        i = 0
        # Use a for loop to iterate through all the properties for the real estate agent. In each iteration,
        # call the agent display method for the specific property type.
        for i in range(len(self._properties_list)):
            try:
                self._properties_list[i].displayHouseForAgent()
            except:
                self._properties_list[i].displayApartmentForAgent()
            print()  # just for more appealing spacing.
            i += 1

    # Method to add the property to the list of properties for a specific agent. Note that we are adding
    # the property objects to one list so we can call on their methods later as well as the property names
    # to another list so they are easily displayed.
    def AddProperty(self, property):
        self._properties_list.append(property)
        self._properties_names_list.append(property._property_name)
        print("{} has been added to {}'s property list".format(property._property_name, self._name))
        print("{}'s full property list includes:\n{}".format(self._name, self._properties_names_list))
