log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)

#We are telling the code to check the dates. If the day is monday, We would like the code to log that for us.