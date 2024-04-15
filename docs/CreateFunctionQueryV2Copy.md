# CreateFunctionQueryV2Copy

Indicates the _source_ of initial assets for a _new function_.  When using this query parameter, the request body does not need to contain assets, but any assets in the request body will overwrite the copied assets.  #### Selection of _assets_ source  * If set as `<sourceName>[@<sourceVersionRange>]`, the _new function_ will be created with copied assets of the selected _source function_. * If set as `!example`, a `runtime` query parameter is required, and the _new function_ will be initialized with assets of the _runtime example_.  #### Selection of the _source function_  When `<sourceVersionRange>` is a range (or is not given), the latest _published_ version (in that range) is used.  If no _published_ version exists, the latest _draft_ is selected.  If no versions in the range exist, a `404` _Not Found_ error is returned.  #### The `name` of the _new function_  If a `name` is NOT specified (either as query parameter, or in an optional manifest asset in the request body), the `name` of the _new function_ will be that of the _source function_.  #### The `version` of the _new function_  When the _target_ and _source_ name are equal, the `version` query parameters is defaulted to `<sourceVersionRange>` (`~<sourceVersionRange>` when it's an exact version)  The version of the _new function_ will be: * If a `version` is NOT specified (either as query parameter, in an optional manifest asset, or as `<sourceVersionRange>` _default_)    * a **patch increment** (`<major>.<minor>.<patch>+1`) of the latest **existing version** with the target `name`    * **`1.0.0`** otherwise  * If a `version` is specified:    * the **lowest version** in that range **if no existing version** is in that range.    * an **increment** of the latest existing version, **at the highest level** (_major_,_minor_,_patch_) allowed by that range.    * otherwise, if all allowed versions already exist, a **`409` _Duplicate_ error** is raised.  #### Deployment overrides  The new function will use the deployment overrides of the copied function, unless a _manifest_ was specified in the request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.create_function_query_v2_copy import CreateFunctionQueryV2Copy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFunctionQueryV2Copy from a JSON string
create_function_query_v2_copy_instance = CreateFunctionQueryV2Copy.from_json(json)
# print the JSON string representation of the object
print CreateFunctionQueryV2Copy.to_json()

# convert the object into a dict
create_function_query_v2_copy_dict = create_function_query_v2_copy_instance.to_dict()
# create an instance of CreateFunctionQueryV2Copy from a dict
create_function_query_v2_copy_form_dict = create_function_query_v2_copy.from_dict(create_function_query_v2_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


