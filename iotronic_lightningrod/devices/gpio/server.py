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


from oslo_log import log as logging

from iotronic_lightningrod.devices.gpio import Gpio

LOG = logging.getLogger(__name__)


class ServerGpio(Gpio.Gpio):
    def __init__(self):
        super(ServerGpio, self).__init__("yun")
        LOG.info("Server gpio module inporting...")

    # Enable GPIO
    def EnableGPIO(self):
        LOG.info(" - EnableGPIO CALLED...")
        result = '  - Gpio not available for server device!'
        LOG.info(result)

    def DisableGPIO(self):
        LOG.info(" - DisableGPIO CALLED...")
        result = '  - Gpio not available for server device!'
        LOG.info(result)
