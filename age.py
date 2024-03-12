from datetime import datetime as dt

# take user input and return datetime obj
def enterDate():
    while True:
        try:
            dateInput = input("Enter your date (dd/mm/yyyy): ")
            date = dt.strptime(dateInput, "%d/%m/%Y")
            break
        except:
            print("Please make sure your date is in the correct format.")
    return date

# return absolute difference between the years of d1 and d2
# take the difference in days and divide by 365 (we want age, not year gap)
def yearGap(d1, d2):
    return abs(round((d1 - d2).days / 365))


if __name__ == "__main__":
    userDate = enterDate()
    print(yearGap(userDate, dt.today()))