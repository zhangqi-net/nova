# Copyright 2016 Cloudbase Solutions Srl
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

from oslo_policy import policy

from nova.policies import base


POLICY_ROOT = 'os_compute_api:os-pause-server:%s'


pause_server_policies = [
    policy.DocumentedRuleDefault(
        name=POLICY_ROOT % 'pause',
        check_str=base.PROJECT_MEMBER,
        description="Pause a server",
        operations=[
            {
                'path': '/servers/{server_id}/action (pause)',
                'method': 'POST'
            }
        ],
        scope_types=['project']
    ),
    policy.DocumentedRuleDefault(
        name=POLICY_ROOT % 'unpause',
        check_str=base.PROJECT_MEMBER,
        description="Unpause a paused server",
        operations=[
            {
                'path': '/servers/{server_id}/action (unpause)',
                'method': 'POST'
            }
        ],
        scope_types=['project']
    ),
]


def list_rules():
    return pause_server_policies
