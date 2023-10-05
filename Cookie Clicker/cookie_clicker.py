import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker game")
wn.bgcolor("teal")

wn.register_shape("cookie_clicker/rsz_cookie.gif")

cookie = turtle.Turtle()
cookie.shape("cookie_clicker/rsz_cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks +=1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    cookie.goto(0, -10)
    cookie.penup()
    cookie.goto(0,0)

cookie.onclick(clicked)


wn.mainloop()