from flask import Flask, render_template, Response, request
import json
import psycopg2
import jwt
import time
import bcrypt
import user
import requirements
import projects
import tests123
import re
import issues
import defects

dbconn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port=5432)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/test")
def test():
    return render_template("testorchestrate.html")

@app.route("/test-table")
def test_table():
    return render_template("test-table.html")
    
@app.route("/about")
def about():
    return render_template("table-sort.html")

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/dashboard")
def menu():
    return render_template("dashboard_google.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/load_reqs", methods = ['POST'])
def load_reqs():
    project_id = request.form['jdata[project_id]']
    project_name = request.form['jdata[project_name]']
    result = requirements.load_requirements(dbconn, project_id, project_name)
    return result




@app.route("/reqs")
def reqs():
    return render_template("reqs.html")

@app.route('/add_new_req', methods = ['POST'])
def get_post_javascript_data():
    resp = ''
    req_name = request.form['jdata[Name]']
    test_type = request.form['jdata[Type]']
    req_severity = request.form['jdata[Severity]']
    project_id = request.form['jdata[project_id]']
    req_id = request.form['jdata[req_id]']
    print(req_name)
    print(test_type)
    print(req_severity)
    print(project_id)
    print(req_id)
    if (int(req_id) > 0):
        resp = requirements.update_req(dbconn, req_name, test_type, req_severity, project_id, req_id)
        print(type (req_id))
    else:
        resp = requirements.insert_new_req(dbconn, req_name, test_type, req_severity, project_id)
    print(resp)
    if(resp):
        return "New Requirement added successfully!"
    else:
        return " ERROR: Requirement could not be added!"

    # jsdata = request.form['jdata']
    # print(jsdata)
@app.route('/delete_req', methods = ['POST'])
def delete_req():
    req_ids = request.form['jdata[req_ids]']
    delete_list = req_ids.split(',')
    print(delete_list)
    resp = requirements.delete_requirements(dbconn, delete_list)
    print(resp)
    if(resp > 0):
        return "Requirement(s) deleted successfully!"
    else:
        return "Could not delete the Requirements!"

    

@app.route('/login', methods=['POST'])
def get_data():
    data = json.loads(request.data)
    # print('Recieved from client: {}'.format(data))
    username = data['username']
    # print(username)
    password = data['password']
    # print(password)

    token = user.validate_user_password(dbconn, username, password)
    project_list = projects.get_project_list(dbconn, username)
    print(project_list)

    if (token):
        # project_list = projects.get_project_list(dbconn, username)
        # print(project_list)
        resp = {
            "result" : "passed",
            "token" : token,
            "project_list" : project_list
        }
        return Response(json.dumps(resp))
    
    else:
        resp = {
            "result" : "failed",
            "resp" : "Incorrect username of password. Please check and try again."
        }
        return Response(json.dumps(resp))
    
@app.route("/tests")
def tests():
    return render_template("tests.html")

@app.route("/add_test")
def add_test():
    return render_template("add_test.html")

@app.route("/load_tests", methods = ['POST'])
def load_tests():
    project_id = request.form['jdata[project_id]']
    project_name = request.form['jdata[project_name]']
    result = tests123.load_tests(dbconn, project_id, project_name)
    return result

@app.route('/add_new_test', methods = ['POST'])
def add_new_test():
    resp = ''
    project_id = request.form['jdata[project_id]']
    testname = request.form['jdata[testname]']
    severity = request.form['jdata[severity]']
    type = request.form['jdata[type]']
    framework = request.form['jdata[framework]']
    runner = request.form['jdata[runner]']
    tag = request.form['jdata[tag]']
    platform = request.form['jdata[platform]']
    precondition = request.form['jdata[precondition]']
    steps = request.form['jdata[steps]']
    steps = json.loads(steps)
    print(project_id)
    print(testname)
    print(severity)
    print(type)
    print(framework)
    print(runner)
    print(tag)
    print(platform)
    print(precondition)
    print(steps)
    

    # resp = tests123.insert_new_test(dbconn, 100, 'test', 'critical', 'functional', 'testcase_s', 'automated','tag', 'windows', 'preconditions', steps )
    resp = tests123.insert_new_test(dbconn, project_id, testname, severity, type, framework, runner, tag, platform, precondition, steps)
    print(resp)

    return "Test Case Added Successfully"

   
    # print(req_name)
    # print(test_type)
    # print(req_severity)
    # print(project_id)
    # print(req_id)
    # if (int(req_id) > 0):
    #     resp = requirements.update_req(dbconn, req_name, test_type, req_severity, project_id, req_id)
    #     print(type (req_id))
    # else:
    #     resp = requirements.insert_new_req(dbconn, req_name, test_type, req_severity, project_id)
    # print(resp)
    # if(resp):
    #     return "New Requirement added successfully!"
    # else:
    #     return " ERROR: Requirement could not be added!"

@app.route('/get_steps', methods = ['POST'])
def get_steps():
    test_id = request.form['jdata[test_id]']
    print(test_id)
    print(type(test_id))
    number_pattern = "^\\d+$"
    if (re.match(number_pattern, test_id)):
        result = tests123.get_steps(dbconn, test_id)
        return result
    else:
        return "Test id should be numbers only!"

@app.route('/delete_tests', methods = ['POST'])
def delete_tests():
    test_ids = request.form['jdata[test_ids]']
    delete_list = test_ids.split(',')
    print(delete_list)
    resp = tests123.delete_tests(dbconn, delete_list)
    print(resp)
    # if(resp > 0):
    return "Test(s) deleted successfully!"
    # else:
    #     return "Could not delete the Requirements!"

@app.route("/defects")
def defects():
    return render_template("defects.html")


@app.route("/load_issues", methods = ['POST'])
def load_issues():
    project_id = request.form['jdata[project_id]']
    project_name = request.form['jdata[project_name]']
    result = issues.load_issues(dbconn, project_id, project_name)
    return result

    
if __name__ == "__main__":
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)



