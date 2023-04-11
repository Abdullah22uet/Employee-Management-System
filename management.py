# Start of the program
def addData():
    name = input("Enter name : ")
    id = input("Enter id : ")
    contact = input("Enter contact : ")
    address = input("Enter address : ")
    f=open("StoredDataa.txt","a")
    f.write(id+"\t")
    f.write(name+"\t")
    f.write(contact+"\t")
    f.write(address+"\t")
    f.close()
def updateData():
    i = input("Enter id of employee to update : ")
    f=open("StoredDataa.txt","r")
    all=f.readlines()
    f.close()
    f=open("StoredDataa.txt","a")
    for data in all:
        d=data.split("\t")
        if d[0]==i:
            name = input("Enter name : ")
            id = input("Enter id : ")
            contact = input("Enter contact : ")
            address = input("Enter address : ")
            f.write(id+"\t"+name+"\t"+contact+"\t"+address+"\t")
            print("Employee data updated successfully.")
        else:
            f.write(data)
def deleteData():
    i = input("Enter id of employee to delete : ")
    f=open("StoredDataa.txt","r")
    all=f.readlines()
    f.close()
    f=open("StoredDataa.txt","w")
    for data in all:
        d=data.split("\t")
        if d[0]!=i:
            f.writelines(data)
        else:
            print("Employee deleted successfully.")
def showData():
    print("Id\tName\tContact\tAddress")
    f=open("StoredDataa.txt","r")
    all=f.readlines()
    f.close()
    for data in all:
        print(data)
while True:
    print("Press 1 to add new employee")
    print("Press 2 to delete employee")
    print("Press 3 to update employee data")
    print("Press 4 to show employee data")
    choice = int(input("Enter your decision : "))
    if(choice == 1):
        addData()
    elif(choice == 2):
        deleteData()
    elif(choice ==3):
        updateData()
    elif(choice == 4):
        showData()
    else:
        print("Invalid choice.Kindly give your decision according to given opttions.") 
# End of the program