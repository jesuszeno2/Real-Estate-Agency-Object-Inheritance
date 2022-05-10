"""
Jesus Zeno SIE508 Assignment 3
This main program uses the class Real Estate agent along with Property and its children classes House
and Apartment. Together they make a list of real estate agents and display all the agents as well as the
different aspects about each property. In addition, the program tells us which agent is in charge of
what properties.
"""

from Property import Property, House, Apartment
from RealEstateAgent import RealEstateAgent

def main():

    # Here wake make the two agent objects Leo Fitz and Agent Coulson
    agent_Fitz = RealEstateAgent("Leo Fitz")
    agent_Coulson = RealEstateAgent("Phil Coulson")

    # Print the current list of real estate agents.
    agent_Coulson.printAgentList()

    # Make the first house object and display its properties
    print("Please input the values for House 1")
    house_1 = House()
    house_1.displayHouse()

    # Make second house object and display its properties
    print("Please input the values for House 2")
    house_2 = House()
    house_2.displayHouse()

    # Make first Apartment object and display its properties
    print("Please input the values for Apartment 1")
    apartment_1 = Apartment()
    apartment_1.displayApartment()

    # Assign Coulson House 1 and Apartment 1
    agent_Coulson.AddProperty(house_1)
    agent_Coulson.AddProperty(apartment_1)

    # List Coulson's properties that he is in charge of
    agent_Coulson.ListProperties()

    # Assign Fitz house 2 and list the property he is in charge of.
    agent_Fitz.AddProperty(house_2)
    agent_Fitz.ListProperties()

if __name__ == '__main__':
    main()
