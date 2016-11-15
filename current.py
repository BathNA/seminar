#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("1st Semester 2016/2017")

seminars = []
# Fields: date, speaker, institution, title, homepage URL, abstract link, misc

seminars.append(["07 Oct 2016", "James Hook", "Bath", "Applications of tropical mathematics in numerical linear algebra", "http://www.bath.ac.uk/imi/people/index.html", "hook.txt", None])
seminars.append(["14 Oct 2016", "Silvia Gazzola", "Bath", "New challenges in the numerical solution of large-scale inverse problems", "http://people.bath.ac.uk/sg968/", "gazzola.txt", None])
seminars.append(["21 Oct 2016", "Abdul-Lateef Haji-Ali", "Oxford", "Multi-index methods for quadrature", "https://www.maths.ox.ac.uk/people/abdullateef.hajiali", "hajiali.txt", None])
seminars.append(["28 Oct 2016", "Lei Zhang", "Shanghai Jiao Tong", "Solving multi-scale PDEs: from numerical homogenization to fast solvers", "http://ins.sjtu.edu.cn/faculty/zhanglei", "zhang.txt", None])
seminars.append(["04 Nov 2016", "Alastair Gregory", "Imperial", "A multilevel Monte Carlo approach to ensemble transform particle filtering", "http://www.imperial.ac.uk/people/a.gregory14", "gregory.txt", None])
seminars.append(["11 Nov 2016", "Sébastien Loisel", "Heriot-Watt", "Optimized Schwarz methods for heterogeneous problems", "http://www.macs.hw.ac.uk/~sl398/", "loisel.txt", None])
seminars.append(["18 Nov 2016", "Rob Scheichl", "Bath", "Multilevel Subset Simulation to Predict Rare Events", "http://www.bath.ac.uk/math-sci/contacts/academics/rob-scheichl/", "", None])
seminars.append(["25 Nov 2016", "Claudia Schillings", "HU Berlin", "Scaling Limits in Computational Bayesian Inversion", "https://www2.mathematik.hu-berlin.de/~schillcl/", "schillings.txt", None])
seminars.append(["02 Dec 2016", "Joab Winkler", "Sheffield", "Image Processing by Polynomial Computations", "http://staffwww.dcs.shef.ac.uk/people/J.Winkler/", "winkler.txt", None])
seminars.append(["09 Dec 2016", "Zhiwen Zhang", "Hong Kong", "", "http://hkumath.hku.hk/MathWWW/people.php?faculty.zhangzw", "", None])
seminars.append(["16 Dec 2016", "Elizabeth Arter", "Bath", "", "", "", None])

links = []
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
