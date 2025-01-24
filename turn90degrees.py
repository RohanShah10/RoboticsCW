import brickpi3  # Import the BrickPi3 library
import time      # Import time for delays

# Initialize the BrickPi3
BP = brickpi3.BrickPi3()

try:
    # Reset motor encoders to zero
    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A))
    BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D))

    # Define motor speeds and rotation angle (adjust as needed for precision)
    motor_speed = 30   # Set motor speed
    turn_degrees = 90  # Target turn in degrees

    # Calculate encoder value for 90-degree turn (trial and error calibration may be needed)
    # This is robot-specific, and you may need to adjust this value.
    encoder_value = 232  # Replace with the appropriate value for your setup

    # Set motors to rotate for the turn
    BP.set_motor_position_relative(BP.PORT_A, -encoder_value)  # Motor A rotates backward
    BP.set_motor_position_relative(BP.PORT_D, encoder_value)   # Motor D rotates forward

    # Wait for the motors to complete the movement
    while (abs(BP.get_motor_encoder(BP.PORT_A)) < encoder_value or
           abs(BP.get_motor_encoder(BP.PORT_D)) < encoder_value):
        time.sleep(0.01)  # Delay to avoid excessive CPU usage

    # Stop the motors after the turn
    BP.set_motor_power(BP.PORT_A, 0)
    BP.set_motor_power(BP.PORT_D, 0)

except KeyboardInterrupt:
    # Handle program interruption gracefully
    print("Program interrupted. Stopping motors.")
    BP.reset_all()
finally:
    # Ensure motors are stopped and resources are released
    BP.reset_all()