# class Singleton:
#     _instance = None  # single instance
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.value = "init value"
#         return cls._instance
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1.value)
# obj2.value = "New value"
# print(obj1)
# # print(obj1 is obj2)




# class OldPrinter:
#     """Old system."""
#     def old_print(self, text):
#         print(f"Starý tisk: {text}")
# class PrinterAdapter:
#     """Adapter to convert old to new"""
#     def __init__(self, old_printer):
#         self.old_printer = old_printer
#     def print(self, text):
#         self.old_printer.old_print(text)
# old_printer = OldPrinter()
# adapter = PrinterAdapter(old_printer)
# adapter.print("Tisknu přes adaptér")



# class OldCurrencySystem:
#     """Starý systém vrací ceny pouze v CZK."""
#     def get_price_czk(self):
#         return 1000  # Například 1000 Kč
# class CurrencyAdapter:
#     """Adaptér převádí CZK na EUR podle aktuálního kurzu."""
#     EXCHANGE_RATE = 0.04  # 1 CZK = 0.04 EUR
#     def __init__(self, old_system):
#         self.old_system = old_system
#     def get_price_eur(self):
#         price_czk = self.old_system.get_price_czk()
#         return round(price_czk * self.EXCHANGE_RATE, 2)  # Převod na EUR
# # Použití Adapteru
# old_system = OldCurrencySystem()
# adapter = CurrencyAdapter(old_system)
# print(f"Cena v CZK: {old_system.get_price_czk()} Kč")
# print(f"Cena v EUR: {adapter.get_price_eur()} €")





# from flask import Flask, render_template
# app = Flask(__name__)
# # Model – Data
# class User:
#     def __init__(self, name):
#         self.name = name
# # Controller – Správa logiky
# @app.route("/")
# def home():
#     user = User("Alice")
#     return render_template("index.html", user=user)
# # Spuštění aplikace
# if __name__ == "__main__":
#     app.run(debug=True)

# class Model:
#     def __init__(self):
#         # Initialize an empty list to hold tasks.
#         self.tasks = []
#     # Adds a task to the list of tasks.
#     def add_task(self, task):
#         self.tasks.append(task)
#     # Returns the list of tasks.
#     def get_tasks(self):
#         return self.tasks
# # View class responsible for
# # handling user interaction and display.
# class View:
#     # Reads a task from the user.
#     def input_task(self):
#         return input("Input task:\n")
#     # Displays the list of tasks to the user.
#     def show_tasks(self, tasks):
#         for item in tasks:
#             print(item)
#     # Shows the menu and returns the user's choice.
#     def show_menu(self):
#         print("*************************")
#         print("1 - Add task")
#         print("2 - Show tasks")
#         print("3 - Exit")
#         result = int(input("Choose what to do:\n"))
#         print("*************************")
#         return result
#     # Controller class to act
#     # as an intermediary between the Model and View.
# class Controller:
#     # Initialize the Controller with a Model and a View.
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#     # Method to handle adding a new task.
#     def action_input_task(self):
#         task = self.view.input_task()
#         self.model.add_task(task)
#     # Method to handle showing the list of tasks.
#     def action_show_tasks(self):
#         tasks = self.model.get_tasks()
#         self.view.show_tasks(tasks)
# # Initialize the MVC components.
# obj_controller = Controller(Model(), View())
# # Main application loop.
# while True:
#     # Display menu and get user choice.
#     result = obj_controller.view.show_menu()
#     # Match user choice to appropriate action.
#     match result:
#         case 1:
#             # Add a new task.
#             obj_controller.action_input_task()
#         case 2:
#             # Show list of tasks.
#             obj_controller.action_show_tasks()
#         case 3:
#             # Exit the application.
#             print("Bye!")
#             break
#         case _:
#             # Handle invalid user input.
            # print("\nWrong choice. Try again!\n")




# class Articcle:
#     def __init__ (self,title , author)           
#      self.title=title
#      self.author=author





# Model
class Article:
    def __init__(self, author, content, publisher, summary):
        self.author = author
        self.content = content
        self.char_count = len(content)
        self.publisher = publisher
        self.summary = summary

# Controller
class ArticleController:
    def __init__(self):
        self.model = None
        self.view = None

    def set_model(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    def update_view(self):
        self.view.display_article(self.model)

# View
class ArticleView:
    def display_article(self, article):
        print(f"Autor: {article.author}")
        print(f"Počet znaků: {article.char_count}")
        print(f"Vydavatel: {article.publisher}")
        print(f"Shrnutí: {article.summary}")

# Použití
article = Article("Jan Novák", "Obsah článku...", "example.com", "Krátké shrnutí článku")
controller = ArticleController()
view = ArticleView()

controller.set_model(article)
controller.set_view(view)
controller.update_view()












