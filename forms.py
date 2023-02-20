from wtforms import Form, validators
from wtforms import StringField
#from wtforms import IntegerField
#from wtforms import TextAreaField

class ExperimentForm(Form):
    
    exname = StringField('Experiment name (or number): ', [validators.DataRequired()])
    piname = StringField('Pilot name: ', [validators.DataRequired()])
    timeint = StringField('Time interval (in minutes): ', [validators.DataRequired()])
    #timeint = IntegerField('Time interval (in minutes): ', [validators.DataRequired()])

    def validate(self):
        if not super().validate():
            return False
                
        try:
            int(self.timeint.data)
            return True
        except ValueError:
            self.timeint.errors.append('Please, use an integer number for Time interval')
            return False
