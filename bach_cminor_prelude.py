from music21 import *

s = converter.parse('BWV_0847a.xml')

parts = s.getElementsByClass('Part')
print("parts", len(parts))
rh = parts[0]
lh = parts[1]
rhbars = rh.getElementsByClass('Measure')
lhbars = lh.getElementsByClass('Measure')

print("rhb1", len(rhbars[0].getElementsByClass('Note')))
print("lh", len(lh.getElementsByClass('Measure')))

def bar2midi(bar):
    return ' '.join(map(lambda note: str(note.pitch.midi), bar.getElementsByClass('Note')))

for bar_number in range(8):
    print ('  rh'+ str(bar_number) + '="' + (bar2midi(rhbars[bar_number])) + '"')
    print ('  lh'+ str(bar_number) + '="' + (bar2midi(lhbars[bar_number])) + '"')


