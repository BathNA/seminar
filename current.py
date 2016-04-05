#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

meta = []
meta.append("2nd Semester 2015/2016")

seminars = []
# Fields: date, speaker, institution, title, homepage URL, abstract link, misc

seminars.append(["05 Feb 2016", "Martin Schreiber", "Exeter", "Massively parallel rational approximation of oscillatory problems", "https://emps.exeter.ac.uk/mathematics/staff/ms698", "schreiber.txt", None])
seminars.append(['''<font color="red"> 08 Feb 2016 (Monday) 13:15, CB 3.11</font>''', "Steven Dargaville", "Imperial", "Parallel multigrid and adaptive space/angle methods for the Boltzmann Transport Equation", "http://www.imperial.ac.uk/people/s.dargaville", "dargaville.txt", None])
seminars.append(["12 Feb 2016", "Mark Opmeer", "Bath", "Approximation of a Quantity of Interest for a PDE", "http://www.maths.bath.ac.uk/~mo221/", "opmeer.txt", None])
seminars.append(["19 Feb 2016", "Raymond Chan", "The Chinese University of Hong Kong", "Point-spread function reconstruction in ground-based astronomy", "http://www.math.cuhk.edu.hk/~rchan/", "chan.txt", None])
seminars.append(["26 Feb 2016", "Anne Reinarz", "Bath", "Sparse Galerkin BEM for the heat equation", "", "reinarz.txt", None])
seminars.append(["04 Mar 2016", "Matt Durey", "Bath", "Droplets on a vibrating bath: from walking to butterflies", "", "durey.txt", None])
seminars.append(['''<font color="red"> 08 Mar 2016 (Tuesday) 13:15</font>''', "Markus Bachmayr", "Laboratoire Jacques Louis Lyons, Paris", "Representations of Gaussian random fields and sparse approximation of lognormal diffusion problems", "https://www.ljll.math.upmc.fr/~bachmayr/", "bachmayr.txt", None])
seminars.append(["11 Mar 2016", "Sergey Dolgov", "Bath", "Tensor product approach for solution of multidimensional differential equations", "http://www.mpi-magdeburg.mpg.de/37834/employee_page?c=842836&amp;employee_id=39297", "dolgov.txt", None])
seminars.append(["18 Mar 2016", "Daniel Ruprecht", "Leeds", "Boris-SDC and FWSW-SDC: Two new integration methods based on spectral deferred corrections", "https://www.engineering.leeds.ac.uk/people/mechanical/staff/d.ruprecht", "ruprecht.txt", None])
seminars.append(["08 Apr 2016", "Matthew Thomas", "Bath", "The Numerical Analyst's guide to Approximate Bayesian Inference", "https://people.bath.ac.uk/mlt21/", "thomas.txt", None])
seminars.append(["15 Apr 2016", "Patrick Kuerschner", "MPI Magdeburg", "Model Order Reduction and Large-scale Matrix Equations", "http://www2.mpi-magdeburg.mpg.de/mpcsc/kuerschner/", None, None])
seminars.append(["22 Apr 2016", "Christian Litterer", "York", "TBC", "http://maths.york.ac.uk/www/cl1566", None, None])
seminars.append(["29 Apr 2016", "Alison Ramage", "Strathclyde", "A multilevel preconditioner for data assimilation with 4D-Var", "http://www.strath.ac.uk/staff/ramagealisondr/", "ramage.txt", None])
seminars.append(["TBC", "Ivan Graham", "Bath", "TBC", "http://people.bath.ac.uk/masigg/", None, None])

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
