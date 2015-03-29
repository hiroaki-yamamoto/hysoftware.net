'''
Contact form model
'''

from common import gen_hash
from django.db import models
from django.conf import settings

# pylint: disable=too-few-public-methods


class VerifiedEmail(models.Model):
    '''
    Verified email list.
    Note that email field should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(max_length=40, primary_key=True)
    assignee = models.ForeignKey("about.Developer")

    @classmethod
    def find_by_email(cls, email, assignee=None):
        '''
        Find the instance by email
        '''
        # pylint: disable=no-member
        if assignee:
            return cls.objects.filter(
                email_hash=gen_hash(email),
                assignee=assignee
            )
        else:
            return cls.objects.filter(
                email_hash=gen_hash(email)
            )
        # pylint: enable=no-member

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "Verified Email: {} (hash), Asignee: {}"
        ).format(self.email_hash, self.assignee)

    __unicode__ = __str__


class PendingVerification(models.Model):
    '''
    Email verification pending.
    Note that email and token fields should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(
        max_length=40,
        primary_key=True
    )
    assignee = models.ForeignKey("about.Developer")
    name = models.TextField()
    message = models.TextField(default="")
    expires = models.DateTimeField()

    @classmethod
    def find_by_email(cls, email, assignee=None):
        '''
        Find the instance by email
        '''
        # pylint: disable=no-member
        if assignee:
            return cls.objects.filter(
                email_hash=gen_hash(email),
                assignee=assignee
            )
        else:
            return cls.objects.filter(
                email_hash=gen_hash(email)
            )
        # pylint: enable=no-member

    @classmethod
    def by_email(cls, email):
        '''
        Return verification pending object by email
        '''
        # pylint: disable=no-member
        return cls.objects.get(email_hash=gen_hash(email))
        # pylint: enable=no-member

    @classmethod
    def remove_expired(cls):
        '''
        Remove expired verifications
        '''
        from django.utils import timezone
        expire_condition =\
            timezone.now() - settings.CONTACT_VIRIFICATION_EXPIRES

        # pylint: disable=no-member
        cls.objects.filter(expires__lt=expire_condition).delete()
        # pylint: enable=no-member

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "Email Verification: {} (hash), "
            "Expires: {}, Assignee: {}, "
            "Message: \n {}"
        ).format(
            self.email_hash,
            self.expires,
            self.assignee,
            self.message
        )

    __unicode__ = __str__
