def convert(m_time):
    hour = int(m_time[0:2])
    minutes = (m_time[2:4])
    period = "AM"

    if hour == 0:
        hour = 12
    elif hour == 12:
        period = "PM"
    elif hour >= 13:
        hour -= 12
        period = "PM"

    return f"{hour}:{minutes} {period}"

while True:
    time = input("Input Military Time: ")
    if len(time) == 4 and time.isdigit():
        if int(time) <= 2400:
            if int(time[2:4]) <= 60:
                break
    print(f"{time} Is Not Valid As A Military Time!")

normal_time = convert(time)

if 900 > int(time) > 1700:
    print(f"{normal_time} Is Out of Office Time!")
else:
    print(f"{normal_time} Meeting Schedule Status: Available")

