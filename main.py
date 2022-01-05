def on_received_number(receivedNumber):
    if receivedNumber == 1:
        for index in range(4):
            basic.show_leds("""
                # . # . #
                                # . # . #
                                . # # # .
                                . # # # .
                                . # # # .
            """)
    if receivedNumber == 2:
        for index2 in range(4):
            basic.show_leds("""
                . . # . .
                                . . # . .
                                . . # # #
                                # # . . .
                                # # . . .
            """)
    if receivedNumber == 3:
        for index3 in range(4):
            basic.show_leds("""
                # . # . #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    music.set_volume(127)
    music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
    radio.set_group(1000)
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.set_volume(127)
    music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
    radio.set_group(1000)
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.set_volume(127)
    music.start_melody(music.built_in_melody(Melodies.CHASE), MelodyOptions.ONCE)
    radio.set_group(1000)
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                # # . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                # # # . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                # # # # .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    """)
basic.forever(on_forever)
