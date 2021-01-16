#!/usr/bin/env pyhton3

import logging

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker

from .config import config

logger = logging.getLogger()
logger.debug(f"CONFIG: {str(config)[27:-2]}")
logger.debug(f"DATABASE_URI: {config.SQLALCHEMY_DATABASE_URI}")
logger.debug(f"MQTT_SERVER: {config.MQTT_SERVER}:{config.MQTT_PORT}")

def connect_db():
    # init engines
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    engine_probes = create_engine(config.SQLALCHEMY_BINDS['probe_request'])

    # get data objects
    metadata = MetaData()
    metadata.reflect(engine, only=['room_data', 'mqtt_messages', 'rf_data', 'states', 'tablet_battery'])
    Base = automap_base(metadata=metadata)
    Base.prepare()

    RoomData = Base.classes.room_data
    RfData = Base.classes.rf_data
    Mqtt = Base.classes.mqtt_messages
    State = Base.classes.states
    TabletBattery = Base.classes.tablet_battery

    metadata_probes = MetaData()
    metadata_probes.reflect(engine_probes, only=['probe_requests'])
    Base_probes = automap_base(metadata=metadata_probes)
    Base_probes.prepare()

    ProbeRequest = Base_probes.classes.probe_requests

    Session = sessionmaker()
    Session.configure(binds={
        RoomData: engine,
        RfData: engine,
        Mqtt: engine,
        State: engine,
        TabletBattery: engine,
        ProbeRequest: engine_probes
    })

    @contextmanager
    def database_session():
        """Provide a transactional scope around a series of operations."""
        session = Session()
        try:
            yield session
            session.commit()
        except Exception as error:
            logger.error(error)
            session.rollback()
            raise
        finally:
            session.close()
    
    return Mqtt, State, RfData, RoomData, TabletBattery, ProbeRequest, database_session

Mqtt, State, RfData, RoomData, TabletBattery, ProbeRequest, db_session = connect_db()
