# Copyright 2020 Jacob Glueck
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing as t
from tako.core.types import *


@protogen
def basic() -> t.Dict[str, t.Any]:
    return {"Foo": Struct(x=i8), "Bar": Struct(x=i8)}


@protogen
def basic_pair() -> t.Dict[str, t.Any]:
    return {"FooPair": Struct(a=basic.Foo, b=basic.Foo)}


@protogen
def basic_transform() -> t.Dict[str, t.Any]:
    original = basic.as_dict()
    return {
        **original,
        "Msg": Variant[u8](
            {
                struct: index
                for index, struct in enumerate(original.values())
                if isinstance(struct, StructDef)
            }
        ),
    }
