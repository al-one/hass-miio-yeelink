# Xiaomi Miio For Yeelink devices

## Tested Devices

- MJXDD02YL | yeelink.light.ceiling21
- MJXDD01SYL | yeelink.light.ceiling22
- MJXDD03YL | yeelink.light.ceiling23
- YLXD56YL | yeelink.light.ceiling18
- YLMB05YL | yeelink.light.panel1
- YLYB02YL | yeelink.bhf_light.v2
- YLFD02YL | yeelink.light.fancl1

## Tested By Community
- yeelink.bhf_light.v1
- yeelink.light.lamp3


## Installing

> Or manually copy `xiaomi_gateway3` folder to `custom_components` folder in your HomeAssistant config folder

or

> You can install component with [HACS](https://hacs.xyz) custom repo: `al-one/hass-miio-yeelink`


## Config

### HomeAssistant GUI

> Configuration > Integration > ➕ > Miio For Yeelink

### Configuration variables:

- **host**(*Required*): The IP of your device
- **token**(*Required*): The Token of your device
- **name**(*Optional*): The name of your device
- **model**(*Optional*): The model of your device (like: yeelink.light.ceiling22), Get form miio info if empty
- **mode**(*Optional*): `light,fan` Guess from Model if empty
