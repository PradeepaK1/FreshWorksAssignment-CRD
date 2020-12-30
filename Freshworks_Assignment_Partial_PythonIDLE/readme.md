#import threading, json, time for itertion and calculation purposes
#Dictionary datatype is used to store data in json like format
#create_record function block is for creating new data field, and the way of using is 'create_record('key',value,timeout)' in the console, here timeout is optional
#It has Error message for repeating record
#It has Mentioned constraint for object value less than 16KB & file size less than 1GB  
#It has Calculation for user defined timeout
#It has Error for key length more than 32
#It has Error for key containing special characters or numerical values

#read_record function block is for reading the stored data, and the way of using is 'read_record('key')' in the console, this has only one parameter - key
#It has Error Message to indicate unknown or unstored data is being entered
#It has formatting to retrieve data in json like format
#It has Error Message for indicating time of key has expired

#delete_record function block is for deleting the specified key record, and the way of using is 'delete_record('key')' in the console, this has only one parameter - key
#It has Error Message to indicate unknown or unstored data is being entered
#It has Error Message for indicating time of key has expired

#It is different from other methods in:
#1. It provides options for users to choose the mode of operation to be done
#2. It works in PYTHON IDLE and Command Prompt
#3. It has partial working status till create operation
#4. It stores the created record in JSON and TXT files for later manipulation and retrieval