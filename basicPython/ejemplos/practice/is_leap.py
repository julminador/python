from json.tool import main


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

if __name__ == "__main__":
    year = int(input('Year: '))
    print(is_leap(year))