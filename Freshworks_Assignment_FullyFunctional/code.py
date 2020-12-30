import time as t
#We are importing only one package time to calculate user defined timeout value
dictionary={} 
#Dictionary datatype is used to store data in json like format
#This function block is for creating new data field, and the way of using is 'create_record('key',value,timeout)' in the console, here timeout is optional
def create_record(key,value,timeout=0):
    if key in dictionary:
        print("Error Message: The key entered already exists in database") #Error for repeating record
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): #Mentioned constraint for object value less than 16KB & file size less than 1GB  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,t.time()+timeout] #Calculation for user defined timeout
                if len(key)<=32: #Mentioned constraints for key less than 32 characters
                    dictionary[key]=l
                    print("Record added successfully")

            else:
                print("Error Message: Memory limit exceeded, Enter with in 32 letters")#Error for key length more than 32
        else:
            print("Error Message: Invalind key, key must contain only alphabets and no special characters or numbers")#Error for key containing special characters or numerical values

#This function block is for reading the stored data, and the way of using is 'read_record('key')' in the console, this has only one parameter - key
def read_record(key):
    if key not in dictionary:
        print("Error Message: Entered key does not exist in database. Please enter a valid key") #Error Message to indicate unknown or unstored data is being entered
    else:
        storeclass=dictionary[key]
        if storeclass[1]!=0:
            if t.time()<storeclass[1]: 
                record=str(key)+":"+str(storeclass[0]) #To retrieve data in json like format
                return record
            else:
                print("Error Message: Time-To-Live of the ",key," has expired") #Error Message for indicating time of key has expired
        else:
            record=str(key)+":"+str(storeclass[0])
            return record

#This function block is for deleting the specified key record, and the way of using is 'delete_record('key')' in the console, this has only one parameter - key
def delete_record(key):
    if key not in dictionary:
        print("Error Message: Entered key does not exist in database. Please enter a valid key") #Error Message to indicate unknown or unstored data is being entered
    else:
        storeclass=dictionary[key]
        if storeclass[1]!=0:
            if t.time()<storeclass[1]: 
                del dictionary[key]
                print("Key, successfully deleted")
            else:
                print("Error Message: Time-To-Live of the ",key," has expired") #Error Message for indicating time of key has expired
        else:
            del dictionary[key]
            print("Key, successfully deleted")

#We can also use threads to pass multiple requests simultaneously 
#Procedure for execution are:
#create_record('key',4)
#create_record('key',4,3)
#read_record('key')
#delete_record('key')
