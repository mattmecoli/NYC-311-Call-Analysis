# Project 
* Analyzed 311 calls from the last two years to see if there were any seasonality to make staffing recommendations for dispatchers and agency workers

# Database set up and exploration 
* Used NYC open data library to pull 311 calls for the last two years:
 
   https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
* Due to a large number of calls received in a given time period, we looked at the past two years for calls related to: 
  * Loud Music/Partying
  * Loud Talking 
  * Graffiti 
  * Request to Recycle Electronics 
  * Request for a tree 
  * Mouse/Rat Sighting
* Set up SQL database using SQL Alchemy using the following classes and relationships:
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
Implemented Dash app to display finidngs based off of zipcode, and borough: 

## Total calls 
* Additional option to filter complaint by zip code
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Screen%20Shot%202018-10-08%20at%204.06.31%20PM.png" width="850" height="350">

## Total call type by borough
* Loud noise complaints had the highest amount of calls in every borough
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Screen%20Shot%202018-10-08%20at%204.06.53%20PM.png" width="850" height="350">

# Time series analysis for load noise complaint:
## Number of calls by hour
* Highest number of calls come in from 10pm - 1am 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Call%20by%20hour.png" width="450" height="350">

## Number of calls by month
* Calls peak during the summer month with June having the highest amount of calls 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/Calls%20by%20month.png" width="450" height="350">

## Number of calls by DOW
* Friday and Saturday are the days with the largest amount of calls 
<img src="https://github.com/jarty13/Anlysis-of-311-calls-NYC-/blob/master/image/call%20by%20DOW.png" width="450" height="450">

# Results and Findings:
## Loud Noise: 
* Overall Loud Music/Partying had the highest volume of calls among all boroughs. With Brooklyn and Manhattan having the most. We saw areas such as the East Village and Williamsburg neighborhoods were some of the loudest neighborhoods 
* Loud noise complaints starts to peak from May- September when it becomes warmer, school's  are out and there are more activities to do outside. June is the highest month with calls, and it starts to dip in August but picks back up in September when Universities are back in session
* High majority of calls tend to be placed during 10 pm- 1 am through Friday and Saturday. 
* Recommend higher staff to receive call columns during the summer months, 10pm-1am on weekends, as well as the NYPD since they are the agency to investigate the calls 
## For one address: 
* New York has a policy if you are a property owner, you can request to have a tree planted on your street for free! The highest amount of calls for this request came in Brooklyn, Queens, and Staten Island.Wwe saw a higher frequency of calls Staten Island and Brooklyn since they are areas with more space to plant trees in the area 
* Recommend having more personal in Staten Island and Brooklyn to be available to plant the trees versus other boroughs
* With requesting Large Appliance /Electronic removal, the only area we saw a majority of the calls come through Staten Island since residents of Brooklyn, Western Queens can request free curbside pick up of their appliances.
## Other Complaints: 
* Rat and Graffiti sightings were the two categories that did not have significant complaints by time or area. Our assumptions are since rodent sighting and graffiti are something people dont tend to call about since its an every day occurance in NYC. Next step would look at how these two complaints have changed over the years and then see if there have any initiatives in place to control Graffiti and rat/mouse sightings. 
