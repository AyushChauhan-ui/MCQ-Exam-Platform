from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ExamForm(FlaskForm):
    title = StringField('Exam Title', validators=[DataRequired()])
    description = StringField('Exam Description', validators=[DataRequired()])
    duration = IntegerField('Exam Duration (in minutes)', validators=[DataRequired(), NumberRange(min=1)])
    questions = IntegerField('Number of Questions', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Create Exam')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExamForm()
    if form.validate_on_submit():
        # Save the exam details to the database
        return 'Exam created successfully!'
    return render_template('index.html', form=form)
