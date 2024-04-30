# waylay.services.registry.ModelsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ModelsApi.md#create) | **POST** /registry/v2/models/ | Create Model
[**delete_asset**](ModelsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Model Asset
[**get_archive**](ModelsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Model Archive
[**get_asset**](ModelsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get File From Model Archive
[**get_latest**](ModelsApi.md#get_latest) | **GET** /registry/v2/models/{name} | Get Latest Model Version
[**get**](ModelsApi.md#get) | **GET** /registry/v2/models/{name}/versions/{version} | Get Model Version
[**jobs**](ModelsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Model Jobs
[**list**](ModelsApi.md#list) | **GET** /registry/v2/models/ | List Models
[**list_versions**](ModelsApi.md#list_versions) | **GET** /registry/v2/models/{name}/versions | List Model Versions
[**patch_metadata**](ModelsApi.md#patch_metadata) | **PATCH** /registry/v2/models/{name}/versions/{version}/metadata | Patch Model Metadata
[**publish**](ModelsApi.md#publish) | **POST** /registry/v2/models/{name}/versions/{version}/publish | Publish Draft Model
[**rebuild**](ModelsApi.md#rebuild) | **POST** /registry/v2/models/{name}/versions/{version}/rebuild | Rebuild Model
[**remove_version**](ModelsApi.md#remove_version) | **DELETE** /registry/v2/models/{name}/versions/{version} | Remove Model Version
[**remove_versions**](ModelsApi.md#remove_versions) | **DELETE** /registry/v2/models/{name} | Remove Model
[**update_asset**](ModelsApi.md#update_asset) | **PUT** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Update Model Asset
[**update_assets**](ModelsApi.md#update_assets) | **PUT** /registry/v2/models/{name}/versions/{version}/content | Update Model Assets
[**verify**](ModelsApi.md#verify) | **POST** /registry/v2/models/{name}/versions/{version}/verify | Verify Health Of Model

# **create**
> create(
> query: CreateQuery,
> files,
> headers
> ) -> PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2

Create Model

Creates a new <em>model</em> function by uploading its assets.      The assets for a <em>model</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>model</em> in the <code>copy</code> argument</li>   </ul>    The required <code>model.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=kfserving</code>).    For each <em>runtime</em> other files will be required or supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Create Model
    # calls `POST /registry/v2/models/`
    api_response = await waylay_client.registry.models.create(
        # query parameters:
        query = {
            'deploy': True
            'scaleToZero': False
            'deprecatePrevious': 'none'
            'dryRun': True
            'async': True
            'draft': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = None # bytearray | The assets for a <em>model</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>model</em> in the <code>copy</code> argument</li>   </ul>    The required <code>model.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=kfserving</code>).    For each <em>runtime</em> other files will be required or supported.  (optional)
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/tar', 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'application/gzip', 'multipart/form-data', 'application/json', '*/*+json', 
        headers = {
            'content-type': 'application/octet-stream'
        },
    )
    print("The response of registry.models.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.create: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | **bytearray** | json request body | The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;model&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;model.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;kfserving&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;model&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;model.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;kfserving&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deprecatePrevious']** (dict) <br> **query.deprecate_previous** (Query) | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
**query['dryRun']** (dict) <br> **query.dry_run** (Query) | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['version']** (dict) <br> **query.version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, the function version will be an increment of the latest existing version that satisfies the &#x60;version&#x60; range. Note that this increment always takes precedence over an explicit &#x60;version&#x60; in the function manifest. | [optional] 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | If set, the value will be used as the function name instead of the one specified in the manifest. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. | [optional] [default False]
**query['runtime']** (dict) <br> **query.runtime** (Query) | **str** | query parameter `"runtime"` | If set, the created function will use the indicated runtime (latest version within specified range).  This takes precedence over the runtime specified in a function manifest (copied or from request body). | [optional] 
**query['copy']** (dict) <br> **query.copy_from** (Query) | [**CreateWebscriptsCopyParameter**](.md) | query parameter `"copy"` | Indicates the _source_ of initial assets for a _new function_.  When using this query parameter, the request body does not need to contain assets, but any assets in the request body will overwrite the copied assets.  #### Selection of _assets_ source  * If set as &#x60;&lt;sourceName&gt;[@&lt;sourceVersionRange&gt;]&#x60;, the _new function_ will be created with copied assets of the selected _source function_. * If set as &#x60;!example&#x60;, a &#x60;runtime&#x60; query parameter is required, and the _new function_ will be initialized with assets of the _runtime example_.  #### Selection of the _source function_  When &#x60;&lt;sourceVersionRange&gt;&#x60; is a range (or is not given), the latest _published_ version (in that range) is used.  If no _published_ version exists, the latest _draft_ is selected.  If no versions in the range exist, a &#x60;404&#x60; _Not Found_ error is returned.  #### The &#x60;name&#x60; of the _new function_  If a &#x60;name&#x60; is NOT specified (either as query parameter, or in an optional manifest asset in the request body), the &#x60;name&#x60; of the _new function_ will be that of the _source function_.  #### The &#x60;version&#x60; of the _new function_  When the _target_ and _source_ name are equal, the &#x60;version&#x60; query parameters is defaulted to &#x60;&lt;sourceVersionRange&gt;&#x60; (&#x60;~&lt;sourceVersionRange&gt;&#x60; when it&#39;s an exact version)  The version of the _new function_ will be: * If a &#x60;version&#x60; is NOT specified (either as query parameter, in an optional manifest asset, or as &#x60;&lt;sourceVersionRange&gt;&#x60; _default_)    * a **patch increment** (&#x60;&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;+1&#x60;) of the latest **existing version** with the target &#x60;name&#x60;    * **&#x60;1.0.0&#x60;** otherwise  * If a &#x60;version&#x60; is specified:    * the **lowest version** in that range **if no existing version** is in that range.    * an **increment** of the latest existing version, **at the highest level** (_major_,_minor_,_patch_) allowed by that range.    * otherwise, if all allowed versions already exist, a **&#x60;409&#x60; _Duplicate_ error** is raised.  #### Deployment overrides  The new function will use the deployment overrides of the copied function, unless a _manifest_ was specified in the request body. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`, `application/tar`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `application/gzip`, `multipart/form-data`, `application/json`, `*/*+json`

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [PostModelJobSyncResponseV2](PostModelJobSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, multipart/form-data, application/json, */*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(
> name: str,
> version: str,
> wildcard: str,
> query: DeleteAssetQuery,
> headers
> ) -> PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2

Delete Model Asset

Delete an asset from the model's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Delete Model Asset
    # calls `DELETE /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.models.delete_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
    )
    print("The response of registry.models.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.delete_asset: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [PostModelJobSyncResponseV2](PostModelJobSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive**
> get_archive(
> name: str,
> version: str,
> query: GetArchiveQuery,
> headers
> ) -> bytearray

Get Model Archive

Get the specification archive of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
try:
    # Get Model Archive
    # calls `GET /registry/v2/models/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.models.get_archive(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.models.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.get_archive: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** (dict) <br> **query.ls** (Query) | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`bytearray`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> get_asset(
> name: str,
> version: str,
> wildcard: str,
> query: GetAssetQuery,
> headers
> ) -> bytearray

Get File From Model Archive

Get a file from the specification archive of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
try:
    # Get File From Model Archive
    # calls `GET /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.models.get_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.models.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.get_asset: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** (dict) <br> **query.ls** (Query) | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`bytearray`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest**
> get_latest(
> name: str,
> query: GetLatestQuery,
> headers
> ) -> GetModelResponseV2

Get Latest Model Version

Fetch the latest version of a <em>model</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>model version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Get Latest Model Version
    # calls `GET /registry/v2/models/{name}`
    api_response = await waylay_client.registry.models.get_latest(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'includeDraft': True
            'includeDeprecated': True
        },
    )
    print("The response of registry.models.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.get_latest: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetModelResponseV2`** |  | [GetModelResponseV2](GetModelResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> name: str,
> version: str,
> headers
> ) -> GetModelResponseV2

Get Model Version

Get a model by name and version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Get Model Version
    # calls `GET /registry/v2/models/{name}/versions/{version}`
    api_response = await waylay_client.registry.models.get(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.models.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetModelResponseV2`** |  | [GetModelResponseV2](GetModelResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> jobs(
> name: str,
> version: str,
> query: JobsQuery,
> headers
> ) -> JobsForModelResponseV2

List Model Jobs

List the ongoing and completed operations on a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_for_model_response_v2 import JobsForModelResponseV2
try:
    # List Model Jobs
    # calls `GET /registry/v2/models/{name}/versions/{version}/jobs`
    api_response = await waylay_client.registry.models.jobs(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
        },
    )
    print("The response of registry.models.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.jobs: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/jobs
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['type']** (dict) <br> **query.type** (Query) | [**List[JobTypeSchema]**](JobTypeSchema.md) | query parameter `"type"` | Filter on job type | [optional] 
**query['state']** (dict) <br> **query.state** (Query) | [**List[JobStateResult]**](JobStateResult.md) | query parameter `"state"` | Filter on job state | [optional] 
**query['functionType']** (dict) <br> **query.function_type** (Query) | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | Filter on function type | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on jobs that created before the given timestamp or age | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on jobs that created after the given timestamp or age | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`JobsForModelResponseV2`** |  | [JobsForModelResponseV2](JobsForModelResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> LatestModelsResponseV2

List Models

List the (latest) versions of available <em>models</em>.  ### List Latest Model Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>model</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no version filters are used, each listed <em>model version</em> contains representations of the latest draft (`entities[]._links.draft`)  or latest published (`entities[]._links.published`) version (if existing and different).   Use the query parameter `showRelated` to include only a link (default `showRelated=link`) or a full representation (`showRelated=embed`).  ### List Latest Model Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>model</em> that satisfy the filters, but **without links**.  ### List All Model Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>models</em> versions that satisfy the query, possibly multiple versions per named <em>models</em>. No HAL links are provided.  #### Filter on _status_ By default <em>model versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>model</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft` 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.latest_models_response_v2 import LatestModelsResponseV2
from waylay.services.registry.models.show_related_type import ShowRelatedType
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Models
    # calls `GET /registry/v2/models/`
    api_response = await waylay_client.registry.models.list(
        # query parameters:
        query = {
            'includeDraft': True
            'includeDeprecated': True
            'deprecated': True
            'draft': True
            'createdBy': '@me'
            'updatedBy': '@me'
            'latest': True
            'showRelated': 'embed'
        },
    )
    print("The response of registry.models.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** (dict) <br> **query.page** (Query) | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**query['deprecated']** (dict) <br> **query.deprecated** (Query) | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['nameVersion']** (dict) <br> **query.name_version** (Query) | [**List[str]**](str.md) | query parameter `"nameVersion"` | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
**query['version']** (dict) <br> **query.version** (Query) | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['runtimeVersion']** (dict) <br> **query.runtime_version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"runtimeVersion"` | Filter on the runtime version. | [optional] 
**query['createdBy']** (dict) <br> **query.created_by** (Query) | **str** | query parameter `"createdBy"` | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['updatedBy']** (dict) <br> **query.updated_by** (Query) | **str** | query parameter `"updatedBy"` | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on funtions that were created before the given timestamp or age. | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on funtions that were created after the given timestamp or age. | [optional] 
**query['updatedBefore']** (dict) <br> **query.updated_before** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedBefore"` | Filter on funtions that were updated before the given timestamp or age. | [optional] 
**query['updatedAfter']** (dict) <br> **query.updated_after** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedAfter"` | Filter on funtions that were updated after the given timestamp or age. | [optional] 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** (dict) <br> **query.runtime** (Query) | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**query['latest']** (dict) <br> **query.latest** (Query) | **bool** | query parameter `"latest"` | When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;, except when specific versions are selected with the &#x60;nameVersion&#x60; filter. | [optional] 
**query['showRelated']** (dict) <br> **query.show_related** (Query) | [**ShowRelatedType**](.md) | query parameter `"showRelated"` | Sets the representation of related function versions (like the _latest_ draft and/or published) in the response. - &#x60;embed&#x60;: as full summary representation (in &#x60;_embedded&#x60;). - &#x60;link&#x60;: as HAL link in (in &#x60;_links&#x60;). - &#x60;none&#x60;: omitted. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`LatestModelsResponseV2`** |  | [LatestModelsResponseV2](LatestModelsResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> list_versions(
> name: str,
> query: ListVersionsQuery,
> headers
> ) -> ModelVersionsResponseV2

List Model Versions

List all deployed versions of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.model_versions_response_v2 import ModelVersionsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Model Versions
    # calls `GET /registry/v2/models/{name}/versions`
    api_response = await waylay_client.registry.models.list_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'deprecated': True
            'draft': True
            'createdBy': '@me'
            'updatedBy': '@me'
        },
    )
    print("The response of registry.models.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.list_versions: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** (dict) <br> **query.page** (Query) | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['deprecated']** (dict) <br> **query.deprecated** (Query) | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['version']** (dict) <br> **query.version** (Query) | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['runtimeVersion']** (dict) <br> **query.runtime_version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"runtimeVersion"` | Filter on the runtime version. | [optional] 
**query['createdBy']** (dict) <br> **query.created_by** (Query) | **str** | query parameter `"createdBy"` | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['updatedBy']** (dict) <br> **query.updated_by** (Query) | **str** | query parameter `"updatedBy"` | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on funtions that were created before the given timestamp or age. | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on funtions that were created after the given timestamp or age. | [optional] 
**query['updatedBefore']** (dict) <br> **query.updated_before** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedBefore"` | Filter on funtions that were updated before the given timestamp or age. | [optional] 
**query['updatedAfter']** (dict) <br> **query.updated_after** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedAfter"` | Filter on funtions that were updated after the given timestamp or age. | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** (dict) <br> **query.runtime** (Query) | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ModelVersionsResponseV2`** |  | [ModelVersionsResponseV2](ModelVersionsResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metadata**
> patch_metadata(
> name: str,
> version: str,
> query: PatchMetadataQuery,
> headers
> ) -> GetModelResponseV2

Patch Model Metadata

Patch the metadata of a model version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_meta import FunctionMeta
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Patch Model Metadata
    # calls `PATCH /registry/v2/models/{name}/versions/{version}/metadata`
    api_response = await waylay_client.registry.models.patch_metadata(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.FunctionMeta() # FunctionMeta |  (optional)
    )
    print("The response of registry.models.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.patch_metadata: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/models/{name}/versions/{version}/metadata
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**FunctionMeta**](FunctionMeta.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetModelResponseV2`** |  | [GetModelResponseV2](GetModelResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> publish(
> name: str,
> version: str,
> query: PublishQuery,
> headers
> ) -> PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2

Publish Draft Model

Mark the <em>model</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>model</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Publish Draft Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/publish`
    api_response = await waylay_client.registry.models.publish(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'chown': False
            'deprecatePrevious': 'none'
            'async': True
        },
    )
    print("The response of registry.models.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.publish: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/publish
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['deprecatePrevious']** (dict) <br> **query.deprecate_previous** (Query) | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [PostModelJobSyncResponseV2](PostModelJobSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Model Published |  -  |
**202** | Model Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> rebuild(
> name: str,
> version: str,
> query: RebuildQuery,
> headers
> ) -> RebuildModelSyncResponseV2 \| RebuildModelAsyncResponseV2

Rebuild Model

Rebuild and deploy a model with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.rebuild_model_sync_response_v2 import RebuildModelSyncResponseV2
from waylay.services.registry.models.rebuild_policy import RebuildPolicy
try:
    # Rebuild Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/rebuild`
    api_response = await waylay_client.registry.models.rebuild(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'dryRun': True
            'async': True
            'upgrade': 'patch'
            'ignoreChecks': True
            'skipRebuild': True
        },
    )
    print("The response of registry.models.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.rebuild: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/rebuild
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['dryRun']** (dict) <br> **query.dry_run** (Query) | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, checks whether rebuild jobs are needed, but do not start any jobs. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['upgrade']** (dict) <br> **query.upgrade** (Query) | [**RebuildPolicy**](.md) | query parameter `"upgrade"` | If set, force a rebuild with the given &lt;em&gt;runtime&lt;/em&gt; version selection policy. &lt;ul&gt;  &lt;li&gt;&lt;code&gt;same&lt;/code&gt; &lt;b&gt;patch&lt;/b&gt; version.   This should only include backward compatible upgrades.  &lt;/li&gt;  &lt;li&gt;&lt;code&gt;minor&lt;/code&gt; &lt;b&gt;major&lt;/b&gt; version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .&lt;/li&gt; &lt;/ul&gt; | [optional] 
**query['forceVersion']** (dict) <br> **query.force_version** (Query) | **str** | query parameter `"forceVersion"` | If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the &#x60;upgrade&#x60; parameter. | [optional] 
**query['ignoreChecks']** (dict) <br> **query.ignore_checks** (Query) | **bool** | query parameter `"ignoreChecks"` | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
**query['skipRebuild']** (dict) <br> **query.skip_rebuild** (Query) | **bool** | query parameter `"skipRebuild"` | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RebuildModelSyncResponseV2 \| RebuildModelAsyncResponseV2`** |  | [RebuildModelSyncResponseV2](RebuildModelSyncResponseV2.md) <br> [RebuildModelAsyncResponseV2](RebuildModelAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_version**
> remove_version(
> name: str,
> version: str,
> query: RemoveVersionQuery,
> headers
> ) -> UndeployedResponseV2 \| UndeploySubmittedResponseV2

Remove Model Version

Deprecate, undeploy and/or remove a <em>model</em> version.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
try:
    # Remove Model Version
    # calls `DELETE /registry/v2/models/{name}/versions/{version}`
    api_response = await waylay_client.registry.models.remove_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'async': True
            'force': True
            'undeploy': True
        },
    )
    print("The response of registry.models.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.remove_version: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['force']** (dict) <br> **query.force** (Query) | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`UndeployedResponseV2 \| UndeploySubmittedResponseV2`** |  | [UndeployedResponseV2](UndeployedResponseV2.md) <br> [UndeploySubmittedResponseV2](UndeploySubmittedResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_versions**
> remove_versions(
> name: str,
> query: RemoveVersionsQuery,
> headers
> ) -> UndeployedResponseV2 \| UndeploySubmittedResponseV2

Remove Model

Deprecate, undeploy and/or remove all versions of this named <em>model</em>.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
try:
    # Remove Model
    # calls `DELETE /registry/v2/models/{name}`
    api_response = await waylay_client.registry.models.remove_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'force': True
            'undeploy': True
            'async': True
        },
    )
    print("The response of registry.models.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.remove_versions: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['force']** (dict) <br> **query.force** (Query) | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`UndeployedResponseV2 \| UndeploySubmittedResponseV2`** |  | [UndeployedResponseV2](UndeployedResponseV2.md) <br> [UndeploySubmittedResponseV2](UndeploySubmittedResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> update_asset(
> name: str,
> version: str,
> wildcard: str,
> query: UpdateAssetQuery,
> headers
> ) -> PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2

Update Model Asset

The provided asset will be added to the <em>model</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the model.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.file_upload import FileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Update Model Asset
    # calls `PUT /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.models.update_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 
        headers = {
            'content-type': 'application/octet-stream'
        },
    )
    print("The response of registry.models.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.update_asset: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | A single asset file. | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [PostModelJobSyncResponseV2](PostModelJobSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assets**
> update_assets(
> name: str,
> version: str,
> query: UpdateAssetsQuery,
> files,
> headers
> ) -> PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2

Update Model Assets

Update a draft <em>model</em> function by updating its assets.      The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>model</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Update Model Assets
    # calls `PUT /registry/v2/models/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.models.update_assets(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/tar', 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'application/gzip', 'multipart/form-data', 
        headers = {
            'content-type': 'application/octet-stream'
        },
    )
    print("The response of registry.models.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.update_assets: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/models/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;model&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`, `application/tar`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `application/gzip`, `multipart/form-data`

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostModelJobSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [PostModelJobSyncResponseV2](PostModelJobSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> verify(
> name: str,
> version: str,
> query: VerifyQuery,
> headers
> ) -> VerifyModelSyncResponseV2 \| PostModelJobAsyncResponseV2

Verify Health Of Model

Verify health of model deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.verify_model_sync_response_v2 import VerifyModelSyncResponseV2
try:
    # Verify Health Of Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/verify`
    api_response = await waylay_client.registry.models.verify(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'async': True
        },
    )
    print("The response of registry.models.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.models.verify: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/verify
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`VerifyModelSyncResponseV2 \| PostModelJobAsyncResponseV2`** |  | [VerifyModelSyncResponseV2](VerifyModelSyncResponseV2.md) <br> [PostModelJobAsyncResponseV2](PostModelJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Model Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

