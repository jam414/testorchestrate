import json
import psycopg2
import jwt
import time
import bcrypt

def insert_new_test(dbconn, project_id, testname, severity, type, framework, runner, tag, platform, precondition, steps):
    
    cursor = dbconn.cursor()
    resp =''
    steps = steps
    sql =''
    val =''
    # print(type(steps))
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    
    # sql = "INSERT INTO tx_requirements(testcase_id, testcasename, testcaseseverity, testcasetype, framework, testrunner, tag, platform, pre_condition) VALUES (" + "nextval('test_id_generator'),'"+ testname + "','" + type + "','" + severity + "') RETURNING req_id;"
    if(framework == 'Test Case (Simple)'):
        sql = "INSERT INTO tx_testcases(testcase_id, creationdate, testcasename, testcaseseverity, testcasetype, framework, testrunner, tag, platform, pre_conditions, project_id, steps, expected_results) VALUES (nextval('test_id_generator'), now(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING testcase_id;"
        val = (testname, severity, type, framework, runner, tag, platform, precondition, project_id, steps[0], steps[1])
    if(framework == 'Test Case with Steps'):
        sql = "INSERT INTO tx_testcases(testcase_id, creationdate, testcasename, testcaseseverity, testcasetype, framework, testrunner, tag, platform, pre_conditions, project_id) VALUES (nextval('test_id_generator'), now(), %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING testcase_id;"
        val = (testname, severity, type, framework, runner, tag, platform, precondition, project_id)
    print(sql)
    print(val)
    try:
        resp = cursor.execute(sql, val)
        test_id = cursor.fetchone()[0]
        test_id = str(test_id)
        project_id = str(project_id)
        sql_update = "UPDATE tx_testcases SET testcase_code = 'TC" + test_id + "' WHERE testcase_id = "+ test_id + ";"
        sql_associate_projectID_with_testcase_id = "INSERT INTO tx_projects_tests (projectid, testid) VALUES (" + project_id + "," + test_id + ");"
        print(sql_update)
        cursor.execute(sql_update)
        cursor.execute(sql_associate_projectID_with_testcase_id)
        # print(value)
        if (framework == 'Test Case with Steps'):
            print('inside framework block')
            for step in steps:
                sql = "INSERT INTO tx_steps (step_id, step_index, step_name, step_expresult, testcase_id) VALUES (nextval('step_id_generator'), %s, %s, %s, %s) RETURNING step_id;"
                val = (step[0], step[1], step[2], test_id)
                resp = cursor.execute(sql, val)
                step_id = cursor.fetchone()[0]
                step_id = str(step_id)
                sql_update = "UPDATE tx_steps SET step_code = 'SC" + step_id + "' WHERE step_id = "+ step_id + ";"
                cursor.execute(sql_update)
                sql_associate_testcase_id_with_step_id = "INSERT INTO tx_testcase_steps (stepid, testcaseid) VALUES (" + step_id + "," + test_id + ");"
                cursor.execute(sql_associate_testcase_id_with_step_id)
    except Exception as e:
        print(e)
        return e
    else:
        resp1 = dbconn.commit()

        print(resp)
        print(resp1)
        return resp1

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
    
def load_tests(dbconn, project_id, project_name):
    cursor = dbconn.cursor()
    resp =''
    # sql = "INSERT INTO tx_requirements(?,?,?) VALUES(name, )"
    # sql = "INSERT INTO tx_requirements(reqid, reqname, reqdesc, reqtype, reqpriority, reqseverity), values (123, name, 'SOme desc', type, 'Critical',severity)"
    # sql = "SELECT FROM tx_user(user_id) WHERE uname = "+username+";"
    sql = "SELECT projectid FROM tx_user_projects WHERE userid = %s"
    # sql = "INSERT INTO tx_requirements(req_id, reqname, reqtype, reqseverity) VALUES (" + "nextval('user_id_generator'),'"+ name + "','" + type + "','" + severity + "') RETURNING req_id;"
    # sql1 = '''
    #             SELECT tx_requirements.req_id, tx_requirements.req_code, tx_requirements.reqname, tx_requirements.reqtype, tx_requirements.reqseverity
    #             FROM tx_requirements
    #             INNER JOIN tx_projects_reqs ON tx_requirements.req_id = tx_projects_reqs.reqid
    #             WHERE tx_projects_reqs.projectid = %s order by req_id asc
    #         '''
    sql1 = '''
                SELECT *
                FROM tx_testcases
                INNER JOIN tx_projects_tests ON tx_testcases.testcase_id = tx_projects_tests.testid
                WHERE tx_projects_tests.projectid = %s order by testcase_id asc
            '''
                    

    try:
        data = project_id
        cursor.execute(sql1, (data,))
        record = cursor.fetchall()
        print(type(record))

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
    
def get_steps(dbconn, test_id):
    
    cursor = dbconn.cursor()
    resp =''
    sql = '''
            SELECT tx_steps.step_index, tx_steps.step_name, tx_steps.step_expresult
            FROM tx_steps
            INNER JOIN tx_testcase_steps ON tx_steps.step_id = tx_testcase_steps.stepid
            WHERE tx_testcase_steps.testcaseid = %s    
    '''
    try:
        data = test_id
        resp = cursor.execute(sql, (data,))
        record = cursor.fetchall()
        # print(type(record))

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

    
def delete_tests(dbconn, test_ids):
    sql1 = "DELETE FROM tx_projects_tests WHERE testid IN %s"
    sql2 = "DELETE FROM tx_testcase_steps WHERE testcaseid IN %s"
    sql3 = "DELETE FROM tx_testcases WHERE testcase_id IN  %s"
    sql4 = "DELETE FROM tx_steps WHERE testcase_id IN %s"
    resp =''
    print("Delete test_ids?")
    print(test_ids)
    strg = ''
    if (len(test_ids) == 1):
        strg = eval(", ".join(str(x) for x in test_ids))
        sql1 = "DELETE FROM tx_projects_tests WHERE testid = %s"
        sql2 = "DELETE FROM tx_testcase_steps WHERE testcaseid = %s"
        sql3 = "DELETE FROM tx_testcases WHERE testcase_id = %s"
        sql4 = "DELETE FROM tx_steps WHERE testcase_id = %s"
        
    else:
        strg = eval("(" +  ", ".join(str(x) for x in test_ids) + ")")
        print(strg)

    
    cursor = dbconn.cursor()
    
    

    try:
        cursor.execute(sql1, (strg,))
        cursor.execute(sql2, (strg,))
        cursor.execute(sql4, (strg,))
        cursor.execute(sql3, (strg,))
        # cursor.execute(sql4, (strg,))
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
    
