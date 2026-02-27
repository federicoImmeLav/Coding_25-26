import turtle

# ----------------------------
# Creazione schermata
# ----------------------------
screen = turtle.Screen()
screen.title("Turtle con movimento e rotazione")
screen.listen()

# ----------------------------
# Creazione turtle
# ----------------------------
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# ----------------------------
# Dizionario dei tasti
# ----------------------------
keys = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

# ----------------------------
# Funzioni pressione tasti
# ----------------------------
def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

# Collegamento tasti premuti
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeypress(lambda: key_press("Left"), "Left")
screen.onkeypress(lambda: key_press("Right"), "Right")

# Collegamento tasti rilasciati
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Left"), "Left")
screen.onkeyrelease(lambda: key_release("Right"), "Right")

# ----------------------------
# Movimento continuo
# ----------------------------
def move():
    x, y = t.position()

    dx = 0
    dy = 0
    step = 5

    if keys["Up"]:
        dy += step
    if keys["Down"]:
        dy -= step
    if keys["Left"]:
        dx -= step
    if keys["Right"]:
        dx += step

    # Se si sta muovendo
    if dx != 0 or dy != 0:

        # Impostiamo direzione
        if dx == 0 and dy > 0:
            t.setheading(90)
        elif dx == 0 and dy < 0:
            t.setheading(270)
        elif dy == 0 and dx > 0:
            t.setheading(0)
        elif dy == 0 and dx < 0:
            t.setheading(180)
        elif dx > 0 and dy > 0:
            t.setheading(45)
        elif dx < 0 and dy > 0:
            t.setheading(135)
        elif dx < 0 and dy < 0:
            t.setheading(225)
        elif dx > 0 and dy < 0:
            t.setheading(315)

        t.goto(x + dx, y + dy)

    screen.ontimer(move, 20)

move()

turtle.mainloop()