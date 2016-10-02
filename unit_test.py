import unittest
import urllib2
import requests

class WeatherApiUnitTest(unittest.TestCase):

	def setUp(self):
		self.ApiUrl = "http://api.openweathermap.org/data/2.5/weather?q="
		self.ApiKey = "&appid=badd72f59b5326f8500a230fcb7f33c3"
	
	def test_response_200(self):
		city = 'Campinas'
		testurl = (self.ApiUrl + city + self.ApiKey)
		resp = requests.get(testurl)
		self.assertEqual(200, resp.status_code)
		print "API returned response code 200 and unit test passed"

	def test_valid_city_name(self):
		city = 'Campinas'
		testurl = (self.ApiUrl + city + self.ApiKey)
		response = urllib2.urlopen(testurl)
		json=response.read()
		self.assertTrue(city in json)
		print city + " city was successfully found at Json and unit test passed"

	def test_invalid_city_name(self):
		city = 'asdfasfdasfdasfasdf'
		testurl = (self.ApiUrl + city + self.ApiKey)
		response = urllib2.urlopen(testurl)
		json=response.read()
		self.assertTrue("Not found city" in json)
		print "Not found city error message was successfully returned for invalid city"

	def test_empty_city_name(self):
		city = ''
		testurl = (self.ApiUrl + city + self.ApiKey)
		response = urllib2.urlopen(testurl)
		json=response.read()
		self.assertTrue("Not found city" in json)
		print "Not found city error message was successfully returned for empty city"

if __name__ == "__main__":
		unittest.main()

