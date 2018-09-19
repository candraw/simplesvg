class Scene:
    header = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xml="https://www.w3.org/2000/svg" version="1.1" height="{}" width="{}">'''
    footer = '''</svg>'''

    def __init__(self, height=500, width=500):
        self.height = height
        self.width = width
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def render(self):
        return '\n'.join([self.header.format(self.height, self.width)] +\
                        [e.render() for e in self.elements] +\
                        [self.footer])

    def render_to_file(self, filename):
        f = open(filename, 'w')
        f.write(self.render())
        f.close()


class Path:
    def __init__(self, *points, stroke="black", width=4):
        self.points = points
        self.stroke = stroke
        self.width = width

    def render(self):
        pointlist = ' '.join(['{},{}'.format(p[0],p[1]) for p in self.points])
        
        return '<polyline points="{}" stroke="{}" stroke-width="{}" fill="none" />'\
                .format(pointlist, self.stroke, self.width)

class Circle:
    def __init__(self, m, r, stroke="black", fill="none", swidth=4):
        self.m = m
        self.r = r
        self.stroke = stroke
        self.swidth = swidth
        self.fill = fill

    def render(self):
        return '<circle cx="{}" cy="{}" r="{}" fill="{}" stroke="{}" stroke-width="{}" />'\
                .format(self.m[0], self.m[1], self.r, self.fill, self.stroke, self.swidth)

class Text:
    def __init__(self, p, msg):
        self.p = p
        self.msg = msg
