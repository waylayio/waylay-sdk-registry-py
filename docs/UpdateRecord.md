# UpdateRecord

An update report corresponding to a modifying operation initiated by a user/administrator on the entity.

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

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRecord from a JSON string
update_record_instance = UpdateRecord.from_json(json)
# print the JSON string representation of the object
print UpdateRecord.to_json()

# convert the object into a dict
update_record_dict = update_record_instance.to_dict()
# create an instance of UpdateRecord from a dict
update_record_form_dict = update_record.from_dict(update_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


