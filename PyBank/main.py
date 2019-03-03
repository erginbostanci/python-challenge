import os
import csv

csv_file_path_db = os.path.join('..\Resources\budget_data.csv')
with open(csv_file_path_db) as csvfile:
    
    csvreader=csv.reader(csvfile,delimiter=',')
   
    month_count=0
    revenue_total_count=0
    
    rows=[r for r in csvreader]
    
    change_revenue_total_count=int(rows[1][1])

    max_value = rows[1]
    min_value=rows[1]

    
    for i in range(1,len(rows)):
        
        month_count=month_count+1
        row=rows[i]
        revenue_total_count= int(row[1]) + revenue_total_count
        
        
        if i > 1:
            change_revenue_total_count=change_revenue_total_count + int(row[1])-int(rows[i-1][1])
        
        if int(max_value[1]) < int(row[1]):
            max_value=row
        
        if int(min_value[1]) > int(row[1]):
            min_value=row

average= int(revenue_total_count /month_count)
average_change_revenue_total_count=int(change_revenue_total_count/month_count)


print("Results")
print("****************")
print("Total time period in terms of Months: " + str(month_count))
print("Total revenue: " +"$" +str(revenue_total_count))       
print("Average revenue Change: " +"$"+ str(average))
print("Average Change in revenue Change: " +"$"+ str(average_change_revenue_total_count))
print("Greatest Increase in revenue:" + str(max_value[0])+" ($" + str(max_value[1])+")")
print("Greatest Decrease in revenue:" + str(min_value[0])+" ($" + str(min_value[1])+")")
