import os
with open("../../../AppData/Roaming/.minecraft/logs/latest.log") as lt:
    GP = lt.readlines()

if "GpXaiver" or "@GpXavier" in GP:
    print("Works")
else:
    print("Nope")