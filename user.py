class User:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.playing = None
        self.played  = []

def get_user(users, chat_id):
    for user in users:
        if user.chat_id == chat_id:
            return user
