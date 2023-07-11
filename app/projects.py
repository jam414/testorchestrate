import json
import psycopg2
import jwt
import time
import bcrypt
import user


def get_project_list(dbconn, username):
    cursor = dbconn.cursor()
    resp =''
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    # sql = "SELECT FROM tx_user(user_id) WHERE uname = "+username+";"
    sql = "SELECT projectid FROM tx_user_projects WHERE userid = %s"
    # sql = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('user_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
    sql1 = '''
                SELECT tx_projects.project_id, tx_projects.pname
                FROM tx_projects
                INNER JOIN tx_user_projects ON tx_projects.project_id = tx_user_projects.projectid
                WHERE tx_user_projects.userid = %s
            '''
                    

    try:
        user_id = user.get_user_id(dbconn, username)
        print(user_id)
        data = user_id
        cursor.execute(sql1, (data,))
        record = cursor.fetchall()
        print(record)

        # record = json.dumps(record)

        print(record)

        # return record

        for x in record:
   
            # iterate in each tuple element
            for y in x:
                print(y)

    except Exception as e:
        print(e)
        return e
    else:
        resp1 = dbconn.commit()

        print(resp)
        print(resp1)
        # return record

    finally:
        return record