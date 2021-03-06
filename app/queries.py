users_table = """ 
        CREATE TABLE IF NOT EXISTS USERS(
            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME  TEXT    NOT NULL,
            PASSWORD TEXT NOT NULL,
            AUTH_TOKEN TEXT DEFAULT "",
            CREATEDAT  TIMESTAMP DEFAULT (strftime('%s', 'now')),
            ISACTIVE BOOLEAN DEFAULT 1
            );
"""

def get_user(username):
    return """ SELECT * FROM USERS WHERE USERNAME = "{0}" """.format(username)

def create_user(username,password):
    return """INSERT INTO USERS (USERNAME, PASSWORD)
                        VALUES("{0}","{1}")
            """.format(username,password)

def update_user(username, password):
    return """ UPDATE USERS SET PASSWORD = "{0}" WHERE USERNAME = "{1}" """.format(password, username)

def check_password(password):
    return """ SELECT * FROM USERS WHERE password = "{0}" """.format(password)

def update_token(username, token):
    return """ UPDATE USERS SET AUTH_TOKEN = "{0}" WHERE USERNAME = "{1}" """.format(token, username)

def get_token(username):
    return """ SELECT AUTH_TOKEN FROM USERS WHERE USERNAME = "{0}" """.format(username)
    

    
