import os


class Config:

    def __init__(self):
        self.user_id = os.getenv('USER_ID', 'admin1')