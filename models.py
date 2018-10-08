from calls.__init__ import db
from datetime import datetime


class Complaint(db.Model):
    __tablename__= 'complaints'
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.Text)
    status = db.Column(db.Text)
    method = db.Column(db.Text)
    date= db.Column(db.Text)
    # date_id =db.Column(db.Integer, db.ForeignKey('dates.id'))
    agency_name = db.Column(db.Text,db.ForeignKey('agencies.name'))
    agency=db.relationship('Agency',back_populates='complaints')
    location = db.relationship('Location',back_populates='complaints')
    location_id = db.Column(db.Integer,db.ForeignKey('locations.id'))
    # location_name = db.Column(db.Text, db.ForeignKey('locations.name'))
    #city = db.relationship('City',back_populates='complaints')
    #city_name = db.Column(db.Text,db.ForeignKey('cities.name'))
    borough_name=db.Column(db.Integer, db.ForeignKey('boroughs.name'))
    borough = db.relationship('Borough', back_populates='complaints')

    # city= relationship...

class Location(db.Model):
    __tablename__='locations'
    id = db.Column(db.Integer,primary_key = True)
    # name = db.Column(id.Text)
    zip= db.Column(db.String)
    # borough = db.Column(db.Text)
    complaints= db.relationship('Complaint',back_populates='location')
    # name = db.Column(db.Text)
    borough_id = db.Column(db.Integer, db.ForeignKey('boroughs.id'))
    borough = db.relationship("Borough", back_populates='locations')
    # borough_name =db.Column(db.Integer, db.ForeignKey('boroughs.name'))




    #relationship with complaint

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






    #city= db.relationship('City', back_populates='agencies')
    #city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

# class Neighborhood(db.Model):
#     __tablename__= 'neighborhoods'
#     id = db Column(db.Integer, primary_key= True)
#     name = db.Column(db)



# class Date(db.Model):
#     __tablename__='dates'
#     id= db.Column(db.Integer, primary_key= True)
#     date= db.Column(db.Date)
#     complaints = db.relationship('Complaint', back_populates='date')

# class City(db.Model):
#     __tablename__:'cities'
#     id= db.Column(db.Integer, primary_key = True)
#     name= db.Column(db.Text)
#     complaints = db.relationship('Complaint', back_populates='city')
#     agencies= db.relationship('Agency', back_populates= 'city')
