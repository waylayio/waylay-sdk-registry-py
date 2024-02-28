# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""


from __future__ import annotations
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, ValidationError, field_validator
from pydantic import Field
from typing_extensions import Annotated

from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from pydantic import Field, ConfigDict

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

TIMESTAMPAGE_ANY_OF_SCHEMAS = ["str"]


class TimestampAge(BaseModel):
    """A timestamp expressed as a age relative to now."""

    # data type: str
    anyof_schema_1_validator: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="An ISO8601 period expression"
    )
    # data type: str
    anyof_schema_2_validator: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="An duration expression. A numeric value without unit is interpreted as milliseconds.",
    )
    if TYPE_CHECKING:
        actual_instance: Optional[Union[str]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = TIMESTAMPAGE_ANY_OF_SCHEMAS

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    def __init__(self, *args, **kwargs) -> None:
        """Create a TimestampAge model instance."""
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    @classmethod
    def actual_instance_must_validate_anyof(cls, v):
        """Validate the actual instance on deserialisation."""
        instance = TimestampAge.model_construct()  # noqa: F841
        error_messages = []
        # validate data type: str
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: str
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in TimestampAge with anyOf schemas: str. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Get a dict representation of an object."""
        return cls.from_json(json.dumps(obj, default=str))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Get the object represented by the JSON string."""
        instance = cls.model_construct()  # noqa: F841
        error_messages = []
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into TimestampAge with anyOf schemas: str. Details: "
                + ", ".join(error_messages)
            )
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
