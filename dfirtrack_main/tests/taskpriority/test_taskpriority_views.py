from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Taskpriority
import urllib.parse

class TaskpriorityViewTestCase(TestCase):
    """ taskpriority view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskpriority.objects.create(taskpriority_name='prio_1')
        # create user
        test_user = User.objects.create_user(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')

    def test_taskprioritys_list_not_logged_in(self):
        """ test list view """

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskprioritys/', safe='')
        # get response
        response = self.client.get('/taskprioritys/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskprioritys_list_logged_in(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskprioritys_list_template(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskpriority/taskprioritys_list.html')

    def test_taskprioritys_list_get_user_context(self):
        """ test list view """

        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskpriority')

    def test_taskprioritys_detail_not_logged_in(self):
        """ test detail view """

        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskprioritys/' + str(taskpriority_1.taskpriority_id), safe='')
        # get response
        response = self.client.get('/taskprioritys/' + str(taskpriority_1.taskpriority_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskprioritys_detail_logged_in(self):
        """ test detail view """

        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/' + str(taskpriority_1.taskpriority_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskprioritys_detail_template(self):
        """ test detail view """

        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/' + str(taskpriority_1.taskpriority_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskpriority/taskprioritys_detail.html')

    def test_taskprioritys_detail_get_user_context(self):
        """ test detail view """

        # get object
        taskpriority_1 = Taskpriority.objects.get(taskpriority_name='prio_1')
        # login testuser
        login = self.client.login(username='testuser_taskpriority', password='VxuP85UUDkfXwRuwRFqA')
        # get response
        response = self.client.get('/taskprioritys/' + str(taskpriority_1.taskpriority_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskpriority')
