# Xiaomi Miio For Yeelink devices

## Tested Devices

- MJXDD02YL | yeelink.light.ceiling21
- MJXDD01SYL | yeelink.light.ceiling22
- MJXDD03YL | yeelink.light.ceiling23
- YLXD56YL | yeelink.light.ceiling18
- YLMB05YL | yeelink.light.panel1
- YLYB02YL | yeelink.bhf_light.v2
- YLFD02YL | yeelink.light.fancl1
- YLYB05YL | yeelink.ven_fan.vf1

## Tested By Community
- yeelink.bhf_light.v1
- yeelink.light.lamp3
- yeelink.light.lamp5
- yeelink.light.fancl2
- yeelink.light.fancl3


## Installing

> Download and copy `miio_yeelink` folder to `custom_components` folder in your HomeAssistant config folder

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


## Obtain miio token

- Use MiHome mod by [@vevsvevs](https://github.com/custom-components/ble_monitor/issues/7#issuecomment-595874419)
  1. Down apk from [СКАЧАТЬ ВЕРСИЮ 5.x.x](https://www.kapiba.ru/2017/11/mi-home.html)
  2. Create folder `/your_interlal_storage/vevs/logs/`
  3. Find token from `vevs/logs/misc/devices.txt`
