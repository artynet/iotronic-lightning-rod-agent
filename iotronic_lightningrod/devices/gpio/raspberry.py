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

__author__ = "Nicola Peditto <n.peditto@gmail.com>"

from oslo_log import log as logging

from iotronic_lightningrod.devices.gpio import Gpio

LOG = logging.getLogger(__name__)


class RaspberryGpio(Gpio.Gpio):
    def __init__(self):
        super(RaspberryGpio, self).__init__("raspberry")
        LOG.info("Raspberry GPIO module importing...")

    # Enable GPIO
    def EnableGPIO(self):
        result = " - GPIO not available for 'raspberry' device!"
        LOG.info(result)

    def DisableGPIO(self):
        result = " - GPIO not available for 'raspberry' device!"
        LOG.info(result)