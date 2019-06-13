from flask import Flask,render_template, request, session, Response, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from database import connector
from model import entities
import json


db = connector.Manager()
engine = db.createEngine()
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

#CHECK LOGIN
@login_manager.user_loader
def load_user(user_id):
    db_session = db.getSession(engine)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - L O G I N - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/authenticate', methods = ["POST"])
def authenticate():
    message = json.loads(request.data)
    email = message['email']
    password = message['password']
    #2. look in database
    db_session = db.getSession(engine)
    try:
        user = db_session.query(entities.Users).filter(entities.Users.email == email).one()
        if check_password_hash(user.password, password):
            message = {'message': 'Authorized'}
            return Response(message, status=200, mimetype='application/json')
        else:
            message = {'message': 'Unauthorized'}
            return Response(message, status=401, mimetype='application/json')
    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - L O G O U T - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return render_template('index.html')

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - -  C R E A T E - U S E R - - - - -  - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/createUser', methods = ["POST"])
def createUser():
    message = json.loads(request.data)
    try:
        hashed_password = generate_password_hash(message['password'], method='sha256')
        user = entities.Users(
        firstName=message['firstName'],
        lastName=message['lastName'],
        password=hashed_password,
        email=message['email']
        )
        session = db.getSession(engine)
        session.add(user)
        session.commit()
        message = {'message': 'User Created'}
        return Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Error'}
        return Response(message, status=401, mimetype='application/json')

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - -  C R U D - U S E R S  - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Users)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

@app.route('/users', methods = ['POST'])
def post_users():
    c =  json.loads(request.form['values'])
    hashed_password = generate_password_hash(c['password'], method='sha256')
    user = entities.Users(
        firstName =c['firstName'],
        lastName =c['lastName'],
        password = hashed_password,
        email =c['email']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Created User'

@app.route('/users', methods = ['PUT'])
def update_users():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.Users).filter(entities.Users.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return 'Updated User'

@app.route('/users', methods = ['DELETE'])
def delete_user():
    id = request.form['key']
    session = db.getSession(engine)
    messages = session.query(entities.Users).filter(entities.Users.id == id)
    for message in messages:
        session.delete(message)
    session.commit()
    return "User Deleted"\


# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - -  O L D - M E T H O D  - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

@app.route("/loginold", methods=['GET', 'POST'])
def loginold():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'
    return render_template('login.html', form=form)


"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(email=form.email.data, firstName=form.firstName.data, lastName=form.lastName.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('register.html', form=form)

"""

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - C R U D - C H A M P I O N S H I P - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #

#create championship
@app.route('/championship', methods = ['POST'])
def post_championship():
    c =  json.loads(request.form['values'])
    championship = entities.Championship(
        title =c['title'],
        maxCompetitors =c['maxCompetitors'],
        location =c['location']
    )
    session = db.getSession(engine)
    session.add(championship)
    session.commit()
    return 'Created Championship'

#read championship
@app.route('/championship', methods = ['GET'])
def get_championship():
    session = db.getSession(engine)
    dbResponse = session.query(entities.Championship)
    data = []
    for championship in dbResponse:
        data.append(championship)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

#update championship
@app.route('/championship', methods = ['PUT'])
def update_championship():
    session = db.getSession(engine)
    id = request.form['key']
    championship = session.query(entities.Championship).filter(entities.Championship.id == id).first()
    c = json.loads(request.form['values'])
    for key in c.keys():
        setattr(championship, key, c[key])
    session.add(championship)
    session.commit()
    return 'Updated Championship'

#delete championship
@app.route('/championship', methods = ['DELETE'])
def delete_championship():
    id = request.form['key']
    session = db.getSession(engine)
    championships = session.query(entities.Championship).filter(entities.Championship.id == id)
    for championship in championships:
        session.delete(championship)
    session.commit()
    return "User Deleted"

# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - C R U D - S A I L I N G - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #
#create sailing
@app.route('/sailing', methods = ['POST'])
def post_sailing():
    c =  json.loads(request.form['values'])
    inscription = entities.InscriptionSailing(
        sailingNumber=c['sailingNumber'],
        category=c['category'],
        user_id=c['user_id'],
        championship_id=c['championship_id']
    )
    session = db.getSession(engine)
    session.add(inscription)
    session.commit()
    return 'Created Sailing Inscription'

#read sailing
@app.route('/sailing', methods = ['GET'])
def get_sailing():
    session = db.getSession(engine)
    dbResponse = session.query(entities.InscriptionSailing)
    data = []
    for inscription in dbResponse:
        data.append(inscription)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

#update sailing
@app.route('/sailing', methods = ['PUT'])
def update_sailing():
    session = db.getSession(engine)
    id = request.form['key']
    inscription = session.query(entities.InscriptionSailing).filter(entities.InscriptionSailing.id == id).first()
    c = json.loads(request.form['values'])
    for key in c.keys():
        setattr(inscription, key, c[key])
    session.add(inscription)
    session.commit()
    return 'Updated Sailing Inscription'

#delete sailing
@app.route('/sailing', methods = ['DELETE'])
def delete_sailing():
    id = request.form['key']
    session = db.getSession(engine)
    inscription = session.query(entities.InscriptionSailing).filter(entities.InscriptionSailing.id == id)
    for inscription in inscriptions:
        session.delete(inscription)
    session.commit()
    return "Sailing Inscription Deleted"



# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - C R U D - S O C C E R - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #
#create soccer
"""
@app.route('/soccer', methods = ['POST'])
def post_soccer():
    j = json.loads(request.form['values'])
    inscripcion = entities.InscriptionSoccer(
        soccerTeam=j['soccerTeam'],
        category=j['category'],
        user_id=j['user_id'],
        championship_id=j['championship_id']
        )
    session = db.getSession(engine)
    session.add(inscription)
    session.commit()
    return 'Created Soccer Inscription'

#read soccer
@app.route('/soccer', methos = ['GET'])
def get_soccer():
    session = db.getSession(engine)
    dbResponse = session.query(entities.InscriptionSoccer)
    data = []
    for inscription in dbResponse:
        data.append(inscription)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

#update soccer
@app.route('/soccer', methods = ['PUT'])
def update_soccer():
    session = db.getSession(engine)
    id = request.form['key']
    inscription = session.query(entities.InscriptionSoccer).filter(entities.InscriptionSoccer.id == id).first()
    j = json.loads(request.form['values'])
    for key in j.keys():
        setattr(inscription, key, j[key])
    session.add(inscription)
    session.commit()
    return 'Updated Soccer Inscription'

#delete soccer
@app.route('/soccer', methods = ['DELETE'])
def delete_soccer():
    id = request.form['key']
    session = db.getSession(engine)
    inscription = session.query(entities.InscriptionSoccer).filter(entities.InscriptionSoccer.id == id)
    for inscription in inscriptions:
        session.delete(inscription)
    session.commit()
    return "Soccer Inscription Deleted"
"""
# - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - N O T I F I C A T I O N S - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - #
#create notification
@app.route('/notifications', methods = ['POST'])
def post_notifications():
    c =  json.loads(request.form['values'])
    notification = entities.Notification(
        date=c['date'],
        text=c['text'],
        type=c['type']
    )
    session = db.getSession(engine)
    session.add(inscription)
    session.commit()
    return 'Created Sailing Inscription'

#read notification
@app.route('/sailing', methods = ['GET'])
def get_sailing():
    session = db.getSession(engine)
    dbResponse = session.query(entities.InscriptionSailing)
    data = []
    for inscription in dbResponse:
        data.append(inscription)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')

#update notification
@app.route('/sailing', methods = ['PUT'])
def update_sailing():
    session = db.getSession(engine)
    id = request.form['key']
    inscription = session.query(entities.InscriptionSailing).filter(entities.InscriptionSailing.id == id).first()
    c = json.loads(request.form['values'])
    for key in c.keys():
        setattr(inscription, key, c[key])
    session.add(inscription)
    session.commit()
    return 'Updated Sailing Inscription'

#delete notification
@app.route('/sailing', methods = ['DELETE'])
def delete_sailing():
    id = request.form['key']
    session = db.getSession(engine)
    inscription = session.query(entities.InscriptionSailing).filter(entities.InscriptionSailing.id == id)
    for inscription in inscriptions:
        session.delete(inscription)
    session.commit()
    return "Sailing Inscription Deleted"


@app.route("/inscripcion")
def inscripcion():
    return render_template('form1.html')



if __name__ == '__main__':
    app.secret_key = ".."
    app.run(debug=True,port=8020, threaded=True, host=('0.0.0.0'))
