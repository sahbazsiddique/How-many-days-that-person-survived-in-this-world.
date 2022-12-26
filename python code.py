def count_Leap_Years(day):
    years = day.year
    if (day.month <= 2):  
        years -= 1  
    return int(years / 4) - int(years / 100) + int(years / 400)  

def get_difference(date_1, date_2):   
    n_1 = date_1.year * 365 + date_1.day
    for K in range(0, date_1.month - 1):  
        n_1 += month_Days[K]

    n_1 += count_Leap_Years(date_1)
    n_2 = date_2.year * 365 + date_2.day

    for K in range(0, date_2.month - 1):  
        n_2 += month_Days[K]  
    n_2 += count_Leap_Years(date_2) 
    return (n_2 - n_1)

class date_n:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
month_Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

print("\nIt the DATE CALCULATOR in which you can calculate the no. of days between two given dates.\n\n")

a=int(input("Enter 1st date(DD): "))
b=int(input("Enter 1st month(MM): "))
c=int(input("Enter 1st year(YYYY): "))
d=int(input("Enter 2nd date(DD): "))
e=int(input("Enter 2nd month(MM): "))
f=int(input("Enter 2nd year(YYYY): "))

date_1 = date_n(a,b,c)  
date_2 = date_n(d,e,f)

print(("Number of Days between the given Dates are: ", get_difference(date_1, date_2), "days."))

