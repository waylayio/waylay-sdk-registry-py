# UpdateRecord

An update report corresponding to a modifying operation initiated by a user/administrator on the entity.

**Source:** `waylay.services.registry.models.update_record`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**operation** | [**RequestOperation**](RequestOperation.md) |  | 
**jobs** | **List[str]** | The job id&#39;s of the corresponding jobs, if applicable. | [optional] 
**at** | **datetime** |  | 
**by** | **str** | The user that initiated this operation. | 


## Example

```python
from waylay.services.registry.models.update_record import UpdateRecord

update_record = UpdateRecord(comment=..., operation=..., jobs=..., at=..., by=...)

# Create from JSON
update_record = UpdateRecord.from_json(
    '{ "comment": ..., "operation": ..., "jobs": ..., "at": ..., "by": ... }'
)

# Export to dictionary
update_record_dict = update_record.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


