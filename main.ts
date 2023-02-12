// Add ten to the answer by pressing A
input.onButtonPressed(Button.A, function () {
    answer += 10
})
function play () {
    answer = 0
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    correct_answer = num1 * num2
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 620, 3919, 255, 93, 400, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
    basic.showString("" + num1 + "x" + ("" + num2) + "=")
}
function lost_life () {
    game.removeLife(1)
    play()
}
// Add one to the answer by pressing B
input.onButtonPressed(Button.B, function () {
    answer += 1
})
// Show the equation by pressing the logo
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("" + num1 + "x" + ("" + num2) + "=")
})
let correct_answer = 0
let num2 = 0
let num1 = 0
let answer = 0
play()
game.setLife(2)
basic.forever(function () {
    if (answer < correct_answer) {
        basic.showNumber(answer, 80)
    } else if (answer == correct_answer) {
        game.addScore(1)
        music.playMelody("D E F E F G A A ", 322)
        play()
    } else {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 5000, 1467, 255, 0, 450, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
        lost_life()
    }
})
