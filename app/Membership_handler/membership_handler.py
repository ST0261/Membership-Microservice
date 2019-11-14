from flask import Blueprint, render_template, abort, jsonify, request
from Database_user_handler.db_handler import Db_handler as db

db_handler = db()


membership_router = Blueprint('membership_api', 
                                import_name=__name__, 
                                url_prefix='/membership')

def set_db(db):
    db_handler = db;


@membership_router.route('/')
def index():
    return "Membership handler component"

@membership_router.route('/recognition/id/<id>', methods=['GET'])
def id_recognition(id):
    return jsonify(db_handler.get_one_user(user_id = id))

@membership_router.route('/recognition/card_id/<car_id>', methods=['GET'])
def car_id_recognition(car_id):
    return jsonify(db_handler.get_one_user(user_card = car_id))

@membership_router.route('/affiliation/', methods=['POST'])
def affiliation():
    data = request.get_json()
    print(data)

    user_name = data['user_name']
    user_id = data['user_id']
    user_type = data['user_type']
    user_birth_day = data['user_birth_day']
    user_email = data['user_email']

    response = db_handler.user_profile_affiliation(user_name, user_id, user_type, user_birth_day,user_email)

    return jsonify(response)

@membership_router.route('/user/profile/id/<id>', methods=['GET'])
def user_profile_id(id):
    return jsonify(db_handler.user_profile_recognition(user_id = id))

@membership_router.route('/user/profile/card_id/<mongo_id>', methods=['GET'])
def user_profile_card_id(mongo_id):
    return jsonify(db_handler.user_profile_recognition(user_card = mongo_id))

@membership_router.route('/user/birthday/id/<id>', methods=['GET'])
def user_birthday_id(id):
    return jsonify(db_handler.user_birth_day(user_id = id))

@membership_router.route('/user/birthday/card_id/<mongo_id>', methods=['GET'])
def user_birthday_card_id(mongo_id):
    return jsonify(db_handler.user_birth_day(user_card = mongo_id))


@membership_router.route('/user/all', methods=['GET'])
def user_all():
    return jsonify(db_handler.getUsers())