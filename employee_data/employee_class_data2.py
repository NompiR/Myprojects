employee_details = {'h105657': {'Emp_name': {'Firstname': 'Arun', 'Lastname': 'Kumar'}, 'Salary': 50000.255, 'Dept': 'Technology', 'Date of joining': {'Day':23, 'Month': 5, 'Year':2024}, 'DOB': {'Day':21, 'Month': 11, 'Year': 1984}}, 'n105658': {'Emp_name': {'Firstname': 'Pankaj', 'Lastname': 'Raj'}, 'Salary': 21000.02, 'Dept': 'Operation', 'Date of joining': {'Day':23, 'Month': 6, 'Year':2024}, 'DOB': {'Day':2, 'Month': 11, 'Year': 1990}}}

employee_management = {'h105657': {'Manager1': 'Ramkrishna', 'Manager2': 'Priyanka'}, 'n105658': {'Manager1': 'Naeen', 'Manager2': 'Harish'}}
emp_ids = ['h105657', 'n105658']

class Employee:
    
    def __init__(self, id):
        self.id = id

    def select_employee_id(self):
        for i, k in employee_details.items():
            if i == self.id:
                return k
    def Merge_employee_id_to_management(self):
        for a, b in employee_management.items():
            if a == self.id:
                return b
            
    def return_all_emp_details(self):
        emp_details = self. select_employee_id()
        for key, val in emp_details.items():
            if key == 'Salary':
                salary = round(float(val), 2)
            if key == 'Dept':
                dept = val
            if key == 'Emp_name':
                for key1, val1 in val.items():
                    if key1 == 'Firstname':
                        firstname = val1
                    if key1 == 'Lastname':
                        lastname = val1
            if key == 'Date of joining':
                for key2, val2 in val.items():
                    if key2 == 'Day':
                        emp_join_Day = val2
                    if key2 == 'Month':
                        emp_join_month = val2
                    if key2 == 'Year':
                        emp_join_year = val2
            if key == 'DOB':
                for key3, val3 in val.items():
                    if key3 == 'Day':
                        emp_birth_Day = val3
                    if key3 == 'Month':
                        emp_birth_month = val3
                    if key3 == 'Year':
                        emp_birth_year = val3
        return (salary, dept, firstname, lastname, emp_join_Day, emp_join_month, emp_join_year, emp_birth_Day, emp_birth_month, emp_birth_year)
    
    def return_merge_emp_to_management(self):
        emp_management_details = self.Merge_employee_id_to_management()
        for key, val in emp_management_details.items():
            if key == 'Manager1':
                mone = val
            if key == 'Manager2':
                mtwo = val
        return (mone, mtwo)

    def display_emp_details(self, all_details, emp_management):
        emp_salary, emp_dept, emp_fname, emp_lname, emp_join_day, emp_join_month, emp_join_year, emp_birth_day, emp_birth_month, emp_birth_year = all_details
        emp_full_name = emp_fname +' '+ emp_lname
        
        if emp_birth_month == 1 or emp_join_month == 1:
            M = 'Jan'
        elif emp_birth_month == 2 or emp_join_month == 2:
            M = 'Feb'
        elif emp_birth_month == 3 or emp_join_month == 3:
            M = 'Mar'
        elif emp_birth_month == 4 or emp_join_month == 4:
            M = 'Apr'
        elif emp_birth_month == 5 or emp_join_month == 5:
            M = 'May'
        elif emp_birth_month == 6 or emp_join_month == 6:
            M = 'Jun'
        elif emp_birth_month == 7 or emp_join_month == 7:
            M = 'Jul'
        elif emp_birth_month == 8 or emp_join_month == 8:
            M = 'Aug'
        elif emp_birth_month == 9 or emp_join_month == 9:
            M = 'Sep'
        elif emp_birth_month == 10 or emp_join_month == 10:
            M = 'Oct'
        elif emp_birth_month == 11 or emp_join_month == 11:
            M = 'Nov'
        elif emp_birth_month == 12 or emp_join_month == 12:
            M = 'Dec'
        else:
            M = ' '

        emp_m1, emp_m2 = emp_management
        print("-------------------------------------------------")
        print("\t\tEmployee Datails")
        print("-------------------------------------------------")
        print("Employee\'s full name: ", emp_full_name)
        print("Employee\'s department : ", emp_dept)
        print("Employee\'s Joining date: ", M, emp_join_year)
        print("Employee\'s DOB: ", M,'-',emp_birth_month,'-',emp_birth_year)
        print("Employee\'s Manager1 :", emp_m1)
        print("Employee\'s Manager2 :", emp_m2)
        print("Employee\'s Salary :", emp_salary)
        print("-------------------------------------------------")
            
user_input_emp_id = input("Enter Employee id: ")
while user_input_emp_id not in emp_ids:
    print("Employee\'s is not valid, Try again..")
    user_input_emp_id = input("Enter Employee id: ")
    
    if user_input_emp_id in ['h105657', 'n105658']:
        emp_obj = Employee(user_input_emp_id)
        emp_obj.select_employee_id()
        emp_salary, emp_dept, emp_fname, emp_lname, emp_join_day, emp_join_month, emp_join_year, emp_birth_day, emp_birth_month, emp_birth_year = emp_obj.return_all_emp_details()
        all_details = (emp_salary, emp_dept, emp_fname, emp_lname, emp_join_day, emp_join_month, emp_join_year, emp_birth_day, emp_birth_month, emp_birth_year)
        emp_m1, emp_m2 = emp_obj.return_merge_emp_to_management()
        emp_management = (emp_m1, emp_m2)
        emp_obj.display_emp_details(all_details, emp_management)
        break

