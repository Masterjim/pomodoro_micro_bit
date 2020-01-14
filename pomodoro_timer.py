from microbit import *

SECONDS_IN_MINUTE = 60
MATRIX_X_SIZE = 5
MATRIX_Y_SIZE = 5
FULL_BRIGHTNESS = 9
POMODORO = 25
PAUSE = 5


def timer_image(minutes):
    image = Image("00000:"
                  "00000:"
                  "00000:"
                  "00000:"
                  "00000:")

    nbr_minutes = minutes
    for y in range(MATRIX_X_SIZE):
        for x in range(MATRIX_Y_SIZE):
            if nbr_minutes > 0:
                image.set_pixel(x, y, FULL_BRIGHTNESS)
                nbr_minutes -= 1
    return image


def timer(minutes):
    current_minute = minutes
    while current_minute > 0:
        current_image = timer_image(current_minute)
        next_image = timer_image(current_minute - 1)
        current_second = SECONDS_IN_MINUTE
        while current_second > 0:
            display.show(current_image)
            sleep(500)
            display.show(next_image)
            sleep(500)
            current_second -= 1
        current_minute -= 1


def main():
    while True:
        if button_a.is_pressed():
            timer(POMODORO)
        elif button_b.is_pressed():
            timer(PAUSE)
        else:
            display.show(Image.SURPRISED)


if __name__ == '__main__':
    main()
