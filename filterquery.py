Employees_data = [{"id":"1", "name":"siva","department":"Development", "salary":"12000"},
     {"id":"2", "name":"saran","department":"Tester", "salary":"11000"},
     {"id":"3", "name":"gokul","department":"Team Lead", "salary":"13000"},
     {"id":"4", "name":"gopi","department":"IT", "salary":"12250"},
     {"id":"5", "name":"sudhakar","department":"IT", "salary":"14000"},
     {"id":"6", "name":"pugal","department":"IT", "salary":"16000"},
     {"id":"7", "name":"boopathy","department":"IT", "salary":"20000"},
     {"id":"8", "name":"rivi","department":"IT", "salary":"51000"},
     {"id":"9", "name":"jeeva","department":"IT", "salary":"83000"},
     {"id":"10", "name":"manoj","department":"IT", "salary":"91000"},
     {"id":"11", "name":"sridhar","department":"IT", "salary":"77000"}]


def query_data(department, top):
    filter_data = [obj for obj in Employees_data if obj["department"] == department]
    

    filter_salary = sorted(filter_data, key=lambda i: i["salary"],reverse=True)

    top_employees = filter_salary[:top]

    return top_employees


department = input("Enter the department: ")
top = int(input("Enter the top employees: "))
response = query_data(department, top)
print(response)