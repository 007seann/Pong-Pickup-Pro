from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

#info = lidar.get_info()
#print(info)

#health = lidar.get_health()
#print(health)
safe_distance = 400
found = False
'''for scan in (lidar.iter_scans()):
    #print('%d: Got %d measurments' % (i, len(scan)))
    for j in scan:
       #print("angel: " + f"{j[1]}\n")
       #print("distance" + f"{j[2]}\n")
        if(j[2]<safe_distance):
           #print("so close")
           if(j[1]<45 or j[1]>315):
               continue
           print("angel: " + f"{j[1]}\n")
           print("distance  " + f"{j[2]}\n")
           found = True
           break
    if (found == True):
        if(j[1]>90 and j[1]<180):
           message = "on the left"
           print(message)
        elif(j[1]>180 and j[1]<270):
           message = "on the right"
           print(message)
        break
'''

for scan in (lidar.iter_scans()):
    for j in scan:
        dis,ang = j[2], j[1]
        if (dis < safe_distance and 90<=ang<=270):
            found = True
            if (180<ang<=270): print("On the Right")
            if (90<=ang<=180): print("On the left")
        print(f"Angle: {ang}\n\nDistance: {dis}")
    if (found): break
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
