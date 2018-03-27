time = int(input("Enter Time in Seconds "))
days = time // (24*60*60)
print("Days ", days)
remaining_seconds = time % (24*60*60)
print("Remaining Seconds ", remaining_seconds)
hours = remaining_seconds // 3600
print ("Hours", hours)
seconds_left = remaining_seconds % 3600
print ("Remaining Seconds ", seconds_left)
minutes = seconds_left // 60
print("Minutes ", minutes )
seconds_end = seconds_left % 60
seconds = seconds_end
print ("Seconds ", seconds_end)
print("Total Time Days, Hours, Minutes, Seconds", days, hours, minutes, seconds)  
