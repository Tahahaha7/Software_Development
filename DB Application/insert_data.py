from create import *

# INSERT DATA INTO THE DATABASE

# Open the session
Session = sessionmaker(bind=engine)
session = Session()

list_property = [
    # address, n_bedrooms, n_bathrooms, price, zipcode, date, status, office_id, agent_id
    ['Property1', 9, 3, 1500000, 94102, dt(2020, 3, 9), 'ON SALE', 1, 4],
    ['Property2', 4, 2, 700000, 94105, dt(2020, 2, 16), 'ON SALE', 3, 2],
    ['Property3', 2, 3, 400000, 94106, dt(2020, 3, 11), 'ON SALE', 2, 6],
    ['Property4', 4, 2, 175000, 94102, dt(2020, 2, 19), 'ON SALE', 4, 7],
    ['Property5', 5, 2, 300000, 94103, dt(2020, 1, 21), 'ON SALE', 4, 1],
    ['Property6', 6, 1, 80000, 94105, dt(2020, 1, 26), 'ON SALE', 7, 5],
    ['Property7', 4, 2, 90000, 94103, dt(2020, 2, 26), 'ON SALE', 3, 2]]

list_office = [
               # office_name, office_address
               ['Office1', '1412 Market st'],
               ['Office2', '851 Nob Hill'],
               ['Office3', '458 Powel st'],
               ['Office4', '1145 Market st'],
               ['Office5', '855 Nob Hill'],
               ['Office6', '745 Van Ness'],
               ['Office7', '935 Van Ness']]

list_agent = [
              # agent_name, phone
              ['Agent1','415-678-0001'],
              ['Agent2','415-678-0002'],
              ['Agent3','415-678-0003'],
              ['Agent4','415-678-0004'],
              ['Agent5','415-678-0005'],
              ['Agent6','415-678-0006'],
              ['Agent7','415-678-0007']]

list_buyer = [
              # buyer_name, phone
              ['Buyer1','415-678-1000'],
              ['Buyer2','415-678-2000'],
              ['Buyer3','415-678-3000'],
              ['Buyer4','415-678-4000'],
              ['Buyer5','415-678-5000'],
              ['Buyer6','415-678-6000'],
              ['Buyer7','415-678-7000']]


# Compile the list into a distionaries with attributes as keys
classes = [Property, Office, Agent, Buyer]
lists = [list_property, list_office, list_agent, list_buyer]
columns = [Class.__table__.columns.keys()[1:] for Class in classes]

for i in range(len(classes)):
    temp = []
    for item in lists[i]:
        items = dict(zip(columns[i], item))
        temp.append(items)
    # Add entries for each table
    for t in temp:
        session.add(classes[i](**t))
        
# Commit the changes and close the session
session.commit()
session.close()

# ENTER THE DATA ON SOLD PROPERTIES
# estate, agent, buyer, date
sold_property(1, 5, 2, dt(2020, 3, 19))
sold_property(2, 4, 5, dt(2020, 4, 5))
sold_property(3, 4, 1, dt(2020, 3, 25))
sold_property(4, 7, 6, dt(2020, 3, 29))
sold_property(5, 6, 3, dt(2020, 4, 1))
sold_property(6, 3, 4, dt(2020, 4, 3))
sold_property(7, 6, 7, dt(2020, 3, 21))