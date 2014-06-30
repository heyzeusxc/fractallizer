import turtle

#turtle.shape('turtle')

x = 0.0
y = 0.1
r = 255
g = 255
b = 255
switch = 0
turtle.bgcolor('black')
turtle.hideturtle()
turtle.speed(0)

while True:
	rgb = (r,g,b)
	turtle.pendown()
	turtle.forward(x/3)
	turtle.left(x/2)
	turtle.forward(x/8)
	turtle.right(x/2)
	turtle.forward(x/3)
	turtle.left(x/2)
	turtle.forward(x/8)
	turtle.right(x/2)
	turtle.forward(x/3)
	turtle.left(x)
	turtle.colormode(255)
	x += y	
	turtle.pencolor(rgb)
	if switch == 0:
		r -= 1
		g -= 1
		b -= 1
	elif switch == 1:
		r += 1
		g += 1
		b += 1
	if rgb[0] == 254:
		switch = 0
	if rgb[0] == 35:
		switch = 1
	print rgb[1],switch

