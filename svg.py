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


class Polyline:
    def __init__(self, *points, stroke="black", stroke_width=4):
        self.points = points
        self.stroke = stroke
        self.stroke_width = stroke_width

    def render(self):
        pointlist = ' '.join(['{},{}'.format(p[0],p[1]) for p in self.points])
        
        return '<polyline points="{}" stroke="{}" stroke-width="{}" fill="none" />'\
                .format(pointlist, self.stroke, self.stroke_width)

    def from_array(a, stroke="black", width=4):
        return Path(*a, stroke, width)

class Rect:
    def __init__(self, pos, width, height, fill="none", stroke="black", stroke_width=4):
        self.p = pos
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        
    def render(self):
        return '<rect x="{}" y="{}" width="{}" height="{}" fill="{}" stroke="{}" stroke-width="{}" />'\
                .format(self.p[0], self.p[1], self.width, self.height, self.fill, self.stroke, self.stroke_width)

class Circle:
    def __init__(self, m, r, stroke="black", fill="none", stroke_width=4):
        self.m = m
        self.r = r
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.fill = fill

    def render(self):
        return '<circle cx="{}" cy="{}" r="{}" fill="{}" stroke="{}" stroke-width="{}" />'\
                .format(self.m[0], self.m[1], self.r, self.fill, self.stroke, self.stroke_width)

class Ellipse:
    def __init__(self, pos, width, height, stroke="black", fill="none", stroke_width=4):
        self.pos = pos
        self.width = width
        self.height = height
        self.stroke = stroke
        self.fill = fill
        self.stroke_width = stroke_width

    def render(self):
        return '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" stroke="{}" stroke-width="{}" fill="{}" />'\
                .format(self.pos[0], self.pos[1], self.width, self.height, self.stroke, self.stroke_width, self.fill)

class Line:
    def __init__(self, p1, p2, stroke="black", stroke_width=4):
        self.p1 = p1
        self.p2 = p2
        self.stroke = stroke
        self.stroke_width = stroke_width

    def render(self):
        return '<line x1="{}" y2="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}" />'\
                .format(self.p1[0], self.p1[1], self.p2[0], self.p2[1], self.stroke, self.stroke_width)



class Text:
    def __init__(self, p, msg):
        self.p = p
        self.msg = msg
