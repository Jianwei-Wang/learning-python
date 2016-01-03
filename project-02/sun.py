from urllib import urlopen
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF

URL = "ftp://wangjw:luofangli@10.0.208.37/ftp_server/data.txt"

drawing = Drawing(400, 200)

data = []
for line in urlopen(URL).readlines():
    if not line.isspace() and not line[0] in '#:':
        data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
rad_pred = [row[5] for row in data]
rad_high = [row[6] for row in data]
rad_low = [row[7] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred), zip(times, high), zip(times, low), \
           zip(times, rad_pred), zip(times, rad_high), zip(times, rad_low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green
lp.lines[3].strokeColor = colors.yellow
lp.lines[4].strokeColor = colors.black
lp.lines[5].strokeColor = colors.brown

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize = 14, fillColor = colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
