# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from ..models.latest_function_versions_query import LatestFunctionVersionsQuery
from ..models.latest_functions_query import LatestFunctionsQuery

from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

KFSERVINGLATESTVERSIONSQUERYV2_ANY_OF_SCHEMAS = ["LatestFunctionVersionsQuery", "LatestFunctionsQuery"]


class KFServingLatestVersionsQueryV2(BaseModel):
    """Latest model versions listing query.."""

    # data type: LatestFunctionVersionsQuery
    anyof_schema_1_validator: Optional[LatestFunctionVersionsQuery] = None
    # data type: LatestFunctionsQuery
    anyof_schema_2_validator: Optional[LatestFunctionsQuery] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[LatestFunctionVersionsQuery, LatestFunctionsQuery]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = KFSERVINGLATESTVERSIONSQUERYV2_ANY_OF_SCHEMAS

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        """Create a KFServingLatestVersionsQueryV2 model instance."""
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    @classmethod
    def actual_instance_must_validate_anyof(cls, v):
        """Validate the actual instance on deserialisation."""
        instance = KFServingLatestVersionsQueryV2.model_construct()
        error_messages = []
        # validate data type: LatestFunctionVersionsQuery
        if not isinstance(v, LatestFunctionVersionsQuery):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LatestFunctionVersionsQuery`")
        else:
            return v

        # validate data type: LatestFunctionsQuery
        if not isinstance(v, LatestFunctionsQuery):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LatestFunctionsQuery`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in KFServingLatestVersionsQueryV2 with anyOf schemas: LatestFunctionVersionsQuery, LatestFunctionsQuery. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Get a dict representation of an object."""
        return cls.from_json(json.dumps(obj, default=str))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Get the object represented by the JSON string."""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[LatestFunctionVersionsQuery] = None
        try:
            instance.actual_instance = LatestFunctionVersionsQuery.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[LatestFunctionsQuery] = None
        try:
            instance.actual_instance = LatestFunctionsQuery.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into KFServingLatestVersionsQueryV2 with anyOf schemas: LatestFunctionVersionsQuery, LatestFunctionsQuery. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Get the JSON representation of the actual instance."""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()  # type: ignore
        else:
            return json.dumps(self.actual_instance, default=str)

    def to_dict(self) -> Optional[Dict]:
        """Get the dict representation of the actual instance."""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()  # type: ignore
        else:
            return json.dumps(self.actual_instance, default=str)  # type: ignore

    def to_str(self) -> str:
        """Get the string representation of the actual instance."""
        return pprint.pformat(self.model_dump())
