CREATE TABLE tx_users (
    user_id INT PRIMARY KEY,
	uname VARCHAR(50) NOT NULL,
    fname VARCHAR(50) NOT NULL,
	lname VARCHAR(50),
    email VARCHAR(50) NOT NULL,
	dept VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE tx_projects (
    project_id INT PRIMARY KEY,
    pname VARCHAR(50),
    pdesc VARCHAR(255)
);

CREATE TABLE tx_user_projects (
    userid INT,
    projectid INT,
    date_assigned DATE,
    
    PRIMARY KEY (userid, projectid),
    FOREIGN KEY (userid) REFERENCES tx_users(user_id),
    FOREIGN KEY (projectid) REFERENCES tx_projects(project_id)
);

CREATE TABLE tx_user_role (
		role_id INT PRIMARY KEY,
		rolename VARCHAR(50) NOT NULL,
		roledesc VARCHAR(50)
);

CREATE TABLE tx_testcases (
		testcase_id INT PRIMARY KEY,
		testcase_code VARCHAR(12),
		testcasename VARCHAR(50) NOT NULL,
		testcasedesc VARCHAR(50),
		testcasetype VARCHAR(50),
		testcasepriority VARCHAR(50),
		testcasetemplate VARCHAR (100),
		mission VARCHAR(1000),
		goals VARCHAR(1000),
	  	pre_conditions VARCHAR(1000),
		expected_results VARCHAR(1000)
);

CREATE TABLE tx_steps (
	step_id INT PRIMARY KEY,
	step_code VARCHAR (12),
	stepname VARCHAR (250)
);

CREATE TABLE tx_bdd_scenarios (
	scenario_id INT PRIMARY KEY,
	scenario_code VARCHAR (12),
	scenario VARCHAR (1000)
);

CREATE TABLE tx_testcase_steps (
		testcaseid INT,
		stepid INT,
		PRIMARY KEY (testcaseid, stepid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcase_id),
    	FOREIGN KEY (stepid) REFERENCES tx_steps(step_id)
);

CREATE TABLE tx_testcase_bdd_scenarios (
		testcaseid INT,
		scenarioid INT,
		PRIMARY KEY (testcaseid, scenarioid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcase_id),
    	FOREIGN KEY (scenarioid) REFERENCES tx_bdd_scenarios(scenario_id)
);

CREATE TABLE tx_requirements (
		req_id INT PRIMARY KEY,
		req_code VARCHAR (12),
		reqname VARCHAR(300) NOT NULL,
		reqdesc VARCHAR(500),
		reqtype VARCHAR(100),
		reqpriority VARCHAR(50),
		reqseverity VARCHAR(50)
);

CREATE TABLE tx_testcase_reqs (
		testcaseid INT,
		reqid INT,
		PRIMARY KEY (testcaseid, reqid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcase_id),
    	FOREIGN KEY (reqid) REFERENCES tx_requirements(req_id)
);

CREATE TABLE tx_projects_reqs (
		projectid INT,
		reqid INT,
		PRIMARY KEY (projectid, reqid),
    	FOREIGN KEY (projectid) REFERENCES tx_projects(project_id),
    	FOREIGN KEY (reqid) REFERENCES tx_requirements(req_id)
);
CREATE TABLE tx_projects_tests (
		projectid INT,
		testid INT,
		PRIMARY KEY (projectid, testid),
    	FOREIGN KEY (projectid) REFERENCES tx_projects(project_id),
    	FOREIGN KEY (testid) REFERENCES tx_testcases(testcase_id) ON DELETE CASCADE
);

CREATE TABLE tx_defects (
		id SERIAL PRIMARY KEY,
		component VARCHAR(250),
		summary VARCHAR(500) NOT NULL,
		description VARCHAR(1000),
		fix_version VARCHAR(50),
		defect_label VARCHAR(50),
		estimate VARCHAR (100),
		affects_version VARCHAR(1000),
		epic_link VARCHAR(200),
	  	assignee VARCHAR(100),
		attachment bytea
);

CREATE TABLE tx_testcases_defects (
		testid INT,
		defectid INT,
		FOREIGN KEY (testid) REFERENCES tx_testcases(testcase_id),
    		FOREIGN KEY (defectid) REFERENCES tx_defects(defect_id)
);

++++++++This below is a schema for dummy to show projects, Tests and Steps relationship +++++++++++++++++++++++++++


Project - Test - Step Schema

CREATE TABLE projects (
  project_id INT PRIMARY KEY,
  project_name VARCHAR(255)
);

CREATE TABLE tests (
  test_id INT PRIMARY KEY,
  test_name VARCHAR(255),
  project_id INT,
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE steps (
  step_id INT PRIMARY KEY,
  step_name VARCHAR(255),
  test_id INT,
  FOREIGN KEY (test_id) REFERENCES tests(test_id)
);

Query to find all the test cases and steps for a given project
SELECT t.test_name, s.step_name 
FROM projects p 
JOIN tests t ON p.project_id = t.project_id 
JOIN steps s ON t.test_id = s.test_id 
WHERE p.project_name = 'given_project_name';

++++++++++++++++++++++++++++++End of Dummy+++++++++++++++++++++++++++++++++++++++++++++


Make sure to add ON DELETE CASCADE for each foreighn key

select *
from tx_testcases
inner join tx_projects_tests on tx_testcases.testcase_id = tx_projects_tests.testid
where tx_projects_tests.projectid = 100 
order by testcase_id asc











