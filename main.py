Number2 = 0

def on_sound_loud():
    basic.show_icon(IconNames.HEART)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_shake():
    global Number2
    Number2 = randint(1, 6)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_sound_quiet():
    basic.show_icon(IconNames.SMALL_HEART)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

def on_forever():
    if Number2 == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    elif Number2 == 2:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        # . . . #
                        . . . . .
                        . . . . .
        """)
    elif Number2 == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    elif Number2 == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    elif Number2 == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    elif Number2 == 6:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
    else:
        basic.clear_screen()
basic.forever(on_forever)
