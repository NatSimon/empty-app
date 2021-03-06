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
thicc = LineStyle(20, red)
x = LineStyle(14, green)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(1000, 500, thinline, blue)
Circle2 = CircleAsset(300, thinline,black)
Circle = CircleAsset(100, thinline,red)
Ellipse = EllipseAsset(230,35, thinline, green)
Ellipse2 = EllipseAsset(230,35, thinline, black)
Polygon = PolygonAsset(((10,70,), (30,50),(60,60)), thicc, red)
rectangle2 = RectangleAsset(100, 300, thicc, red)
Polygon2 = PolygonAsset(((10,70,), (30,5),(90,60)), thicc, blue)
Polygon3 = PolygonAsset(((10,70,), (30,5),(90,60)), thinline, blue)
Circle3 = CircleAsset(30, thicc,blue)
# Now display a rectangle
Sprite(rectangle)
Sprite(Circle2)
Sprite(Circle)
Sprite(Ellipse2, (320,320))
Sprite(Ellipse, (300,300))
Sprite(Polygon)
Sprite(rectangle2, (400,400))
Sprite(Polygon2, (100,400))
Sprite(Polygon3, (300,200))
Sprite(Circle3,(20,500))

myapp = App()
myapp.run()
