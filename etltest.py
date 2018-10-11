import pandas as pd
from calls import db
from calls.models import *
import csv

db.create_all()

raw_data = pd.read_csv('calls/everything.csv', index_col=0, dtype={'incident_zip': str})
raw_data_2 = raw_data.fillna("00000")
data = raw_data_2.to_dict('raw_data_2')

def agency_objects(data):
    temp_list = []
    # agency_list = []
    for a in data:
        if a['Agency'] not in temp_list:
            agency = Agency(name =a['Agency'])
            temp_list.append(a['Agency'])
            # agency_list.append(agency)
        db.session.add(agency)
    # return agency_list
    db.session.commit()

def borough_objects(data):
    temp_list=[]
    for b in data:
        if b['Borough'] not in temp_list:
            borough = Borough(name=b['Borough'])
            temp_list.append(b['Borough'])
        db.session.add(borough)
    db.session.commit()
borough_objects(data)

def location_objects(data):
    temp_list = []
    # agency_list = []
    for l in data:
        borough_id = Borough.query.filter(Borough.name == l['Borough']).first().id
        if l['Incident Zip'] not in temp_list:
            location = Location(zip =l['Incident Zip'],borough_id=borough_id)
            temp_list.append(l['Incident Zip'])
            # agency_list.append(agency)
    # return agency_list
        db.session.add(location)
        # db.session.add(location_2)
    db.session.commit()

def complaint_objects(data):
    # complaint_list =[]

    for c in data:
        agency_name = Agency.query.filter(Agency.name==c['Agency']).first().name
        location_id= Location.query.filter(Location.zip==c['Incident Zip']).first().id
        borough_name = Borough.query.filter(Borough.name == c['Borough']).first().name
        new_date = (c['Created Date'].split(" ")[0])
        c['Created Date']= new_date
        complaint= Complaint(type=c['Descriptor'],status=c['Status'],method=c['Open Data Channel Type'],date=c['Created Date'], agency_name = agency_name, location_id = location_id, borough_name= borough_name)
        # complaint_list.append(complaint)
    # return complaint_list
        db.session.add(complaint)
    db.session.commit()


agency_objects(data)
location_objects(data)
complaint_objects(data)
