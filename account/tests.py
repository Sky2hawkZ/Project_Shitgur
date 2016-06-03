from django.test import TestCase
from django.contrib.auth.models import User
from account.models import user_data

# logreg = login/registration page
# accmanage = account management page

# tests for templates
class TemplateTestCase(TestCase):

    # check if access to logreg is possible
    def test_logreg_response(self):
        logregresponse = self.client.get('/account/')
        self.assertEqual(logregresponse.status_code, 200)
    
    # if user is not logged in
    def test_accmanage_response(self):
        logregresponse = self.client.get('/account/Management/')
        self.assertEqual(logregresponse.status_code, 404)

    # if user is logged in
    def test_accmanage_response_loggedin(self):
        pass


# tests for views.py
class ViewTestCase(TestCase):
    pass


# tests for models.py
class ModelTestCase(TestCase):

    # test user_data model "about" 
    def test_about(self):
        userdata = user_data(about="Wendy i can fly!")
        self.assertEqual("Wendy i can fly!", userdata.about)


# tests for forms.py
class FormTestCase(TestCase):
    pass