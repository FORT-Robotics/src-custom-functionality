#!/usr/bin/env python
​
def requestSetUserValue(key, value):
    if key <= 0xff:
        maskedValue = int(value) & 0xffffffff
        valueStr = "{:02x}{:02x}{:02x}{:02x}".format(
            (maskedValue) & 0xff,
            (maskedValue >> 8) & 0xff,
            (maskedValue >> 16) & 0xff,
            (maskedValue >> 24) & 0xff)
        
        messageString = "{:02x}".format(key) + valueStr + "FFFFFF\r"
        print "Set key {} to {}".format(key, value) + " :: " + messageString
​
def requestSetUserStringValue(key, string):
    if key <= 0xff:
        string = string[:18] # truncate to 18 characters max
        
        # break into 6-character chunks, with missing characters padded with spaces
        stringChunks = [string[i*6:i*6 + 6] for i in range(0,3)]
        
        segment = 0
        for chunk in stringChunks:
            messageString = "{:02x}{:02x}".format(key, segment) + chunk.encode("hex").ljust(12, '0') + "\r"
            print "Set key {} to '{}', segment {} ('{}') :: {}".format(key, string, segment, chunk, messageString)
            segment += 1
​
requestSetUserValue(99, 1)
requestSetUserStringValue(90, "This is line 1")
requestSetUserStringValue(91, "Second line")
requestSetUserStringValue(92, "Line number 3")
requestSetUserStringValue(93, "#4:Fourth line 4")