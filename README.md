# Project 
* Looked at 311 calls from the last two years to see if there were any seasonality to make staffing recommendaitons for dispatchers and agency workers

# Database set up and exploration 
* Used NYC open data lirbary to pull 311 calls for the last two years
* Due to the large amount of calls received in a given time period, we looked at the past two years for calls related to: 
  * Loud Music/Partying
  * Loud Talking 
  * Graffiti 
  * Request to Recyle Electronics 
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

#Finding s
