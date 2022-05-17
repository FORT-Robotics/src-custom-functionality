#!/usr/bin/env python
"""Python 2 module for setting customer values on an FORT Robotics Safety Remote Contorller (SRC)."""
​
def set_user_value(key, value):
    """Set a specified key to a specified integer value.
    
    Args:
        key (int): The key to set.
        value (int): The new value of the key.
    """
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
def set_user_str_value(key, string):
    """Set a specified key to a specified string value.
    
    Args:
        key (int): The key to set.
        value (int): The new value of the key.
    """
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
set_user_value(99, 1)
set_user_str_value(90, "This is line 1")
set_user_str_value(91, "Second line")
set_user_str_value(92, "Line number 3")
set_user_str_value(93, "#4:Fourth line 4")