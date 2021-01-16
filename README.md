# smrt-uncrn-cllctr
Connect incoming Mqtt-Messages to Database

## About
This python module connects to the in `config.py` specified mqtt broker and subscribes to various mqtt topics.
If incoming messages are getting parsed and - if successfully parsed - are getting added to a database, also specified in `config.py`

## Usage

```
git clone git@github.com:lheimbs/smrt-uncrn-cllctr.git
cd smrt-uncrn-cllctr
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m smrtuncrncllctr
```

## Configuration
If the database has a password, rename `.env.example` to `.env` and replace the password with your databases password.
To choose a development or production config include `export HANDLER_ENV=development` or `production` respectively in the `.env` file.

To use the offline mqtt broker with randomly generated data:
- Make sure mosquitto mqtt broker is installed on your system,
- `mosquitto` executable is in your `PATH`,
- add `export OFFLINE=True` (Any string is valid) to the `.env`.

To increase the verbosity either use `python3 -m smrtuncrncllctr -v` or to show all debug messages `python3 -m smrtuncrncllctr -d`.
