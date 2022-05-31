#
# The data we need to retrieve.
# 
#  Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import csv

import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize accumulator (total_vote) counter --- initialize here so that every time file is opened total_votes is 0
total_votes = 0

# Declare a new list
candidate_options = []

# Declare new dictionary
candidate_votes = {}

# Declare winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

#To do: read and analyze the data here

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)


    # Read the header row.
    headers = next(file_reader)
    ##print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
                
        #2. Add to the total vote_count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]


        # If candidate is not in the list ...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Count candidate vote count
            candidate_votes[candidate_name] = 0

        # Increment vote each time candidate name appers in a row
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts

# Iterate through the candidate list
for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = round(float(votes)/float(total_votes)*100,1)
        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {votes} votes.  {vote_percentage}% of the votes.\n")
       
        # Determine winning vote and candidate

        # if statetement determining if vote is grater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true set winning count == to votes
            winning_count = votes
            # if true set winning percentage == vote percentage
            winning_percentage = vote_percentage
            # if true set winning candiate == to candidate name
            winning_candidate = candidate_name
        
        ## to do: Print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
    f"--------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage}%\n"
    f"--------------------------------\n")
print(winning_candidate_summary)

#3. Print the total votes
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)


    # # Print the file object.
    #  print(election_data)
# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")
# # Close the file
# outfile.close()

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file using the newline (\n) escape sequence
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")