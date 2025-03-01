# Initial dictionary of employees
company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

# Print the initial dictionary
print(company_employees)

# Input employee details
department = str(input("Enter the department of the employee: "))
name = str(input("Enter the employee's name: "))
age = int(input("Enter the employee's age: "))
role = str(input("Enter the employee's role: "))

# Add new employee to the dictionary
company_employees[department][name] = {'age': age, 'role': role}

# Print updated dictionary
print(company_employees)

# Count total number of employees
count = 0
for key, value in company_employees.items():
    for key2, value2 in company_employees[key].items():
        count += 1

# Print total employee count
print(f"the total count of employees is: {count}")
