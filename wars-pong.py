# Nabeel Warsalee
# Oct 9 2018
# Practicing python

# Pong remake

from SimpleGraphics import *

scale = 10

resize(500,500)

def drawGrid():
    # Drawing vertical lines
    for i in range(50):
        setColor(101,101,101)
        line(i*10, 0, i*10, 500)
    # Drawing horizontal lines
    for i in range(50):
        setColor(101,101,101)
        line(0, i*10, 500, i*10)

background(0,0,0)

paddleWidth = 1*scale
paddleHeight = 7*scale

paddleY1 = 15*scale
paddleY2 =  15*scale

ballX = 25*scale
ballY = 10*scale
ballLength = 1*scale
ballDx = 5
ballDy = 10

p1Score = 0
p2Score = 0

while not closed():
    setFont("Arial","24","bold")
    text(125,50,str(p1Score))
    text(375,50,str(p2Score))
    if (p1Score == 5 or p2Score == 5):
        break
    #drawGrid()
    keys = getHeldKeys()
    print(keys)
    # Movement for paddle 1
    if ("w" in keys):
        if (paddleY1 > 0):
            paddleY1 -= 10
    elif ("s" in keys):
        if (paddleY1+paddleHeight < 500):
            paddleY1 += 10
    # Movement for paddle 2
    if ("Up" in keys):
        if (paddleY2 > 0):
            paddleY2 -= 10
    elif ("Down" in keys):
        if (paddleY2+paddleHeight < 500):
            paddleY2 += 10
    # Movement for ball
    if (ballY <= 0 or ballY+ballLength >= 500):
        ballDy *= -1
    # Resetting ball and awarding points to players
    if (ballX <= 0):
        p2Score += 1
        ballX = 25*scale
        ballY = 10*scale
    elif (ballX >= 500):
        p1Score += 1
        ballX = 25*scale
        ballY = 10*scale
    # Changing the direction of the ball after hitting a paddle
    if ((ballX == 47*scale and ballY in range(paddleY2,paddleY2+paddleHeight))
    or (ballX == 2*scale and ballY in range(paddleY1,paddleY1+paddleHeight))):
        ballDx *= -1
    ballX += ballDx
    ballY += ballDy
    clear()
    line(250, 0, 250, 500)
    # Drawing both paddles
    setColor("white")
    rect(1*scale,paddleY1,paddleWidth,paddleHeight) # Paddle 1
    rect(48*scale,paddleY2,paddleWidth,paddleHeight) # Paddle 2
    #Drawing the ball
    rect(ballX, ballY, ballLength,ballLength)
    sleep(0.02)

if (p1Score == 5):
    text(100, 250, "P1 wins!")
else:
    text(400, 250, "P2 wins!")

setFont("Times New Roman", 14, "bold")
text(250, 450, "Game by Nabeel Warsalee")
