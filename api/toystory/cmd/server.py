# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo.config import cfg

from toystory import bootstrap
from toystory.common import cli


@cli.runnable
def run():
    # TODO(kgriffs): For now, we have to use the global config
    # to pick up common options from openstack.common.log, since
    # that module uses the global CONF instance exclusively.
    conf = cfg.CONF
    conf(project='toystory', prog='toystory')

    server = bootstrap.Bootstrap(conf)
    server.run()
