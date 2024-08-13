#Sloan-Digital-Sky-Survey-SDSS-galaxy-classification

##Data
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
