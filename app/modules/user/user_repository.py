class UserRepository:
    def __init__(self):
        self.users =[]
     
    #create user 
    def create_user(self,user_data):
        user = {  
              "id" : len(self.users)+1,
              "name" : user_data['name'],
              "email" : user_data['email'],
              "address" : user_data['address']
            } 
           
        self.users.append(user)
        return user
      
    # get all user
    def get_all_users(self):
        return self.users