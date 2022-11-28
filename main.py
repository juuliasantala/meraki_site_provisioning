#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sample code that creates a new Meraki site and assigns an available Z1 to
that site. The app also then sends a Webex message to a predefined space
to share the details of the created site, and the serial number of the
assigned Z1.

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

import os
from flask import Flask, render_template, request, url_for, redirect
from webex import WebexBot
from meraki import MerakiHandler

__copyright__ = "Copyright (c) 2022 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

APP = Flask(__name__)
MERAKI = MerakiHandler(os.getenv("MERAKI_TOKEN"), os.getenv("MERAKI_ORG"))
WEBEX = WebexBot(os.getenv("WEBEX_BOT_TOKEN"))
WEBEX_ROOM = os.getenv("WEBEX_ROOM")

@APP.route('/')
def new_network():
    '''
    Function that renders the template new_site.html with the template names
    returned by the get_config_templates() Meraki method.
    This will be run when the user accesses the root (/) address of the app.
    '''
    configuration_templates = MERAKI.get_config_templates()
    return render_template("new_site.html", templates=configuration_templates)

@APP.route('/create_network', methods=["GET","POST"])
def pnp():
    '''
    Function that runs the methods needed to create the new Meraki site, assign
    the Z1, and sending a message to Webex space about the assignment.
    '''
    network_name = request.form.get('network_name')
    template = request.form.get('network_template')
    sid = MERAKI.create_site(network_name)
    MERAKI.bind_to_site(sid, template)
    serial = MERAKI.find_a_Z1(sid)
    MERAKI.claim_Z1(sid, serial)
    WEBEX.post_message(
        WEBEX_ROOM,
        f"New site **{network_name}** created!\nThe following Z1 assigned: {serial}"
        )
    return redirect(url_for("new_network"))
