"""The objective of this exercise is to convert geographical coordinates 
along with orientation to the relative position and orientation in a 
robot's coordinate system.

This conversion is useful for various robotic applications, 
including localization and navigation.

Note:
    Assume a left-hand coordinate system with the Z-axis pointing 
    towards the sky. You can also assume that the locations are 
    reasonably close to each other. We are only interested in the 
    heading (yaw, given in degrees) and not the full orientation 
    information.
"""


if __name__ == "__main__":
    coordinates = [
        {
            "latitude": 47.665470,
            "longitude": 9.447470,
            "heading": 0,
        },
        {
            "latitude": 47.665123,
            "longitude": 9.445673,
            "heading": -180,
        },
        {
            "latitude": 47.664361,
            "longitude": 9.445963,
            "heading": -120,
        },
    ]
    # implement your solution here
