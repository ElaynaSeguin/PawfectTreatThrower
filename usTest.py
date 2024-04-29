from machine import Pin, time_pulse_us
import utime

# Define GPIO pins connected to the ultrasonic sensor
trigger_pin = Pin(12, Pin.OUT)  # GP12 for trigger
echo_pin = Pin(10, Pin.IN)       # GP10 for echo

def read_distance():
    # Send a 10 microsecond trigger pulse to start the measurement
    trigger_pin.off()
    utime.sleep_us(2)
    trigger_pin.on()
    utime.sleep_us(10)
    trigger_pin.off()

    # Measure the duration of the echo pulse (in microseconds)
    pulse_duration = time_pulse_us(echo_pin, 1, 30000)  # Timeout of 30 milliseconds (30,000 microseconds)
    
    if pulse_duration > 0:
        # Calculate distance based on the speed of sound (343 meters/second)
        # Divide by 2 because the sound wave travels to the object and back
        distance_cm = (pulse_duration / 2) * 0.0343
        return distance_cm
    else:
        return None

try:
    while True:
        # Read distance from the ultrasonic sensor
        distance = read_distance()
        
        if distance is not None:
            print("Distance: {:.2f} cm".format(distance))
        else:
            print("Error: Measurement timeout")

        utime.sleep(1)  # Delay for 1 second between measurements

except KeyboardInterrupt:
    pass
