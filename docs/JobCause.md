# JobCause

The motivation for including or excluding a job (<em>build</em>, <em>deploy</em>, <em>verify</em>, ...) in response to a <em>rebuild</em> request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the argument configuration for this job has changed in comparison to the previous job execution. A &lt;code&gt;false&lt;/code&gt; will prevent the job to be run. Use &lt;code&gt;forceVersion&lt;/code&gt; or &lt;code&gt;upgrade&lt;/code&gt; parameter to force a rebuild. | 
**reason** | **str** | Human readable message describing the cause. | 
**backoff** | **bool** | If &lt;code&gt;true&lt;/code&gt;, recent failures of the job prevented the re-execution. Use &lt;code&gt;forceVersion&lt;/code&gt; or &lt;code&gt;upgrade&lt;/code&gt; parameter to force a rebuild. | [optional] 
**new_value** | **object** | The new configuration value that causes the change. | [optional] 
**old_value** | **object** | The old configuration value used by the last succeeded job. | [optional] 

## Example

```python
from waylay.services.registry.models.job_cause import JobCause

# TODO update the JSON string below
json = "{}"
# create an instance of JobCause from a JSON string
job_cause_instance = JobCause.from_json(json)
# print the JSON string representation of the object
print JobCause.to_json()

# convert the object into a dict
job_cause_dict = job_cause_instance.to_dict()
# create an instance of JobCause from a dict
job_cause_form_dict = job_cause.from_dict(job_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


