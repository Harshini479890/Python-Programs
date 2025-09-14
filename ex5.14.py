'''Q13. InvalidTemperatureError
Create a custom exception InvalidTemperatureError.
Scenario:
 A weather app accepts temperature in Celsius.
 If the temperature is below -100°C or above 100°C, raise the exception with a
warning message.'''
class InvalidTemperatureError(Exception):
    def __init__(self):
        super().__init__("Temperature is tremendous.")
temp=int(input("Enter the temperature in celsius "))
try:
    if temp>100 or temp<-100:
        raise InvalidTemperatureError
    else:
        print("Temparature is good to survive.")
except InvalidTemperatureError as i:
    print(i)
