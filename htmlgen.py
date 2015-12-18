import pickle

semfile = open("foo.pickle", "r")
seminars = pickle.load(semfile)
semfile.close()

page = '''\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <meta http-equiv="content-type" content="text/html;
      charset=UTF-8">
    <title>Bath Numerical Analysis Seminars</title>
  </head>
  <body>
    <br>
    <table>
      <tbody>
        <tr>
          <td width="7%"><br>
          </td>
          <td>
            <table cellpadding="3" border="1" width="100%">
              <tbody>
                <tr>
                  <td align="LEFT" valign="TOP" width="20%"><a
                      href="http://www.bath.ac.uk/"> <img
                        src="http://www.bath.ac.uk/assets/graphics/logo-blu-xs.gif"
                        alt="University of Bath" title="University of
                        Bath" align="left" border="0"> </a></td>
                  <td colspan="1" align="CENTER">
                    <h2>Bath Numerical Analysis Seminar, 
                        '''

page += "1st Semester 2015/2016"

page += '''</h2>
                  </td>
                </tr>
              </tbody>
            </table>
            <hr> <br>
            The Numerical Analysis seminar at Bath has been running
            continuously since 1986 and features a range of invited
            talks from distinguished visitors as well as internal talks
            by staff and students of Mathematical Sciences and other
            Departments at the University of Bath. <br>
            <br>
            <hr> <br>
            The Bath Numerical Analysis Seminar takes place Fridays at <b>12.15</b>
            in <b>4W1.7</b> (also known as the Wolfson Lecture
            Theatre). Campus maps can be found <a
              href="http://www.bath.ac.uk/travel-advice/location-maps/index.html">here</a>.
            <br>
            <p> <b> Everyone is welcome at these talks and don't forget
                to join us for lunch after the seminar. </b> </p>
            <hr>
            <p> </p>
            <div align="CENTER"> <b>Schedule</b> </div>
            <p> </p>
            <div align="CENTER">
              <table cellpadding="3" border="1" width="98%">
                <!--- HEADER --> <tbody>
                  <tr>
                    <td align="LEFT" valign="TOP" width="95">Date</td>
                    <td align="LEFT" valign="TOP" width="190">Speaker</td>
                    <td align="LEFT" valign="TOP" width="360">Title</td>
                  </tr>
'''
for index, seminar in enumerate(seminars):
    date, speaker, homepage, institution, other, title, abstract = seminar
    entry = ""
    if index % 2 == 0:
        entry += '''\
                  <tr bgcolor="WhiteSmoke">'''
    else:
        entry += '''\
                  <tr>'''
    entry += '''
                    <td>'''
    entry += date
    entry += '''</td>'''
    entry += '''
                    <td>'''
    if homepage:
        entry += '''<a href="'''
        entry += homepage
        entry += '''">'''

    entry += speaker
    if homepage:
        entry += '''</a>'''
    entry += ''' ('''
    entry += institution
    entry += ')'
    if other:
        entry += ' '
        entry += other
    entry += '''</td>'''
    entry += '''
                    <td>'''
    if abstract:
        entry += '''<a href="'''
        entry += abstract
        entry += '''">'''
    entry += title
    if abstract:
        entry += '''</a>'''
    entry += '''</tr>
'''
    page += entry

page += """\
                </tbody>
              </table>
            </div>
            <h4>How to get to Bath</h4>
            See <a href="http://www.bath.ac.uk/getting-here/">here</a>
            for instructions how to get to Bath. Please email Eike  
            (address below) if you intend to come by car and
            require a parking permit for Bath University Campus for the
            day.
            <h4>Tips for new students on giving talks</h4>
            Since the audience of the NA seminar contains both PhD
            students and staff with quite wide interests and
            backgrounds, the following are some guidelines/hints to make
            sure people don't give you evil looks at lunch afterwards. <br>
            <br>
            Before too much time passes in your talk, ideally the
            audience should know the answers to the following 4
            questions:
            <ul>
              <li>What is the problem you're considering? </li>
              <li>Why do you find this interesting? </li>
              <li>What has been done before on this problem/what's the
                background? </li>
              <li>What is your approach/what are you going to talk
                about? </li>
            </ul>
            There are lots of different ways to communicate this
            information. One way, if you're doing a slide show, could be
            for the first 4 slides to cover these 4 questions; although
            in this case you may want to revisit these points later on
            in the talk (e.g. to give more detail). <br>
            <br>
            Remember:
            <ul>
              <li>"vertebrate style" (structure hidden inside - like the
                skeleton of a vertebrate) = good for detective stories,
                bad for maths talks. </li>
              <li>"crustacean style" (structure visible from outside -
                like the skeleton of a crustacean) = bad for detective
                stories, good for maths talks. </li>
            </ul>
            <h4>Previous Numerical Analysis Seminars</h4>
            <ul>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2014sem2.html">NA seminar for 2nd Semester 2014/2015</a> </li>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2014sem1.html">NA seminar for 1st Semester 2014/2015</a> </li>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2013sem2.html">NA seminar for 2nd Semester 2013/2014</a> </li>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2013sem1.html">NA seminar for 1st Semester 2013/2014</a> </li>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2012sem2.html">NA seminar for 2nd Semester 2012/2013</a> </li>
              <li> <a
href="http://people.bath.ac.uk/em459/NASeminar/naseminar2012sem1.html">NA seminar for 1st Semester 2012/2013</a> </li>
              <li> <a
                  href="http://people.bath.ac.uk/mamamf/naseminar2011sem2.html">NA seminar for 2nd Semester 2011/2012</a> </li>
              <li> <a
                  href="http://people.bath.ac.uk/eas25/naseminar2011sem1.html">NA



                  seminar for 1st Semester 2011/2012</a> </li>
              <li> <a
                  href="http://people.bath.ac.uk/mamamf/naseminar2010sem2.html">NA



                  seminar for 2nd Semester 2010/2011</a> </li>
              <li> <a
                  href="http://people.bath.ac.uk/mamamf/naseminar2010sem1.html">NA



                  seminar for 1st Semester 2010/2011</a> </li>
              <li> <a
                  href="http://people.bath.ac.uk/mamamf/naseminar2009sem2.html">NA



                  seminar for 2nd Semester 2009/2010</a>
                <!--<li> <a href="http://people.bath.ac.uk/cn229/naseminars/">NA seminar for 1st Semester

2009/2010</a>--> </li>
              <li> <a
                  href="http://www.maths.bath.ac.uk/%7Emasrs/nasemarchive.html">An



                  archive of previous NA seminars</a> </li>
            </ul>
            <br>
            If you have any queries, please email Eike 
            (<font face="Courier">e DOT mueller AT bath DOT ac DOT uk</font>). </td>
          <td width="7%"><br>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
"""

outfile = open("test.html", "w")
outfile.write(page)
outfile.close()
