from insert_data import *

# Query 1: Find the top 5 offices with the most sales for that month

sales_count = func.count(Property.office_id).label('Sales')
q1 = session.query(Property.office_id, Office.name, Office.address, sales_count)\
    .join(Office).filter(Property.status == 'SOLD')\
    .group_by(Property.office_id)\
    .order_by(sales_count.desc()).limit(5)

print('Top 5 offices with the most sales for that month: ')
print(pd.read_sql(q1.statement, session.bind))

# Query 2: Find the top 5 estate agents who have sold the most

agent_sale_count = func.count(Property.agent_id).label('Sales')
q2 = session.query(Agent.id, Agent.name, Agent.phone, agent_sale_count)\
    .join(Property).filter(Property.status == 'SOLD')\
    .group_by(Agent.id).order_by(agent_sale_count.desc()).limit(5)

print('Top 5 estate agents who have sold the most: ')
print(pd.read_sql(q2.statement, session.bind))

# Query 3: Calculate the commission that each estate agent must receive

total_coms = func.sum(Sale.commission).label('Commission')
q3 = session.query(Agent.name, Agent.phone, total_coms)\
    .join(Property, Property.agent_id == Agent.id)\
    .join(Sale, Sale.estate_id == Property.id)\
    .group_by(Agent.id)

print('The commission that each estate agent must receive: ')
print(pd.read_sql(q3.statement, session.bind))

# Query 4: For all houses that were sold that month, 
# calculate the average number of days that the houses were on the market.

begin = pd.read_sql(session.query(Property.list_date)\
                    .join(Sale).filter(Property.status == 'SOLD')\
                    .statement, session.bind)

end = pd.read_sql(session.query(Sale.sale_date).statement, session.bind)

duration = np.mean([(end['sale_date'][i] - begin['list_date'][i]).days 
                    for i in range(len(end))])
print('The average number of days that the houses were on the market: ', round(duration, 0))


# Query 5: For all houses that were sold that month, calculate the average selling price

avg_price = func.avg(Sale.sale_price).label('Average Price')
q5 = session.query(avg_price).filter(extract('month', Sale.sale_date) == dt.today().month)

print('The average selling price in the current month: ')
print(pd.read_sql(q5.statement, session.bind).values[0][0])
# Query 6: Find the zip codes with the top 5 average sales prices

avg_price = func.avg(Sale.sale_price).label('Average Price')
q6 = session.query(Property.zipcode, avg_price)\
    .join(Sale).filter(Property.status == 'SOLD')\
    .group_by(Property.zipcode)\
    .order_by(avg_price.desc()).limit(5)

print('The zip codes with the top 5 average sales prices: ')
print(pd.read_sql(q6.statement, session.bind))