#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import pickle

meta = []
meta.append("1st Semester 2015/2016")

seminars = []
# Fields: date, speaker, homepage URL, institution, misc, title, abstract link

seminars.append(["02 Oct 2015", "Euan Spence", "http://people.bath.ac.uk/eas25/", "Bath", None, "Does the Galerkin method converge when applied to the standard second-kind integral equations for the Laplacian on Lipschitz domains?", None])
seminars.append(["09 Oct 2015", "John Pearson", "http://www.kent.ac.uk/smsas/our-people/profiles/pearson_john.html", "Kent", None, "Four perspectives on the numerical solution of PDE-constrained optimization problems", "Abstracts/abstract_pearson.txt"])
seminars.append(["16 Oct 2015", "Benedict Leimkuhler", "http://www.maths.ed.ac.uk/people/show?person=10", "Edinburgh", None, "Thermostatic Controls for Noisy Gradient Systems and Applications to Machine Learning", "Abstracts/abstract_leimkuhler.txt"])
seminars.append(["23 Oct 2015", "Patrick Farrell", "https://www.maths.ox.ac.uk/people/patrick.farrell", "Oxford", None, "Deflation techniques for distinct solutions of nonlinear PDEs", "Abstracts/abstract_farrell.txt"])
seminars.append(["30 Oct 2015", "Dan Simpson", None, "Bath", None, "Why is scaling up computations for statistical models so hard? A case for constructive kleptomania", "Abstracts/abstract_simpson.txt"])
seminars.append(["06 Nov 2015", "Christoph Reisinger", "https://people.maths.ox.ac.uk/reisinge/", "Oxford", None, "Piecewise constant policy approximations to Hamilton-Jacobi-Bellman equations", "Abstracts/abstract_reisinger.txt"])
seminars.append(["13 Nov 2015", "Andrew McRae", "http://www.imperial.ac.uk/people/a.mcrae12", "Bath", None, "Compatible finite element methods for 3D atmospheric dynamical cores", "Abstracts/abstract_mcrae.txt"])
seminars.append(["20 Nov 2015", "Will Saunders", "http://people.bath.ac.uk/wrs20/", "Bath", "TBC", "An introduction to Molecular Dynamics and cell based methods for short range interactions", "Abstracts/abstract_saunders.txt"])
seminars.append(["27 Nov 2015", "Dan Green", None, "Bath", None, "Goal-Oriented Inference: Predicting the future without calculating the past", "Abstracts/abstract_green.txt"])
seminars.append(["04 Dec 2015", "Matthew Parkinson", None, "Bath", "TBC", "Multi-Index Monte Carlo for Uncertainty Quantification", "Abstracts/abstract_parkinson.txt"])
seminars.append(['''11 Dec 2015, <font color="red">13:15h</font>''', "Martin Redmann", "http://www.mpi-magdeburg.mpg.de/37834/employee_page?c=842836&amp;employee_id=26685", "MPI Magdeburg", None, " 	Model order reduction for linear controlled SDEs with Lévy Noise", "Abstracts/abstract_redmann.txt"])

links = []
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

pickle.dump([seminars, meta], open('foo.pickle', 'w'))
