import json
import psycopg2
import jwt
import time
import bcrypt



def encrypt_user_password(password):
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword

def encode_user(uname, email):
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"userid": uname, "email" : email, "iat": int(time.time()), "exp": int(time.time()+3600)},
                              key='8x/A?D(G+KbPdSgVkYp3s6v9y$B&E)H@',
                              algorithm="HS256")

    return encoded_data

def decode_user(token: str):
    """
    :param token: jwt token
    :return:
    """
    decoded_data = jwt.decode(jwt=token,
                              key='secret', # enter the secret key used to encode the data
                              algorithms=["HS256"])

    print(decoded_data)

def validate_user_password(dbconn, uname, user_password):
    stored_password = ''
    user_password = user_password.encode('utf-8')
    cursor = dbconn.cursor()
    try:
        sql = "SELECT password, user_id, email from tx_users where uname = %s"
        data = uname
        cursor.execute(sql, (data,))
        record = cursor.fetchall()
        stored_password = record[0][0]
        user_id = record[0][1]
        email = record[0][2]
    except Exception as e:
        print(e)
    else:
        stored_password =  stored_password.encode('utf-8')
        print(stored_password)
        print(user_password)
        print(user_id)
        print(email)

        if bcrypt.checkpw(user_password, stored_password):
            token = encode_user(uname, email)
            print(token)
            return token
        else:
            return False
        
def get_user_id(dbconn, uname):
    cursor = dbconn.cursor()
    try:
        sql = "SELECT user_id FROM tx_users WHERE uname = %s"
        data = uname
        cursor.execute(sql, (data,))
        record = cursor.fetchall()
        user_id = record[0][0]
        print(record)
        
    except Exception as e:
        print(e)
    else:
        print(user_id)
        return user_id

        





    