from flask import Flask, request, render_template, url_for

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def rootpage():
    weight = ''
    height = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = request.form.get('weight')
    if request.method == 'POST' and 'height' in request.form:
        height = request.form.get('height')
    bmi = int(weight) / ((int(height) ** 2)
    return render_template("index.html",
                                bmi=bmi)

app.run()

