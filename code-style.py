## django code style

### 1.1 make your code readable

- avoid abbreviate variable name
- write out your function argument names
- document your class and methods
- comment your code
- refactor repeated lines of code into reusable funcitons or methods
- keep function and methods short. A good rule of thumb is that scrolling should not be necessary to read an entire function or method

### 1.2 PEP8

All the python file in your django projects should follow `PEP8`. If you have trouble remembering the PEP8 guidelines, find a plugin for your code editor that checks your code as you type.

`Tip1:`
Use flake8 for checking code quality
https://flake8.readthedocs.org/en/latest/

### 1.3 The world on imports

PEP8 suggests that imports should be grouped in the following order:

- Standard library imports
- Related django imports
- Related third-party imports
- Local application or library specific imports

```
Example 1
# standard imports
from __future__ import absolute_import
from math import sqrt
from os.path import abspath

# core django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# third-party app imports
from django_extensions.db.models import TimeStampedModel

# user related app imports
from userapp.models import Customer
```

### 1.4 Use __future__ feature

- use unicode
- use absolute import

```
from __future__ import unicode_literals
from __future__ import absolute_import
```

### 1.5 Use utf-8

```
# -*- coding: utf-8 -*-
```

### 1.6 Use splicit relative imports

> Never use implicit import

- One file import the other file which in the same package

Dir list

```
- package-eg
	- __init__.py
	- v1.py
	- v2.py
```

`v1.py`

```
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

data = (1, 2, 3,)
```

`v2.py`
	
```
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

# splicit relative import
from .v1 import data

data = (1, 2, 3,)
```


- One file import the other file which in the different package

Dir list

```
- package-eg-1
	- __init__.py
	- v1.py
- package-eg-2
	- __init__.py
	- v2.py
```

`v1.py`

```
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

data = (1, 2, 3,)
```

`v2.py`
	
```
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

# splicit absolute import
from package-eg-1.v1 import data

data = (1, 2, 3,)
```

### 1.7 Avoid Using import *

Please avoid using import * generally, but which is not absolute. 

In the specially case, you could use it.

For example:

```
# log.py

LOG_CONFIG = {

}

# settings.py

from .log import *
```
