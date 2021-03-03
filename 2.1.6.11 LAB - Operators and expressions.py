hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
#1os tropos
minutes = (mins + dura) % 60
hours = int(hour + (mins + dura) / 60) % 24
print (hours,":",minutes, sep="")

#2os tropos
mins = mins + dura
hour = hour + mins // 60
print (hour % 24, ":" , mins % 60 , sep="")
