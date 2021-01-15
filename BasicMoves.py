from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

# Turns on camera
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("DroneCam", img)
    cv2.waitKey(1)




# Takeoff, move for 2 seconds, move right for 2 seconds, land

# me.takeoff()

# me.send_rc_control(0, 50, 0, 0)
# sleep(2)

# me.send_rc_control(50, 0, 0, 0)
# sleep(2)

# me.send_rc_control(0, 0, 0, 0)
# me.land()
