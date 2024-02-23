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
from ..models.job_event_sse import JobEventSSE
from ..models.keep_alive_event_sse import KeepAliveEventSSE
from ..models.stream_closing import StreamClosing
from ..models.stream_ready import StreamReady

from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field, ConfigDict
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

EVENTWITHCLOSESSE_ANY_OF_SCHEMAS = ["JobEventSSE", "KeepAliveEventSSE", "StreamClosing", "StreamReady"]


class EventWithCloseSSE(BaseModel):
    """SSE stream events with closing protocol."""

    # data type: StreamReady
    anyof_schema_1_validator: Optional[StreamReady] = None
    # data type: JobEventSSE
    anyof_schema_2_validator: Optional[JobEventSSE] = None
    # data type: KeepAliveEventSSE
    anyof_schema_3_validator: Optional[KeepAliveEventSSE] = None
    # data type: StreamClosing
    anyof_schema_4_validator: Optional[StreamClosing] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[JobEventSSE, KeepAliveEventSSE, StreamClosing, StreamReady]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = EVENTWITHCLOSESSE_ANY_OF_SCHEMAS

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    def __init__(self, *args, **kwargs) -> None:
        """Create a EventWithCloseSSE model instance."""
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
        instance = EventWithCloseSSE.model_construct()
        error_messages = []
        # validate data type: StreamReady
        if not isinstance(v, StreamReady):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StreamReady`")
        else:
            return v

        # validate data type: JobEventSSE
        if not isinstance(v, JobEventSSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JobEventSSE`")
        else:
            return v

        # validate data type: KeepAliveEventSSE
        if not isinstance(v, KeepAliveEventSSE):
            error_messages.append(f"Error! Input type `{type(v)}` is not `KeepAliveEventSSE`")
        else:
            return v

        # validate data type: StreamClosing
        if not isinstance(v, StreamClosing):
            error_messages.append(f"Error! Input type `{type(v)}` is not `StreamClosing`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in EventWithCloseSSE with anyOf schemas: JobEventSSE, KeepAliveEventSSE, StreamClosing, StreamReady. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[StreamReady] = None
        try:
            instance.actual_instance = StreamReady.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[JobEventSSE] = None
        try:
            instance.actual_instance = JobEventSSE.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[KeepAliveEventSSE] = None
        try:
            instance.actual_instance = KeepAliveEventSSE.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[StreamClosing] = None
        try:
            instance.actual_instance = StreamClosing.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EventWithCloseSSE with anyOf schemas: JobEventSSE, KeepAliveEventSSE, StreamClosing, StreamReady. Details: " + ", ".join(error_messages))
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
