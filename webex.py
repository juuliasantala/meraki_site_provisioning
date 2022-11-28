#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WebexBot class for running sending a Webex message.

Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests

__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

class WebexBot():
    '''
    Class to handle the Webex bot details and a method to send messages.
    '''
    base_url = "https://webexapis.com/v1"

    @property
    def headers(self):
        '''
        Headers needed for the Webex API calls.
        '''
        headers = {
            "authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        return headers

    def __init__(self, token):
        '''
        Initializing the WebexBot object with the bot's authentication
        token.
        '''
        self.token = token

    def post_message(self, roomid, message):
        '''
        Method to post a message to a Webex space.
        '''
        print(message)
        url = f"{self.base_url}/messages"
        payload = {
            "roomId":roomid,
            "markdown":message,
            }
        response = requests.post(url, headers=self.headers, json=payload, timeout=30)
        print(response)
