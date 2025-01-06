import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Print the timer, overwriting the previous output
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

duration = int(input("Enter the countdown time in seconds: "))
countdown_timer(duration)