from turtle import*


#we want to paint a house

#step 1:draw a square
speed(5)
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170,170)
pendown()
 
 #drawing a window
color("green")
begin_fill()
right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)


penup()
goto(30,140)
pendown()


right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()