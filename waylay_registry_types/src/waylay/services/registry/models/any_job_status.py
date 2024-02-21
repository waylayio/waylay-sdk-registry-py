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
from ..models.batch_job_status import BatchJobStatus
from ..models.build_job_status import BuildJobStatus
from ..models.deploy_job_status import DeployJobStatus
from ..models.scale_job_status import ScaleJobStatus
from ..models.undeploy_job_status import UndeployJobStatus
from ..models.verify_job_status import VerifyJobStatus

from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

ANYJOBSTATUS_ANY_OF_SCHEMAS = ["BatchJobStatus", "BuildJobStatus", "DeployJobStatus", "ScaleJobStatus", "UndeployJobStatus", "VerifyJobStatus"]


class AnyJobStatus(BaseModel):
    """AnyJobStatus."""

    # data type: BuildJobStatus
    anyof_schema_1_validator: Optional[BuildJobStatus] = None
    # data type: DeployJobStatus
    anyof_schema_2_validator: Optional[DeployJobStatus] = None
    # data type: VerifyJobStatus
    anyof_schema_3_validator: Optional[VerifyJobStatus] = None
    # data type: UndeployJobStatus
    anyof_schema_4_validator: Optional[UndeployJobStatus] = None
    # data type: ScaleJobStatus
    anyof_schema_5_validator: Optional[ScaleJobStatus] = None
    # data type: BatchJobStatus
    anyof_schema_6_validator: Optional[BatchJobStatus] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[BatchJobStatus, BuildJobStatus, DeployJobStatus, ScaleJobStatus, UndeployJobStatus, VerifyJobStatus]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = ANYJOBSTATUS_ANY_OF_SCHEMAS

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        """Create a AnyJobStatus model instance."""
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
        instance = AnyJobStatus.model_construct()
        error_messages = []
        # validate data type: BuildJobStatus
        if not isinstance(v, BuildJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BuildJobStatus`")
        else:
            return v

        # validate data type: DeployJobStatus
        if not isinstance(v, DeployJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeployJobStatus`")
        else:
            return v

        # validate data type: VerifyJobStatus
        if not isinstance(v, VerifyJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VerifyJobStatus`")
        else:
            return v

        # validate data type: UndeployJobStatus
        if not isinstance(v, UndeployJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UndeployJobStatus`")
        else:
            return v

        # validate data type: ScaleJobStatus
        if not isinstance(v, ScaleJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScaleJobStatus`")
        else:
            return v

        # validate data type: BatchJobStatus
        if not isinstance(v, BatchJobStatus):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BatchJobStatus`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in AnyJobStatus with anyOf schemas: BatchJobStatus, BuildJobStatus, DeployJobStatus, ScaleJobStatus, UndeployJobStatus, VerifyJobStatus. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[BuildJobStatus] = None
        try:
            instance.actual_instance = BuildJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[DeployJobStatus] = None
        try:
            instance.actual_instance = DeployJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[VerifyJobStatus] = None
        try:
            instance.actual_instance = VerifyJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[UndeployJobStatus] = None
        try:
            instance.actual_instance = UndeployJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[ScaleJobStatus] = None
        try:
            instance.actual_instance = ScaleJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[BatchJobStatus] = None
        try:
            instance.actual_instance = BatchJobStatus.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AnyJobStatus with anyOf schemas: BatchJobStatus, BuildJobStatus, DeployJobStatus, ScaleJobStatus, UndeployJobStatus, VerifyJobStatus. Details: " + ", ".join(error_messages))
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
