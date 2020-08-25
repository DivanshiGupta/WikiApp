from wikipedia import wikipedia
from wtforms.validators import Required
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os
import json
import sys
from googletrans import Translator
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some?bamboozle#string-foobar'

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


class TitleForm(FlaskForm):
    title = StringField('Add title of page', validators=[Required()])
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    search = ''
    if request.method == "POST":
        title = request.form["title"]
        lang = request.form["lang"]
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
            translator = Translator()
            if lang != "en":
                message = translator.translate(message, dest=lang)
    return render_template('index.html', message=message, search=search)


@app.route('/template', methods=['GET', 'POST'])
def template():
    message = ''
    if request.method == "POST":
        title = request.form["title"]
        lang = request.form["lang"]
        json_object = json.dumps(title, indent=4)
        with open("test.json", "w") as outfile:
            outfile.write(json_object)
        x = "This page does not exist or does not belong to the CEO category"
        json_object = json.dumps(x, indent=4)
        with open("generated_templates.json", "w") as outfile:
            outfile.write(json_object)
        x = ""
        json_object = json.dumps(x, indent=4)
        with open("key_val.json", "w") as outfile:
            outfile.write(json_object)

        os.system("python3 key_val.py")
        os.system("python3 template.py")
        f = open('generated_templates.json')
        message = json.load(f)
        translator = Translator()
        if lang != "en":
            message = translator.translate(message, dest=lang)
        print(message)
    return render_template('template.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
