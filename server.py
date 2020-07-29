from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from wikipedia import wikipedia

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some?bamboozle#string-foobar'

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


class TitleForm(FlaskForm):
    title = StringField('Add title of page', validators=[Required()])
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TitleForm()
    message = ''
    search = ''
    if form.validate_on_submit():
        title = form.title.data
        search = wikipedia.search(title)
        y = []
        if search == y:
            search = 'This Wikipedia page does not exists.'
            message = ''
        else:
            try:
                message = wikipedia.summary(search[0])
            except wikipedia.DisambiguationError as e:
                s = e.options[0]
                message = wikipedia.summary(s)
            search = 'This Wikipedia page already exists. Following is a summary of the same'
            # message = wikipedia.summary(title)
    return render_template('index.html', form=form, message=message, search=search)

# # @app.route('/add', methods=['POST'])
# @app.route('/add',methods=('GET','POST'))

# def add():

#     return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
