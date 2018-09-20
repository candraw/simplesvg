class Scene:
    header = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="{}" width="{}">'''
    footer = '''</svg>'''

    def __init__(self, height=500, width=500):
        self.height = height
        self.width = width
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def add_array(self, a):
        for e in a:
            self.add(e)

    def render(self):
        return '\n'.join([self.header.format(self.height, self.width)] +\
                        [e.render() for e in self.elements] +\
                        [self.footer])

    def render_to_file(self, filename):
        f = open(filename, 'w')
        f.write(self.render())
        f.close()

class Element:
    def __init__(self):
        self.options = {}

    def option(self, key, value):
        self.options[key] = value

    def render_options(self):
        return ' '.join(['{}="{}"'.format(k, self.options[k]) for k in self.options.keys()])

class Shape(Element):
    def __init__(self):
        Element.__init__(self)

    def stroke(self, s):
        self.option('stroke', s)

    def stroke_width(self, sw):
        self.option('stroke-width', sw)

    def fill(self, f):
        self.option('fill', s)

class Polyline(Shape):
    def __init__(self, *points, stroke="black"):
        Shape.__init__(self)
        self.points = points
        self.stroke(stroke)

    def render(self):
        pointlist = ' '.join(['{},{}'.format(p[0],p[1]) for p in self.points])
        
        return '<polyline points="{}" {} />'\
                .format(pointlist, self.render_options())

    def from_array(a, stroke="black", width=4):
        return Path(*a, stroke, width)

class Rect(Shape):
    def __init__(self, pos, width, height, stroke="black"):
        Shape.__init__(self)
        self.p = pos
        self.width = width
        self.height = height
        self.stroke(stroke)
        
    def render(self):
        return '<rect x="{}" y="{}" width="{}" height="{}" {} />'\
                .format(self.p[0], self.p[1], self.width, self.height, self.render_options())

class Circle(Shape):
    def __init__(self, m, r, stroke="black"):
        Shape.__init__(self)
        self.m = m
        self.r = r
        self.stroke(stroke)

    def render(self):
        return '<circle cx="{}" cy="{}" r="{}" fill="{}" {} />'\
                .format(self.m[0], self.m[1], self.r, self.render_options())

class Ellipse(Shape):
    def __init__(self, pos, width, height, stroke="black"):
        Shape.__init__(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.stroke(stroke)

    def render(self):
        return '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" {} />'\
                .format(self.pos[0], self.pos[1], self.width, self.height, self.render_options())

class Line(Shape):
    def __init__(self, p1, p2, stroke="black"):
        Shape.__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.stroke(stroke)

    def render(self):
        return '<line x1="{}" y1="{}" x2="{}" y2="{}" {} />'\
                .format(self.p1[0], self.p1[1], self.p2[0], self.p2[1], self.render_options())
