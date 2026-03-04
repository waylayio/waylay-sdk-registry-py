# JobCause

The motivation for including or excluding a job (<em>build</em>, <em>deploy</em>, <em>verify</em>, ...) in response to a <em>rebuild</em> request.

**Source:** `waylay.services.registry.models.job_cause`




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

job_cause = JobCause(changed=..., reason=..., backoff=..., new_value=..., old_value=...)

# Create from JSON
job_cause = JobCause.from_json(
    '{ "changed": ..., "reason": ..., "backoff": ..., "newValue": ..., "oldValue": ... }'
)

# Export to dictionary
job_cause_dict = job_cause.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


