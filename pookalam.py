from turtle import Turtle, Screen
from math import cos, sin, radians
t=Turtle()
t.shape("circle")
t.speed(0)
t.pencolor("white")
screen = Screen()
screen.bgcolor("white")
screen.title("Happy Onam")
t.hideturtle()
screen.tracer(0) 

colors1 = ["#F30C0C", "#D86A10", "#F10C0C"]
colors = ["#FFFB00","#FFF204","#F2FF00"]
colors2=["#FF8000","#FF9100","#D47800"]
color=["#17F902","#0EA301","#59FF00"]


#ring pattern
def ring(radius,size,color):
    t.setheading(270)
    t.penup()
    t.goto(-radius,0)
    t.pendown()
    t.pensize(size)
    t.color(color)
    t.circle(radius)
    t.pensize(0)

#spiral pattern
def spiral(i,length, radius,color,value,pensize):
    t.penup()
    t.goto(0,0)
    t.setheading(i * value)
    t.forward(radius)
    t.pensize(pensize)
    t.pendown()
    for i in range(36):
        t.color(color[i % 3])
        t.forward(length)
        t.backward(length)
        t.right(10)
    t.pensize(0)

#flower pattern
def flower(i,value,radius,pensize,length,color):
    t.penup()
    t.goto(0,0)
    t.setheading(i * value)
    t.forward(radius)
    t.pensize(pensize)
    t.pendown()
    for i in range(8):
        t.color(color)
        t.forward(length)
        t.backward(length)
        t.right(45)
    t.pensize(0)


def diamond(radius,color,angle,size):
    t.penup()
    t.goto(0,0)
    t.setheading(angle)
    t.forward(radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(t.heading())
    for _ in range(2):
        
        t.forward(size)
        t.left(60)
        t.forward(size)
        t.left(120)
    t.end_fill()

#half flower pattern
def draw_half_flower_circle(
    big_radius=200,
    count=8,
    petals_per_half=6,
    petal_arc_radius=30,
    center_radius=10,
    fan_spread_deg=180,
    petal_fill="#fac107",
    petal_outline="#fefa22",
    center_fill="#ff7802",
    center_outline="#f88a14",
    draw_big_guide=False
):
    

    def jump(x, y):
        t.up(); t.goto(x, y); t.down()

    def draw_petal(arc_r=90, extent=60):
        t.circle(arc_r, extent)
        t.left(145 - extent)
        t.circle(arc_r, extent)
        t.left(145)

    def draw_half_flower(center_x, center_y, facing_deg=0):
        start_heading = facing_deg - fan_spread_deg/2
        step = fan_spread_deg / (petals_per_half - 1 if petals_per_half > 1 else 1)

        t.pensize(2)
        t.pencolor(petal_outline)
        t.fillcolor(petal_fill)

        for i in range(petals_per_half):
            angle = start_heading + i*step
            t.up()
            t.goto(center_x, center_y)
            t.setheading(angle)
            t.forward(center_radius * 0.6)
            t.down()
            t.begin_fill()
            draw_petal(arc_r=petal_arc_radius, extent=60)
            t.end_fill()

        
        t.up()
        t.goto(center_x, center_y - center_radius)
        t.setheading(0)
        t.down()
        t.pensize(4)
        t.pencolor(center_outline)
        t.fillcolor(center_fill)
        t.begin_fill()
        t.circle(center_radius)
        t.end_fill()


    if draw_big_guide:
        t.pensize(1)
        t.pencolor("#aaaaaa")
        jump(0, -big_radius)
        t.circle(big_radius)

    for i in range(count):
        theta = 360 * i / count
        rad = radians(theta)
        x = big_radius * cos(rad)
        y = big_radius * sin(rad)
        draw_half_flower(x, y, facing_deg=theta)


def draw_diamond(size, color):
    t.fillcolor(color)
    t.pencolor("white")
    t.begin_fill()
    for i in range(2):
        t.forward(size)
        t.left(60)
        t.forward(size)
        t.left(120)
    t.end_fill()

# Function to draw a ring of diamonds
def diamond_ring(radius, diamonds, colors):
    t.penup()
    t.pencolor("white")
    t.goto(0, -radius)
    t.pendown()
    
    for i in range(diamonds):
        t.penup()
        t.goto(0,0)
        t.forward(radius)
        t.left(90)
        t.pendown()
        
        draw_diamond(30, colors[i % len(colors)])
        t.right(90)
        t.penup()
        t.goto(0,0)
        t.setheading(i*5)


ring(radius=115,size=10,color="#01B51F")
for i in range(20):
    spiral(i=i,length=10,radius=30,color=colors1,value=20,pensize=2)
    spiral(i=i,length=10,radius=50,color=colors2,value=20,pensize=5)
    spiral(i=i,length=20,radius=70,color=colors,value=20,pensize=2)
    spiral(i=i,length=8,radius=70,color=colors1,value=20,pensize=2)
    flower(i=i,length=10,radius=95,color="#FE7504",value=20,pensize=5)
    flower(i=i,length=0,radius=95,color="#FFFFFF",value=20,pensize=5)
    for k in range(30):
        spiral(i=i+k,length=10,radius=120,color=colors1,value=10,pensize=5)
        spiral(i=i+k,length=10,radius=140,color=color,value=8,pensize=5)
        spiral(i=i+k,length=10,radius=160,color=colors1,value=8,pensize=5)
        spiral(i=i+k,length=10,radius=180,color=colors2,value=8,pensize=10)

draw_half_flower_circle(big_radius=180,count=20,petals_per_half=4,     
                        draw_big_guide=False)

screen.update()  
screen.exitonclick()