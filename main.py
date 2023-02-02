import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    print(flask.url_for('index'))
    return flask.render_template('index.html')


#Elon Musk
@app.route('/Elon_Musk/')
def Elon_Mask():
    return flask.render_template('Elon_mask/Elon_Mask.html')


@app.route('/Elon_Musk/Tesla')
def Tesla():
    return flask.render_template('Elon_mask/tesla/tesla.html')


@app.route('/Elon_Musk/SpaceX')
def spacex():
    return flask.render_template('Elon_mask/SpaceX/SpaceX.html')


@app.route('/Elon_Musk/Company')
def company():
    return flask.render_template('Elon_mask/Company/Company.html')


@app.route('/Elon_Musk/Tesla/Models')
def models():
    return flask.render_template('Elon_mask/tesla/tesla_models/Tesla_models.html')


#Steve Jobs
@app.route('/Steve_Jobs/')
def Steve_Jobs():
    return flask.render_template('Steve_Jobs/Steve_Jobs.html')


@app.route('/Steve_Jobs/Apple')
def Apple():
    return flask.render_template('Steve_Jobs/Apple/Apple.html')


def user(user_id):
    return f"пользователь: №{user_id}"


if __name__ == "__main__":
    app.run(debug=False)

