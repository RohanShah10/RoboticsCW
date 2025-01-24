from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division        #                           ''

import time  # import the time library for the sleep function
import brickpi3  # import the BrickPi3 drivers

BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

def reset_encoders():
    try:
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))  # reset encoder A
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))  # reset encoder D
    except IOError as error:
        print(error)

try:
    BP.set_motor_limits(BP.PORT_A, 50, 200)
    BP.set_motor_limits(BP.PORT_D, 50, 200)

    # Set motion parameters
    forty_cm = -200
    ninty_deg = -235

    for _ in range(4):
        reset_encoders()

        # Move forward
        BP.set_motor_position(BP.PORT_A, forty_cm)
        BP.set_motor_position(BP.PORT_D, forty_cm)

        while abs(BP.get_motor_encoder(BP.PORT_A) - forty_cm) > 5:
            print("Motor A Status", BP.get_motor_encoder(BP.PORT_A), "Motor D Status", BP.get_motor_encoder(BP.PORT_D))
            time.sleep(0.1)

        reset_encoders()

        # Turn 90 degrees
        BP.set_motor_position(BP.PORT_A, ninty_deg)
        BP.set_motor_position(BP.PORT_D, -ninty_deg)

        while abs(BP.get_motor_encoder(BP.PORT_A) - ninty_deg) > 5:
            print("Motor A Status", BP.get_motor_encoder(BP.PORT_A), "Motor D Status", BP.get_motor_encoder(BP.PORT_D))
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram interrupted! Stopping motors...")
finally:
    # Ensure all motors are stopped and BrickPi3 is reset
    print("Resetting all motors and BrickPi3...")
    BP.reset_all()
