import svg

s = svg.Scene()
s.add(svg.Path((0,0), (500,500), stroke="blue"))
s.add(svg.Circle((120, 250), 100, stroke="blue", fill="red"))
s.render_to_file('test.svg')
