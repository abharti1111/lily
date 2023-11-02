import datetime
import time_uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class BaseModel(DjangoCassandraModel):
    id = columns.TimeUUID(primary_key=True, default=time_uuid.TimeUUID())
    created_at = columns.DateTime(default=datetime.datetime.now())
    updated_at = columns.DateTime(default=datetime.datetime.now())
    is_active = columns.Boolean(default=True)
    meta_data = columns.Text(required=False)
