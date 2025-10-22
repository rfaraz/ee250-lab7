import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink_led(led_gpio=17, blinks=5, interval=0.5):
    for b in range(blinks):
        print(f"Blink {b + 1}")
        GPIO.output(led_gpio, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(led_gpio, GPIO.LOW)

def main():
    led_gpio = 17
    GPIO.setup(led_gpio, GPIO.OUT)
    blink_led()
    GPIO.cleanup()

if __name__ == '__main__':
    main()