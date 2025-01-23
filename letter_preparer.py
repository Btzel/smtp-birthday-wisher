import pandas as pd
import datetime as dt
import random

class LetterPreparer:
    def __init__(self):
        self.data = pd.read_csv("birthdays.csv")
        self.birthday_persons = self.pick_birthday_persons()
        self.prepare_letters()

    def pick_birthday_persons(self):
        today = dt.datetime.now()
        person_dict = self.data.to_dict(orient='records')

        birthday_persons = [person_details for person_details in person_dict
                            if person_details['month'] == today.month
                            and person_details['day'] == today.day]
        return birthday_persons

    def prepare_letters(self):
        for person in self.birthday_persons:
            letter_file = open(f"./letter_templates/letter_{random.randint(1, 3)}.txt")
            person['letter'] = letter_file.read().replace("[NAME]", f"{person['name']}")
            letter_file.close()