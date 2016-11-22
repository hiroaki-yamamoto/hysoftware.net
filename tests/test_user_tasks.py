#!/usr/bin/env python
# coding=utf-8

"""User tasks."""

import requests

from unittest.mock import patch, call, MagicMock
from django.test import TestCase

from app.user.models import UserInfo, GithubProfile, TaskLog
from app.user.tasks import fetch_github_profile


class GithubFetchTaskTest(TestCase):
    """Github profile fetch task test."""

    def setUp(self):
        """Setup."""
        from django.contrib.auth import get_user_model

        self.users = [
            get_user_model().objects.create_user(
                username="test%d" % count,
                email="test%d@example.com" % count,
                password="This is a test",
                first_name="Test",
                last_name="Example %d" % count
            ) for count in range(3)
        ]
        self.models = [
            UserInfo.objects.create(
                user=self.users[0], github="hiroaki-yamamoto"
            ),
            UserInfo.objects.create(user=self.users[1], github="octocat")
        ]
        self.server_resp = {
            "login": "octocat",
            "id": 1,
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url":
                "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url":
                "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url":
                "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url":
                "https://api.github.com/users/octocat/subscriptions",
            "organizations_url":
                "https://api.github.com/users/octocat/orgs",
            "repos_url":
                "https://api.github.com/users/octocat/repos",
            "events_url":
                "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url":
                "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": False,
            "name": "monalisa octocat",
            "company": "GitHub",
            "blog": "https://github.com/blog",
            "location": "San Francisco",
            "email": "octocat@github.com",
            "hireable": False,
            "bio": "There once was...",
            "public_repos": 2,
            "public_gists": 1,
            "followers": 20,
            "following": 0,
            "created_at": "2008-01-14T04:33:35Z",
            "updated_at": "2008-01-14T04:33:35Z"
        }

    def tearDown(self):
        """Teardown."""
        from django.contrib.auth import get_user_model
        get_user_model().objects.all().delete()
        UserInfo.objects.all().delete()

    def task_name_check(self):
        """The name of the task should be 'user.github.fetch'."""
        self.assertEqual(fetch_github_profile.name, "user.github.fetch")

    @patch("requests.get")
    def test_task_normal_call(self, get):
        """All users who have github should update github profile."""
        get.return_value.json.return_value = self.server_resp
        fetch_github_profile()
        self.assertEqual(get.call_count, 2)
        get.assert_has_calls((
            call(
                "https://api.github.com/users/%s" % model.github,
                headers={"Accept": "application/vnd.github.v3+json"},
                timeout=(10.0, 10.0)
            ) for model in self.models
        ), any_order=True)
        for github in [
            {
                field.name: getattr(info.github_profile, field.name)
                for field in info.github_profile._meta.get_fields()
            } for info in self.models if hasattr(self.models, "github_profile")
        ]:
            self.assertDictContainsSubset(
                github, get.return_value.json.return_value
            )

    @patch("requests.get")
    def test_task_not_found(self, get):
        """When requests get error, log it."""
        resp = MagicMock()
        resp.status_code = 502
        resp.text = "The service is under mentainance."
        get.return_value.raise_for_status.side_effect = requests.HTTPError(
            response=resp
        )
        fetch_github_profile()
        self.assertEqual(GithubProfile.objects.count(), 0)
        self.assertEqual(TaskLog.objects.count(), 2)
        logs = TaskLog.objects.all()
        self.assertListEqual([
            "Github Profile Fetch Failed", "Github Profile Fetch Failed"
        ], [item.title for item in logs])
        self.assertListEqual(
            [self.users[0], self.users[1]], [item.user for item in logs]
        )
        self.assertListEqual([
            (
                "Fetching github profile failed because of "
                "this error:\ncode:%d\nPayload: %s\nGithubID: %s"
            ) % (resp.status_code, resp.text, info.github)
            for info in self.models
        ], [item.message for item in logs])

    @patch("requests.get")
    @patch("app.user.tasks.UserInfo.objects")
    def test_github_individual_update(self, objects, get):
        """The task should update only the corresponding profile."""
        get.return_value.json.return_value = self.server_resp
        fetch_github_profile(self.models[0].id)
        objects.filter.assert_called_once_with(id=self.models[0].id)
        objects.filter.return_value.all.assert_called_once_with()
        get.assert_called_once_with(
            "https://api.github.com/users/%s" % self.models[0].github,
            headers={"Accept": "application/vnd.github.v3+json"},
            timeout=(10.0, 10.0)
        )
        self.assertDictContainsSubset({
            field.name: getattr(self.models[0].github_profile, field.name)
            for field in self.models[0].github_profile._meta.get_fields()
        }, get.return_value.json.return_value)
        self.assertFalse(any([
            hasattr(info, "github_profile") for info in self.models[1:]
        ]))
