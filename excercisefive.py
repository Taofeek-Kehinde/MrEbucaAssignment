
#(Fill in the Missing Code?) Replace the ***s in the seconds_since_midnight func-
#tion so that it returns the number of seconds since midnight. The function should receive
#three integers representing the current time of day. Assume that the hour is a value from
#0 (midnight) through 23 (11 PM) and that the minute and second are values from 0 to 59.
#Test your function with actual times. For example, if you call the function for 1:30:45 PM
#by passing 13, 30 and 45, the function should return 48645.

def seconds_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600      # 1 hour = 3600 seconds
    minute_in_seconds = minute * 60    # 1 minute = 60 seconds
    return hour_in_seconds + minute_in_seconds + second

# it is 1:30:45 PM = 13:30:45
print(seconds_since_midnight(13, 30, 45))  # 48645
