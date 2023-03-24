from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

#info = lidar.get_info()
#print(info)

#health = lidar.get_health()
#print(health)
safe_distance = 200
found = False
for scan in (lidar.iter_scans(max_buf_meas=100)):
    #print('%d: Got %d measurments' % (i, len(scan)))
    for j in scan:
       #print("angel: " + f"{j[1]}\n")
       #print("distance" + f"{j[2]}\n")
        if(j[2]<safe_distance):
           #print("so close")
           print("angel: " + f"{j[1]}\n")
           print("distance" + f"{j[2]}\n")
           found = True
           break
    if (found == True):
        break
     
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
