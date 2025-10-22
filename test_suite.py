import RPi.GPIO as GPIO
import time
import datetime as dt
import mcp3008

# set mode as GPIO numbers instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# blinking function
    # interval is in seconds 
def blink_led(led_gpio=17, blinks=5, interval=0.5):
    for b in range(blinks):
        print(f"Blink {b + 1}")
        GPIO.output(led_gpio, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(led_gpio, GPIO.LOW)
        time.sleep(interval)

def read_light(channel=mcp3008.CH0, interval=0.1, duration=5):
    adc = mcp3008.MCP3008()
    num_readings = int(duration / interval)
    threshold = 20 # Tested threshold

    for r in range(num_readings):
        raw_val = adc.read([channel])
        print("Raw value:", raw_val)
        print("Dark\n") if raw_val[0] < threshold else print("Light\n")
        time.sleep(interval)

    adc.close()

def read_sound(channel=mcp3008.CH1, interval=0.1, duration=5):
    adc = mcp3008.MCP3008()
    num_readings = int(duration / interval)
    threshold = 20 # Tested threshold

    for r in range(num_readings):
        raw_val = adc.read([channel])
        print("Raw value:", raw_val)
        time.sleep(interval)

    adc.close()

def main():
    # led setup
    led_gpio = 17
    GPIO.setup(led_gpio, GPIO.OUT)

    # first blink
    blink_led()

    # read output of light sensor
    read_light()

    # second blink 
    blink_led(blinks=4, interval=0.2)

    # read output of sound sensor
    read_sound()

    # cleanup pin assignments
    GPIO.cleanup()

if __name__ == '__main__':
    main()