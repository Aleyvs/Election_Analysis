# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of vote cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received/.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.7.4, Visual Studio Code

## Summary

The analysis of the election shows that:

- There were 369,711 votes cast in the election.

- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham: received 23.0% of the votes. (85,213)
    - Diana DeGette: received 73.8% of the votes. (272,892)
    - Raymon Anthony Doane: received 3.1% of the votes. (11,606)
- The winner of the election was:
    - Diana DeGette: received 73.8% of the votes. (272,892)

## Challenge - Overview of Election Audit

The Colorado Board of Elections employee has asked for additional data to complete the audit:

6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine which is the county with the highest turnout.

## Election-Audit Results

In further analysis of the  election data shows: 

- There were a total of 369,711 votes cast for the congressional election.

- The counties included in the election were:
    - Jefferson
    - Denver
    - Arapahoe
- The county with the largest number of votes was:
    - Denver
- The results per county were:
    - Jefferson: received 10.5% of the votes. (38,855)
    - Denver: received 82.8% of the votes. (306,055)
    - Arapahoe: received 6.7% of the votes. (24,801)
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham: received 23.0% of the votes. (85,213)
    - Diana DeGette: received 73.8% of the votes. (272,892)
    - Raymon Anthony Doane: received 3.1% of the votes. (11,606)
- The winner of the election was:
    - Diana DeGette: received 73.8% of the votes. (272,892)

## Election-Audit Summary

To summarize, the use of the data set together with the python script is a much more efficient way to visualize the information. With the script created during this project we can easily reuse for any other elections simply by adding a different data set. 

![Import File](Resources/import_file.png)

The .csv file can be the information of any district or county and the script will show all the different candidates and counties as well as the votes each received by going through the loops and adding each different name to a list.

![For Loops to add to list](Resources/for_loop_lists.png)

Another modification we can do is to show further information on the winner. Such as, from where they received their votes; which county supports them the most, and so on.



