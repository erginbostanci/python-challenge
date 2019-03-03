
import os
import csv

file_db = input("Enter the name  of the file you want to analyze ")
votes = 0
candidate_db_ = ""
candidate_db__votes = {}
candidate_db__percent ={}
win_vt = 0
win_db = ""

file_db_path = os.path.join("raw_data", file_db)
with open(file_db_path,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        votes = votes + 1
        candidate_db_ = row[2]
        if candidate_db_ in candidate_db__votes:
            candidate_db__votes[candidate_db_] = candidate_db__votes[candidate_db_] + 1
        else:
            candidate_db__votes[candidate_db_] = 1
            
for person, vote_count in candidate_db__votes.items():
    candidate_db__percent[person] = '{0:.0%}'.format(vote_count / votes)
    if vote_count > win_vt:
        win_vt = vote_count
        win_db = person

leave_space = "-------------------------"

# print out results
print("Election Results")
print(leave_space)
print(f"Total Votes: {votes}")
print(leave_space)
for person, vote_count in candidate_db__votes.items():
    print(f"{person}: {candidate_db__percent[person]} ({vote_count})")
print(leave_space)
print(f"win_db: {win_db}")
print(leave_space)

store_results_as_txt = file_db.strip(".csv") + "_results.txt"
file_db_path = os.path.join(".", store_results_as_txt)
with open(file_db_path,'w') as text:
    text.write(leave_space + "\n")
    text.write(f"Total Votes: {votes}" + "\n")
    text.write(leave_space + "\n")
    for person, vote_count in candidate_db__votes.items():
        text.write(f"{person}: {candidate_db__percent[person]} ({vote_count})" + "\n")
    text.write(leave_space + "\n")
    text.write(f"win_db: {win_db}" + "\n")
    text.write(leave_space + "\n")
