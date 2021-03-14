#import text file of sales info
log_file = open("um-server-01.txt")

#define function for the sales reports
def sales_reports(log_file):
    #iterate through the lines in the sales info file
    for line in log_file:
        #take out the whitespace from the right of every line and save it in the variable of line
        line = line.rstrip()
        #select the first 3 characters and save it in the variable of day
        day = line[0:3]
        #create logic to select a specific string from the day variable
        #this is incorrectly set to "Tue", which we will change to "Mon"
        if day == "Mon":
            #if the string is identified within the day variable, we will print the line
            print(line)

#calling the sales reports fuctions
sales_reports(log_file)
