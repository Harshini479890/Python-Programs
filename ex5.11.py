'''Q10. OverSpeedError
Create a custom exception OverSpeedError.
Scenario:
 A car speed monitoring system checks vehicle speed.
 If speed > 120 km/h, raise the exception with the message:
"Overspeeding detected! Slow down."'''
class OverSpeedError(Exception):
    def __init__(self):
        super().__init__("Overspeeding detected! Slow down.")
speed=int(input("Enter the speed in km per hour "))
try:
    if speed>120:
        raise OverSpeedError
    else:
        print("Speed ",speed)
except OverSpeedError as i:
    print(i)
