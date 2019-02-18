from django.test import TestCase
from dfirtrack_main.forms import ReasonForm

class ReasonFormTestCase(TestCase):
    """ reason form tests """

    def test_reason_name_label(self):

        # get object
        form = ReasonForm()
        # compare
        self.assertEquals(form.fields['reason_name'].label, 'Reason name (*)')

    def test_reason_name_empty(self):

        # get object
        form = ReasonForm(data = {'reason_name': ''})
        # compare
        self.assertFalse(form.is_valid())

    def test_reason_name_filled(self):

        # get object
        form = ReasonForm(data = {'reason_name': 'reason_1'})
        # compare
        self.assertTrue(form.is_valid())
