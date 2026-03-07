import time

class TODO:
    todos = [
    #     {
    #     id,
    #     desc,
    #     iscompilted
    # },{},{}
    ]
    
    def add_todo(self, desc):
        # 1. take the desc form the user
        # 2. create one dictonary in which we will add the todos
        # 3. we have to append that dictonary inside todos
       
        self.todos.append( {
            "id":int(time.time()),
            "desc":desc,
            "is_complited":False
        })

    
    def remove_todo(self, id):
        if len(self.todos)==0 : return 
        for i in self.todos:
            if i["id"]==id:
               self.todos.remove(i)
               break
            else: 
                print("there is nothing to remove")
                break
    
    def display_todos(self):
        if len(self.todos)==0 : return 
        for i in self.todos:
            print(i)

    
    def update_todo(self, id, new_desc):
        for i in self.todos:
            if i["id"]==id:
                i["desc"]=new_desc
                break
            else: print("no such todo found")

    def toggle_mark_as_completed(self, id):
        for i in self.todos:
            if i["id"]==id:
                i["is_completed"]=True
                break
    
    def completed_todos(self):
        if len(self.todos)==0 : return 
        for i in self.todos:
            if i["is_complited"]:
                print(i)
    
    
    def incompleted_todos(self):
        if len(self.todos)==0 : return 
        for i in self.todos:
            if i["is_complited"]==False:
                print(i)
    


