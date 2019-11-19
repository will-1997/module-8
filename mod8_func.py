# Motor code modified from:
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


def motor_init(in1, in2, en, freq, dutycycle):
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    pwm_pin = GPIO.PWM(en, freq)
    pwm_pin.start(dutycycle)
    return pwm_pin


def motor_direction(in1, in2, direction):
    # direction -1 -backwards, 0 - stop, 1 - forward
    if direction < 0:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
    elif direction == 0:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
    else:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)


def motor_message():
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high ")
    print("c- change to floating point duty cycle with user input")
    print("e-exit")
    print("\n")


def movingAvg(array_list, numvals_for_average, size_of_array, position):
    sumvals = 0
    for i in range(numvals_for_average):
        if position - i >= 0:
            sumvals = sumvals + array_list[position - i]
        else:
            sumvals = sumvals + array_list[size_of_array + (position - i)]
    return sumvals / numvals_for_average


def motor_control(x, in1, in2, pwm_pin):
    if x == "r":
        # print("run")
        motor_direction(in1, in2, 1)
        # print("forward")
        x = "z"

    elif x == "s":
        # iprint("stop")
        motor_direction(in1, in2, 0)
        x = "z"

    elif x == "f":
        # print("forward")
        motor_direction(in1, in2, 1)
        x = "z"

    elif x == "b":
        # print("backward")
        motor_direction(in1, in2, -1)
        x = "z"

    elif x == "l":
        # print("low")
        pwm_pin.ChangeDutyCycle(25)
        x = "z"

    elif x == "m":
        # print("medium")
        pwm_pin.ChangeDutyCycle(50)
        x = "z"

    elif x == "h":
        # print("high")
        pwm_pin.ChangeDutyCycle(75)
        x = "z"

    elif x == "c":
        newPWM = float(input("Enter a new PWM duty cycle 0-100: "))
        # Caution NO sanity check here
        pwm_pin.ChangeDutyCycle(newPWM)
        x = "z"

    elif x == "e":
        print("Stopping")

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        x = "z"

