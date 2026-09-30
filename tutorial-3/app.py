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

@app.post("/devices")
def create_device(device: dict):
    readings.append(device)
    return device

def average_temp(devices):
    online_temps = [device["temp"] for device in devices if device["online"]]
    if not online_temps:
        return None
    return sum(online_temps) / len(online_temps)

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

@app.get("/devices/{name}") 
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.get("/stats")
def get_stats():
    avg_temp = average_temp(readings)
    return {"average_temp": avg_temp}

@app.get("/rooms/{room}/devices")
def get_devices_by_room(room: str):
    if room not in [device["room"] for device in readings]:
        raise HTTPException(status_code=404, detail=f"No room called {room}")
    devices_in_room = [device for device in readings if device["room"] == room]
    return devices_in_room
