## retrieve the subject svg
``` bash
curl https://projects.intra.42.fr/uploads/document/document/5614/athlete_events.csv > a.csv
```

## ex00
``` bash
cd ex00 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
```
``` python
loader.display(data, 12)
loader.display(data, 3)
loader.display(data, -3)
loader.display(data, 0)
loader.display(data, "LOL")
print(loader.display(data, "LOL"))
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex01
``` bash
cd ex01 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
from YoungestFellah import youngestfellah
```
```python
print(youngestfellah(data, 1992))
# output is: "{'f': 12.0, 'm': 11.0}"
print(youngestfellah(data, 2004))
# output is: "{'f': 13.0, 'm': 14.0}"
print(youngestfellah(data, 2010))
# output is: "{'f': 15.0, 'm': 15.0}"
print(youngestfellah(data, 2003))
# output is: "{'f': nan, 'm': nan}"
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex02
``` bash
cd ex02 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
from ProportionBySport import proportionBySport
```
``` python 
print(proportionBySport(data, 2004, 'Tennis', 'F'))
# output is 0.01935634328358209
print(proportionBySport(data, 2008, 'Hockey', 'F'))
# output is 0.04149467738431458
print(proportionBySport(data, 1964, 'Biathlon', 'M'))
# output is 0.009539842873176206
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex03
``` bash
cd ex03 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
from HowManyMedals import howManyMedals
```
``` python
print(howManyMedals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"
print(howManyMedals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"
print(howManyMedals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex04
``` bash
cd ex04 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv") ; df = data
from SpatioTemporalData import SpatioTemporalData ; sp = SpatioTemporalData(df)
```
``` python
print(sp.where(2000))
# output is: ['Sydney']
print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva']
print(sp.when('London'))
# output is: [2012, 1948, 1908]
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex05
``` bash
cd ex05 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv") ; df = data
from HowManyMedalsByCountry import howManyMedalsByCountry
```
``` python
print(howManyMedalsByCountry(df, "United States") == {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 87, 'S': 41, 'B': 35}, 1924: {'G': 65, 'S': 41, 'B': 36}, 1928: {'G': 39, 'S': 22, 'B': 18}, 1932: {'G': 60, 'S': 57, 'B': 43}, 1936: {'G': 30, 'S': 29, 'B': 28}, 1948: {'G': 57, 'S': 34, 'B': 30}, 1952: {'G': 55, 'S': 38, 'B': 25}, 1956: {'G': 39, 'S': 57, 'B': 21}, 1960: {'G': 83, 'S': 27, 'B': 19}, 1964: {'G': 75, 'S': 36, 'B': 28}, 1968: {'G': 86, 'S': 36, 'B': 35}, 1972: {'G': 70, 'S': 58, 'B': 33}, 1976: {'G': 62, 'S': 46, 'B': 30}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 143, 'S': 75, 'B': 33}, 1988: {'G': 66, 'S': 48, 'B': 36}, 1992: {'G': 79, 'S': 46, 'B': 52}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 98, 'S': 41, 'B': 28}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 69, 'S': 34, 'B': 48}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 65, 'S': 66, 'B': 38}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 64, 'S': 61, 'B': 47}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 82, 'S': 44, 'B': 38}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 95, 'S': 52, 'B': 45}})
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex06
``` bash
cd ex06 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
from MyPlotLib import MyPlotLib as mp
```
``` python
mp.histogram(data, ["Height", "Weight", "Age"])
mp.density(data, ["Height", "Weight", "Age"])
mp.pair_plot(data, ["Height", "Weight", "Age"])
mp.box_plot(data, ["Height", "Weight", "Age"])
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```

## ex07
``` bash
cd ex07 ; python
```
``` python
from FileLoader import FileLoader ; loader = FileLoader() ; data = loader.load("../a.csv")
from Komparator import Komparator ; kp = Komparator(data)
```
``` python
kp.compare_box_plots('Medal', 'Age')
kp.density('Medal', 'Age')
kp.compare_histograms('Medal', 'Age')
```
`^D` => control + D to quit python console (or `exit()`)
``` bash
cd ..
```