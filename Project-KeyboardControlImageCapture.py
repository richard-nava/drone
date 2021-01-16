from djitellopy import tello
import KeyPressModule as kp
import cv2
import time

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()


# to check key presses
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 60

    if kp.getKey("LEFT"):lr = -speed
    elif kp.getKey("RIGHT"):lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"):fb = -speed

    if kp.getKey("w"):ud = speed
    elif kp.getKey("s"):ud = -speed

    if kp.getKey("a"):yv = -speed
    elif kp.getKey("d"):yv = speed

    if kp.getKey("y"):
        me.land()
        time.sleep(3)
    if kp.getKey("t"): me.takeoff()

    if kp.getKey("q"): me.emergency()

    if kp.getKey("v"): me.end()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    if kp.getKey("j"): me.flip_left()
    if kp.getKey("l"): me.flip_right()

    return [lr, fb, ud, yv]




while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("DroneCam", img)
    cv2.waitKey(1)

