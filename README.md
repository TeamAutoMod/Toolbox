# Toolbox
A few simple Python utils

### Install
```shell
py -3 -m pip install toolbox-py
```

### Usage
```py
from toolbox import asciify


string = asciify("t̤̜̗e͖s̯̘͓t̜̣̮̼͉̣̜")

if __name__ == "__main__":
    print(string) # -> test
```

```py
from toolbox import S


data = {
    "username": "xezzz",
    "password": "123",
    "info": {
        "role": "dev",
        "location": "Germany"
    }
 }

obj = S(data)

if __name__ == "__main__":
    print(obj.username) # -> xezzz

    print(obj.info.role) # -> dev
```
