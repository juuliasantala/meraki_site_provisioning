# Two clicks and a site is provisioned - How to use Python logic to simplify user experience when configuring a new Meraki site

This Git repository includes the code that is covered in the Cisco Live Melbourne 2022 Ligthning Talk.

**Content**
- [Prerequisities to run this code]()
- [Running the code]()
- [How to modify the script]()
- [Authors & Maintainers]()
- [License]()

## Prerequisities to run this code
- Python 3 installed on your workstation
- Meraki account
- A non-claimed device in your Meraki organization that can be used in the script
- Webex account [not mandatory]

## Running the code

### Set up your workstation by cloning the code and installing requirements
1. Clone this repository to your workstation
```Bash
git clone
```
2. Install the requirements in you Python environment
```Bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Rename the .env.template to .env
```Bash
mv .env.template .env
```

### Get required data from your Meraki account and add them into the `.env` file
1. Get your Meraki token
2. Get your Meraki organisation ID
3. Fill the Meraki details in the .env file
```
export MERAKI_TOKEN=<YOUR TOKEN>
export MERAKI_ORG=<YOUR ORG>
```
### Get required data from your Webex account and add them into the `.env` file

1. Get your or your bot's Webex token
2. Get the ID of the room you want to send a message. 
3. Fill the Webex details in the .env file
```
export WEBEX_BOT_TOKEN=<YOUR BOT TOKEN>
export WEBEX_ROOM=<YOUR WEBEX ROOM ID>
```

> **Note**: If you want to test only the Meraki functionality without the Webex messages, leave the Webex details in the `.env`file with the placeholder values, and comment out the lines 59-62 in the `main.py` file:
```Python
    # WEBEX.post_message(
    #     WEBEX_ROOM,
    #     f"New site **{network_name}** created!\nThe following Z1 assigned: {serial}"
    #     )
```

### Source the environment variables and run the app

1. Source the environment variables (Meraki and Webex detailed you filled in, as well as FLASK_APP that informs Flask which Python file to use as the entry point)
```Bash
source .env
```

2. Run the script using `flask run`. This will spin up the app in your localhost
```Bash
flask run
```

3. Access the GUI in your browser using the port printed out on the terminal. Example output, the app could be accessed on the browser by navigating to `http://127.0.0.1:5000`
```Bash
 * Serving Flask app 'main.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## Authors & Maintainers
People responsible for the creation and maintenance of this project:
* Juulia Santala jusantal@cisco.com

## License
This project is licensed to you under the terms of the [Cisco Sample Code License](LICENSE).
