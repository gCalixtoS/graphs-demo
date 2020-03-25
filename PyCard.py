## Import 

import uuid
import csv
import random
from faker import Faker
fake = Faker()
from datetime import datetime
from random import randint

from faker.providers import BaseProvider


class Provider(BaseProvider):
    def foo(self):
        return 'bar'
    
fake.add_provider(Provider)


## Set Language

guidf=str(uuid.uuid1())
#Here you can change the pt_BR for your language like 'de_DE'
fake=Faker('pt_BR') 

 
#Generate or Open the csv file

g=open("PERSONS_1k.csv","w",newline='')
w=csv.writer(g)
 
#Generate Header of csv file
    
w.writerow(('ID','NAME','INFECTED','INFECTED_DATE'))


#Loop to generafe the rows... You can change the total of iteration to generate more or less rows
for i in range(1000):
		w.writerow((( i, 
		              fake.name(),
					  random.choice(['1','0']),
                      fake.unix_time(end_datetime=None, start_datetime=None)
				)))
g.close()
 