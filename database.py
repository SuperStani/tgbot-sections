import mysql.connector as db

def connect():
    mydb = db.connect(
        user      = "admin",
        passwd    = "@Naruto96",
        database  = "easyseller",
        host      = "localhost"
    )
    return mydb

def query(query, *args, one=False, read=False):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, args)
    try:
        if read:
            if not one:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
        else:
           connection.commit() 
           return cursor.lastrowid
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()

#Get page session of user
def getPage(chat_id):
    return query("SELECT page FROM users WHERE chat_id = %s", chat_id, one=True, read=True)[0]

#Change page session of user
def page(page_text, chat_id):
    query("UPDATE users SET page = %s WHERE chat_id = %s", page_text, chat_id)
    
#Write query
def wquery(raw_query, *args):
    return query(raw_query, *args)

#Read query
def rquery(raw_query, *args, one = False):
    return query(raw_query, *args, one=one, read=True)

def create_users_table():
    query_s = """
      CREATE TABLE IF NOT EXISTS 'users' (
          'chat_id' int PRIMARY KEY,
          'page` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
          'subscribed_on' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
    query(query_s)
    
def newUser(user_id, username=None):
    try:
        query("INSERT INTO users SET chat_id = %s, username = %s, page = %s", user_id, username, 'start')
        return True
    except:
        return False
