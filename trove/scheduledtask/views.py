# Copyright 2013 OpenStack Foundation
# Copyright 2013 Rackspace Hosting
# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import json
from trove.common.views import create_links
DT_FMT = '%Y-%m-%dT%H:%M:%S.%fZ'


class ScheduledTaskView(object):

    def __init__(self, scheduled_task, req=None):
        self.scheduled_task = scheduled_task
        self.req = req

    def data(self):
        task_view = {
            "id": self.scheduled_task.id,
            "tenant_id": self.scheduled_task.tenant_id,
            "instance_id": self.scheduled_task.instance_id,
            "type": self.scheduled_task.type,
            "enabled": self.scheduled_task.enabled,
            "name": self.scheduled_task.name,
            "frequency": self.scheduled_task.frequency,
            "window_start": self.scheduled_task.window_start.strftime(DT_FMT),
            "window_end": self.scheduled_task.window_end.strftime(DT_FMT),
            "description": self.scheduled_task.description,
            "metadata": {},
            "links": self._build_links(),
        }

        if self.scheduled_task.metadata:
            task_view['metadata'] = json.loads(self.scheduled_task.metadata)

        return {"scheduled_task": task_view}

    def _build_links(self):
        return create_links("scheduled_tasks", self.req,
                            self.scheduled_task.id)


class ScheduledTasksView(object):

    def __init__(self, scheduled_tasks, req=None):
        self.scheduled_tasks = scheduled_tasks
        self.req = req

    def data(self):
        data = []
        for scheduled_task in self.scheduled_tasks:
            task_view = ScheduledTaskView(scheduled_task, req=self.req)
            task_data = task_view.data()['scheduled_task']
            data.append(task_data)
        return {'scheduled_tasks': data}


class ScheduledTaskTypeView(object):

    def __init__(self, scheduled_task_type, req=None):
        self.scheduled_task_type = scheduled_task_type
        self.req = req

    def data(self):
        type_view = {
            "type": self.scheduled_task_type.type,
            "description": self.scheduled_task_type.description,
            "enabled": self.scheduled_task_type.enabled,
            "links": self._build_links(),
        }

        return {"scheduled_task_type": type_view}

    def _build_links(self):
        return create_links("scheduled_task_types", self.req,
                            self.scheduled_task_type.type)


class ScheduledTaskTypesView(object):

    def __init__(self, scheduled_task_types, req=None):
        self.scheduled_task_types = scheduled_task_types
        self.req = req

    def data(self):
        data = []
        for scheduled_task_type in self.scheduledtasktypes:
            type_view = ScheduledTaskTypeView(scheduled_task_type, req=self.req)
            type_data = type_view.data()['scheduled_task_type']
            data.append(type_data)
        return {'scheduled_task_types': data}
