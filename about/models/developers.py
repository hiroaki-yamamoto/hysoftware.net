'''
Developer profiles
'''

from django.db import models


class Developer(models.Model):
    '''
    Developer Information
    '''
    # pylint: disable=too-few-public-methods
    first_name = models.CharField(max_length=20, db_index=True)
    last_name = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(max_length=40, primary_key=True)
    title = models.CharField(max_length=40, db_index=True)

    def to_dict(self):
        '''
        Convert to dict
        '''
        result = {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "email": self.email,
            "title": self.title
        }
        return result

    def __str__(self):
        '''
        Represents class
        '''
        return (
            "Developer: {} {} <{}> -- {}"
        ).format(
            self.first_name,
            self.last_name,
            self.email,
            self.title
        )

    __unicode__ = __str__
