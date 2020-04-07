# DB Application

## Description
Managing real estate sales and listing using SQLAlchemy. The App contains the schema in ```create.py``` for building the tables needed as well as the relational joints between them given the standards of SQL normalization. Then the file ```insert_data.py``` serves as an example of feeding data into the database which then form a reference for the queries performed by ```query_data.py``` file. Finally, the unit testing section is run by ```test.py```.  
  
![Github](https://github.com/Tahahaha7/Software_Development/blob/master/DB%20Application/relational%20table.jpg)

## Running instructions
As mentioned in the assigment description, the app runs as follow:
```bash
python3.6 -m venv .venv  
source .venv/bin/activate   
pip3 install -r requirements.txt  
python3 create.py  
python3 insert_data.py  
python3 query_data.py  
python3 test.py  
```
