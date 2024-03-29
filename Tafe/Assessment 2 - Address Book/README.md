Assessment Tasks:

Create a new Python module called addressbook.py consisting of a class called Record that defines an address book record. 
The module should also offer several functions to enable address book record creation and manipulation. 

Import the module into your main code file, called main.py (this is the file you should be executing).

The Record class should consist of 4 properties: name, email, phone and address of a person/customer. 
These properties can be public values so that they are easily obtained from the Record object.

Record objects will be saved (serialized) to a binary file using the Python pickle module and this will be our address book database.

Define and code the following:

A function to open the address book file in “append binary” mode and add a Record. (Hint: use pickle.dump)

A function to open the address book file in “read binary” mode and fetch a customer Record by name. (Hint: use pickle.load) 
Note: this function must make use of the index discussed below and raise a ValueError exception if the index hasn’t been created or is empty.

The addressbook module should also have a global variable named index defined as a Python dictionary. 
The keys will be the name property and the value should be the file position of that Record in the address book. Define the function below to build the index.

The function should open the address book file in “read binary” mode and use a while loop.
