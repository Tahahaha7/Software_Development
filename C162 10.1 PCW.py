#!/usr/bin/env python
# coding: utf-8

# # Bank Loan

# In[1]:


import sqlalchemy
import datetime as dt
from sqlalchemy import update
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime


# In[4]:


engine = create_engine('sqlite:///:memory:', echo = True)
engine.connect()
Base = declarative_base()

class customer(Base):
    __tablename__ = 'clients'
    clientnumber = Column(Integer, ForeignKey('loans.clientnumber'), primary_key=True)
    fullname = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return '<Client(clientnumber={0}, fullname={1},email={2}, phone={3})>'        .format(self.clientnumber, self.fullname, self.email, self.phone)

class loan(Base):
    __tablename__ = 'loans'
    accountnumber = Column(Integer, primary_key=True)
    clientnumber = Column(Integer)
    startdate = Column(DateTime())
    startmonth = Column(Integer)
    term = Column(Integer)
    
    remaining_term = Column(Integer)
    principaldebt = Column(Numeric)
    accountlimit = Column(Numeric)
    balance = Column(Numeric)
    status = Column(String)
    
    def __repr__(self):
        return '''<Loan(accountnumber={0}, clientnumber={1}, startdate={2}, 
                  startmonth={3}, term={4}, remaining_term={5}, principaldebt={6}, 
                  accountlimit={7}, balance={8}, status={9})>'''\
        .format(self.accountnumber, self.clientnumber, self.startdate, 
                self.startmonth, self.term, self.remaining_term, self.principaldebt, 
                self.accountlimit, self.balance, self.status)

def date_format(date):
        return dt.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

Base.metadata.create_all(engine)

client_list = [customer(clientnumber=1, fullname='Harold Grimes', 
                        email='HaroldVGrimes@dayrep.com', phone='(671) 925-1352'),
               customer(clientnumber=2, fullname='Robert Warren', 
                        email='RobertDWarren@teleworm.us', phone='(251) 546-9442'),
               customer(clientnumber=3, fullname='Vincent Brown', 
                        email='VincentHBrown@rhyta.com', phone='(125) 546-4478'),
               customer(clientnumber=4, fullname='Martina Kershner', 
                        email='MartinaMKershner@rhyta.com', phone='(630) 446-8851'),
               customer(clientnumber=5, fullname='Tony Schroeder', 
                        email='TonySSchroeder@teleworm.us', phone='(226) 906-2721')]


loan_list = [loan(accountnumber=1, clientnumber=1,startdate=date_format('2017-11-01 10:00:00'), 
                  startmonth=201712, term=36, remaining_term=35, principaldebt=10000.00, 
                  accountlimit=15000.00, balance=9800.00, status='NORMAL'),
             loan(accountnumber=2, clientnumber=2,startdate=date_format('2018-01-01 10:00:00'), 
                  startmonth=201802, term=24, remaining_term=24, principaldebt=1000.00, 
                  accountlimit=1500.00, balance=1000.00, status='NORMAL'),
             loan(accountnumber=3, clientnumber=1,startdate=date_format('2016-11-01 10:00:00'), 
                  startmonth=201612, term=12, remaining_term=-3, principaldebt=2000.00, 
                  accountlimit=15000.00, balance=4985.12, status='ARREARS'),
             loan(accountnumber=4, clientnumber=3,startdate=date_format('2018-01-01 10:00:00'), 
                  startmonth=201802, term=24, remaining_term=24, principaldebt=3500.00, 
                  accountlimit=5000.00, balance=1300.00, status='NORMAL'),
             loan(accountnumber=5, clientnumber=4,startdate=date_format('2017-11-01 10:00:00'), 
                  startmonth=201712, term=12, remaining_term=35, principaldebt=10000.00, 
                  accountlimit=15000.00, balance=0.00, status='PAID OFF'),
             loan(accountnumber=6, clientnumber=5,startdate=date_format('2018-01-01 10:00:00'), 
                  startmonth=201802, term=48, remaining_term=24, principaldebt=1000.00, 
                  accountlimit=1500.00, balance=0.00, status='PAID OFF'),
             loan(accountnumber=7, clientnumber=6,startdate=date_format('2015-11-01 10:00:00'), 
                  startmonth=201512, term=12, remaining_term=-20, principaldebt=10000.00, 
                  accountlimit=15000.00, balance=9800.00, status='Arrears')]

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()
session.add_all(client_list)
session.add_all(loan_list)
session.commit()


# In[5]:


# Update the query for client number #7
session.query(loan).filter(loan.accountnumber==7).update({loan.status:"PAID OFF", loan.principaldebt:0})
# Show the updated status for the client #7
print('\nResult of query: \n', session.query(loan).filter_by(accountnumber=7).all())


# # Online retail

# In[6]:


engine = create_engine('sqlite:///:memory:', echo = True)
engine.connect()
Base = declarative_base()


# In[7]:


# Add tables
class Product(Base):
    __tablename__ = 'products'
    ProductID = Column(Integer, primary_key=True)
    Title = Column(String)
    Description = Column(String)
    Price = Column(Numeric)
    Cost = Column(Numeric)

class Orders(Base):
    __tablename__ = 'orders'
    OrderID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey("customers.CustomerID"))
    DateOrdered = Column(String)
    MonthOrdered = Column(Integer)

class OrderItems(Base):
    __tablename__ = 'orderItems'
    OrderID = Column(Integer, ForeignKey("orders.OrderID"), primary_key=True)
    ProductID = Column(Integer, ForeignKey("products.ProductID"))
    Quantity = Column(Integer)

class Warehouse(Base):
    __tablename__ = 'warehouse'
    WarehouseID = Column(Integer, primary_key=True)
    WarehouseName = Column(String)
    Address = Column(String)

class Inventory(Base):
    __tablename__ = 'inventory'
    RowID = Column(Integer, ForeignKey("warehouse.WarehouseID"), primary_key=True)
    WarehouseID = Column(Integer, ForeignKey("warehouse.WarehouseID"))
    ProductID = Column(Integer, ForeignKey("products.ProductID"))
    Quantity = Column(Integer)
    Quantity = Column(String)

class Supplier(Base):
    __tablename__ = 'supplier'
    SupplierID = Column(Integer, primary_key=True)
    SupplierName = Column(String)
    Address = Column(String)
    PhoneNumber = Column(String)
    Email = Column(String)


class SupplierProduct(Base):
    __tablename__ = 'supplierProduct'
    SupplierID = Column(Integer, ForeignKey("supplier.SupplierID"), primary_key=True)
    ProductID = Column(Integer, ForeignKey("products.ProductID"))
    DaysLeadTime = Column(Integer)
    Cost = Column(Numeric)

class SupplierOrders(Base):
    __tablename__ = 'supplierOrders'
    SupplierOrderID = Column(Integer, primary_key=True)
    SupplierID = Column(Integer, ForeignKey("supplier.SupplierID"))
    ProductID = Column(Integer, ForeignKey("products.ProductID"))
    WarehouseID = Column(Integer, ForeignKey("warehouse.WarehouseID"))
    Quantity = Column(Integer)
    Status = Column(String)
    DateOrdered = Column(String)
    DateDue = Column(String)

class Customer(Base):
    __tablename__ = 'customers'
    CustomerID = Column(Integer, primary_key=True)
    FirstName = Column(String)
    Surname = Column(String)
    Address = Column(String)
    PhoneNumber = Column(String)
    Email = Column(String)

Base.metadata.create_all(engine)

#Insert data
product_list = [Product(ProductID=3001, Title="Widget",Description="", Price=1, Cost=1),
                Product(ProductID=3002, Title="Wodget",Description="", Price=1, Cost=1)]

order_list = [Orders(OrderID=1000, CustomerID=2000, DateOrdered="2025-01-01 10:00:00", MonthOrdered=202501)]

orderItems_list = [OrderItems(OrderID=1000, ProductID=3001, Quantity=1),
                   OrderItems(OrderID=1001, ProductID=3001, Quantity=1)]

warehouse_list = [Warehouse(WarehouseID=4001, WarehouseName="ABC Warehouse", 
                            Address="1374 Elkview Drive"),
                  
                  Warehouse(WarehouseID=4002, WarehouseName="XYZ Warehouse", 
                            Address="1576 Walnut Street")]

inventory_list = [Inventory(WarehouseID=4001, ProductID=3001, Quantity=3),
                  Inventory(WarehouseID=4001, ProductID=3002, Quantity=1),
                  Inventory(WarehouseID=4002, ProductID=3001, Quantity=1),
                  Inventory(WarehouseID=4002, ProductID=3002, Quantity=4)]

supplier_list = [Supplier(SupplierID=5001, SupplierName="Widge Suppliers Ltd", 
                          Address="3316 Whitetail Lane", PhoneNumber="479-357-6159", 
                          Email="TimothyCSilva@widge.com"),
                 
                 Supplier(SupplierID=5002, SupplierName="Wodge Suppliers Ltd", 
                          Address="3316 Whitetail Lane", PhoneNumber="479-357-6159", 
                          Email="TimothyCSilva@widge.com")]

supplierProduct_list = [SupplierProduct(SupplierID=5001, ProductID=3001, DaysLeadTime=3, Cost=15),
                        SupplierProduct(SupplierID=5002, ProductID=3002, DaysLeadTime=3, Cost=13)]

supplierOrder_list = [SupplierOrders(SupplierOrderID=6001, SupplierID=5001, ProductID=3001, 
                                     WarehouseID=4001, Quantity=99, Status="Ordered", 
                                     DateOrdered="2025-01-15", DateDue="2025-01-21"),
                      SupplierOrders(SupplierOrderID=6002, SupplierID=5002, ProductID=3001, 
                                       WarehouseID=4002, Quantity=99, Status="Delivered", 
                                       DateOrdered="2025-01-16", DateDue="2025-01-23")]

customer_list = [Customer(CustomerID=2000, FirstName="Gertrud", Surname="Karr", 
                          Address="3316 Whitetail Lane", PhoneNumber="479-357-6159", 
                          Email="TimothyCSilva@widge.com"),
                 
                 Customer(CustomerID=2001, FirstName="Clara", Surname="Tang", 
                         Address="3316 Whitetail Lane", PhoneNumber="479-357-6159", 
                         Email="TimothyCSilva@widge.com")]


# In[8]:


from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()
session.add_all(product_list)
session.add_all(order_list)
session.add_all(orderItems_list)
session.add_all(warehouse_list)
session.add_all(inventory_list)
session.add_all(supplier_list)
session.add_all(supplierProduct_list)
session.add_all(supplierOrder_list)
session.add_all(customer_list)
print('-- all tables added --')


# In[ ]:


session.commit()

session.query(Inventory).filter(Inventory.WarehouseID==4001 and Inventory.ProductID==3001).update({Inventory.Quantity:Inventory.Quantity+99})

print(session.query(Inventory).filter_by(Inventory.WarehouseID==4001 and Inventory.ProductID==3001).all())

session.add_all([Orders(OrderID=1001, CustomerID=2000, DateOrdered="2025-01-01 10:00:00", 
                        MonthOrdered=202501), OrderItems(OrderID=1000, ProductID=3001, Quantity=500),
                 SupplierOrders(SupplierOrderID=6003, SupplierID=5002, ProductID=3002,
                                WarehouseID=4001, Quantity=500, Status="Ordered", 
                                DateOrdered="2025-01-15", DateDue="2025-01-21")])

