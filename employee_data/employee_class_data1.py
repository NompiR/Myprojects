employee_details = {'h105657': {'Emp_name': {'Firstname': 'Arun', 'Lastname': 'Kumar'}, 'Salary': 50000.255, 'Dept': 'Operation', 'Date of joining': {'Day':23, 'Month': 5, 'Year':2024}}, 'h105658': {'Emp_name': {'Firstname': 'Pankaj', 'Lastname': 'Raj'}, 'Emp_salary': 50000, 'Emp_dept': 'Operation', 'Date_joining': {'Day':23, 'Month': 6, 'Year':2024}}}
employee_management = {'h105657': {'Manager': 'Ramkrishna'}, 'h105658': {'Manager': 'Naeen'}}

class Employee:
    
    def __init__(self, id):
        self.id = id
        #self.emp_details = emp_details

    def select_employee_id(self):
        for i, k in employee_details.items():
            if i == self.id:
                return k

    def return_last_name(self):
        emp_details = self. select_employee_id() 
        for key, val in emp_details.items():
            if key == 'Emp_name':
                for key1, val1 in val.items():
                    if key1 == 'Lastname':
                        return val1
                    
    def return_first_name(self):
        emp_details = self. select_employee_id()   
        for key, val in emp_details.items():
            if key == 'Emp_name':
                for key1, val1 in val.items():
                    if key1 == 'Firstname':
                        return val1  

    def return_emp_salary(self):
        emp_details = self. select_employee_id()
        for key, val in emp_details.items():
            if key == 'Salary':
                return round(float(val), 2)
            
    

input_user_emp_id = input("Enter Employee id: ")
try:

    emp_obj = Employee(input_user_emp_id)
    emp_obj.select_employee_id()
    lname = emp_obj.return_last_name()
    fname = emp_obj.return_first_name()
    salary = emp_obj.return_emp_salary()

    print("Your Full name: ", fname + ' ' + lname)
    print(salary)
except AttributeError:
    print("There is not valid employee id. ")




