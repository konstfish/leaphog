import sys, thread, time
import socket
import random
import os
import sys
sys.path.append('llib/')
import Leap

def transmission(r, l):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ('192.168.1.109', 1337)
    client_socket.connect(server_addr)
    client_socket.send(str(r) + "." + str(l))
    print("sent" + str(r) + "." + str(l))

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
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        inFor = False
        for hand in frame.hands:
            inFor = True
            handType = "Left" if hand.is_left else "Right"

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            #print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #    direction.yaw * Leap.RAD_TO_DEG)


            #print(hand.palm_position)

            deg = normal.roll * Leap.RAD_TO_DEG
            posi = hand.palm_position[2]
            #print(deg)

            speedl = 0
            speedr = 0

            #if(posi > 70):
            #    #print("back")
            #    speedr += int((400 * (posi / 100)) * -1)
            #    speedl += int((400 * (posi / 100)) * -1)

            if(posi < -70):
                #print("vor")
                speedr += int((400 * (posi / 100)) * -1)
                speedl += int((400 * (posi / 100)) * -1)

            max = 120
            print(str(deg) + " " + handType)
            if(deg > 25):
                #print(handType + " Links Code " + str(deg))
                if deg < max:
                    per = (int((deg / max) * 1000))
                else:
                    per = 1000
                per -= 200
                speedr += int(400 * (deg / 100))
                speedl -= int(400 * (deg / 100))

            if(deg < -25):
                #print(handType + " Rechts Code " + str(deg))
                if(deg > (max * -1)):
                    per = int((deg / (max)) * 1000)
                else:
                    per = -1000
                per += 200
                speedl -= int(400 * (deg / 100))
                speedr += int(400 * (deg / 100))

            else:
                per = 0
            #print(per)

            if(speedr > 800):
                speedr = 800
            elif(speedr < -800):
                speedr = -800

            if(speedl > 800):
                speedl = 800
            elif(speedl < -800):
                speedl= 800

            print("Sending -> R: " + str(speedr) + " L: " + str(speedl))
            os.system("python send.py " + str(speedr) + " " + str(speedl))

        if(not inFor):
            os.system("python send.py 0 0")
            #try:
        #        transmission(i, i)
        #        time.sleep(0.05)
        #    except:
        #        print("[H] Connection Lost...")
        #        time.sleep(2)

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
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
