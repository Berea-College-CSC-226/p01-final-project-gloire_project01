from datetime import datetime
import random


class Journal:
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __init__ (self):
        return f"{self.date}: {self.content}"
