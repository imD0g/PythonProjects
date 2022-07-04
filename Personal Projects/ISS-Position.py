# Api call to GET http://aviation-edge.com/v2/public/satelliteDetails?key=[API_KEY]&code=25544 and print the data
import requests
import json
import time
def get_iss_location():
      try:
            while True:
                  url = 'http://api.open-notify.org/iss-now.json'
                  response = requests.get(url)
                  data = response.json()
                  print(f"The current latitude of the ISS is: ",data['iss_position'] ['latitude'])
                  print(f"The current longitude of the ISS is: ",data['iss_position'] ['longitude'])
                  print("If you want to stop this program, press Ctrl+C")
                  print("\n")
                  time.sleep(5)
      except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            exit()

get_iss_location()

