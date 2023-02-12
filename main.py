# Add ten to the answer by pressing A

def on_button_pressed_a():
    global answer
    answer += 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def play():
    global answer, num1, num2, correct_answer
    answer = 0
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    correct_answer = num1 * num2
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            620,
            3919,
            255,
            93,
            400,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_string("" + str(num1) + "x" + ("" + str(num2)) + "=")
def lost_life():
    game.remove_life(1)
    play()
# Add one to the answer by pressing B

def on_button_pressed_b():
    global answer
    answer += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Show the equation by pressing the logo

def on_logo_pressed():
    basic.show_string("" + str(num1) + "x" + ("" + str(num2)) + "=")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

correct_answer = 0
num2 = 0
num1 = 0
answer = 0
play()
game.set_life(2)

def on_forever():
    if answer < correct_answer:
        basic.show_number(answer, 80)
    elif answer == correct_answer:
        game.add_score(1)
        music.play_melody("D E F E F G A A ", 322)
        play()
    else:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                5000,
                1467,
                255,
                0,
                450,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        lost_life()
basic.forever(on_forever)
