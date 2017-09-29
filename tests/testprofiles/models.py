# Copyright (C) 2011-2012 Yaco Sistemas (http://www.yaco.es)
# Copyright (C) 2010 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import django
from django.db import models

if django.VERSION < (1, 7):
    class TestProfile(models.Model):
        user = models.OneToOneField('auth.User')
        age = models.CharField(max_length=100, blank=True)

        def process_first_name(self, first_name):
            self.first_name = first_name[0]
else:
    from django.contrib.auth.models import AbstractUser
    class TestUser(AbstractUser):
        age = models.CharField(max_length=100, blank=True)
        def process_first_name(self, first_name):
            self.first_name = first_name[0]

    class StandaloneUserModel(models.Model):
        """
        Does not inherit from Django's base abstract user and does not define a
        USERNAME_FIELD.
        """
        username = models.CharField(max_length=30, unique=True)
