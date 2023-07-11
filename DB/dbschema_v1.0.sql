CREATE TABLE tx_user (
    userid INT PRIMARY KEY,
	uname VARCHAR(50) NOT NULL,
    fname VARCHAR(50) NOT NULL,
	lname VARCHAR(50),
    email VARCHAR(50) NOT NULL,
	dept VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE tx_projects (
    projectid INT PRIMARY KEY,
    pname VARCHAR(50),
    pdesc VARCHAR(255)
);

CREATE TABLE tx_user_projects (
    userid INT,
    projectid INT,
    date_assigned DATE,
    
    PRIMARY KEY (userid, projectid),
    FOREIGN KEY (userid) REFERENCES tx_users(userid),
    FOREIGN KEY (projectid) REFERENCES tx_projects(projectid)
);

CREATE TABLE tx_user_role (
		roleid INT PRIMARY KEY,
		rolename VARCHAR(50) NOT NULL,
		roledesc VARCHAR(50)
);

CREATE TABLE tx_testcases (
		testcaseid VARCHAR(50) PRIMARY KEY,
		testcasename VARCHAR(50) NOT NULL,
		testcasedesc VARCHAR(50),
		testcasetype VARCHAR(50),
		testcasepriority VARCHAR(50),
		testcasetemplate VARCHAR (100),
		mission VARCHAR(1000),
		goals VARCHAR(1000),
	  	pre_conditions VARCHAR(1000),
		expected_results VARCHAR(1000),
);

CREATE TABLE tx_steps (
	stepid VARCHAR(50) PRIMARY KEY,
	stepname VARCHAR (250)
);

CREATE TABLE tx_bdd_scenarios (
	scenarioid VARCHAR(50) PRIMARY KEY,
	scenario VARCHAR (1000)
);

CREATE TABLE tx_testcase_steps (
		testcaseid VARCHAR(50),
		stepid VARCHAR(50),
		PRIMARY KEY (testcaseid, stepid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcaseid),
    	FOREIGN KEY (stepid) REFERENCES tx_steps(stepid)
);

CREATE TABLE tx_testcase_bdd_scenarios (
		testcaseid VARCHAR(50),
		scenarioid VARCHAR(50),
		PRIMARY KEY (testcaseid, scenarioid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcaseid),
    	FOREIGN KEY (scenarioid) REFERENCES tx_bdd_scenarios(scenarioid)
);

CREATE TABLE tx_requirements (
		reqid VARCHAR(50) PRIMARY KEY,
		reqname VARCHAR(300) NOT NULL,
		reqdesc VARCHAR(500),
		reqtype VARCHAR(100),
		reqpriority VARCHAR(50),
		reqseverity VARCHAR(50)
);

CREATE TABLE tx_testcase_reqs (
		testcaseid VARCHAR(50),
		reqid VARCHAR(50),
		PRIMARY KEY (testcaseid, reqid),
    	FOREIGN KEY (testcaseid) REFERENCES tx_testcases(testcaseid),
    	FOREIGN KEY (reqid) REFERENCES tx_requirements(reqid)
);








