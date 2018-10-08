# #complaint
# from __init__ import db
# from models import *
# db.create_all()
#
# # id = db.Column(db.Integer,primary_key = True)
# # type = db.Column(db.Text)
# # status = db.Column(db.Text)
# # method = db.Column(db.Text)
# complaint_1=Complaint(type = 'DOF Property - Reduction Issue', status='Closed', date='06/12/2018',method='PHONE')
# complaint_2=Complaint(type='Blocked Driveway', status='closed', date='04/27/2018',method='PHONE')
# complaint_3=Complaint(type='Street Condition',status='Closed',date='04/26/2018',method='UNKNOWN')
# complaint_4=Complaint(type='Building/Use',status='Closed',date='06/23/2018',method='UNKNOWN')
# complaint_5=Complaint(type='Request Large Bulky Item Collection',status='Closed',date='05/21/2018',method='PHONE')
# complaint_6=Complaint(type='Noise - Residential',status='Closed',date='07/05/2018',method='ONLINE')
# complaint_7=Complaint(type='General Construction/Plumbing',status='Closed',date='07/16/2018',method='UNKNOWN')
# complaint_8=Complaint(type='Street Light Condition',status='Open',date='07/16/2018',method='UNKNOWN')
# complaint_9=Complaint(type='Noise - Street/Sidewalk',status='Closed',date='07/17/2018',method='PHONE')
# complaint_10=Complaint(type='Street Condition',status='Closed',date='07/18/2018',method='UNKNOWN')
#
#
# complaint_1.location=Location(zip='10314',borough='STATEN ISLAND')
# complaint_2.location=Location(zip='10460',borough='BRONX')
# complaint_3.location=Location(zip='11105',borough='QUEENS')
# complaint_4.location=Location(zip='11377',borough='QUEENS')
# complaint_5.location=Location(zip='11365',borough='QUEENS')
# complaint_6.location=Location(zip='11212',borough='BROOKLYN')
# complaint_7.location=Location(zip='10014',borough='MANHATTAN')
# complaint_8.location=Location(zip=' ',borough='BROOKLYN')
# complaint_9.location=Location(zip='10014',borough='MANHATTAN')
# complaint_10.location=Location(zip='11413',borough='QUEENS')
#
# complaint_1.agency=Agency(name='DOF')
# complaint_2.agency=Agency(name='NYPD')
# complaint_3.agency=Agency(name='DOT')
# complaint_4.agency=Agency(name='DOB')
# complaint_5.agency=Agency(name='DSNY')
# complaint_6.agency=Agency(name='DOB')
# complaint_7.agency=Agency(name='DSNY')
# complaint_8.agency=Agency(name='NYPD')
# complaint_9.agency=Agency(name='DOF')
# complaint_10.agency=Agency(name='DOB')


# complaint_1.date= Date(date='06/12/2018')
# complaint_2.date=Date(date='04/27/2018')
# complaint_3.date=Date(date='04/26/2018')
# complaint_4.date=Date(date='06/23/2018')
# complaint_5.date=Date(date='05/21/2018')
# complaint_6.date=Date(date='07/05/2018')
# complaint_7.date=Date(date='07/16/2018')
# complaint_8.date=Date(date='07/16/2018')
# complaint_9.date=Date(date='07/17/2018')
# complaint_10.date=Date(date='07/18/2018')

# location
# zip = db.Column(db.Integer)
# borough = db.Column(db.Text)
# location_1=Location(zip='10314',borough='STATEN ISLAND')
# location_2=Location(zip='10460',borough='BRONX')
# location_3=Location(zip='11105',borough='QUEENS')
# location_4=Location(zip='11377',borough='QUEENS')
# location_5=Location(zip='11365',borough='QUEENS')
# location_6=Location(zip='11212',borough='BROOKLYN')
# location_7=Location(zip='10014',borough='MANHATTAN')
# location_8=Location(zip=' ',borough='BROOKLYN')
# location_9=Location(zip='10012',borough='MANHATTAN')
# location_10=Location(zip='11413',borough='QUEENS')


# Agency
#     name = db.Column(db.Text)
# agency_1 = Agency(name='DOF')
# agency_2 = Agency(name='NYPD')
# agency_3 = Agency(name='DOT')
# agency_4 = Agency(name='DOB')
# agency_5 = Agency(name='DSNY')


#Date:
#     date= db.Column(db.Date)

# date_1= Date(date='06/12/2018')
# date_2= Date(date='04/27/2018')
# date_3= Date(date='04/26/2018')
# date_4= Date(date='06/23/2018')
# date_5= Date(date='05/21/2018')
# date_6= Date(date='07/05/2018')
# date_7= Date(date='07/16/2018')
# date_8= Date(date='07/17/2018')
# date_9= Date(date='07/18/2018')
# db.session.add_all(
db.session.add_all([complaint_1,complaint_2,complaint_3,complaint_4,complaint_5,complaint_6,complaint_7,complaint_8,complaint_9,complaint_10])
# db.session.add_all(location_1,location_2,location_3,location_4,location_5,location_6,location_7,location_8,location_9,location_10)
# db.session.add_all(agency_1,agency_2,agency_3,agency_4,agency_5)

db.session.commit()

#
#City
#     name= db.Column(db.Text)
