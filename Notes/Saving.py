import json


class Saving:
    def __init__(self, dct):
        self.dct = dct

    def saving_note(self):
        with open("/Users/station/PycharmProjects/Notes/note.json", "w", encoding="utf-8") as outfile:
            json.dump(self.dct, outfile)