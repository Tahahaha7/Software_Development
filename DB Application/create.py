# Importing packages

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime as dt
from sqlalchemy import*
import numpy as np
import pandas as pd

# Create an engine and a declarative bases
engine = create_engine('sqlite:///:memory:', echo = False)
#engin = create_engine('sqlite:///database.db')
engine.connect()
Base = declarative_base()

# CREATING TABLES AND THEIR ATTRIBUTES
'''
All the relevant details of that house need to be captured, ie. at least: 
seller details, # of bedrooms, # of bathrooms, listing price, zip code, 
date of listing, the listing estate agent, and the appropriate office.
'''
class Property(Base):
    __tablename__ = 'Listings'
    id = Column(Integer, primary_key = True)
    address = Column(Text)
    n_bedrooms = Column(Integer)
    n_bathrooms = Column(Integer)
    list_price = Column(Integer)
    zipcode = Column(Integer)
    list_date = Column(Date)
    status = Column(Text)   
    office_id = Column(Integer, ForeignKey('Offices.id'))
    agent_id = Column(Integer, ForeignKey('Agents.id'))    

class Agent(Base):
    __tablename__ = 'Agents'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    phone = Column(Text)
    
class Office(Base):
    __tablename__ = 'Offices'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    address = Column(Text)

class Buyer(Base):
    __tablename__ = 'Buyers'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    phone = Column(Text)   
    
'''
All appropriate details related to the sale must be captured, ie. at least: 
buyer details, sale price, date of sale,the selling estate agent.
'''
class Sale(Base):
    __tablename__ = 'Sales'
    id = Column(Integer, primary_key = True)
    estate_id = Column(Integer, ForeignKey('Listings.id'))
    agent_id = Column(Integer, ForeignKey('Agents.id'))
    buyer_id = Column(Integer, ForeignKey('Buyers.id'))
    sale_date = Column(Date)
    sale_price = Column(Integer)
    commission = Column(Integer)

Base.metadata.create_all(bind=engine)


def sold_property(estate, agent, buyer, date):
    '''
    The function is called whenever we wish to record a sale.
    It takes the property_id, agent_id, buyer_id, data as input
    '''
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Compute the comission based on the property price
    sold_price = session.query(Property.list_price).filter(Property.id == estate)
    # List the range of prices and their respective commission rates
    price_range = [10**5, 2*10**5, 5*10**5, 10**6, np.inf]
    rate = [.01, .075, .06, .05, .04]
    # List the possible cases for the commission rates
    cases = case([(Property.list_price < price_range[i], rate[i]) 
                  for i in range(len(price_range))])
    
    # Insert the commission based on the 
    commission = session.query(Property.list_price * cases).filter(Property.id == estate)
    
    # Add the property into the Sales table along with the attriibutes
    session.add(Sale(estate_id = estate, agent_id = agent, sale_date = date,
                     sale_price = sold_price, commission = commission))
    
    # Update the status of the property as SOLD
    sold_estate = session.query(Property).filter(Property.id == estate)
    sold_estate.update({Property.status: 'SOLD'})
    
    # Commit the changes and close the session
    session.commit()
    session.close()