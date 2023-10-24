import datetime
class ABC_ltd:
  def __init__(self):
    self.emp_list= {"A1234":["ARTHY","CONFIRMED","FEMALE",12,12,18,180],
    "B1234":["BABU","UNCONFIRMED","MALE",12,12,0,15], "C1234":["CHITRA","CONFIRMED","FEMALE",12,12,18,180],
                    "D1234":["DIVYA","UNCONFIRMED",12,12,0,180]}
    self.leave_req = {}

  def status(self,data):
    if data in self.leave_req:
      print(f'''Type of Leave: {self.leave_req[data][1]}\nFrom date:{self.leave_req[data][3]}\nTo date:{self.leave_req[data][4]}\nStatus:{self.leave_req[data][5]}''')
    else:
      print("Invalid Reference ID")

  def request_process(self):
    for i in self.leave_req:
      if self.leave_req[i][5] == "pending":
        decision = input(f"Enter approve to approve the leave requested and reject to deny the request for {i}")
        if decision == "approve":
          self.leave_req[i][5] = "approve"
          print(f"The Request ID {i} is Approved")
          print(self.leave_req[i])

        elif decision == "reject":
          self.leave_req[i][5] = "reject"
          print(f"The Request ID {i} is Rejected")
          if self.leave_req[i][1] == "Casual leave":
            self.emp_list[self.leave_req[i][0]][3] += self.leave_req[i][2]
          elif self.leave_req[i][1] == "Sick leave":
            self.emp_list[self.leave_req[i][0]][4] += self.leave_req[i][2]
          elif self.leave_req[i][1] == "Privilege leave":
            self.emp_list[self.leave_req[i][0]][5] += self.leave_req[i][2]
          elif self.leave_req[i][1] == "Maternity leave" or  self.leave_req[i][1] == "Paternity leave":
            self.emp_list[self.leave_req[i][0]][6] += self.leave_req[i][2]
        else:
          print("Invalid decision")

  def leave_bal(self,data):
    print(f"""The Summary of leave balances is as follows:\nCasual Leave :{self.emp_list[data][3]}\nSick Leave :{self.emp_list[data][4]}\nPrivilege Leave : {self.emp_list[data][5]}\nParental Leave : {self.emp_list[data][6]}""")

  def apply(self,data):
    if data in self.emp_list:

      sel = int(input("""Enter the Leave Type as follows:
      1 Casual Leave
      2 Sick Leave
      3 Privilege Leave
      4 Maternity Leave
      5 Paternity Leave"""))

      start_date = input("Enter the start date of leave")
      end_date = input("Enter the end date of leave")
      nofdays = int(input("Enter the no of days"))

      if sel == 1:
        if nofdays >= 3 :
          print("For a month your eligible only for 2 casual leaves consecutively")
        else:
          if self.emp_list[data][3] >= nofdays:
            self.sr = "SRLV202300"+ str(len(self.leave_req))
            self.leave_req[self.sr] = list([data,"Casual leave",nofdays,start_date,end_date,"pending"])
            print(f"Request successfully submitted and the reference id is {self.sr}")
            self.emp_list[data][3] -= nofdays
          else:
            print("you donot have sufficient leave balance")

      elif sel == 2:
        self.sr = "SRLV202300"+ str(len(self.leave_req))
        self.leave_req[self.sr] = list([data,"Sick leave",nofdays,start_date,end_date,"pending"])
        print(f"Request successfully submitted and the reference id is {self.sr}")
        self.emp_list[data][4] -= nofdays

      elif sel == 3:
        if self.emp_list[data][1] == "CONFIRMED":
          if self.emp_list[data][5] >= nofdays:
            self.sr = "SRLV202300"+ str(len(self.leave_req))
            self.leave_req[self.sr] = list([data,"Privilege leave",nofdays,start_date,end_date,"pending"])
            print(f"Request successfully submitted and the reference id is {self.sr}")
            self.emp_list[data][5] -= nofdays
          else:
            print("you donot have sufficient leave balance")
        else:
          print("You are eligible for privilege leave")

      elif sel ==4:
        if self.emp_list[data][2] == "FEMALE" and nofdays<=180:
          self.sr = "SRLV202300"+ str(len(self.leave_req))
          self.leave_req[self.sr] = list([data,"Maternity leave",nofdays,start_date,end_date,"pending"])
          print(f"Request successfully submitted and the reference id is {self.sr}")
          self.emp_list[data][6] -= nofdays
        else:
          print("Eligible criteria for maternity leave is not satisfied")

      elif sel ==5:
          if self.emp_list[data][2] == "MALE" and nofdays<=15:
            self.sr = "SRLV202300"+ str(len(self.leave_req))
            self.leave_req[self.sr] = list([data,"Paternity leave",nofdays,start_date,end_date,"pending"])
            print(f"Request successfully submitted and the reference id is {self.sr}")
            self.emp_list[data][6] -= nofdays
          else:
              print("Eligible criteria for paternity leave is not satisfied")
      else:
          print("Invalid selection")

a = ABC_ltd()


while True:
  print("""Welcome to the HR Module of ABC_ltd
        1 Apply for a Leave
        2 Status of Request
        3 Request processing
        4 Outstanding Leave balances
        5 Exit""")

  selection = int(input("Enter your Choice"))

  if selection == 1:
    empid = input("Enter your employee id: ")
    a.apply(empid.upper())
  elif selection == 2:
    refid = input("Enter your reference id: ")
    a.status(refid.upper())
  elif selection == 3:
    a.request_process()
  elif selection == 4:
    empid = input("Enter your employee id: ")
    a.leave_bal(empid.upper())
  elif selection == 5:
    break
  else:
    print("Invalid selection")
