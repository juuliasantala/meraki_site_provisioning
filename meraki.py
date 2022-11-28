#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MerakiHandler class for retrieving Meraki templates, creating a new site,
binding the site to the template, and assinging a Z1 to the site.

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

class MerakiHandler():
    '''
    Class to handle the connection to Meraki.
    '''
    base_url = "https://api.meraki.com/api/v1"

    @property
    def headers(self):
        '''
        Headers needed for the Meraki API calls.
        '''
        headers = {
            "X-Cisco-Meraki-API-Key":self.token,
            "Content-Type":"application/json"
        }
        return headers

    def __init__(self, token, organization):
        '''
        Initializing the MerakiHandler object with the user's authentication
        token and the ID of the Meraki organization to be targeted with the
        API calls.
        '''
        self.token = token
        self.organization = organization

    def create_site(self, site_name):
        '''
        Method to create a new Meraki site.
        '''
        url = f"{self.base_url}/organizations/{self.organization}/networks"
        body = {
            "name": site_name,
            "timeZone": "Europe/Helsinki",
            "tags": ["Cisco Live Melbourne"],
            "productTypes":[ "appliance"]
        }
        response = requests.post(url, headers=self.headers, json=body, timeout=30)
        print(response.text)
        return response.json()["id"]

    def get_config_templates(self):
        '''
        Method to get configuration templates of the Meraki organization.
        '''
        print("getting config templates")
        templates = []
        url = f"{self.base_url}/organizations/{self.organization}/configTemplates"
        response = requests.get(url, headers=self.headers, timeout=30)
        print(response)
        response=response.json()
        for template in response:
            templates.append({
                "id":template["id"],
                "name":template["name"]
            })
        return templates

    def bind_to_site(self, network_id, template_id):
        '''
        Method to bind a selected template to the new site that has been created.
        '''
        print(f"Binding {template_id} template to {network_id} network")
        url = f"{self.base_url}/networks/{network_id}/bind"
        body = {
            "configTemplateId": template_id,
            "autoBind": False
            }
        response = requests.post(url, headers=self.headers, json=body, timeout=30)
        print(response)

    def find_a_Z1(self, network_id):
        '''
        Method to find an available Z1 in the Organization inventory.
        '''
        print(f"Finding {network_id} network devices")
        url = f"{self.base_url}/organizations/{self.organization}/inventory/devices"
        response = requests.get(url, headers=self.headers, timeout=30)
        print(response)
        response=response.json()

        serial = ""
        for devices in response:
            if devices["model"] == "Z1" and devices["networkId"] is None:
                serial = devices["serial"]
                print("found device {serial}")
                break
        return serial

    def claim_Z1(self,network_id, serial):
        '''
        Method to claim a Z1 to a network.
        '''
        print(f"Claiming Z1 to {network_id} network")
        url = f"{self.base_url}/networks/{network_id}/devices/claim"
        body = {
            "serials": [serial]
            }
        response = requests.post(url, headers=self.headers, json=body, timeout=30)
        print(response.text)
