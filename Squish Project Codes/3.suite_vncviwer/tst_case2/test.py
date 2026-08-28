# -*- coding: utf-8 -*-

import names


def main():
    attachToApplication("VncViewer")
    snooze(1)
    
    mouseClick(waitForObject(names.viewer_oriscreen))
    snooze(1)
    
    mouseClick(waitForImage("run.png", {'tolerant': True, 'threshold': 99.0}))
    snooze(5)
    
    mouseClick(waitForImage("alramOff.png", {'tolerant': True, 'threshold': 99.0}))
    
    # stand-by
    snooze(7)
    
    mouseClick(waitForImage("alramOn.png", {'tolerant': True, 'threshold': 99.0}))
    snooze(4)
    
    mouseClick(waitForImage("win1call.png", {'tolerant': True, 'threshold': 99.0}))
    snooze(1)
    
    test.imagePresent("win1call_result.png", {'tolerant': True, 'threshold': 99.0})