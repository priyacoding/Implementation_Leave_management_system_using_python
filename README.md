# Implementation_Leave_management_system_using_python
Python script provides a command-line interface for the HR module of ABC Ltd's Employee Leave Management System. Employees and HR personnel can use this interface to manage leave-related activities.
## Key Features
### Leave Application: 
Employees can apply for different types of leave by specifying the leave type, start date, end date, and the number of days.

### Leave Balance: 
Employees can check their leave balances, including Casual Leave, Sick Leave, Privilege Leave, and Parental Leave.

### Leave Request Status: 
Employees can view the status of their leave requests.

### Leave Request Processing: 
Admin or management can approve or reject pending leave requests.

## Usage
The ABC_ltd class contains methods for leave application, checking leave balances, and viewing request status.

Employees can use the apply method to apply for leave, specifying the leave type, start date, end date, and the number of days.

To check leave balances, employees can use the leave_bal method.

To view the status of a leave request, the status method can be used.

Admin or management can process leave requests with the request_process method, including approving or rejecting requests.

## Eligibility Criteria
For Maternity Leave, the applicant should be female and the leave duration should be less than or equal to 180 days.

For Paternity Leave, the applicant should be male, and the leave duration should be less than or equal to 15 days.

## Getting Started
Instantiate the ABC_ltd class to start using the leave management system.

Employees can apply for leave using the apply method.

To check leave balances, use the leave_bal method.

Employees can view request status with the status method.

Admin or management can process leave requests using the request_process method.
