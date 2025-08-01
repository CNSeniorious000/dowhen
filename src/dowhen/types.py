# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/dowhen/blob/master/NOTICE


import re
from typing import Literal

IdentifierType = int | str | re.Pattern | Literal["<start>", "<return>"] | None
