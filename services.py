from db import DB


class User:
    db = DB()
    db=db.connect().cursor()

    def login(self):
        cursor=self.db
        username = input("Your username is: @")
        password = input("Your password is: ")

        login_query = "SELECT * FROM users WHERE username=%s and password=%s"""
        print(login_query)
        cursor.execute(login_query, (username, password))
        self.db.commit()
        if login_query:
            return True
        else:
            return 'USer NOT FOUND'

    def register(self, name, email, password, phone):
        insert_query = "INSERT INTO users (name, email, password, phone) VALUES (%s, %s, %s, %s)"


class Todo:
    db = DB()

    def my_todo(self):
        owner_id=input("Your id is: ")
        cursor = self.db
        my_todo_query = "SELECT * FROM todos WHERE owner_id=%s"
        cursor.commit(my_todo_query, owner_id)

        if my_todo_query:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%% YouR ToDo Are Here %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(my_todo_query)
            return my_todo_query

    def update_todo(self, id, new_val):
        cursor = self.db
        self.my_todo()
        choose_updates_todo = "SELECT * FROM todos WHERE id=%s and owner_id=%s"
        if choose_updates_todo:
            menu = """
            Choose in here one
            1)TITLE UPDATE
            2)CREATED_AT UPDATE
            3)STATUS UPDATE            
            """
            choose = input(menu)
            if choose == "1":
                title = self.my_todo()
                print(title)

    def delete_todo(self):
        pass

    def create_todo(self):
        pass


if __name__ == "__main__":
    pass
