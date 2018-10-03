users_table = """ 
        CREATE TABLE IF NOT EXISTS USERS(
            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CHAT_ID  TEXT    NOT NULL,
            USERNAME  TEXT    NOT NULL,
            PASSWORD TEXT NOT NULL,
            CREATEDAT  TIMESTAMP DEFAULT (strftime('%s', 'now')),
            ISACTIVE BOOLEAN DEFAULT 1
            );
"""

