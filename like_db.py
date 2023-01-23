import json
#Create Like counting class
class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def add_user(self, user_id):
        # with open(self.db_path, 'w') as f:
        #     json.dump(self.db, f, indent=4)
        # self.db.append(user_id:{
        #     "likes":0,
        #     "dislikes":0
        # })
        users = self.db.keys()
        users_dict = {}
        for i in users:
            users_dict[i]=0
        add = users_dict.get(user_id, 'net')
        if add == 'net':
            self.db[user_id]={}
            self.db[user_id]['likes']=0
            self.db[user_id]['dislikes']=0
        self.save()
    
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        likes=0
        for like in self.db.keys():
            likes+=self.db[like]['likes']
        return likes
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        dislikes=0
        for dislike in self.db.keys():
            dislikes+=self.db[dislike]['dislikes']
        return dislikes
        
        
    #Add a like to the database
    def add_like(self, user_id:str)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.db[user_id]['likes']==0 and self.db[user_id]['dislikes']==0:
            self.db[user_id]['likes']=1
        elif self.db[user_id]['likes']==1:
            self.db[user_id]['likes']=0
        elif self.db[user_id]['dislikes']==1:
            self.db[user_id]['dislikes']=0
            self.db[user_id]['likes']=1
        self.save()
        

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.db[user_id]['likes']==0 and self.db[user_id]['dislikes']==0:
            self.db[user_id]['dislikes']=1
        elif self.db[user_id]['likes']==1:
            self.db[user_id]['dislikes']=1
            self.db[user_id]['likes']=0
        elif self.db[user_id]['dislikes']==1:
            self.db[user_id]['likes']=0
            self.db[user_id]['dislikes']=0
        self.save()

# likedb = LikeDB('likedb.json')
# print(likedb.all_likes())
# print(likedb.all_dislikes())
# print(likedb.add_like('795394603'))
# print(likedb.add_user('756243577'))