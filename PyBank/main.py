# Modules
import os
import csv

# Input paths
budget_data = os.path.join('Resources/budget_data.csv')
budget_data_output = os.path.join('Analysis/analysis.txt')

# Open and read csv
with open(budget_data, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')

# Read header row
    csv_header = next(csv_reader)

    print(f'Financial Analysis')
    print(f'------------------------------------')
# --------------------------------------------------------------------------------------------
# Total number of months
    total_months = sum(1 for row in csv_reader)
    print(f'Total Months: {total_months}')

# ---------------------------------------------------------------------------------------------
# Net total amount of "Profit/Losses" over the entire period
    
# Open csv file
with open(budget_data) as file:
    next(file)

# Calculates the total of all values in the 'Profit/Losses' column
    total = sum(int(r[1]) for r in csv.reader(file))

    print(f'Total: ${total}')

# ---------------------------------------------------------------------------------------------
# Changes in "Profit/Losses" over the entire period, and the average of those changes
    
# Initialize variables
total_changes = 0
num_changes = 0
max_increase_date = ""
max_increase_amount = 0
max_decrease_date = ""
max_decrease_amount = 0

# Open csv file
with open(budget_data) as file:
 csv_reader = csv.DictReader(file)

# Read the first row to get the initial value
 first_row = next(csv_reader)
 prev_profit_loss = int(first_row['Profit/Losses'])
 
# Iterate through the remaining rows to calculate changes
 for row in csv_reader:
        current_date = row['Date']
        current_profit_loss = int(row['Profit/Losses'])
        change = current_profit_loss - prev_profit_loss
        total_changes += change
        num_changes += 1

# Check if the current change is greater/less than the current maximum increase/decrease
        if change > max_increase_amount:
           max_increase_amount = change
           max_increase_date = current_date

        if change < max_decrease_amount:
           max_decrease_amount = change
           max_decrease_date = current_date
        
        prev_profit_loss = current_profit_loss

# Calculate the average change and round-up
average_change = total_changes / num_changes if num_changes > 0 else 0
round_up = round(average_change * 100) / 100

# Open and write to text file
with open(budget_data_output, 'w', newline='') as csv_file:
    csv.writer = csv.writer(csv_file, delimiter="\t", quoting=csv.QUOTE_NONE)
    csv.writer.writerow([f'Financial Analysis'])
    csv.writer.writerow([f'------------------------------------'])
    csv.writer.writerow([f'Total Months: {total_months}'])
    csv.writer.writerow([f'Total: ${total}'])
    csv.writer.writerow([f'Average Change: ${round_up}'])
    csv.writer.writerow([f'Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})'])
    csv.writer.writerow([f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount})'])

print(f'Average Change: ${round_up}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase_amount})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount})')
