# smrt-uncrn-dsh-mqtthandler
Connect incoming Mqtt-Messages to Database

## About
This python module connects to the in `config.py` specified mqtt broker and subscribes to various mqtt topics.
If incoming messages are getting parsed and - if successfully parsed - are getting added to a database, also specified in `config.py`

## Usage
```
git clone https://github.com/lheimbs/smrt-uncrn-dsh-collector.git
cd smrt-uncrn-dsh-collector
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m mqtthandler
```

To increase the verbosity either use `python3 -m mqtthandler -v` or to show all debug messages `python3 -m mqtthandler -d`.
