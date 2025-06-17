import sys
import re


def read_birthdays(filename):
    birthday = [];
    with open(filename,'r') as file:
        for line in file:
            name , date = line.strip().split(',')
            birthday.append((name,date))
        return birthday


def find_people_by_date(birthdays, target_date):
    result = [];
    for name , date in  birthdays:
        if date == target_date:
            result.append(name)
    return result


def main():
    fileName = 'textfile.txt'
    birthdays = read_birthdays(fileName);
    targetDate = input("Enter a Date (YYYY-MM-DD)")
    matched_Name = find_people_by_date(birthdays, targetDate);
    if matched_Name:
        print('People borned on')
    for name in matched_Name:
        print('--', name)
    else :
        print('No One was on that date.')
if __name__ == "__main__":
    main()



    
