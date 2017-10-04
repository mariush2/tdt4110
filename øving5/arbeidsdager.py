start_date = [1900, 0]
weekdays = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]

def day_newyear(year):
    global start_date, weekdays
    new_year = []
    before = False

    new_year.append(year)

    amount = abs(start_date[0] - year)
    day = start_date[1]

    if(start_date[0] - year > 0):
        before = True

    for i in range(0, amount):
        if(before):
            #Året er før 1900
            year += 1
            if(is_leap_year(year)):
                day -= 2
            else:
                day -= 1
        else:
            #Året er etter 1900
            year -= 1
            if(is_leap_year(year)):
                day += 2
            else:
                day += 1

    day_number = day % 7
    new_year.append(weekdays[day_number])
    print(new_year)
    return day_number


def workdays_in_year(year):
    global start_date
    new_year = []
    workdays = 0
    amount = 365
    new_year.append(year)

    if(is_leap_year(year)):
        amount = 366

    day = day_newyear(year)

    for i in range(0, amount):
        if(is_workday(day)):
            workdays += 1
        day += 1

    workdays = "Workdays: " + str(workdays)
    new_year.append(workdays)
    print(new_year)


def is_workday(day):
    if((day % 7) < 5):
        return True
    return False


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

# for i in range(1900, 1920):
#   day_newyear(i)
#
workdays_in_year(1912)
