contest_date = input()
contest_dict = {}
while contest_date != "end of contests":
    contest, password = contest_date.split(":")
    contest_dict[contest] = password
    contest_date = input()

submission_data = input()
users_dict = {}
while submission_data != "end of submissions":
    (contest, password, user, points) = submission_data.split("=>")

    if contest in contest_dict.keys() and contest_dict[contest] == password:
        if user not in users_dict:
            users_dict[user] = {}

        if contest not in users_dict[user]:
            users_dict[user][contest] = int(points)
        else:
            if users_dict[user][contest] < int(points):
                users_dict[user][contest] = int(points)
    submission_data = input()

best_user = ''
best_points = 0

for user in users_dict.keys():
    total_points = sum(users_dict[user].values())
    if total_points > best_points:
        best_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")

for user in sorted(users_dict.keys()):
    print(f"{user}")
    for contest, points in sorted(users_dict[user].items(), key=lambda cp: -cp[1]):
        print(f"#  {contest} -> {points}")


