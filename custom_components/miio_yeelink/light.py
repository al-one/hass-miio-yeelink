"""Support for Yeelink Light."""
import logging
import asyncio
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.const import *

from . import (
    YeelightEntity,
    MiotLightEntity,
    DOMAIN,
    CONF_MODEL,
    PLATFORM_SCHEMA,
    XIAOMI_MIIO_SERVICE_SCHEMA,
)

_LOGGER = logging.getLogger(__name__)
DATA_KEY = f'light.{DOMAIN}'

SERVICE_SCHEMA_SET_SCENE = XIAOMI_MIIO_SERVICE_SCHEMA.extend(
    {
        vol.Optional('scene', default = 0): vol.All(vol.Coerce(int), vol.Clamp(min=0, max=8)),
        vol.Optional('params'): list,
    },
)

SERVICE_SCHEMA_SET_DELAYED_TURN_OFF = XIAOMI_MIIO_SERVICE_SCHEMA.extend(
    {
        vol.Required('time_period'): cv.positive_time_period,
        vol.Optional('power', default = False): cv.boolean,
    }
)

SERVICE_TO_METHOD = {
    'light_set_scene': {
        'method': 'async_set_scene',
        'schema': SERVICE_SCHEMA_SET_SCENE,
    },
    'light_set_delayed_turn_off': {
        'method': 'async_set_delayed_turn_off',
        'schema': SERVICE_SCHEMA_SET_DELAYED_TURN_OFF,
    },
}

async def async_add_entities_from_config(hass, config, async_add_entities):
    if DATA_KEY not in hass.data:
        hass.data[DATA_KEY] = {}
    host = config[CONF_HOST]
    model = config.get(CONF_MODEL)
    entities = []
    if model.find('light.fancl') > 0:
        entity = MiotLightEntity(config)
        entities.append(entity)
    else:
        entity = YeelightEntity(config)
        entities.append(entity)
    hass.data[DATA_KEY][host] = entity
    async_add_entities(entities, update_before_add = True)

    async def async_service_handler(service):
        method = SERVICE_TO_METHOD.get(service.service)
        params = {
            key: value for key, value in service.data.items() if key != ATTR_ENTITY_ID
        }
        entity_ids = service.data.get(ATTR_ENTITY_ID)
        if entity_ids:
            target_devices = [
                dev
                for dev in hass.data[DATA_KEY].values()
                if dev.entity_id in entity_ids
            ]
        else:
            target_devices = hass.data[DATA_KEY].values()
        update_tasks = []
        for target_device in target_devices:
            if not hasattr(target_device, method['method']):
                continue
            await getattr(target_device, method['method'])(**params)
            update_tasks.append(target_device.async_update_ha_state(True))
        if update_tasks:
            await asyncio.wait(update_tasks)
    for srv in SERVICE_TO_METHOD:
        schema = SERVICE_TO_METHOD[srv].get('schema', XIAOMI_MIIO_SERVICE_SCHEMA)
        hass.services.async_register(DOMAIN, srv, async_service_handler, schema = schema)


async def async_setup_entry(hass, config_entry, async_add_entities):
    config = hass.data[DOMAIN]['configs'].get(config_entry.entry_id,config_entry.data)
    await async_add_entities_from_config(hass, config, async_add_entities)

async def async_setup_platform(hass, config, async_add_entities, discovery_info = None):
    await async_add_entities_from_config(hass, config, async_add_entities)
