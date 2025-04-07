contacts = {
    'Akshay Prasad': '8590567517', 
    'Aban Falaki': '8943187777', 
    'Md Shahbaz Alam': '8409081789', 
    'Mishail': '9605292768', 
    'Renin': '7654345678', 
    'Md Shinad': '7898665461', 
    'Adarsh Aggarwal': '6387786334', 
    'Shahasin': '7880965432', 
    'Aayush': '9527141276', 
    'Ankit': '8847295877', 
    'Adarsh Singh': '8308468215', 
    'Aayush Shreyash': '7651804387', 
    'Anirban Sasmal': '89203118761', 
    'Md Azeem': '7981732170', 
    'Jatin': '8054807870', 
    'Manish': '7091613823', 
    'Mubassir Ahmed': '7766805177', 
    'Ripudaman': '8296772731', 
    'Rohit': '8168365014', 
    'Subham': '7017577412', 
    'Utsav Visnoi': '7906044957', 
    'Vansh': '7037191676', 
    'Vipul Singh': '9555122307', 
    'Abhishek Ray': '6202966849', 
    'Aayush Singh': '6203655501', 
    'Gurudatt': '6306569446', 
    'Soumen Pal': '7056197530', 
    'Prince Roy': '7061692906', 
    'Nipun': '7500560748', 
    'Pavan': '781508224', 
    'Rajan': '8100676814', 
    'Saksham Pundir': '8218012509', 
    'Dibyam': '8252805199', 
    'Ashim': '8597304224', 
    'Aritra': '8653977896', 
    'Amrit Raj': '8709115173', 
    'Vivek': '8789064886', 
    'Harsh Kumar': '8847463046', 
    'Dwarikesh Ojha': '8953544473', 
    'Mukul Deshwal': '8979867355', 
    'Chaitanya': '9063032569', 
    'Naresh Tiwari': '9407869368', 
    'Venkat': '9658346666', 
    'Mudassir': '9682540621', 
    'Nitesh': '9953006253', 
}

print("1: Search a Contact, 2: Display all, 3: Extract multiple numbers")
choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter the name of the contact: ")
    number = contacts.get(name)
    if number:
        print(f"{name}: {number}")
    else:
        print("Contact not found.")
elif choice == 2:
    for name, number in contacts.items():
        print(f"{name}: {number}")
elif choice == 3:
    count = int(input("Enter the number of contacts to extract: "))
    extracted_contacts = []
    for _ in range(count):
        name = input("Enter the name of the contact: ")
        number = contacts.get(name)
        if number:
            extracted_contacts.append(f"{name}: {number}")
        else:
            extracted_contacts.append(f"{name}: Contact not found")
    print(extracted_contacts)
else:
    print("Invalid choice.")