
Install Virtualenv

```bash
    pip3 install virtualenv
    virtualenv venv --python=python3
    source venv/bin/activate
    pip install -r requirements.txt
```


Flash

```bash
    esptool.py --port /dev/cu.wchusbserial1440 erase_flash
    esptool.py --port /dev/cu.wchusbserial1440 --baud 460800 write_flash -fm dio --flash_size=detect 0 esp8266-20180511-v1.9.4.bin
    esptool.py --port /dev/cu.wchusbserial1440 --baud 460800 write_flash --flash_size=detect 0 esp8266-20180511-v1.9.4.bin
```

manage files

```bash
    ampy --port /dev/cu.wchusbserial1440 ls
    ampy --port /dev/tty.usbserial-1440 ls
    screen /dev/cu.wchusbserial1440 115200
```

upip

```python
import gc
import upip
gc.mem_free()
gc.collect()
gc.mem_free()

upip.install('micropython-contextlib')
upip.install('micropython-pcd8544')
```

```bash
micropython -m upip install micropython-umqtt.simple
```

```python
import gc
import micropython

def foo(i):
    gc.collect()
    a = gc.mem_free()
    b = bytearray(i)
    c = gc.mem_free()
    print('bytearray({}) took {} bytes'.format(i, a - c))

for i in range(64):
    foo(i)
```

```bash
    ./webrepl_cli.py cozir.py 192.168.0.199:/cozir.py
```


refs

- https://bigl.es/tooling-tuesday-wemos-d1-mini-micropython/
- https://github.com/mcauser/MicroPython-ESP8266-Nokia-5110-Conways-Game-of-Life
- https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/basics.html#external-components
- https://forum.micropython.org/viewtopic.php?f=16&t=2078&start=20
- https://boneskull.com/micropython-on-esp32-part-2/
- https://kapusta.cc/2018/03/31/epd/
- http://seenaburns.com/2018/04/04/writing-to-the-framebuffer/
