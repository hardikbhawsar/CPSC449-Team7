import os
from flask import Blueprint, render_template, request, jsonify 
from src.constants.http_status_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import validators
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from src.database import User, db
from flask_jwt_extended import jwt_required,create_access_token, create_refresh_token,get_jwt_identity

#Definig the blueprint of the user route
user = Blueprint("user",__name__, url_prefix="/v1/user")
user.config={}
user.config['UPLOAD_FOLDER'] = 'src/static/file'
user.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

#Post method to register a new user
@user.post('/register')
def register():
    #These fields are mandatory to register a new user
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    organisation = request.json['organisation']
    address = request.json['address']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']

    #Password validation if length of password is less than 6
    if len(password)<6:
        return jsonify({'error':"Password is too short", 'error code':'400 Bad Request'}), HTTP_400_BAD_REQUEST

    #Username validation if length of username is less than 3
    if len(username)<3:
        return jsonify({'error':"Username is too short", 'error code':"400 Bad Request"}), HTTP_400_BAD_REQUEST

    #Email validation if the email is not in correct format
    if not validators.email(email):
        return jsonify({'error':"Email is not valid",'error code':'400 Bad Request'}), HTTP_400_BAD_REQUEST

    #Email validation if the email is already registered
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error':"Email already exists", 'error code':'400 Bad Request'}), HTTP_400_BAD_REQUEST

    #Username validation if the username already exists
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error':"Username already exists", 'error code':'400 Bad Request'}), HTTP_400_BAD_REQUEST

    #Converting the password in hash
    pwd_hash = generate_password_hash(password)
    user = User(username=username, password=pwd_hash, email=email, organisation=organisation, address = address, city=city,state=state,country=country)
    #Adding new user
    db.session.add(user)
    db.session.commit()

    #Diplaying success message if user is created
    return jsonify({
        'message':"User created!",
        'user': {
            'username': username, "email":email
        }
    }), HTTP_201_CREATED

#Post method to login the user
@user.route('/login',methods=['GET','POST'])
def login():
    email = request.json.get('email','')
    password = request.json.get('password','')

    user = User.query.filter_by(email=email).first()
    #CHecking the password
    if user:
        correct_pass = check_password_hash(user.password, password)

        if correct_pass:
            #If password is correct generating access token using JWT
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            #Displaying the access and refresh token
            return jsonify({
                'user':{
                    'refresh': refresh,
                    'access': access,
                    'username': user.username,
                    'email':user.email 
                }
            })
    #Displaying error message if user credentials are incorrect
    return jsonify({'error':'Incorrect credentials', 'error code':'401 Unauthorized'}), HTTP_401_UNAUTHORIZED

#Get method to get the details of the user using Access token 
@user.get('/aboutme')
@jwt_required()
def display():
    user_id=get_jwt_identity()
    user=User.query.filter_by(id=user_id).first()
    if user:
        return jsonify({
            'username':user.username,
            'email':user.email,
            'organisation': user.organisation,
            'address':user.address,
            'city':user.city,
            'state':user.state,
            'country':user.country
        }),HTTP_200_OK
    else:
        return jsonify({'error':'Invalid token', 'error code':'404 Not Found'}), HTTP_404_NOT_FOUND

#Regenrating the token using refresh token if token is expired
@user.route('/token/refresh',methods=['GET'])
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)
    if identity:
        return jsonify({
            'access': access
        }), HTTP_200_OK
    else:
        return jsonify({'error':'Incorrect credentials', 'error code':'404 Not Found'}), HTTP_404_NOT_FOUND
    
@user.errorhandler(HTTP_400_BAD_REQUEST)
def handle_400(e):
    return jsonify(
        {
        'error': "Bad Request"
        }
    )

@user.errorhandler(HTTP_404_NOT_FOUND)
def handle_404(e):
    return jsonify(
        {
        'error': "404 Not Found"
        }
    )

#Function to render the file upload page
@user.route('/upload')
def upload_file1():
   return render_template('upload.html')

#Fucntion to check the acceptable format
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf','jpg'}

#Post method to upload file
@user.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      if f and allowed_file(f.filename) and f.content_length<=5*1024*1024:
        f.save(os.path.join(os.path.abspath(os.path.dirname(f.filename)),user.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return jsonify({
            'msg':'file uploaded successfully'
        })
      else:
        return jsonify({
            'error':'Invalid file format. Please upload a file in PDF or JPG/JPEG format and less than 5 MB.'
        }),HTTP_400_BAD_REQUEST

#Function to get public page
@user.route('/public', methods=['GET'])
def public_data():
    return jsonify({
        'message':"This is only page which can be viewed publicly",
        'url':"http://localhost:5000/v1/user/public"
    }), HTTP_200_OK
