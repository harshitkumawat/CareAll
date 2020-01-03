import os
import pymysql
import datetime
from prettytable import PrettyTable
con = pymysql.connect('localhost','root','','careall')
cur = con.cursor()
class information:
	def __init__(self):
		self.name = ""
		self.age = 0
		self.gender=""
		self.mobile_no = 0
		self.address = ""
		self.amount = 0
		self.couple="No"
		self.review = ""
		self.ratings = 0
		self.available = "Y"
		self.descr = ""
		self.track = 0
class oldfolk(information):
	def oldfolksignup(self):
		os.system('clear')
		print("Enter Name -: ",end="")
		self.name = input();
		print("Enter Age  -: ",end="")
		self.age = int(input())
		print("Enter Gender(M/F)  -: ",end="")
		self.gender = input()
		print("Enter Mobile Number  -: ",end="")
		self.mobile_no = int(input())
		print("Enter Address  -: ",end="")
		self.address = input()
		print("Enter Amount you will pay for 1 month -: ",end="")
		self.amount = int(input())
		print("Are You a Couple(Y/N)  -: ",end="")
		self.couple = input()
		try:
			cur.execute("insert into oldfolk (name,age,gender,mobile,address,amount,couple,ratings,review,available) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.name,self.age,self.gender,self.mobile_no,self.address,self.amount,self.couple,self.ratings,self.review,self.available))
			print("\n\nYou Have Successfully Registered with our Application...")
			print("Your Username is -: ",self.name)
			print("Your Password is -: ",self.mobile_no)
		except Exception as e:
			print(e)
			input()
		con.commit()
	def oldfolksignin(self):
		os.system('clear')
		username = input("Enter Username -: ")
		password = input("Enter Password -: ")
		cur.execute("select * from oldfolk")
		data = cur.fetchall()
		for row in data:
			if row[0]==username and row[3]==password:
				print("\nLog in Successfully.....\n\nPress Enter to Continue....")
				input()
				os.system('clear')
				self.oldfolkoptions(username,password)
	def oldfolkoptions(self,username,password):
		choice_for_option = "0"
		while(choice_for_option!=4):
			os.system('clear')
			print("1. Hire Young Folks...\n2. Pending Request...\n3. Want to Leave currently hired young folk...\n4.Log Out...\n\nSelect your Option :",end="")
			choice_for_option = input()
			if choice_for_option=="1":
				cur.execute("select * from youngfolk where available = %s and track<%s",("Y","4"))
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Hired By'])
				print("Available Young Folks are -: ")
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9]])
				print(t)
				cur.execute("select * from hired where old_name = %s and old_mobile = %s",(username,password))
				checkhired = cur.fetchall()
				if not checkhired:
					print("\nWant to Hire(Y/N) -: ",end="")
					ch = input()
					if ch!="Y" or ch=="y":
						continue
					else:
						print("Enter Name of younk folk -: ",end="")
						name = input()
						print("Enter his/her Mobile Number -: ",end="")
						number = input()
						cur.execute("select * from youngfolk where name = %s and mobile = %s",(name,number))
						data = cur.fetchall()
						if not data:
							print("Enter Correct Details...")
						else:
							count = int(data[0][-1])
							count+=1
							if count==4:
								cur.execute("update youngfolk set available = %s, track = %s where name = %s and mobile = %s",("N",count,name,number))
								cur.execute("update oldfolk set available = %s where name = %s and mobile = %s",("N",username,password))
								print("Successfully Hired....")
								cur.execute("insert into hired(old_name,old_mobile,young_name,young_mobile) values(%s,%s,%s,%s)",(username,password,name,number))
							elif count<4:
								cur.execute("update youngfolk set track = %s where name = %s and mobile = %s",(count,name,number))
								cur.execute("update oldfolk set available = %s where name = %s and mobile = %s",("N",username,password))
								cur.execute("insert into hired(old_name,old_mobile,young_name,young_mobile) values(%s,%s,%s,%s)",(username,password,name,number))
								print("Successfully Hired....")
					con.commit()
				else:
					print("You have already hired a person....")
				input()
			elif choice_for_option=="3":
				os.system('clear')
				cur.execute("select * from hired where old_name = %s and old_mobile = %s",(username,password))
				data = cur.fetchall()
				if not data:
					print("Sorry No one is their to take Care...")
					input()
				else:
					print("Currently You have hired -: ")
					cur.execute("select * from youngfolk where name = %s and mobile = %s",(data[0][2],data[0][3]))
					data = cur.fetchall()
					count = int(data[0][9])
					t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Hired By'])
					for i in data:
						t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9]])
					print(t)
					print("\nWant to Leave(Y/N) -: ")
					j = input()
					if j=="Y" or j=="y":
						print("Write Review about person you have hired : ",end="")
						review = input()
						print("Give Ratings out of 5 about person you have hired : ",end="")
						rating = int(input())
						cur.execute("delete from hired where old_name = %s and old_mobile = %s",(username,password))
						count-=1
						cur.execute("update youngfolk set available = %s , review = %s,ratings = %s,track = %s where name = %s and mobile = %s",("Y",review,rating,count,name,number))
						cur.execute("update oldfolk set available = %s where name = %s and mobile = %s",("Y",username,password))
						print("Successfully Fired.....")
					input()
					con.commit()
			elif choice_for_option=="2":
				cur.execute("select * from request where old_name = %s and old_mobile = %s",(username,password))
				data = cur.fetchall()
				if not data:
					print("You Don't Have any Pending Request...")
					input()
				else:
					print("Below Young folks wants to take care of you -: ")
					t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Hired By'])
					for a in data:
						cur.execute("select * from youngfolk where name = %s and mobile = %s",(a[0],a[1]))
						i = cur.fetchall()
						t.add_row([i[0][0],i[0][1],i[0][2],i[0][3],i[0][4],i[0][5],i[0][6],i[0][7],i[0][9]])
					print(t)
					cur.execute("select * from hired where old_name = %s and old_mobile = %s",(username,password))
					checkhired = cur.fetchall()
					if not checkhired:
						print("\nWant to approve any request(y/n) -: ",end="")
						ch = input()
						if ch=="y" or ch=="Y":
							print("Enter Name -: ",end="")
							name = input()
							print("Enter Mobile Number -: ",end="")
							number = input()
							cur.execute("select * from youngfolk where name = %s and mobile = %s",(name,number))
							check_correct_details = cur.fetchall()
							if not check_correct_details:
								print("Invalid Details....")
								input()
							else:
								cur.execute("delete from request where old_name = %s and old_mobile = %s",(username,password))
								cur.execute("update oldfolk set available = %s where name = %s and mobile = %s",("N",username,password))
								cur.execute("insert into hired(old_name,old_mobile,young_name,young_mobile) values(%s,%s,%s,%s)",(username,password,name,number))
								print("Successfully Hired.....")
						elif ch=="n" or ch=="N":
							print("Want to delete any Request(y/n) :",end="")
							deletechoice = input()
							if deletechoice=="y" or deletechoice=="Y":
								print("Enter Name -: ",end="")
								name = input()
								print("Enter Mobile Number -: ",end="")
								number = input()
								cur.execute("select * from youngfolk where name = %s and mobile = %s",(name,number))
								check_correct_details = cur.fetchall()
								if not check_correct_details:
									print("Invalid Details....")
									input()
								else:
									cur.execute("delete from request where young_name = %s and young_mobile = %s",(name,number))
									count = check_correct_details[0][-1]
									count-=1
									cur.execute("update youngfolk set available = %s,track = %s where name = %s and mobile = %s",("Y",count,name,number))
									print("Request deleted Successfully...")
									input()
						con.commit()
									
					else:
						print("You have already hired a young folk to take care of you....")
						input()
			else:
				return
	def showoldfolks(self):
		ch = "0"
		while ch!="5":
			os.system('clear')
			print("1. Show all Old Folks...\n2. Show Available Old Folks...\n3. Show Old Folks Taken care by Young Folks...\n4. Show Old Couple Taken care by Young Folks...\n5. Go Back to Main Menu...\n\nSelect your Option : ",end="")
			ch = input()
			if ch=="1":
				os.system('clear')
				cur.execute("select * from oldfolk")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews','Available'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			elif ch=="2":
				os.system('clear')
				cur.execute("select * from oldfolk where available = %s","Y")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews','Available'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			elif ch=="3":
				os.system('clear')
				cur.execute("select * from oldfolk where available = %s","N")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews','Available'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			elif ch=="4":
				os.system('clear')
				cur.execute("select * from oldfolk where available = %s and couple = %s",("N","Y"))
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews','Available'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			else:
				return


class youngfolk(information):
	def youngfolksignup(self):
		os.system('clear')
		print("Enter Name -: ",end="")
		self.name = input();
		print("Enter Age  -: ",end="")
		self.age = int(input())
		print("Enter Gender(M/F)  -: ",end="")
		self.gender = input()
		print("Enter Mobile Number  -: ",end="")
		self.mobile_no = int(input())
		print("Enter Address  -: ",end="")
		self.address = input()
		print("Write about your Qualities -: ",end="")
		self.descr = input()
		try:
			cur.execute("insert into youngfolk (name,age,gender,mobile,address,ratings,review,descr,available,track) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.name,self.age,self.gender,self.mobile_no,self.address,self.ratings,self.review,self.descr,self.available,self.track))
			print("\n\nYou Have Successfully Registered with our Application...")
			print("Your Username is -: ",self.name)
			print("Your Password is -: ",self.mobile_no)
		except Exception as e:
			print(e)
			input()
		con.commit()
	def youngfolksignin(self):
		os.system('clear')
		username = input("Enter Username -: ")
		password = input("Enter Password -: ")
		cur.execute("select * from youngfolk")
		data = cur.fetchall()
		for row in data:
			if row[0]==username and row[3]==password:
				print("\nLog in Successfully as care taker.....\n\nPress Enter to Continue....")
				input()
				os.system('clear')
				self.youngfolkoptions(username,password)
	def youngfolkoptions(self,username,password):
		choice_for_option = "0"
		while(choice_for_option!=4):
			os.system('clear')
			print("1. Get hired by Old Folks...\n2. Want to Leave current Post...\n3.Log Out...\n\nSelect your Option :",end="")
			choice_for_option = input()
			if choice_for_option=="1":
				cur.execute("select * from oldfolk where available = %s",("Y"))
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews'])
				print("Available Old Folks are -: ")
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
				print(t)
				cur.execute("select * from youngfolk where name = %s and mobile = %s",(username,password))
				checkcount = cur.fetchall()
				count = int(checkcount[0][-1])
				if count<=4:
					print("\nWant to Request to take care(Y/N) -: ",end="")
					ch = input()
					if ch!="Y" or ch=="y":
						continue
					else:
						print("Enter Name of old folk -: ",end="")
						name = input()
						print("Enter his/her Mobile Number -: ",end="")
						number = input()
						cur.execute("select * from oldfolk where name = %s and mobile = %s",(name,number))
						data = cur.fetchall()
						if not data:
							print("Enter Correct Details...")
						else:
							count+=1
							if count==4:
								cur.execute("update youngfolk set available = %s, track = %s where name = %s and mobile = %s",("N",count,username,password))
								print("Request Sent Successfully....")
								cur.execute("insert into request(young_name,young_mobile,old_name,old_mobile) values(%s,%s,%s,%s)",(username,password,name,number))
							elif count<4:
								cur.execute("update youngfolk set track = %s where name = %s and mobile = %s",(count,username,password))
								cur.execute("insert into request(young_name,young_mobile,old_name,old_mobile) values(%s,%s,%s,%s)",(username,password,name,number))
								print("Request Sent Successfully....")
					con.commit()
				else:
					print("You have Exceeded the Limit of Request....")
				input()
			elif choice_for_option=="2":
				os.system('clear')
				cur.execute("select * from hired where young_name = %s and young_mobile = %s",(username,password))
				data = cur.fetchall()
				if not data:
					print("Sorry You are not hired by anyone.....")
					input()
				else:
					print("Currently You are hired by -: ")
					cur.execute("select * from oldfolk where name = %s and mobile = %s",(data[0][0],data[0][1]))
					data = cur.fetchall()
					t = PrettyTable(['Name','Age','Gender','Mobile','Address','Amount','Couple','Ratings','Reviews'])
					for i in data:
						t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
					print(t)
					print("\nWant to Leave(Y/N) -: ")
					j = input()
					if j=="Y" or j=="y":
						print("Enter Name -: ",end="")
						name = input()
						print("Enter Mobile Number -: ",end="")
						number = input()
						cur.execute("select * from oldfolk where name = %s and mobile = %s",(name,number))
						data = cur.fetchall()
						if not data:
							print("Enter Correct Details...")
						else:
							print("Write Review about person you are leaving : ",end="")
							review = input()
							print("Give Ratings out of 5 about person you are Leaving : ",end="")
							rating = int(input())
							cur.execute("delete from hired where old_name = %s and old_mobile = %s",(name,number))
							cur.execute("select * from youngfolk where name = %s and mobile = %s ",(username,password))
							countupdate = cur.fetchall()
							count = int(countupdate[0][-1])
							count-=1
							cur.execute("update youngfolk set available = %s ,track = %s where name = %s and mobile = %s",("Y",count,username,password))
							cur.execute("update oldfolk set available = %s,ratings = %s,review = %s where name = %s and mobile = %s",("Y",rating,review,name,number))
							print("You are Successfully Removed from service.....")
					input()
					con.commit()
			else:
				return

	def showyoungfolks(self):
		ch = "0"
		while ch!="4":
			os.system('clear')
			print("1. Show all Young Folks...\n2. Show Available Young Folks...\n3. Show Young Folks Taking care of Old Folks...\n4. Go Back to Main Menu...\n\nSelect your Option : ",end="")
			ch = input()
			if ch=="1":
				os.system('clear')
				cur.execute("select * from youngfolk")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Available','Hired By'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			elif ch=="2":
				os.system('clear')
				cur.execute("select * from youngfolk where available = %s","Y")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Available','Hired By'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			elif ch=="3":
				os.system('clear')
				cur.execute("select * from youngfolk where available = %s","N")
				data = cur.fetchall()
				t = PrettyTable(['Name','Age','Gender','Mobile','Address','Ratings','Reviews','Qualities','Available','Hired By'])
				for i in data:
					t.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
				print(t)
				print("\n\nPress Enter To go Back.....",end="")
				input()
			else:
				return


choice = '0'
while choice!='4':
	os.system('clear')
	print("WELCOME TO CAREALL APPLICATION.\n--------------------------------\n")
	print("1. Sign Up \n2. Sign In \n3. Admin Sign In \n4. Exit..",end="")
	print("\n\nEnter Your Choice -: ",end="")
	choice = input()
	if choice=='1':
		os.system('clear')
		choice_for_signup = '0'
		while choice_for_signup!='3':
			os.system('clear')
			print("Register Yourself here......\n")
			print("1. Need Care....\n2. Want to Care...\n3. Back to Main Menu...\n\nSelect Your Option -: ",end="")
			choice_for_signup = input()
			if choice_for_signup=='1':
				old_folk_obj = oldfolk() 
				old_folk_obj.oldfolksignup()
				input()
			elif choice_for_signup=='2':
				young_folk_obj = youngfolk()
				young_folk_obj.youngfolksignup()
				input()
			elif choice_for_signup!='3':
				print("\nINVALID INPUT...\nEnter any key to Continue...",end="")
				input()
	elif choice=='2':
		os.system('clear')
		choice_for_signin = '0'
		while choice_for_signin!='3':
			os.system('clear')
			print("Log in.....\n")
			print("1. Need Care....\n2. Want to Care...\n3. Back to Main Menu...\n\nSelect Your Option -: ",end="")
			choice_for_signin = input()
			if choice_for_signin=='1':
				old_folk_obj = oldfolk()
				old_folk_obj.oldfolksignin()
				input()
			elif choice_for_signin=='2':
				young_folk_obj = youngfolk()
				young_folk_obj.youngfolksignin()
				input()
			elif choice_for_signin!='3':
				print("\nINVALID INPUT...\nEnter any key to Continue...",end="")
				input()
	elif choice=='3':
		os.system('clear')
		print("Enter Admin Password : ",end="")
		adminpassword = input()
		if adminpassword=="12345":
			choice_for_admin = '0'
			while choice_for_admin!='3':
				os.system('clear')
				print("Admin..........\n")
				print("1. Old Folks...\n2. Young Folks...\n3. Go Back to Main Menu...\n\nSelect your Option -:",end="")
				choice_for_admin = input()
				if choice_for_admin=='1':
					old_folk_obj = oldfolk()
					old_folk_obj.showoldfolks()
					
				elif choice_for_admin=='2':
					young_folk_obj = youngfolk()
					young_folk_obj.showyoungfolks()
					
				elif choice_for_admin!='3':
					print("\nINVALID INPUT...\nEnter any key to Continue...",end="")
					input()
