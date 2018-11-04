# Project Overview  
We analyzed NYC 311 call data from the last two years across seven categories to look for interesting trends and seasonalities in order to identify trends and make staffing recommendations for dispatchers and agency workers. 

## The Data and Exploratory Data Analysis 

Our database is 45 MB and hasn’t been uploaded here, but should be reproducible using the code here. If anything doesn't work, feel free to reach out to me, and I'll take a look. 

The primary data came from an NYC open data library to pull 311 calls for the last two years:
 
   https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
   
The data contained a number of features including call data and geographic information. Much of this wasn't useful for our purposes and was dropped. 

Because of the large number of calls, we limited our data to the past two years for calls related to seven categories: 

  * Loud Music/Partying
  * Loud Talking 
  * Graffiti 
  * Request to Recycle Electronics 
  * Tree Requests  
  * Mouse Sighting
  * Rat Sighting

Additionally, we began the process of gathering other information based upon 'neighborhoods', which are essentially intermediary groupings of zipcodes within boroughs.  The neighborhoods were scraped using the code that can be seen in neighborhoods.py. This data will be used in the future to calculate 'superlatives' (Neighborhood with the greenest thumb - most tree requests, for example) in the future. 

Finally, we pulled census data from the 2010 census and tied population information to each zipcode. We intend to use this to create "per capita" call metrics that are a better method of comparing two zipcodes than purely call volume. This is particularly true because we're concerned that our data suffers from a certain degree of observation bias. Rats aren't necessarily more common in certain zip codes than others so much as the residents of some zip codes might be more bothered or less accustomed to rats and more likely to call 311. 
  
## ETL & Database Architecture 

We pulled the data from the website as a csv file (although we could also have made API requests for JSON, the CSV download was significantly faster). 

We removed a number of unnecessary columns, filled NaN values, and fixed a few smaller issues (datatype consistency, incorrect naming) before we initalized a SQLite database using Flask/SQLAlchemy as an ORM and persisted the data into the database with the following classes and relationships:

```class Complaint(db.Model):
    __tablename__= 'complaints'
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.Text)
    status = db.Column(db.Text)
    method = db.Column(db.Text)
    date= db.Column(db.Text)
    agency_name = db.Column(db.Text,db.ForeignKey('agencies.name'))
    agency=db.relationship('Agency',back_populates='complaints')
    location = db.relationship('Location',back_populates='complaints')
    location_id = db.Column(db.Integer,db.ForeignKey('locations.id'))
    borough_name=db.Column(db.Integer, db.ForeignKey('boroughs.name'))
    borough = db.relationship('Borough', back_populates='complaints')

  class Location(db.Model):
    __tablename__='locations'
    id = db.Column(db.Integer,primary_key = True)
    zip= db.Column(db.String)
    complaints= db.relationship('Complaint',back_populates='location')
    borough_id = db.Column(db.Integer, db.ForeignKey('boroughs.id'))
    borough = db.relationship("Borough", back_populates='locations')
    
  class Agency(db.Model):
    __tablename__='agencies'
    id= db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    complaints = db.relationship('Complaint',back_populates='agency')

  class Borough(db.Model):
    __tablename__ ='boroughs'
    id= db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    locations = db.relationship('Location', back_populates='borough')
    complaints= db.relationship('Complaint',back_populates='borough')
  ```
# Dash Dashboard
We implemented a Dash app built on top of Flask to display our findings based off of zipcode and borough. Running the "run.py" file should launch the dash app locally. The homepage can be found at unique-local-ip/dashboard/

You can see the dashboard video in action here: 

![Dash_Vid](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/dashboard_vid)

## Total calls 
This dropdown allowed us to look at each zipcode's call volume. This was one of the areas that people enjoyed the most during our presentation because they could look at thier own zipcode. It was both interactive and personal. 

![Image](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/dropdown.png)

## Total call type by borough
This allowed us to take a borough-level views of calls by category. While loud noise complaints had the highest amount of calls in every borough, some other trends were notable. Brooklyn has more people, but loud talking is a bigger complain in Manhattan. Tree requests were more common in gentrifying areas. Some zip codes had unusual patterns of calls. One Staten Island zipcode, for example, had almost all of the recycling electronics requests and very few other calls. 

![Image](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/borough.png)

## Call volume for loud noise complaints:

Additioanlly, because we wanted to consider whether or not the data would be useful for staffing considerations, we examined how call volume changed over the course of a day, a week, and a year. 

### Number of calls by hour

Highest number of calls come in from 10pm - 1am 

![Image](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/hour.png)

### Number of calls by day of the week

Friday and Saturday see a spike in the number of calls 

![Image](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/day.png)

### Number of calls by month
* Calls peak during the summer month with June having the highest amount of calls 

![Image](https://github.com/mattymecks/NYC-311-Call-Analysis/blob/master/images/month.png)


## Results and Findings:

### Loud Noise: 

Overall Loud Music/Partying had the highest volume of calls across almost all zipcodes all boroughs with Brooklyn and Manhattan having the most. We saw areas such as the East Village and Williamsburg neighborhoods were some of the loudest neighborhoods, which is not suprising given the large numbers of younger residents in those neighborhoods.

Loud noise complaints starts to peak from May- September when it becomes warmer, schools are out, and there are more activities to do outside. June has the highest volume of calls. 

The majority of calls tend to be placed during 10 pm- 1 am through Friday and Saturday, and we would recommend seasonal staffing to receive calls during the summer months, particularly in the evenings and on weekends. The NYPD might also want to come up with a program or adjust hours, since they are the agency usually tasked with investigating calls, particularly from what make up the majority of the calls: Loud Noise or Loud Music complaints. 

### Tree Requests:

New York has a policy where property owners can request to have a tree planted on their street for free. Given that the most calls for this request came in certain gentrifying neighbborhoods in Brooklyn, Queens, and Staten Island, we'd suggest having more personnel available in those areas to be able to plant trees versus other boroughs.

This also provides some insight into the sort of data that can signal the gentrifying effect occuring in a given area.

# Electronics Disposal:

As of yet, we have not determined why requests for the removal of electonics are so rare across most borough and occur almost entirely within one zipcode in Staten Island, but we continue to investigate. 

## Next Steps

We scraped zipcodes by neighborhood from a NYC Department of Health website and our next step would be to bin zipcodes into neighborhoods and do additional analysis on that level as well as award 'superlatives.' Additionally, we can use population data tied to zipcodes to create 'per capita' metrics to better compare significance of call differences between neighborhoods with widely varying populations. 


## Libraries & Software

#### SQLAlchemy 
Our object relational mapper (ORM) of choice here. 

Docs/install: https://docs.sqlalchemy.org/en/latest/intro.html

#### Flask
Flask “is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application.” Flask is a micro-framework because it has little to no dependence on external libraries. 

Docs/install: http://flask.pocoo.org/docs/1.0/installation/

#### Flash-SQLAlchemy extension 
Makes interacting with Flask/SQLAlchemy simpler and easier. 

Docs/install: https://pypi.org/project/Flask-SQLAlchemy/

#### Dash
Dash is built by Plotly and allows you to build attractive, analytical web applications with a Python framework and no JavaScript required. Can be built on top of Flask/SQLAlchemy as was done here. 

Docs/install: https://dash.plot.ly/installation

#### SQLite 
A small, fast, reliable (and free!) database software, and the most widely deployed database in the world. A great place to start working with relational databases. 

Docs/install: http://www.sqlitetutorial.net/download-install-sqlite/
