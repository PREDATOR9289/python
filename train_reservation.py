import mysql.connector
import random

dataBase = mysql.connector.connect(
    host="localhost",
    username="root",
    password="1Khaledalasad",
    database="project"
)

if dataBase.is_connected():
    print("Connection Established\n")
else:
    print("Connection Refused\n")

print("Press 1 To Enquire About All Trains Passing Through Ghaziabad Junction\n"
      "Press 2 To Enquire About Trains Going To Your Destination\n"
      "Press 3 To Book Tickets\n")

i = int(input())

if i == 1:
    print("'Train No','Train Name','Arrival Time','Departure Time','Source Station,'Destination','Platform No'")

    mycursor = dataBase.cursor()
    query = "SELECT * FROM project.GZB_JUNC_TRAINS"  
    mycursor.execute(query)
    table = mycursor.fetchall()
    for x in table:
        print(x) 
elif i == 2:
    des = input("Enter Your Destination : ")
    
    print("'Train No','Train Name','Arrival Time','Departure Time','Source Station,'Destination','Platform No'")
    
    mycursor = dataBase.cursor()
    query = "SELECT * FROM project.GZB_JUNC_TRAINS WHERE DESTINATION = %s"  
    mycursor.execute(query, (des,))
    
    table = mycursor.fetchall()
    for x in table:
        print(x)
elif i == 3:
    des = input("Enter Your Destination : \n")
    
    print("'Train No','Train Name','Arrival Time','Departure Time','Source Station,'Destination','Platform No'\n")
    
    mycursor = dataBase.cursor()
    query = "SELECT * FROM project.GZB_JUNC_TRAINS WHERE DESTINATION = %s"  
    mycursor.execute(query, (des,))
    
    table = mycursor.fetchall()
    for x in table:
        print(x)
    
    train_no = input("Enter Train No For Booking : \n")
    tickets = int(input("Enter No Of Tickets : \n"))
    name = input("Enter Your Name : \n")
    
    print("\n")

    print("'Train No','Train Name','Arrival Time','Departure Time','Source Station,'Destination','Platform No'\n")

    mycursor = dataBase.cursor()
    query = "SELECT * FROM project.GZB_JUNC_TRAINS WHERE TRAIN_NO = %s"  
    mycursor.execute(query, (train_no,))
    
    table = mycursor.fetchall()
    for x in table:
        trano = x[0]
        trana = x[1]
        traar = x[2]
        trade = x[3]
        traso = x[4]
        trads = x[5]
        trapf = x[6]
        print(x)

    print("\nYour Fare For",tickets,"Is ₹",50*tickets)

    ticket_no = random.randrange(100000,999999)
    seat_no = random.randrange(1,300)
    pnr = random.randrange(1000000000,9999999999)
    
    con = input("\nEnter Yes For Confirming Payment Or No For Denying Payment : ")
    if con == "Yes" or "yes" or "YES":
        print("Payment Succeeded \n")
        print("\n")
        print("Ticket No : ",ticket_no,"                PNR No : ",pnr,"\n"
              "                                      \n"
              "Train Number : ",trano,"                 Train Name : ",trana,"\n"
              "Name Of The Passenger : ",name,"      Number Of Tickets : ",tickets,"\n"
              "Seat No : ",seat_no,"\n"
              "Arrival Time : ",traar,"                 Departure Time : ",trade,"\n"
              "Coming From : ",traso,"                    Destination : ",trads,"\n"
              "Platform No : ",trapf)
        print("\n")
        print("\n")
    elif con == "No" or "no" or "NO":
        print("Payment Failed Try Again")
else:
    print("Invalid Operation")