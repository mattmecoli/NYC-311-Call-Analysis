# Project 
* Looked at 311 calls from the last two years to see if there were any seasonality to make staffing recommendaitons for dispatchers and agency workers

# Database set up and exploration 
* Used NYC open data lirbary to pull 311 calls for the last two years
* Due to the large amount of calls received in a given time period, we looked at the past two years for calls related to: 
  * Loud Music/Partying
  * Loud Talking 
  * Graffiti 
  * Request to Recyle Electronics 
  * Planting a tree 
  * Mouse/Rat Sighiting 
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
* Created Dash app to demonstrate interactive charts of findings of overall calls by zip codes and by borough 

