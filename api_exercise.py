import requests
import json
import difflib
import unittest

class Weather:
	def __init__(self,city):
		self.url = 'http://api.openweathermap.org/data/2.5/weather?q='
		self.api_key = ',&appid=badd72f59b5326f8500a230fcb7f33c3'
		self.city = city
		self.final_url = self.url + self.city + self.api_key

	def get_json(self):
		self.response = requests.get(self.final_url)
		json_object = self.response.json()
		json_to_str = json.dumps(json_object)
		return json_to_str

class Validation:
	def __init__(self, json1,json2):
		self.json1 = json1
		self.json2 = json2

	def validate_json(self):
		if json1 == json2:
			print 'Json 1 is the same as Json 2'
			print 'Json1:'
			print json1
			print 'Json2:'
			print json2
		elif len(json1) != len(json2):
			print 'Json 1 has not the same size as Json 2'
			print 'Json1:'
			print json1
			print 'Json2:'
			print json2
		elif len(json1) == len(json2) and json1 != json2:
			d = difflib.Differ()
			diff = d.compare(json_to_str1.splitlines(),json_to_str2.splitlines())
			print 'Json 1 has the same size of Json 2 but has the differences below:'
			print('\n'.join(diff))

city1 = raw_input("Please enter a city name: ")
weather1 = Weather(city1)
json1 = weather1.get_json()

city2 = raw_input("Please enter a second city name to compare: ")
weather2 = Weather(city2)
json2 = weather2.get_json()

test = Validation(json1,json2)
test.validate_json()

