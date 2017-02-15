#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("2nd Semester 2016/2017")

seminars = []
# Fields: date, speaker, institution, title, homepage URL, abstract link, misc

seminars.append(["10 Feb 2017", "Carlos Galeano Rios", "Bath", "Numerical approximation of a singular integral operator used in linear water wave theory", "", "galeano.txt", None])
seminars.append(["17 Feb 2017", "David Hewett", "UCL", "Wave scattering by fractal screens", "https://iris.ucl.ac.uk/iris/browse/profile?upi=DHEWE35", "hewett.txt", None])
seminars.append(["24 Feb 2017", "Tom Goffrey", "Exeter", "A new approach to stellar models: The MUlti-dimensional Stellar Implicit Code", "http://emps.exeter.ac.uk/physics-astronomy/staff/tg300", "goffrey.txt", None])
seminars.append(["3 Mar 2017", "Tony Kennedy", "Edinburgh", "", "http://www.ph.ed.ac.uk/people/tony-kennedy", "", None])
seminars.append(["10 Mar 2017", "Marta Betcke", "UCL", "", "http://www0.cs.ucl.ac.uk/people/M.Betcke.html", "", None])
seminars.append(["17 Mar 2017", "Ander Biguri and Manuchehr Soleimani", "Bath", "", "http://people.bath.ac.uk/ms350/", "", None])
seminars.append(["24 Mar 2017", "Anders Hansen", "Cambridge", "", "http://www.damtp.cam.ac.uk/people/a.c.hansen/", "", None])
seminars.append(["31 Mar 2017", "", "", "", "", "", None])
seminars.append(["7 Apr 2017", "Oliver Dorn", "Manchester", "", "http://www.maths.manchester.ac.uk/people/staff/profile/?ea=Oliver.Dorn", "", None])
seminars.append(["28 Apr 2017", "Aretha Teckentrup", "Edinburgh", "", "http://www.maths.ed.ac.uk/school-of-mathematics/people?person=544", "", None])
seminars.append(["5 May 2017", "", "", "", "", "", None])

links = []
links.append(["2016/17 1st semester", "naseminar2016sem1.html"])
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
