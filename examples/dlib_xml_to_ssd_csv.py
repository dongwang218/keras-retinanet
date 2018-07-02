import os
import sys
from bs4 import BeautifulSoup
import random

csv = open(sys.argv[1].replace('.xml', '.csv'), 'w')

random.seed(0)
lines = {}
with open(sys.argv[1], 'r') as f:
  soup = BeautifulSoup(f, 'xml')
  for img in soup.findAll('image'):
    file = img['file']
    boxes = img.findAll('box')
    rect = []
    for box in boxes:
      xmin = box['left']
      xmax = int(box['left']) + int(box['width'])
      ymin = box['top']
      ymax = int(box['top']) + int(box['height'])
      rect.append((xmin, xmax, ymin, ymax))
    lines[file] = rect

lines2 = lines.items()
random.shuffle(lines2)

for file, rects in lines2:
  for (xmin, xmax, ymin, ymax) in rects:
    csv.write('%s,%s,%s,%s,%s,1\n' % (os.path.basename(file), xmin, xmax, ymin, ymax))
  # if len(rects) == 0:
  #   csv.write('%s,,,,,\n' % (os.path.basename(file)))
