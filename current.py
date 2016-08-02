#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("1st Semester 2016/2017")

seminars = []
# Fields: date, speaker, institution, title, homepage URL, abstract link, misc

seminars.append(["07 Oct 2016", "", "", "", "", "", None])
seminars.append(["14 Oct 2016", "", "", "", "", "", None])
seminars.append(["21 Oct 2016", "", "", "", "", "", None])
seminars.append(["28 Oct 2016", "", "", "", "", "", None])
seminars.append(["04 Nov 2016", "", "", "", "", "", None])
seminars.append(["11 Nov 2016", "Sébastien Loisel", "Heriot-Watt", "", "http://www.macs.hw.ac.uk/~sl398/", "", None])
seminars.append(["18 Nov 2016", "", "", "", "", "", None])
seminars.append(["25 Nov 2016", "", "", "", "", "", None])
seminars.append(["02 Dec 2016", "Joab Winkler", "Sheffield", "", "http://staffwww.dcs.shef.ac.uk/people/J.Winkler/", "", None])
seminars.append(["09 Dec 2016", "", "", "", "", "", None])
seminars.append(["16 Dec 2016", "", "", "", "", "", None])

links = []
links.append(["2015/16 2nd semester", "naseminar2015sem2.html"])
links.append(["2015/16 1st semester", "naseminar2015sem1.html"])
links.append(["2014/15 2nd semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2014sem2.html"])
links.append(["2014/15 1st semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2014sem1.html"])
links.append(["2013/14 2nd semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2013sem2.html"])
links.append(["2013/14 1st semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2013sem1.html"])
links.append(["2012/13 2nd semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2012sem2.html"])
links.append(["2012/13 1st semester", "http://people.bath.ac.uk/em459/NASeminar/naseminar2012sem1.html"])
links.append(["2011/12 2nd semester", "http://people.bath.ac.uk/mamamf/naseminar2011sem2.html"])
links.append(["2011/12 1st semester", "http://people.bath.ac.uk/eas25/naseminar2011sem1.html"])
links.append(["2010/11 2nd semester", "http://people.bath.ac.uk/mamamf/naseminar2010sem2.html"])
links.append(["2010/11 1st semester", "http://people.bath.ac.uk/mamamf/naseminar2010sem1.html"])
links.append(["2009/10 2nd semester", "http://people.bath.ac.uk/mamamf/naseminar2009sem2.html"])
links.append(["More archived seminars", "http://www.maths.bath.ac.uk/~masrs/nasemarchive.html"])

meta.append(links)

pickle.dump([seminars, meta], open('current.pickle', 'w'))
