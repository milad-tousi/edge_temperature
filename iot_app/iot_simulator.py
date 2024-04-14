import time
import random
import requests

# This IP and port should match the Kubernetes service you will define later
URL = 'http://temperature-processor-service:8000/data'

while True:
    temperature = random.randint(20, 100)
    try:
        requests.post(URL, json={'temperature': temperature})
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")
    time.sleep(5)
