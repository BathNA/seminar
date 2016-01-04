#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("1st Semester 2015/2016")

seminars = []
# Fields: date, speaker, homepage URL, institution, misc, title, abstract link

seminars.append(["05 Feb 2016", "TBC", "", "", None, "", None])
seminars.append(["12 Feb 2016", "TBC", "", "", None, "", None])
seminars.append(["19 Feb 2016", "TBC", "", "", None, "", None])
seminars.append(["26 Feb 2016", "TBC", "", "", None, "", None])
seminars.append(["04 Mar 2016", "TBC", "", "", None, "", None])
seminars.append(["11 Mar 2016", "TBC", "", "", None, "", None])
seminars.append(["18 Mar 2016", "TBC", "", "", None, "", None])
seminars.append(["08 Apr 2016", "TBC", "", "", None, "", None])
seminars.append(["15 Apr 2016", "TBC", "", "", None, "", None])
seminars.append(["22 Apr 2016", "TBC", "", "", None, "", None])
seminars.append(["29 Apr 2016", "TBC", "", "", None, "", None])

links = []
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
