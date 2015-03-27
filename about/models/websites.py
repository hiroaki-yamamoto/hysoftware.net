'''
External Website Models
'''
from django.db import models


class ExternalWebsite(models.Model):
    '''
    External webpages
    '''
    # pylint: disable=too-few-public-methods
    CHOICE = (
        ("G+", "Google Plus"),
        ("LI", "Linkedin"),
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("CW", "Coderwalll"),
        ("AS", "Assembly"),
        ("GH", "Github"),
        ("BB", "Bitbucket"),
        ("OT", "Other")
    )
    website_type = models.CharField(
        max_length=4,
        choices=CHOICE,
        db_index=True
    )
    name = models.CharField(
        max_length=30,
        db_index=True,
        null=True,
        blank=True
    )
    url = models.URLField()
    user = models.ForeignKey("Developer")

    def website_type_name(self):
        '''
        Returns long name of the website type
        '''
        filtered = [
            choice for choice in self.CHOICE if choice[0] == self.website_type
        ]
        if len(filtered) != 1:
            raise ValueError(
                (
                    "Awwww! website type name {} is invalid!"
                ).format(self.website_type)
            )
        return filtered[0][1]

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "External Website of {}: {} ({}) at {}"
        ).format(
            self.user,
            self.name,
            self.url,
            self.website_type
        )

    __unicode__ = __str__
