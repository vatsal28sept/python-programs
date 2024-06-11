# Exponential Backoff
# Implement An Exponential Backoff Strategy That Doubles The Wait Time Between Retris,Starting From 1 Second,But Stops After 5 Retries
import time
wait_time = 1
max_retries = 5 
attempts = 0
while attempts<max_retries:
    print("Attempts ", attempts+1 ,"-Wait Time ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
