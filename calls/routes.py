import pdb

from calls.models import *
from calls import db
from sqlalchemy import func

def locations():
    locations = Location.query.all()
    location_dict = [{'label': location.zip, 'value': location.id} for location in locations]
    return location_dict

def boroughs():
    # the number of times a complaint shows up in a borough
    boroughs= Borough.query.all()
    borough_dict=[{'label': borough.name, 'value': borough.id} for borough in boroughs]
    return borough_dict


def agencies():
    agencies = Agency.query.all()
    agency_dict = [{'label': agency.name, 'value': agency.id} for agency in agencies]
    return agency_dict

def complaints():
    complaints = Complaint.query.all()
    complaint_dict = [{'label':complaint.type, 'value':complaint.id} for complaint in complaints]
    return complaint_dict

def filter_complaints(query,location_values=None):
    if location_values:
        query = query.filter(Complaint.location_id.in_(location_values))
    return query

def complaint_histogram(location_values=None):
    types_query = db.session.query(Complaint.type,func.count(Complaint.id)).group_by(Complaint.type)
    filtered_complaints = filter_complaints(types_query,location_values=location_values)
    complaint_counts = filtered_complaints.all()
    # complaint_types = types_query.all()

    x_values = [complaint_count[0] for complaint_count in complaint_counts]
    y_values = [complaint_count[1] for complaint_count in complaint_counts]

    # pdb.set_trace()
    return {
        'data': [
            {
                'x': x_values,
                'y': y_values,
                'name': 'Trace 1',
                'type':'bar'
            }
        ],
        'layout': {'xaxis': {'range': [0, 7]}}
        }
def borough_count_histogram():
    location_query= db.session.query(Complaint.borough_name, func.count(Complaint.type)).group_by(Complaint.borough_name)
    location_counts= location_query.all()
    x_values = [location_count[0] for location_count in location_counts]
    y_values = [location_count[1] for location_count in location_counts]
    return {
        'data': [
            {
                #'x': x_values,
                'values': [location_count[1] for location_count in location_counts],
                'labels': [location_count[0] for location_count in location_counts],
                # 'name':
                'type':'pie'
                }
            ]
            # 'layout': {'xaxis': {'range': [0, 10]}}
            }

# def filter_borough(query,location_borough=None):
#     if location_borough:
#         query = query.filter(Complaint.borough_name.in_(location_borough))
#     return query
#
# def borough_histogram(location_borough=None):
#     # complaint_counts= db.session.query(Complaint.type,func.count(Complaint.id)).group_by(Complaint.type)
#     types_query= db.session.query(Complaint.borough_name, Complaint.type ,func.count(Complaint.type)).group_by(Complaint.type)
#     filtered_borough = filter_borough(types_query,location_borough= location_borough)
#     b_counts = filtered_borough.all()
#     # c_counts= complaint_counts.all()
#
#     x_values = [b_count[1] for b_count in b_counts]
#     y_values = [b_count[2] for b_count in b_counts]
#
#     # pdb.set_trace()
#     return {
#         'data': [
#             {
#                 'x': x_values,
#                 'y': y_values,
#                 'name': 'Trace 1',
#                 'type':'bar'
#             }
#         ],
#         'layout': {'xaxis': {'range': [0, 7]}}
    # }
# def filter_borough(query, borough_name):
#     if borough_name:
#         query = query.filter(Complaint.borough_name.in_(location_borough))
#     return query
def borough_complaints():
    m=db.session.query(Complaint.type, func.count(Complaint.type)).group_by(Complaint.type).filter(Complaint.borough_name=="MANHATTAN")
    m_counts= m.all()
    b=db.session.query(Complaint.type, func.count(Complaint.type)).group_by(Complaint.type).filter(Complaint.borough_name=="BROOKLYN")
    b_counts= b.all()
    c=db.session.query(Complaint.type, func.count(Complaint.type)).group_by(Complaint.type).filter(Complaint.borough_name=="BRONX")
    c_counts= c.all()
    d=db.session.query(Complaint.type, func.count(Complaint.type)).group_by(Complaint.type).filter(Complaint.borough_name=="QUEENS")
    d_counts= d.all()
    e=db.session.query(Complaint.type, func.count(Complaint.type)).group_by(Complaint.type).filter(Complaint.borough_name=="STATEN ISLAND")
    e_counts= e.all()
    # c_counts= complaint_counts.all()

    mx_values = [m_count[0] for m_count in m_counts]
    my_values = [m_count[1] for m_count in m_counts]
    bx_values = [b_count[0] for b_count in b_counts]
    by_values = [b_count[1] for b_count in b_counts]
    cx_values = [c_count[0] for c_count in c_counts]
    cy_values = [c_count[1] for c_count in c_counts]
    dx_values = [d_count[0] for d_count in d_counts]
    dy_values = [d_count[1] for d_count in d_counts]
    ex_values = [e_count[0] for e_count in e_counts]
    ey_values = [e_count[1] for e_count in e_counts]
    # pdb.set_trace()
    return {
        'data': [
            {'x': mx_values,
            'y': my_values,
            'name': 'Manhattan',
            'type': 'bar'
            },
            {'x': bx_values,
            'y': by_values,
            'name': 'Brooklyn',
            'type': 'bar'},
            {'x': cx_values,
            'y': cy_values,
            'name': 'Bronx',
            'type': 'bar'},
            {'x': dx_values,
            'y': dy_values,
            'name': 'Queens',
            'type': 'bar'},
            {'x': ex_values,
            'y': ey_values,
            'name': 'Staten Island',
            'type': 'bar'},
        ],
        'layout': {'xaxis': {'range': [-0.5, 7]}}
    }
