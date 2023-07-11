import json
import psycopg2
import jwt
import time
import bcrypt

def insert_new_req(dbconn, name, type, severity, project_id):
    cursor = dbconn.cursor()
    resp =''
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    
    sql = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('req_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
    print(sql)
    try:
        resp = cursor.execute(sql)
        value = cursor.fetchone()[0]
        value = str(value)
        project_id = str(project_id)
        sql_update = "UPDATE tx_requirements SET req_code = 'RC" + value + "' WHERE req_id = "+ value + ";"
        sql_associate_projectID_with_ReqId = "INSERT INTO tx_projects_reqs (projectid, reqid) VALUES (" + project_id + "," + value + ");"
        print(sql_update)
        cursor.execute(sql_update)
        cursor.execute(sql_associate_projectID_with_ReqId)
        print(value)
        

    except Exception as e:
        print(e)
        return e
    else:
        resp1 = dbconn.commit()

        print(resp)
        print(resp1)
        return

    finally:
        return True
    
def update_req(dbconn, name, type, severity, project_id, req_id):
    cursor = dbconn.cursor()
    resp =''
    print(req_id)
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    
    # sql = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('user_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
    
    try:
        
        # sql_updat = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('user_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
        sql_update = "UPDATE tx_requirements SET reqname = '" + name + "', reqtype='"+ type +"', reqseverity = '"+ severity +"', project_id="+ project_id + " WHERE req_id = "+ req_id + ";"
        # sql_associate_projectID_with_ReqId = "INSERT INTO tx_projects_reqs (projectid, reqid) VALUES (" + project_id + "," + value + ");"
        print(sql_update)
        cursor.execute(sql_update)
        
        

    except Exception as e:
        print(e)
        return e
    else:
        resp1 = dbconn.commit()

        print(resp)
        # print(resp1)
        return

    finally:
        return True
    
def load_requirements(dbconn, project_id, project_name):
    cursor = dbconn.cursor()
    resp =''
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    # sql = "SELECT FROM tx_user(user_id) WHERE uname = "+username+";"
    sql = "SELECT projectid FROM tx_user_projects WHERE userid = %s"
    # sql = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('user_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
    sql1 = '''
                SELECT tx_requirements.req_id, tx_requirements.req_code, tx_requirements.reqname, tx_requirements.reqtype, tx_requirements.reqseverity
                FROM tx_requirements
                INNER JOIN tx_projects_reqs ON tx_requirements.req_id = tx_projects_reqs.reqid
                WHERE tx_projects_reqs.projectid = %s order by req_id asc
            '''
                    

    try:
        data = project_id
        cursor.execute(sql1, (data,))
        record = cursor.fetchall()
        # print(record)

        # record = json.dumps(record)

        # print(record)

        # return record

        # for x in record:
   
        #     # iterate in each tuple element
        #     for y in x:
        #         print(y)

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
    
def delete_requirements(dbconn, req_ids):
    sql1 = "DELETE FROM tx_projects_reqs WHERE reqid IN %s"
    sql = "DELETE FROM tx_requirements WHERE req_id IN %s"
    resp =''
    print("Delete Req_ids?")
    print(req_ids)
    strg = ''
    if (len(req_ids) == 1):
        strg = eval(", ".join(str(x) for x in req_ids))
        sql1 = "DELETE FROM tx_projects_reqs WHERE reqid = %s"
        sql = "DELETE FROM tx_requirements WHERE req_id = %s"
        
    else:
        strg = eval("(" +  ", ".join(str(x) for x in req_ids) + ")")
        print(strg)

    
    cursor = dbconn.cursor()
    
    

    try:
        cursor.execute(sql1, (strg,))
        cursor.execute(sql, (strg,))
        # record = cursor.fetchall()
        # print(record)

        # record = json.dumps(record)

        # print(record)

        # return record

        # for x in record:
   
        #     # iterate in each tuple element
        #     for y in x:
        #         print(y)

    except Exception as e:
        print(e)
        return e
    else:
        dbconn.commit()

        
        
        # return record

    finally:
        return cursor.rowcount
    
