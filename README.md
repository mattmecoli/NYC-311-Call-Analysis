# Project 
We analyzed NYC 311 call data from the last two years across seven categories to look for interesting trends and seasonalities in order to make staffing recommendations for dispatchers and agency workers.

# Database set up and exploration 
* Used NYC open data library to pull 311 calls for the last two years:
 
   https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
* Due to a large number of calls received in a given time period, we looked at the past two years for calls related to: 
  * Loud Music/Partying
  * Loud Talking 
  * Graffiti 
  * Request to Recycle Electronics 
  * Request for a tree 
  * Mouse Sighting
  * Rat Sighting
* Set up SQL database using Flask/SQLAlchemy as an ORM with the following classes and relationships:
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
Implemented a Dash app built on Flask to display finidngs based off of zipcode, and borough: 

## Total calls 
* Additional option to filter complaint by zip code
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Screen%20Shot%202018-10-08%20at%204.06.31%20PM.png" width="850" height="350">

## Total call type by borough
* Loud noise complaints had the highest amount of calls in every borough. Some zip codes had unusual patterns of calls. One Staten Island zipcode, for example, had a large number of recycling electronics request and very few other calls. Additionally, we were aware that our data suffered from a certain degree of observation bias. Rats aren't necessarily more common in certain zip codes than others so much as the residents of some zip codes might be more bothered or less accustomed to rats and more likely to call 311. 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Screen%20Shot%202018-10-08%20at%204.06.53%20PM.png" width="850" height="350">

# Time series analysis for load noise complaint:
## Number of calls by hour
* Highest number of calls come in from 10pm - 1am 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Call%20by%20hour.png" width="650" height="350">

## Number of calls by month
* Calls peak during the summer month with June having the highest amount of calls 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Calls%20by%20month.png" width="550" height="350">

## Number of calls by DOW
* Friday and Saturday saw a spike in the number of calls 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/call%20by%20DOW.png" width="650" height="450">

# Results and Findings:
## Loud Noise: 
* Overall Loud Music/Partying had the highest volume of calls among all boroughs. With Brooklyn and Manhattan having the most. We saw areas such as the East Village and Williamsburg neighborhoods were some of the loudest neighborhoods, which is not suprising given the large numbers of younger residents in those neighborhoods. 
* Loud noise complaints starts to peak from May- September when it becomes warmer, school's  are out and there are more activities to do outside. June is the highest month with calls, and it starts to dip in August but picks back up in September when Universities are back in session
* High majority of calls tend to be placed during 10 pm- 1 am through Friday and Saturday. 
* Recommend higher staff to receive call columns during the summer months, 10pm-1am on weekends, as well as the NYPD since they are the agency to investigate the calls. We suspect the majority of these calls are Loud Noise or Loud Music complaints. 
## For one address: 
* New York has a policy if you are a property owner, you can request to have a tree planted on your street for free! The highest amount of calls for this request came in certain gentrifying neighbborhoods in Brooklyn, Queens, and Staten Island. We saw the highest frequency of calls in Staten Island and Brooklyn since they have slightly more room.
* As such, we'd suggest having more personal in Staten Island and Brooklyn to be available to plant the trees versus other boroughs. 
* This also provides some insight into the sort of data that can signal the gentrifying effect occuring in a given area.
* With requesting Large Appliance/Electronic removal, the only area we saw a majority of the calls come through Staten Island.
## An additional note:
* We found that people enjoyed our Dash app because of its personal level of interactivity. People were able to search the zip code they lived in and get some insight into how their neighborhood behaves. 
# Next Steps
* We scraped zipcodes by neighborhood from a NYC Department of Health website and our next step would be to bin zipcodes into neighborhoods and do additional analysis on that level. 

