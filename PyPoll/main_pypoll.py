import os 
import csv 

#file to open for the CSV, this is the only way I can get python to navigate to the folder. 
votes= os.path.join(r"Resources","election_data.csv")
# file destination for the txt file. This is the only way I can get python to navigate to folder.
output_file = os.path.join(r"Analysis","Election_Results.txt")
#set your initial variables to 0
total_votes = 0 
max_votes = 0 
winner = ""
#create your dictionaries 
candidates_list = {}


   
with open(votes,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)


    #loop through the rows 
    for rows in csvreader:
        

        #count the total rows 
        total_votes += 1 
        #set the candidate variable to read row two 
        candidate = rows[2]
        #if statement to add the candidate to the {} & count how many votes 
        if candidate in candidates_list:
         #if they are already in the dictionary add another value 
         candidates_list[candidate] += 1
        else:
         #if the candidate is not already in the candidate_list then add them in and set their initial count to 1 
         candidates_list[candidate] = 1 
         #figure out the max votes 
        if candidates_list[candidate]>max_votes:
            max_votes =candidates_list[candidate]
            winner = candidate
            #set the output for text / print 
            output_winner = (
                             f'---------------------------------- \n'
                             f'Winner: {winner} \n'
                             f'---------------------------------- \n')
        
    
        
#open your CSV 
with open(output_file, "w") as txt_file:
     #print the iniatl lines 
     out_text=(
           f" Election Results \n"
           f"---------------------------------- \n"
           f" Total Votes: {total_votes} \n"
           f"---------------------------------- \n")
     print(f'{out_text}')
     txt_file.write(out_text)
     #loop through cnadidate list to find the percentagest and total votes for the candidates 
     for candidate in candidates_list:
        vote_count = candidates_list[candidate]
        Candidate_percent = round(float(vote_count)/float(total_votes)*100,3)
        output_votes = (
             f'{candidate}: {Candidate_percent}% ({vote_count})\n')
        txt_file.write(output_votes)
        print(output_votes)
     txt_file.write(output_winner)
     print(f'{output_winner}')

    
   



    
