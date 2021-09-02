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
- yeelink.bhf_light.v5
- yeelink.light.lamp3
- yeelink.light.lamp5
- yeelink.light.fancl2
- yeelink.light.fancl3
- yeelink.light.color5 ([#26](https://github.com/al-one/hass-miio-yeelink/issues/26))


## Installing

> Download and copy `custom_components/miio_yeelink` folder to `custom_components` folder in your HomeAssistant config folder

```shell
# Auto install via terminal shell
wget -q -O - https://cdn.jsdelivr.net/gh/al-one/hass-xiaomi-miot/install.sh | DOMAIN=miio_yeelink REPO_PATH=al-one/hass-miio-yeelink bash -
```

> Or you can install component with [HACS](https://hacs.xyz)


## Config

### HomeAssistant GUI

> Configuration > Integration > ➕ > Miio For Yeelink

### Configuration variables:

- **host**(*Required*): The IP of your device
- **token**(*Required*): The Token of your device
- **name**(*Optional*): The name of your device
- **model**(*Optional*): The model of your device (like: yeelink.light.ceiling22), Get form miio info if empty
- **mode**(*Optional*): `light,fan` Guess from Model if empty

### Customize entity

```yaml
# configuration.yaml
homeassistant:
  customize: !include customize.yaml

# customize.yaml (Configuration > Customize > Select Entity > Add Other Attribute)
light.your_entity_id:
  support_color: true
  support_brightness: true
  support_color_temp: true
  min_color_temp: 2700
  max_color_temp: 6500

fan.your_entity_id:
  support_oscillate: true
  support_direction: true
```


## Obtain miio token

- Use MiHome mod by [@vevsvevs](https://github.com/custom-components/ble_monitor/issues/7#issuecomment-595874419)
  1. Down apk from [СКАЧАТЬ ВЕРСИЮ 6.x.x](https://www.kapiba.ru/2017/11/mi-home.html)
  2. Create folder `/your_interlal_storage/vevs/logs/`
  3. Find token from `vevs/logs/misc/devices.txt`
