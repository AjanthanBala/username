#login program
print ("\t\t\t ...Program to Check If Username Available For Use...\n\n\n")
admin_users = ("Ajanthan", "Nadeen")
users = []
username = input("Enter Your Username :")

if users and admin_users:
  for username in users or admin_users:
    print ("username already Used")

else:
  print ("username "  + username + " is available")
  sign = input(" Would you like to Sign Up? Y/N : ").upper()
  if sign == 'N':
   print(" Thank You ! Have A Nice Day!!:)")
 
  elif sign == 'Y':
    print("what type of user do you want to sign in as \n \t\t 1. Admin \n\t\t 2. User \n")

  req_admin = str(input("Admin \ User : ")).title()
  if (req_admin == 'Admin' ) or (req_admin == '1'):
    print ("You do not have privileges to add Admin:")
  elif(req_admin == 'User' ) or (req_admin == '2'):
    print ("Enter the Username :")
    user = str(input()).title() 
    users.append(user)
    print("username " + user + "\tadded successfully to users")
  else:
    print("invalid Entry Try Again") 
  
 
 

