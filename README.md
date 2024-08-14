**Sloan-Digital-Sky-Survey-SDSS-galaxy-classification**

1.**Data**

Context

Sloan Digital Sky Survey current DR16 Server Data release with Galaxies, Stars and Quasars.

License: Creative Commons Attribution license (CC-BY) More datailes here. Find more here.

Content
The table results from a query which joins two tables:

"PhotoObj" which contains photometric data

"SpecObj" which contains spectral data.

16 variables (double) and 1 additional variable (char) 'class'.

A class object can be predicted from the other 16 variables.

Variables description:

objid = Object Identifier

ra = J2000 Right Ascension (r-band)

dec = J2000 Declination (r-band)

u = better of deV/Exp magnitude fit (u-band)

g = better of deV/Exp magnitude fit (g-band)

r = better of deV/Exp magnitude fit (r-band)

i = better of deV/Exp magnitude fit (i-band)

z = better of deV/Exp magnitude fit (z-band)

run = Run Number

rerun = Rerun Number

camcol = Camera column

field = Field number

specobjid = Object Identifier

class = object class (galaxy, star or quasar object)

redshift = Final Redshift

plate = plate number

mjd = MJD of observation

fiberid = fiberID

2.**EDA**

There is no null values in data.

There is no duplicated data.

Handling outliers using quantile method with capping.

3.**Feature selection**

Extratreeclassifier is used for feature importance.

There are zero importance of objid and rerun 
so we drop objid and rerun.

4.**Model buliding**

A decision tree is a flowchart-like structure used to make decisions or predictions. 

It consists of nodes representing decisions or tests on attributes, branches representing the outcome of these decisions,
and leaf nodes representing final outcomes or predictions. 

Each internal node corresponds to a test on an attribute, each branch corresponds to the result of the test, and each leaf node corresponds to a class label or a continuous value.

5.**Model Evalution**



║     class    ║ precision ║ recall ║ f1-score ║ support ║

║ 0            ║ 1.00      ║ 0.99   ║ 0.99     ║ 983     ║

║ 1            ║ 0.99      ║ 1.00   ║ 0.99     ║ 971     ║

║ 2            ║ 1.00      ║ 1.00   ║ 1.00     ║ 1045    ║

║ accuracy     ║           ║        ║ 0.99     ║ 2999    ║

║ macro-avg    ║ 0.99      ║ 0.99   ║ 0.99     ║ 2999    ║

║ weighted-avg ║ 0.99      ║ 0.99   ║ 0.99     ║ 2999    ║

