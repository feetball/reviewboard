from __future__ import unicode_literals

from django_evolution.mutations import AddField
from djblets.db.fields import JSONField


MUTATIONS = [
    AddField('Profile', 'extra_data', JSONField, null=True)
]
