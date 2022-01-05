radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # . # . #
                # . # . #
                . # # # .
                . # # # .
                . # # # .
                `)
        }
    }
    if (receivedNumber == 2) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                . . # . .
                . . # . .
                . . # # #
                # # . . .
                # # . . .
                `)
        }
    }
    if (receivedNumber == 3) {
        for (let index = 0; index < 4; index++) {
            basic.showLeds(`
                # . # . #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
        }
    }
})
input.onButtonPressed(Button.A, function () {
    music.setVolume(127)
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
    radio.setGroup(1000)
    radio.sendNumber(1)
})
input.onButtonPressed(Button.AB, function () {
    music.setVolume(127)
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
    radio.setGroup(1000)
    radio.sendNumber(3)
})
input.onButtonPressed(Button.B, function () {
    music.setVolume(127)
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.Once)
    radio.setGroup(1000)
    radio.sendNumber(2)
})
basic.forever(function () {
    basic.showLeds(`
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # # . . .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # # # . .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # # # # .
        `)
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        `)
})
