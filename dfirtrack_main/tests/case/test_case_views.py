from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Case
import urllib.parse

class CaseViewTestCase(TestCase):
    """ case view tests """

    @classmethod
    def setUpTestData(cls):

        # create user
        test_user = User.objects.create_user(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')

        # create object
        Case.objects.create(
            case_name='case_1',
            case_is_incident=True,
            case_created_by_user_id=test_user,
        )

    def test_cases_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/cases/', safe='')
        # get response
        response = self.client.get('/cases/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_cases_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_cases_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/cases_list.html')

    def test_cases_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_cases_detail_not_logged_in(self):
        """ test detail view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/cases/' + str(case_1.case_id), safe='')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_cases_detail_logged_in(self):
        """ test detail view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_cases_detail_template(self):
        """ test detail view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/cases_detail.html')

    def test_cases_detail_get_user_context(self):
        """ test detail view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_cases_add_not_logged_in(self):
        """ test add view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/cases/add/', safe='')
        # get response
        response = self.client.get('/cases/add/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_cases_add_logged_in(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/add/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_cases_add_template(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/add/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/cases_add.html')

    def test_cases_add_get_user_context(self):
        """ test add view """

        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/add/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')

    def test_cases_edit_not_logged_in(self):
        """ test edit view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/cases/' + str(case_1.case_id) + '/edit/', safe='')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id) + '/edit/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_cases_edit_logged_in(self):
        """ test edit view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_cases_edit_template(self):
        """ test edit view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/case/cases_edit.html')

    def test_cases_edit_get_user_context(self):
        """ test edit view """

        # get object
        case_1 = Case.objects.get(case_name='case_1')
        # login testuser
        login = self.client.login(username='testuser_case', password='DcHJ6AJkPn0YzSOm8Um6')
        # get response
        response = self.client.get('/cases/' + str(case_1.case_id) + '/edit/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_case')
