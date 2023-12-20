import time
local_time = time.localtime()
hour=local_time.tm_hour
if(hour<12):
    print("Hi!,Hello!,Good Morning!")
elif(hour>=12 and hour<17):
    print("Hi!,Hello!,Good Afternoon!")
elif(hour>=17 and hour<20):
    print("Hi!,Hello!,Good Evening!")
else:
    print("Bye!,Tata!,Good Night!")
