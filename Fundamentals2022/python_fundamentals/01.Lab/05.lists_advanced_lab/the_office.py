employees = input().split(' ')
happiness_factor = int(input())
employees = list(map(int, employees))

happy_employees = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
