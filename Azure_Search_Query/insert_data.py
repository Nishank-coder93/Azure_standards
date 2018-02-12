import pyodbc
import os

server = ''
database = ''
username = ''
password = ''
driver= ''
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

if cnxn:
    print("Connected To DataBase")
else:
    print("Unable to connect")

# create_table = "if not exists (select * from sysobjects where name='recipes' and xtype='U') create table recipes(recipe_id int not null primary key, recipe_name varchar(25), recipe_type varchar(25), recipe_weight varchar(100), recipe_ingredients varchar(255));"
fullpath = os.path.join(os.path.expanduser('~'), 'Desktop', 'Cloud_Computing', 'Azure_Search_query', 'dataset', 'main.csv')
print(fullpath)
insert_values = "BULK INSERT recipes FROM \"{}\" WITH ( FIELDTERMINATOR =',', ROWTERMINATOR = '\n')".format(fullpath)
cursor = cnxn.cursor()
with cursor.execute(insert_values):
    print ("Successfully created or already exists")
cnxn.commit()