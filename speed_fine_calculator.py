#create a function that runs the whole code
def main():
    speed_limit = float(input("What was the speed limit? "))
    actual_speed = float(input("What was the driver's actual speed? "))
    overspeed = calculate_overspeed(speed_limit, actual_speed)
    fine = get_fined(overspeed)
    print(fine)

# create a function to calculate the overspeeding
def calculate_overspeed(speed_limit, actual_speed):
    return actual_speed - speed_limit

#create a function which assigns the fine according to overspeed
def get_fined(overspeed):
    if overspeed<=0:
        return "No fine. Drive safely"
    elif 0<overspeed<=10:
        return "Fine is $50"
    elif 10<overspeed<=20:
        return "Fine is $150"
    elif 20<overspeed<=30:
        return "Fine is $300"
    else:
        return "License suspended.$500 fine"

#provide the user with the output
main()
