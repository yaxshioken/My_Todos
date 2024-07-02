from services import User, Todo


class Ui(object):
    def main(self):
        menu="""
        ##########//Welcome To Todo PRojecT \\\############################
        
        ===============MeNu=============================
                1)Login
                2)Register 
                3)Exit
                >>>>>>>"""
        choose=input(menu)
        if choose=='1':
            if User().login():
                self.Todo_menu()
            else:
                print("Something went wrong")
        elif choose=='2':
            User.register()
        elif choose=='3':
            pass
    def Todo_menu(self):
        print('------------------------Welcome to Your Todo menu-------------------------')
        menu="""
        1)My Todo List
        2)Create a Todo 
        3)Update a Todo 
        4)Delete a Todo
        """
        choose=input(menu)
        if choose=='1':
            Todo().my_todo()
        elif choose=='2':
            Todo().create_todo()
        elif choose=='3':
            Todo().update_todo()
        elif choose=='4':
            Todo().delete_todo()



if __name__ == '__main__':

    Ui().main()

