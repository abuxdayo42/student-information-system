import json


class StudentRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            print("Error: student.json file was not found.")
            return None

        except json.JSONDecodeError:
            print("Error: student.json contains invalid JSON.")
            return None

        except OSError:
            print("Error: Could not read student data.")
            return None

    def save(self, data):
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)

            return True

        except OSError:
            print("Error: Could not save student data.")
            return False