# david fischer 2018
# simple program to read data from the leap motion and send it to a controller (hedgehog)

import sys, thread, time
import socket
import random
import os
import sys
import Leap

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()

        inFor = False
        # gets hands
        for hand in frame.hands:
            inFor = True
            # hand type
            handType = "Left" if hand.is_left else "Right"
            normal = hand.palm_normal
            direction = hand.direction

            deg = normal.roll * Leap.RAD_TO_DEG
            posi = hand.palm_position[2]
            #print(deg)

            #sets speeds for left and right servo
            speedl = 0
            speedr = 0


            if(posi < -70):
                speedr += int((400 * (posi / 100)) * -1)
                speedl += int((400 * (posi / 100)) * -1)

            max = 120
            print(str(deg) + " " + handType)
            # if hand right (or left lol)
            if(deg > 25):
                if deg < max:
                    per = (int((deg / max) * 1000))
                else:
                    per = 1000
                per -= 200
                speedr += int(400 * (deg / 100))
                speedl -= int(400 * (deg / 100))

            # if hand rechts (or left idk)
            if(deg < -25):
                if(deg > (max * -1)):
                    per = int((deg / (max)) * 1000)
                else:
                    per = -1000
                per += 200
                speedl -= int(400 * (deg / 100))
                speedr += int(400 * (deg / 100))

            else:
                per = 0

            # caps the numbers at -800/800 - could have been done better but meh
            if(speedr > 800):
                speedr = 800
            elif(speedr < -800):
                speedr = -800

            if(speedl > 800):
                speedl = 800
            elif(speedl < -800):
                speedl= -800

            print("Sending -> R: " + str(speedr) + " L: " + str(speedl))
            os.system("python send.py " + str(speedr) + " " + str(speedl))

        if(not inFor):
            # if there is no hand send 0 0 so the bot stops moving
            os.system("python send.py 0 0")

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
