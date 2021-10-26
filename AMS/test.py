import mysql.connector  
#Create the connection object   
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root",passwd = "Bhoomi@12", database = "AMS")  
  
#printing the connection object   
print(myconn)   
  
# #creating the cursor object  
# cur = myconn.cursor()  
  
# print(cur)  