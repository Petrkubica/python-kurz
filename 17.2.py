import json
import pickle
class Student:
    def __init__(self, jmeno, vek, obor):
        self.jmeno = jmeno
        self.vek = vek
        self.obor = obor
    # def __str__(self):
    #     return f"Student(jmeno={self.jmeno}, vek={self.vek}, obor={self.obor})"
    # def __repr__(self):
    #     return f"Student(jmeno={self.jmeno}, vek={self.vek}, obor={self.obor})"
    # def reprezentace_na_str(self):
    #     return f"Student(jmeno={self.jmeno}, vek={self.vek}, obor={self.obor})"
# def save_to_txt(filename, obj):
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(str(obj))
student1 = Student("Pavel", 23, "Informatika")
with open("studentTest1.txt","w", encoding='utf-8') as testFile:
    testFile.write(f"Student(jmeno={student1.jmeno}, vek={student1.vek}, obor={student1.obor})")
    # testFile.write(str(student1))
def load_from_txt(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
# def save_to_pickle(filename, obj):
#     with open(filename, "wb") as file:
#         pickle.dump(obj, file)
# def load_from_pickle(filename):
#     with open(filename, "rb") as file:
#         return pickle.load(file)
# def save_to_json(filename, obj):
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(obj.to_dict(), file, ensure_ascii=False, indent=4)
# def load_from_json(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         data = json.load(file)
#         return Student.from_dict(data)
# student1 = Student("Petr", 23, "Informatika")
# #print(student1)
# save_to_txt("student.txt", student1)
# print("TXT načteno:", load_from_txt("student.txt"))
# save_to_pickle("student.pkl", student1)
# print("Pickle načteno:", load_from_pickle("student.pkl"))
# save_to_json("student.json", student1)
# print("JSON načteno:", load_from_json("student.json"))

# React

# Reply








