import datetime  # we import datetime

data = datetime.date(2025, 1, 2)  # here we define date by using datetime
today = datetime.date.today()

time = datetime.time(12, 30, 0) #here we define time by using datetime
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %D-%M-%Y") #ये date/time को अपने हिसाब से format करने के लिए use होता है

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1) #yaha variable define kiya "target_datetime"
current_datetime = datetime.datetime.now()  # yaha " current_datetime"  define kiya

if target_datetime < current_datetime:   # condition
    print("Target date has passed")   
else:
    print("Target date has NOT passed")


print(now)