from pymongo import MongoClient
from bson.objectid import ObjectId

class Db_handler:
    def __init__(self):
        self.db, self.membership_collection = self.connection()
        
    def connection(self):
        client = MongoClient('3.227.75.85', 80)
        db = client['losFieles']
        colllection = db['membership']

        return db, colllection

    def user_profile_recognition(self,user_id = None, user_card = None):
        get_one_user_response = self.get_one_user(user_id= user_id, user_card= user_card)

        if get_one_user_response['status'] == 'ok':
            response = {
                'status': 'ok',
                'type':get_one_user_response['user']['user_type']
            }

            return response
        else:
            return get_one_user_response

    def user_birth_day(self,user_id = None, user_card = None):
        get_one_user_response = self.get_one_user(user_id= user_id, user_card= user_card)

        if get_one_user_response['status'] == 'ok':
            response = {
                'status': 'ok',
                'user_birth_day':get_one_user_response['user']['user_birth_day']
            }

            return response
        else:
            return get_one_user_response

    
    def get_one_user(self,user_id = None, user_card = None):
        user = None

        if not(user_id  == None ):
            user = self.membership_collection.find_one({'user_id': user_id})

        elif not(user_card == None):
            user = self.membership_collection.find_one({'_id': ObjectId(user_card)})
        
        else:
            response = {
                "status":"err",
                "err": "neither user card nor id were specified "
            }
            return response
        
        if user == None:
            response = {
                "status":"err",
                "err": "User doesn't exist"
            }

            return response

        user["_id"] = str(user["_id"])

        response = {
            "status":"ok",
            "user": user
        }
        
        return response

    '''
        Gets -> name, user_id and type

        type -> 
            1 -> SoyLocatel
            2 -> SoyLocatel Medicos
            3 -> Club Bebes

        return -> card_id === _id
    '''
    def user_profile_affiliation(self, user_name, user_id, user_type, user_birth_day,user_email):
        
        _is_created = self.membership_collection.find_one({'user_id': user_id})

        response = {}

        if (_is_created):

            response = {
                "status":"err",
                "err": "User Id already exist"
            }
            return response

        user = {
            "user_name": user_name,
            "user_id": user_id,
            "user_type": user_type,
            "user_birth_day":user_birth_day,
            "user_email":user_email
        }
        result = self.membership_collection.insert_one(user).inserted_id
        id = str(result)
        response = {
            "status":"ok",
            "id": id
        }

        return response

    '''
        How can i validate applications 
        I mean that they can call me 
    '''
    def getUsers(self):
        users = []
        for user in self.membership_collection.find({}):
            user["_id"] = str(user["_id"])
            users.append(user)
        
        response = {
            "status":"ok",
            "users": users
        }

        return response



        
    
