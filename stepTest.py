#stepper motor test, need to increase rate of turning and possibly power input for treat dispenser

from machine import Pin
import utime as time

# Define GPIO pins connected to the ULN2003 driver inputs
coil_A_1_pin = Pin(11, Pin.OUT)  # IN1
coil_A_2_pin = Pin(12, Pin.OUT)  # IN2
coil_B_1_pin = Pin(13, Pin.OUT)  # IN3
coil_B_2_pin = Pin(14, Pin.OUT)  # IN4

# Define stepper motor sequence (8-step sequence for 28BYJ-48)
step_sequence = [
    [1, 0, 0, 1],  # Step 1
    [1, 0, 0, 0],  # Step 2
    [1, 1, 0, 0],  # Step 3
    [0, 1, 0, 0],  # Step 4
    [0, 1, 1, 0],  # Step 5
    [0, 0, 1, 0],  # Step 6
    [0, 0, 1, 1],  # Step 7
    [0, 0, 0, 1]   # Step 8
]

# Define function to perform a single step of the stepper motor
def step_motor(sequence, step_number):
    for pin, value in zip([coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin], sequence[step_number]):
        pin.value(value)

# Main loop to rotate the stepper motor continuously
try:
    while True:
        # Rotate clockwise (4 steps per revolution for 28BYJ-48)
        for i in range(512):  # 512 steps = 360 degrees (full revolution)
            step_motor(step_sequence, i % 8)
            time.sleep_ms(10)  # Increase delay to 10 milliseconds (ms) for slower rotation
        
except KeyboardInterrupt:
    pass
finally:
    # Turn off all motor coils to stop motor movement
    for pin in [coil_A_1_pin, coil_A_2_pin, coil_B_1_pin, coil_B_2_pin]:
        pin.value(0)
