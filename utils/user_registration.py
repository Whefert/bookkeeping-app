import sqlite3

class User:
    # Initialize user with relevant info
    def __init__(self, firstname, lastname,username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<Username: {self.firstname}, Password: {self.password}'

    def add_user(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO users VALUES(?,?,?,?)',
                       (self.firstname, self.lastname,self.username,self.password))
        connection.commit()
        connection.close()


