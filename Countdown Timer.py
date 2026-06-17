
import time
total_seconds = int(input("Enter time in seconds: "))
for seconds in range(total_seconds, 0, -1):
    min = seconds //60
    sec =seconds % 60

    print(f"{min:02}:{sec:02}")

    time.sleep(1)

print("Time's up!")
