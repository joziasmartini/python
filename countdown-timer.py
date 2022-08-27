import time

# Function that makes the contdown
def contdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
  print('Time is up!')

# Get the time from the user
t = input("Enter the time in seconds: ")

# Call the function
contdown(int(t))
