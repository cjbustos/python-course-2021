date = input("Write the date by following format (dd/mm):")

if len(date) == 5 and date[2] == "/":
    dia = date[:2]
    month = int(date[3:])
    months = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    )
    print("You enter", dia, "of", meses[mes - 1])
else:
    print("Wrong format!")