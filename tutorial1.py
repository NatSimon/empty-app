from ggame import App
myapp = App()
myapp.run()
from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(5, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(1000, 500, thinline, blue)
Circle2 = CircleAsset(300, thinline,black)
Circle = CircleAsset(100, thinline,red)
Ellipse = EllipseAsset(230,35, thinline, green)

# Now display a rectangle
Sprite(rectangle)
Sprite(Circle2)
Sprite(Circle)
Sprite(Ellipse, (100,20))


myapp = App()
myapp.run()
