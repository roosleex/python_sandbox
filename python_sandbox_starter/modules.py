# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
today = datetime.date.today()
print(today)

from datetime import date
today2 = date.today()
print(today2)

import time
timestamp = time.time()
print(timestamp)

from time import time
timestamp2 = time()
print(timestamp2)



#import custom module
import validator
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print(f'Email {email} is valid')
else:
    print(f'Email {email} is not valid')

email2 = 'test2test.com'
if validate_email(email2):
    print(f'Email {email2} is valid')
else:
    print(f'Email {email2} is not valid')
