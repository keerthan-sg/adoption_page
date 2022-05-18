from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField


class AddForm(FlaskForm):
    name =  StringField('Name of puppy:')
    submit = SubmitField('add puppy')

class DelForm(FlaskForm):
    id = IntegerField('Enter id of puppy to remove')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    name = StringField('Enter name of Owner')
    pup_id = IntegerField('Enter pup id to link with owner')
    submit = SubmitField('Add owner')