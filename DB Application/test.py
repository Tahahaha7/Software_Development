import unittest
from create import*
from insert_data import*

# CREATING A CLASS FOR UNIT TESTING
class InsertTestCase(unittest.TestCase):
    
    engine = create_engine('sqlite:///:memory:')
    #engin = create_engine('sqlite:///test.db')
    engine.connect()
    # Inserting fake data (as if the original one was not)
    test_agents = [['test_agent1', '415-123-4567'],
                   ['test_agent2', '415-123-5678'],
                   ['test_agent3', '415-123-6789']]

    test_offices = [['test_office1', '5th Ave'],
                    ['test_office2', '6th Ave'],
                    ['test_office3', '7th Ave']]

    test_buyers = [['test_buyer1','415-678-1111'],
                   ['test_buyer2','415-678-2222'],
                   ['test_buyer3','415-678-3333']]

    test_properties = [['test_property1', 5, 2, 100, 94102, dt(2020, 3, 15), 'ON SALE', 1, 2],
                       ['test_property2', 6, 2, 200, 94103, dt(2020, 3, 8), 'ON SALE', 2, 3],
                       ['test_property3', 2, 1, 100, 94102, dt(2020, 3, 3), 'ON SALE', 3, 1]]
    
    # Adding the data into the database
    for i in range(3):
        session.add(Agent(**dict(zip(Agent.__table__.columns.keys()[1:], test_agents[i]))))
        session.add(Office(**dict(zip(Office.__table__.columns.keys()[1:], test_offices[i]))))
        session.add(Buyer(**dict(zip(Buyer.__table__.columns.keys()[1:], test_buyers[i]))))
        session.add(Property(**dict(zip(Property.__table__.columns.keys()[1:], test_properties[i]))))  
    # Testing the insertion of data in all tables as well as the validity of the queries
    def test_insert_agent(self):
        test_query = session.query(Agent).filter_by(name='test_agent2', phone='415-123-5678').first()
        self.assertTrue(test_query.name == 'test_agent2')

    def test_insert_office(self):
        test_query = session.query(Office).filter_by(name='test_office1', address='5th Ave').first()
        self.assertTrue(test_query.address == '5th Ave')

    def test_insert_property(self):
        test_query = session.query(Property).filter_by(address='test_property1').first()
        self.assertTrue(test_query.status == 'ON SALE')


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)