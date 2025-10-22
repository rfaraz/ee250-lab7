import RPi.GPIO as GPIO
import time

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


def main():
    # led setup
    led_gpio = 17
    GPIO.setup(led_gpio, GPIO.OUT)

    # first blink
    blink_led()

    # second blink 
    blink_led(blinks=4, interval=0.2)

    # cleanup pin assignments
    GPIO.cleanup()

if __name__ == '__main__':
    main()