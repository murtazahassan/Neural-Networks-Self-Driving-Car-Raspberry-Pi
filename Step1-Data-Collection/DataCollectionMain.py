import WebcamModule as wM
import DataCollectionModule as dcM
import JoyStickModule as jsM
import MotorModule as mM
import cv2
from time import sleep


maxThrottle = 0.25
motor = mM.Motor(2, 3, 4, 17, 22, 27)

record = 0
while True:
    joyVal = jsM.getJS()
    #print(joyVal)
    steering = joyVal['axis1']
    throttle = joyVal['o']*maxThrottle
    if joyVal['share'] == 1:
        if record ==0: print('Recording Started ...')
        record +=1
        sleep(0.300)
    if record == 1:
        img = wM.getImg(True,size=[240,120])
        dcM.saveData(img,steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    motor.move(throttle,-steering)
    cv2.waitKey(1)