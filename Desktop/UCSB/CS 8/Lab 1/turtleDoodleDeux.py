import turtle as t
t.shape('turtle')

def polygon(n, x, y, c):
    'n is number of sides in the polygon, x, y is an ordered pair, c is the color'
    t.color(c)
    t.up()
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    count = 0
    while count < n:
        bearing = (180*(n-2))/n
        t.right(180-bearing)
        t.forward(50)
        count += 1
    t.end_fill()
    t.up()
    
    

polygon(10, 150, 150,'blue')
polygon(6, -100, -100, 'green')
polygon(5, 150, -100, 'yellow')
polygon(8, -100, 150, 'purple')
polygon(4, 0, 0, 'red')
