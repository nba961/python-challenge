# Modules
import os
import csv

# Input and output paths
election_data = os.path.join('Resources/election_data.csv')
election_data_output = os.path.join('Analysis/analysis.txt')

# Open and read csv
with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# Read header row
    csv_header = next(csv_reader)

    print(f'Election Results')
    print(f'------------------------------------')
    
# --------------------------------------------------------------------------------------------
# Total number of votes cast
    total_votes = sum(1 for row in csv_reader)

    print(f'Total Votes: {total_votes}')
    print(f'------------------------------------')

# ---------------------------------------------------------------------------------------------
# A complete list of candidates who received votes
    
# Dictionary to store candidate-wise votes
candidate_votes = {}

# Open the CSV file and count votes for each candidate
with open(election_data) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        candidate = row['Candidate']
        
        # Update candidate_votes dictionary
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Open and write to text file
with open(election_data_output, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t", quoting=csv.QUOTE_NONE)
    csv_writer.writerow([f"Election Results"])
    csv_writer.writerow([f"------------------------------------"])
    csv_writer.writerow([f"Total Votes: {total_votes}"])
    csv_writer.writerow([f"------------------------------------"])

# Percentage of votes and total number of votes each candidate won
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        csv_writer.writerow([f"{candidate}: {percentage:.3f}% ({votes})"])
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    csv_writer.writerow([f"------------------------------------"])

    print(f'------------------------------------')

# The winner of the election based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
    winner_votes = candidate_votes[winner]
    csv_writer.writerow([f"Winner: {winner}"])
    csv_writer.writerow([f"------------------------------------"])
    print(f"Winner: {winner}")

print(f'------------------------------------')