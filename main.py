from names import names
from glob import glob
from sys import argv
from os.path import basename, dirname, join
from os import rename
import music_tag

currentNames = sorted(glob(f"{argv[1]}/*.mp3"), key=lambda name: int(basename(name).split(".")[0]))
counter = 1
for name in currentNames:
  f = music_tag.load_file(name)
  f["trackNumber"] = counter
  f["totalTracks"] = 114
  f.save()
  rename(name, join(dirname(name), f"{counter:03d} - {names[counter-1]}.mp3"))
  counter += 1
  print(basename(name))
