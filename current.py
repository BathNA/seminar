#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("2nd Semester 2016/2017")

seminars = []
# Fields: date, speaker, institution, title, homepage URL, abstract link, misc

seminars.append(["10 Feb 2017", "", "", "", "", "", None])
seminars.append(["17 Feb 2017", "", "", "", "", "", None])
seminars.append(["24 Feb 2017", "reserved", "", "reserved", "", "", None])
seminars.append(["3 Mar 2017", "", "", "", "", "", None])
seminars.append(["10 Mar 2017", "", "", "", "", "", None])
seminars.append(["17 Mar 2017", "", "", "", "", "", None])
seminars.append(["24 Mar 2017", "", "", "", "", "", None])
seminars.append(["31 Mar 2017", "", "", "", "", "", None])
seminars.append(["7 Apr 2017", "", "", "", "", "", None])
seminars.append(["28 Apr 2017", "", "", "", "", "", None])
seminars.append(["5 May 2017", "", "", "", "", "", None])

links = []
links.append(["2016/17 1st semester", "Archive/naseminar2016sem1.html"])
links.append(["2015/16 2nd semester", "Archive/naseminar2015sem2.html"])
links.append(["2015/16 1st semester", "Archive/naseminar2015sem1.html"])
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
