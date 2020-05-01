import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior

def invalidLogin():
	pop = Popup(title="Invalid Login",
			content=Label(text="Invalid username or password"),
			size_hint=(None,None), size=(400,400))
	pop.open()

def invalidForm():
	pop = Popup(title="Invalid Form",
			content=Label(text="Please fill in all of the inputs"),
			size_hint=(None,None), size=(400,400))
	pop.open()

class LoginWindow(Screen):
	email = ObjectProperty(None)
	password = ObjectProperty(None)

	def login_button(self):
		if db.validate(self.email.text, self.password.text):
			LoginWindow.current = self.email.text
			self.reset()
			ScreenManager.current = "second"
		else:
			invalidLogin()


	def verify_credentials(self):
		if self.ids["email"].text == "username" and self.ids["password"].text == "password": self.manager.current = "second"

class CreateAccountWindow(Screen):
	namee = ObjectProperty(None)
	email = ObjectProperty(None)
	password = ObjectProperty(None)

	def submit(self):
		if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
			if self.password != "":
				db.add_user(self.email.text, self.password.text, self.namee.text)

				self.reset()

				ScreenManager.current = "login"
			else:
				invalidForm()
		else:
			invalidForm()
	def login(self):
		self.reset()
		ScreenManager.current = "login"

	def reset (self):
		self.email.text = ""
		self.password.text = ""
		self.namee.text = ""

class SecondWindow(Screen):
	pass

class Lunch_Menu(Screen):

	def change_text(self):
		if self.label7.text != "":
			self.label8.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label6.text != "":
			self.label7.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label5.text != "":
			self.label6.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label4.text != "":
			self.label5.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label3.text != "":
			self.label4.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label2.text != "":
			self.label3.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		elif self.label1.text != "":
			self.label2.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		else:
			self.label1.text = str(self.ids.new_menu_item.text)
			self.ids.new_menu_item.text = ""
		
class Dinner_Menu(Screen):
	pass

class WindowManager(ScreenManager):
	pass

class DataBase:
	def __init__(self, filename):
		self.filename = filename
		self.users = None
		self.file = None
		self.load()

	def load(self):
		self.file = open(self.filename, "r")
		self.users = {}

		for line in self.file:
			email, password, name, created = line.strip().split(";")
			self.users[email] = (password, name, created)

		self.file.close()

	def get_user(self, email):
		if email in self.users:
			return self.users[email]
		else:
			return -1

	def add_user(self, email, password, name):
		if email.strip() not in self.users:
			self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
			self.save()
			return 1
		else:
			print("Email address already exists")
			return -1

	def validate(self, email, password):
		if self.get_user(email) != -1:
			return self.users[email][0] == password
		else:
			return False

	def save(self):
		with open(self.filename, "w") as f:
			for user in self.users:
				f.write(user + ";" + self.users[user][0] + self.users[user][1] + ";" + self.users[user][2] + "\n")

	def get_date():
		return str(datetime.datetime.now()).split(" ")[0]

kv = Builder.load_file("my4.kv")

class MyMenu(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MyMenu().run()