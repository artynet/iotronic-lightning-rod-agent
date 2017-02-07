# Copyright 2011 OpenStack Foundation
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

__author__ = "MDSLAB Team"

import abc
import six

from oslo_log import log as logging
LOG = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class Module(object):
    """Base class for each s4t Lightning-rod module.

    """

    # __metaclass__ = abc.ABCMeta

    def __init__(self, name, node):

        self.name = name
        self.node = node

        LOG.info("Loading module " + self.name + "...")
        print('- ' + self.name)

    """
    @abc.abstractmethod
    def test(self):
        #Main plugin method.

    """
