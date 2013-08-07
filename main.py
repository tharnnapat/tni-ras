#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import webapp2
from google.appengine.api import rdbms


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

_INSTANCE_NAME="prinya-th-2013:prinya-db"

class MainHandler(webapp2.RequestHandler):
	def get(self):

		templates = {

			# 'course' : cursor.fetchall(),

			}

		template = JINJA_ENVIRONMENT.get_template('credit.html')
		self.response.write(template.render(templates))

class InsertCredit(webapp2.RequestHandler):
	def post(self):
		group_name = self.request.get('group_name');
		faculity = self.request.get('faculity2');
		department = self.request.get('department2');
		flat_rate = self.request.get('flat_rate');
		price_per_credit = self.request.get('price_per_credit');	
		tuition = self.request.get('tuition');

		if tuition=="flat_rate":
			tuition = flat_rate 
		else:
			tuition = price_per_credit
		# self.response.write(group_name)
		# self.response.write(faculity)
		# self.response.write(department)
		# self.response.write(flat_rate)
		# self.response.write(price_per_credit)
		# self.response.write(tuition)

		conn = rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
    		cursor = conn.cursor()
		cursor.execute("""INSERT into creditprice (faculity,department,creditprice.group,price) 
            values (%s,%s,%s,%s)""",(faculity,department,group_name,tuition))

		conn.close();

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/InsertCredit', InsertCredit),
], debug=True)
