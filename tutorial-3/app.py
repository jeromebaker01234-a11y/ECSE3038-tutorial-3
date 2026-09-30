from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

@app.get("/devices")
def get_devices():
    return readings


#def average_temp(devices):
 #   total_temp = 0
 #   count = 0
  #  for device in devices:
    #    if device["online"]:
        #    total_temp += device["temp"]
         #   count += 1
   # if count > 0:
    #    return total_temp / count
   # else:
     #   return None

#print(f"Average temperature: {average_temp(readings):.1f}C")

@app.get("/devices/hottest")
def hottest():
    hottest_device = None
    for device in readings:
        if hottest_device is None or device["temp"] > hottest_device["temp"]:
            hottest_device = device
    return hottest_device



#def to_status(devices):

   # dict_device = input("Enter the name of a device in dictionary: ") 

  #  for device in devices:
   #     if device["name"] == dict_device:            
   #         if device["online"] == True:
   #             new_device= print("status is OK")
    #        else:
     #           new_device = [
           #         {"device": "fridge", "status": "offline", "celsius": 4.2,},
            #    ]
   # return new_device

#print(to_status(readings))


# def by_room(devices):

#     grouped_rooms = {}

#     for device in devices:

#         room = device["room"]
#         name = device["name"]

#         if room not in grouped_rooms:
#             grouped_rooms[room] = []

#         grouped_rooms[room].append(name)

#     return grouped_rooms

# print(by_room(readings))

@app.get("/devices/online") 
def get_online_devices():
    online_devices = []
    for device in readings:
        if device["online"] == True:
            online_devices.append(device)
    return online_devices

app.get("/devices/{name}") 
def get_device(name: str):
    for device in readings:
        if device["name"] != name:
            raise HTTPException(status_code=404, detail="Device not found")
        if device["name"] == name:
            return device
    

