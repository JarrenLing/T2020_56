import json
import requests

## insert headers ## edit
api_headers = {
'identity': '', 
'token': ''}


## EXTRA TO TEST
def getCarparkAvailability(timestamp):
    api_url = f"https://api.data.gov.sg/v1/transport/carpark-availability?date_time={timestamp}"
    response = requests.get(api_url) #to add api's credentials => headers, use the code below
    # response = requests.get(api_url, headers=api_headers)

# [
#     {items{0{ timestamp, carpark_data{carpark_number, update_time, carpark info{0{total_lots, lots_type, lots_available
#                                                                                  }
#                                                                                }
#                                      }
                                    

#             }
#           }
#     }
# ]


    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

