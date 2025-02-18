# Leaphog
Compact program to send data from the Leap Motion Sensor to the Hedgehog (or any other controller that can run python)

## Setup
This script requires Python2.7 and the [Leap Motion Drivers](https://www.leapmotion.com/setup/desktop/).

### Setup Mac
run: `python2.7 -c "import distutils.sysconfig as c; print(c.PREFIX)"`
append `/lib/libpython2.7.dylib` to the path

run: 
```
install_name_tool -change /Library/Frameworks/Python.framework/Versions/2.7/Python \
***python2.7path***/lib/libpython2.7.dylib \
LeapPython.so
```

### Run
on client: `python2.7 main.py`
on server: `python3 server.py`

:)

1. Make sure the ports in both server.py and send.py match up and set the correct ip in send.py
2. Start server.py on the receiving end (hedgehog).
3. Start main.py on your Leap Motion Device and make sure the ports and IP match up.
The Leap Motion only reads data if the window the script is running in is in focus.

## Leap Motion fixes
Sometimes the Leap Motion isn't able to connect to the python script, so here is a list of all the quick fixes:
 - Stop the script and start it again until it connects
 - Stop the Leap Motion driver and restart the script
 - While the program is still running plug out the Leap Motion and plug it back in
 - Start the Leap Motion Visualizer from the driver menu
 - If nothing else works, restart the computer and make sure the leap drivers don't start up again.
