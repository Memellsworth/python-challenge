import os 
import csv 



# define the path that we are reading from. with my program, I have to copy the path or i get a "file does not exist error"
budget = os.path.join(r'Resources','budget_data.csv')

#create your lists 
date = []
profit_loss = []
MOM_change = []


#set the inital variables to 0 
months = 0
total_profit = 0
current_month = 0
revenue = 0
last_month= 0  
 
#open and reas your CSs, I have to write encoding or i get a unicode error 
with open(budget, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header values
    csv_header = next(csvfile)

    for rows in csvreader:
        # add to total number of months 
        months += 1 
        #append the date list as the correct row value 
        date.append(rows[0])
        #find total profit 
        total_profit+= int(rows[1])
        #set the current month
        current_month = int(rows[1])
        #if statement to find the revenue changes. if first row is the first month then set it as next month 
        if months == 1:
             last_month = current_month
        else:
             revenue = current_month - last_month
             MOM_change.append(revenue)
             last_month = current_month
    
   
    # #average of profit losses & set to read only 2 decimal points 
    Average_PL = round(sum(MOM_change)/(months-1),2)

    # #greatest increse 
    Greatest_increase = max(MOM_change)
    #find the index of the greatest increase 
    inc_index = MOM_change.index(Greatest_increase)
    #find the date of that index 
    date_inc = date[inc_index+1]

    # #greatest decrease 
    Greatest_decrease= min(MOM_change)
    #find the index of the greatest decrease 
    dec_index = MOM_change.index(Greatest_decrease)
    #find the date of that index, add one since the index will start at 0, the result will be the month before date
    date_dec = date[dec_index+1]

#print the results 
print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total_profit))
print(f"Average Change: ${Average_PL}")
print(f"Greatest Increase in Profits: {date_inc} ($ {Greatest_increase}) ")
print(f"Greatest Decrease in Profites {date_dec} ($ {Greatest_decrease})")

output_file = os.path.join(r"Analysis","Financial_Analysis.txt")
out_text=(
       f"Financial Analysis \n"
       f"---------------------------------- \n"
       f"Total Months: {months} \n"
       f"Total: $ {total_profit} \n"
       f"Average Change: ${Average_PL} \n"
       f"Greatest Increase in Profits: {date_inc} ($ {Greatest_increase}) \n"
       f"Greatest Decrease in Profites {date_dec} ($ {Greatest_decrease}) \n")
with open(output_file,"w") as txt_file:
       txt_file.write(out_text)

       