# Copyright 2017 MDSLAB - University of Messina
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

import httplib2
import json

from iotronic_lightningrod.lightningrod import board

from oslo_log import log as logging
LOG = logging.getLogger(__name__)




def getBoardID():
    return board.uuid


def getLocation():
    return board.location


def getBoardGpio():
    return board.device.gpio


def sendRequest(url, action, headers=None, body=None, verbose=False):
    """Generic REST client for plugin users.

    :param url:
    :param action
    :param headers:
    :param data:
    :param verbose:
    :return:

    """
    try:
        http = httplib2.Http()
        headers = headers
        response, send = http.request(url, action, headers=headers, body=body)

        if verbose:
            req = json.loads(send)
            LOG.info("\nREST REQUEST: HTTP " + str(response['status']) + " - success = " + str(req['success']) + " - " + str(
                    req['result']['records']))
            # LOG.info("\nREST RESPONSE:\n" + str(response))

    except Exception as err:
        LOG.error("sendRequest error: " + err)



    return send