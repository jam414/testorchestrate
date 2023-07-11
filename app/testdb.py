import json
import psycopg2
import jwt
import time
import bcrypt
import user
import requirements
import tests


# def validate_user_password(user_password, stored_password):
#     user_password = user_password.encode('utf-8')
#     if bcrypt.checkpw(user_password, stored_password):
#         return True
#     else:
#         return False
    
def create_user(uname, fname, lname, email, dept, password):
    connection = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port=5432)
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    print(hashedPassword)
    cursor = connection.cursor()
    sql = "INSERT INTO tx_users (user_id, uname, fname, lname, email, dept, password) VALUES (" + "nextval('user_id_generator'),'"+ uname + "','" + fname + "','" + lname + "','" + email + "','" + dept + "','" + hashedPassword.decode() + "')"
    print(sql)
    try:
        resp = cursor.execute(sql)
    except Exception as e:
        print('exception thrown')
        print(e)
        return e
    else:
        resp1 = connection.commit()
        print(resp)
        print(resp1)
        return

    finally:
        return 
    
   






# sql = "SELECT password, user_id, email from tx_users where uname = %s"

# data = 'jahmed'
# connection = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port=5432)
# cursor = connection.cursor()
# cursor.execute(sql, (data,))
# record = cursor.fetchall()
# stored_password = (record[0][0])
# # for x in record:
#     # print(x[0])
#     # print(x[1])
#     # print(x[2])
#     # print("Data from Database:- ", record)
#     # return x[0], x[1], x[2]
# # create_user('jahmed', 'jameel', 'ahmed', 'jameel@email.com', 'Marketing', 'password' )
# # user1 =  user.User()
# value = user.validate_user_password(connection, 'jahmed', 'password')
# print (value)


if __name__ == "__main__":
    dbconn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port=5432)
    # user_id = user.get_user_id(dbconn, 'jahmed')
    # records = requirements.load_requirements(dbconn, 100, 'Equity Market')
    # insert_new_test(dbconn, project_id, testname, severity, type, framework, runner, tag, platform, precondition, steps):
    # steps = "[['1','stepname', 'expresult']]"
    # steps = json.dumps(steps)
    create_user('jameel1', 'jameel1', 'ahmed', 'jameel11@email.com', 'Sales', 'password' )

    # resp = tests.insert_new_test(dbconn, 100, 'test', 'critical', 'functional', 'testcase_s', 'automated','tag', 'windows', 'preconditions', steps )
    # print(resp)
    




