# waylay.services.registry.PlugsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PlugsApi.md#create) | **POST** /registry/v2/plugs/ | Create Plug
[**delete_asset**](PlugsApi.md#delete_asset) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Delete Plug Asset
[**get_archive**](PlugsApi.md#get_archive) | **GET** /registry/v2/plugs/{name}/versions/{version}/content | Get Plug Archive
[**get_asset**](PlugsApi.md#get_asset) | **GET** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Get File From Plug Archive
[**get_latest**](PlugsApi.md#get_latest) | **GET** /registry/v2/plugs/{name} | Get Latest Plug Version
[**get**](PlugsApi.md#get) | **GET** /registry/v2/plugs/{name}/versions/{version} | Get Plug Version
[**jobs**](PlugsApi.md#jobs) | **GET** /registry/v2/plugs/{name}/versions/{version}/jobs | List Plug Jobs
[**list**](PlugsApi.md#list) | **GET** /registry/v2/plugs/ | List Plugs
[**list_versions**](PlugsApi.md#list_versions) | **GET** /registry/v2/plugs/{name}/versions | List Plug Versions
[**patch_interface**](PlugsApi.md#patch_interface) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/interface | Patch Plug Interface
[**patch_metadata**](PlugsApi.md#patch_metadata) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/metadata | Patch Plug Metadata
[**protect**](PlugsApi.md#protect) | **POST** /registry/v2/plugs/{name}/versions/{version}/protect | Protect Plug Version
[**protect_versions**](PlugsApi.md#protect_versions) | **POST** /registry/v2/plugs/{name}/protect | Protect Plug
[**publish**](PlugsApi.md#publish) | **POST** /registry/v2/plugs/{name}/versions/{version}/publish | Publish Draft Plug
[**rebuild**](PlugsApi.md#rebuild) | **POST** /registry/v2/plugs/{name}/versions/{version}/rebuild | Rebuild Plug
[**remove_version**](PlugsApi.md#remove_version) | **DELETE** /registry/v2/plugs/{name}/versions/{version} | Remove Plug Version
[**remove_versions**](PlugsApi.md#remove_versions) | **DELETE** /registry/v2/plugs/{name} | Remove Plug
[**update_asset**](PlugsApi.md#update_asset) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Update Plug Asset
[**update_assets**](PlugsApi.md#update_assets) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content | Update Plug Assets
[**verify**](PlugsApi.md#verify) | **POST** /registry/v2/plugs/{name}/versions/{version}/verify | Verify Health Of Plug

# **create**
> create(
> query: CreateQuery,
> files,
> headers
> ) -> PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2

Create Plug

Creates a new <em>plug</em> function by uploading its assets.      The assets for a <em>plug</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>plug</em> in the <code>copy</code> argument</li>   </ul>    The required <code>plug.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=plugs</code>).    For each <em>runtime</em> other files will be required or supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
try:
    # Create Plug
    # calls `POST /registry/v2/plugs/`
    api_response = await waylay_client.registry.plugs.create(
        # query parameters:
        query = {
            'deploy': True
            'scaleToZero': False
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'dryRun': True
            'async': True
            'draft': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = None # bytearray | The assets for a <em>plug</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>plug</em> in the <code>copy</code> argument</li>   </ul>    The required <code>plug.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=plugs</code>).    For each <em>runtime</em> other files will be required or supported.  (optional)
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/tar', 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'application/gzip', 'multipart/form-data', 'application/json', '*/*+json', 
        headers = {
            'content-type': 'application/octet-stream'
        },
    )
    print("The response of registry.plugs.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.create: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | **bytearray** | json request body | The assets for a &lt;em&gt;plug&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;plug&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;plug.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;plugs&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;plug&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;plug&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;plug.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;plugs&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [PostPlugJobSyncResponseV2](PostPlugJobSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
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
> ) -> PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2

Delete Plug Asset

Delete an asset from the plug's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
try:
    # Delete Plug Asset
    # calls `DELETE /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.plugs.delete_asset(
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
    print("The response of registry.plugs.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.delete_asset: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}
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
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [PostPlugJobSyncResponseV2](PostPlugJobSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
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

Get Plug Archive

Get the specification archive of a plug.

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
    # Get Plug Archive
    # calls `GET /registry/v2/plugs/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.plugs.get_archive(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.plugs.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.get_archive: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}/content
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

Get File From Plug Archive

Get a file from the specification archive of a plug.

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
    # Get File From Plug Archive
    # calls `GET /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.plugs.get_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.plugs.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.get_asset: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}
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
> ) -> GetPlugResponseV2

Get Latest Plug Version

Fetch the latest version of a <em>plug</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>plug version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
from waylay.services.registry.models.plug_type import PlugType
try:
    # Get Latest Plug Version
    # calls `GET /registry/v2/plugs/{name}`
    api_response = await waylay_client.registry.plugs.get_latest(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'type': 'sensor'
            'showTags': 'embed'
            'includeDraft': True
            'includeDeprecated': True
        },
    )
    print("The response of registry.plugs.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.get_latest: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['type']** (dict) <br> **query.type** (Query) | [**PlugType**](.md) | query parameter `"type"` | If set, filters on the type of plug. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetPlugResponseV2`** |  | [GetPlugResponseV2](GetPlugResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plug Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> name: str,
> version: str,
> query: GetQuery,
> headers
> ) -> GetPlugResponseV2

Get Plug Version

Get a specific version of a plug.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
try:
    # Get Plug Version
    # calls `GET /registry/v2/plugs/{name}/versions/{version}`
    api_response = await waylay_client.registry.plugs.get(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
        },
    )
    print("The response of registry.plugs.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetPlugResponseV2`** |  | [GetPlugResponseV2](GetPlugResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plug Version Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> jobs(
> name: str,
> version: str,
> query: JobsQuery,
> headers
> ) -> JobsForPlugResponseV2

List Plug Jobs

List the ongoing and completed operations on a specific plug.

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
from waylay.services.registry.models.jobs_for_plug_response_v2 import JobsForPlugResponseV2
try:
    # List Plug Jobs
    # calls `GET /registry/v2/plugs/{name}/versions/{version}/jobs`
    api_response = await waylay_client.registry.plugs.jobs(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
        },
    )
    print("The response of registry.plugs.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.jobs: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}/jobs
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
Literal[""] _(default)_  | False _(default)_ | **`JobsForPlugResponseV2`** |  | [JobsForPlugResponseV2](JobsForPlugResponseV2.md)
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
> ) -> LatestPlugsResponseV2

List Plugs

List the (latest) versions of available <em>plugs</em>.  ### List Latest Plug Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>plug</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no version filters are used, each listed <em>plug version</em> contains representations of the latest draft (`entities[]._links.draft`)  or latest published (`entities[]._links.published`) version (if existing and different).   Use the query parameter `showRelated` to include only a link (default `showRelated=link`) or a full representation (`showRelated=embed`).  ### List Latest Plug Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>plug</em> that satisfy the filters, but **without links**.  ### List All Plug Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>plugs</em> versions that satisfy the query, possibly multiple versions per named <em>plugs</em>. No HAL links are provided.  #### Filter on _status_ By default <em>plug versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>plug</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft`, `tags`, `wql` 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format_filter import ArchiveFormatFilter
from waylay.services.registry.models.latest_plugs_response_v2 import LatestPlugsResponseV2
from waylay.services.registry.models.plug_type import PlugType
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Plugs
    # calls `GET /registry/v2/plugs/`
    api_response = await waylay_client.registry.plugs.list(
        # query parameters:
        query = {
            'type': 'sensor'
            'includeDraft': True
            'includeDeprecated': True
            'deprecated': True
            'draft': True
            'showTags': 'embed'
            'createdBy': '@me'
            'updatedBy': '@me'
            'latest': True
        },
    )
    print("The response of registry.plugs.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['type']** (dict) <br> **query.type** (Query) | [**PlugType**](.md) | query parameter `"type"` | If set, filters on the type of plug. | [optional] 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** (dict) <br> **query.page** (Query) | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**query['deprecated']** (dict) <br> **query.deprecated** (Query) | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['nameVersion']** (dict) <br> **query.name_version** (Query) | [**List[str]**](str.md) | query parameter `"nameVersion"` | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['tags']** (dict) <br> **query.tags** (Query) | [**TagsFilter**](.md) | query parameter `"tags"` | Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
**query['wql']** (dict) <br> **query.wql** (Query) | **str** | query parameter `"wql"` | Query filter using the &#39;wql&#39; query language.  This is a unstable preview feature, currently supporting the following _match terms_: * &#x60;tag:&lt;name&gt;&#x60; entity has a tag that fully matches &#x60;&lt;name&gt;&#x60; (case insensitive). * &#x60;tag:&lt;name1&gt;,&lt;name2&gt;&#x60; entity has a tag that fully matches any of &#x60;&lt;name1&gt;&#x60;, &#x60;&lt;name2&gt;&#x60; (case insensitive). * &#x60;tag:inIgnoreCase(&lt;name1&gt;,&lt;name2&gt;)&#x60; is the fully specified format for the previous statements.   &#x60;inIgnoreCase&#x60; is the _default match predicate_. * &#x60;tag:in(&lt;name1&gt;,&lt;name2&gt;)&#x60; entity has a tag matches one of &#x60;&lt;name1&gt;&#x60;,&#x60;&lt;name2&gt;&#x60; (case sensitive) * &#x60;tag:equals(&lt;name&gt;)&#x60; entity has a tag matches &#x60;&lt;name&gt;&#x60; (case sensitive) * &#x60;tag:like(&lt;pattern&gt;)&#x60; entity has a tag that matches &#x60;&lt;pattern&gt;&#x60; (case insensitive),    where &#x60;&lt;pattern&gt;&#x60; can contain &#x60;*&#x60; (multiple characters) and &#x60;?&#x60; (single character) wildcards.  Each _argument_ of a _match term_ (like &#x60;&lt;name&gt;&#x60; above) can either be a * a _quoted match argument_, quoted using &#x60;\&quot;&#x60;, can contain any character except &#x60;\&quot;&#x60;: &#x60;tag:\&quot;Status:In Review\&quot;&#x60;. * a _safe match argument_ can only contain alpha-numeric characters or &#x60;_&#x60;: &#x60;tag:Status_In_Review&#x60;.  Multiple _match term_s can be combined in a boolean predicate using the &#x60;AND&#x60;, &#x60;OR&#x60; and &#x60;NOT&#x60; operators: * &#x60;tag:abc AND tag:\&quot;My Demo\&quot; AND tag:like(\&quot;prj:*\&quot;)&#x60;: entity has a tag matching &#x60;abc&#x60; **AND** a tag matching &#x60;\&quot;My Demo\&quot;&#x60; **AND**    a tag that has the &#x60;prj:&#x60; prefix * &#x60;tag:abc tag:\&quot;My Demo\&quot; tag:like(\&quot;prj:*\&quot;)&#x60;: same as the previous statement: a (space-deliminated) list of terms is     implicitly combined with &#x60;AND&#x60;. * &#x60;tag:abc OR tag:\&quot;My Demo\&quot;&#x60;: entity has a tag matching &#x60;abc&#x60; **OR** a tag matching &#x60;\&quot;My Demo\&quot;&#x60; * &#x60;NOT tag:abc&#x60;: entity **does not have** a tag matching &#x60;abc&#x60;  Round brackets can be used to combine predicates with different operators: * &#x60;(tag:abc OR tag:\&quot;My Demo\&quot;) AND tag:like(\&quot;prj:*\&quot;)&#x60;: entity has a tag &#x60;abc&#x60; or a tag &#x60;My Demo&#x60;, and a tag with prefix &#x60;prj:*&#x60;  For a _multi-valued attribute_ like &#x60;tag&#x60;, each _match term_ tests the existence of a matching tag assigned to the entity. When _multiple match predicates on the **same** tag_ need to be specified, the boolean operators &#x60;not&#x60;, &#x60;all&#x60;, &#x60;any&#x60; can be used _within_ the match term:  * &#x60;tag:all(like(\&quot;prj:*\&quot;),not(like(\&quot;*:Done\&quot;)))&#x60;: entity has a tag that starts with &#x60;prj:&#x60; and does NOT end with &#x60;:Done&#x60;. * &#x60;tag:not(Done)&#x60;: entity has a tag that does not match &#x60;Done&#x60; (this excludes entities without tags, and with a single &#x60;Done&#x60; tag!). * &#x60;NOT tag:not(in(abc,def))&#x60;: each tag of the entity is in &#x60;abc&#x60; or &#x60;def&#x60; (matches entities without tags!) * &#x60;tag:any(like(\&quot;prj:*\&quot;),not(done)))&#x60;: entity has a tag that either starts with &#x60;prj:&#x60; or does not match &#x60;done&#x60;. | [optional] 
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
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormatFilter]**](ArchiveFormatFilter.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** (dict) <br> **query.runtime** (Query) | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**query['latest']** (dict) <br> **query.latest** (Query) | **bool** | query parameter `"latest"` | When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;, except when specific versions are selected with the &#x60;nameVersion&#x60; filter. | [optional] 
**query['showRelated']** (dict) <br> **query.show_related** (Query) | [**ShowLinkOrEmbedding**](.md) | query parameter `"showRelated"` | Sets the representation of related function versions (like the _latest_ draft and/or published) in the response. Ignored (forced to &#x60;none&#x60;) when any of the _version filter_ query params are used. - &#x60;embed&#x60;: as full summary representation (in &#x60;_embedded&#x60;). - &#x60;link&#x60;: as HAL link in (in &#x60;_links&#x60;). - &#x60;none&#x60;: omitted. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`LatestPlugsResponseV2`** |  | [LatestPlugsResponseV2](LatestPlugsResponseV2.md)
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
> ) -> PlugVersionsResponseV2

List Plug Versions

List all versions of a plug, including deprecated versions or not.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format_filter import ArchiveFormatFilter
from waylay.services.registry.models.plug_versions_response_v2 import PlugVersionsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Plug Versions
    # calls `GET /registry/v2/plugs/{name}/versions`
    api_response = await waylay_client.registry.plugs.list_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'deprecated': True
            'draft': True
            'showTags': 'embed'
            'createdBy': '@me'
            'updatedBy': '@me'
        },
    )
    print("The response of registry.plugs.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.list_versions: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions
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
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['tags']** (dict) <br> **query.tags** (Query) | [**TagsFilter**](.md) | query parameter `"tags"` | Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
**query['version']** (dict) <br> **query.version** (Query) | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['runtimeVersion']** (dict) <br> **query.runtime_version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"runtimeVersion"` | Filter on the runtime version. | [optional] 
**query['createdBy']** (dict) <br> **query.created_by** (Query) | **str** | query parameter `"createdBy"` | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['updatedBy']** (dict) <br> **query.updated_by** (Query) | **str** | query parameter `"updatedBy"` | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on funtions that were created before the given timestamp or age. | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on funtions that were created after the given timestamp or age. | [optional] 
**query['updatedBefore']** (dict) <br> **query.updated_before** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedBefore"` | Filter on funtions that were updated before the given timestamp or age. | [optional] 
**query['updatedAfter']** (dict) <br> **query.updated_after** (Query) | [**TimestampSpec**](.md) | query parameter `"updatedAfter"` | Filter on funtions that were updated after the given timestamp or age. | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormatFilter]**](ArchiveFormatFilter.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** (dict) <br> **query.runtime** (Query) | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PlugVersionsResponseV2`** |  | [PlugVersionsResponseV2](PlugVersionsResponseV2.md)
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

# **patch_interface**
> patch_interface(
> name: str,
> version: str,
> query: PatchInterfaceQuery,
> headers
> ) -> GetPlugResponseV2

Patch Plug Interface

Patch the interface documentation of a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.documentation import Documentation
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
try:
    # Patch Plug Interface
    # calls `PATCH /registry/v2/plugs/{name}/versions/{version}/interface`
    api_response = await waylay_client.registry.plugs.patch_interface(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.Documentation() # Documentation |  (optional)
    )
    print("The response of registry.plugs.patch_interface:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.patch_interface: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/plugs/{name}/versions/{version}/interface
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**Documentation**](Documentation.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetPlugResponseV2`** |  | [GetPlugResponseV2](GetPlugResponseV2.md)
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

# **patch_metadata**
> patch_metadata(
> name: str,
> version: str,
> query: PatchMetadataQuery,
> headers
> ) -> GetPlugResponseV2

Patch Plug Metadata

Patch the metadata of a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
from waylay.services.registry.models.update_plug_metadata_request_v2 import UpdatePlugMetadataRequestV2
try:
    # Patch Plug Metadata
    # calls `PATCH /registry/v2/plugs/{name}/versions/{version}/metadata`
    api_response = await waylay_client.registry.plugs.patch_metadata(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdatePlugMetadataRequestV2() # UpdatePlugMetadataRequestV2 |  (optional)
    )
    print("The response of registry.plugs.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.patch_metadata: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/plugs/{name}/versions/{version}/metadata
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**UpdatePlugMetadataRequestV2**](UpdatePlugMetadataRequestV2.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetPlugResponseV2`** |  | [GetPlugResponseV2](GetPlugResponseV2.md)
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

# **protect**
> protect(
> name: str,
> version: str,
> query: ProtectQuery,
> headers
> ) -> GetPlugResponseV2

Protect Plug Version

Enable/disable protection for a <em>plug</em> version. Enabling protection requires ownership for draft versions.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
try:
    # Protect Plug Version
    # calls `POST /registry/v2/plugs/{name}/versions/{version}/protect`
    api_response = await waylay_client.registry.plugs.protect(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'chown': False
            'showTags': 'embed'
            'enable': True
        },
    )
    print("The response of registry.plugs.protect:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.protect: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/{name}/versions/{version}/protect
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['enable']** (dict) <br> **query.enable** (Query) | **bool** | query parameter `"enable"` | If set to &#x60;true&#x60;, the function assets (including its code) will be protected by requiring additional permissions. If set to &#x60;false&#x60;, the function assets will no longer be protected. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetPlugResponseV2`** |  | [GetPlugResponseV2](GetPlugResponseV2.md)
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

# **protect_versions**
> protect_versions(
> name: str,
> query: ProtectVersionsQuery,
> headers
> ) -> ProtectByNameResponseV2

Protect Plug

Enable/disable protection for all <em>plug</em> versions. Enabling protection requires ownership for draft versions.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.protect_by_name_response_v2 import ProtectByNameResponseV2
try:
    # Protect Plug
    # calls `POST /registry/v2/plugs/{name}/protect`
    api_response = await waylay_client.registry.plugs.protect_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'chown': False
            'showTags': 'embed'
            'enable': True
        },
    )
    print("The response of registry.plugs.protect_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.protect_versions: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/{name}/protect
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['enable']** (dict) <br> **query.enable** (Query) | **bool** | query parameter `"enable"` | If set to &#x60;true&#x60;, the function assets (including its code) will be protected by requiring additional permissions. If set to &#x60;false&#x60;, the function assets will no longer be protected. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ProtectByNameResponseV2`** |  | [ProtectByNameResponseV2](ProtectByNameResponseV2.md)
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

# **publish**
> publish(
> name: str,
> version: str,
> query: PublishQuery,
> headers
> ) -> PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2

Publish Draft Plug

Mark the <em>plug</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>plug</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
try:
    # Publish Draft Plug
    # calls `POST /registry/v2/plugs/{name}/versions/{version}/publish`
    api_response = await waylay_client.registry.plugs.publish(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'chown': False
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'async': True
        },
    )
    print("The response of registry.plugs.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.publish: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/{name}/versions/{version}/publish
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['deprecatePrevious']** (dict) <br> **query.deprecate_previous** (Query) | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [PostPlugJobSyncResponseV2](PostPlugJobSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Plug Published |  -  |
**202** | Plug Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> rebuild(
> name: str,
> version: str,
> query: RebuildQuery,
> headers
> ) -> RebuildPlugSyncResponseV2 \| RebuildPlugAsyncResponseV2

Rebuild Plug

Rebuild and deploy a plug with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.rebuild_plug_sync_response_v2 import RebuildPlugSyncResponseV2
from waylay.services.registry.models.rebuild_policy import RebuildPolicy
from waylay.services.registry.models.rebuild_request_v2 import RebuildRequestV2
try:
    # Rebuild Plug
    # calls `POST /registry/v2/plugs/{name}/versions/{version}/rebuild`
    api_response = await waylay_client.registry.plugs.rebuild(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'dryRun': True
            'async': True
            'showTags': 'embed'
            'upgrade': 'patch'
            'ignoreChecks': True
            'skipRebuild': True
            'skipVerify': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.RebuildRequestV2() # RebuildRequestV2 |  (optional)
    )
    print("The response of registry.plugs.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.rebuild: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/{name}/versions/{version}/rebuild
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | **RebuildRequestV2** | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['dryRun']** (dict) <br> **query.dry_run** (Query) | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, checks whether rebuild jobs are needed, but do not start any jobs. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['upgrade']** (dict) <br> **query.upgrade** (Query) | [**RebuildPolicy**](.md) | query parameter `"upgrade"` | If set, force a rebuild with the given &lt;em&gt;runtime&lt;/em&gt; version selection policy. &lt;ul&gt;  &lt;li&gt;&lt;code&gt;same&lt;/code&gt; &lt;b&gt;patch&lt;/b&gt; version.   This should only include backward compatible upgrades.  &lt;/li&gt;  &lt;li&gt;&lt;code&gt;minor&lt;/code&gt; &lt;b&gt;major&lt;/b&gt; version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .&lt;/li&gt; &lt;/ul&gt; | [optional] 
**query['forceVersion']** (dict) <br> **query.force_version** (Query) | **str** | query parameter `"forceVersion"` | If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the &#x60;upgrade&#x60; parameter. | [optional] 
**query['ignoreChecks']** (dict) <br> **query.ignore_checks** (Query) | **bool** | query parameter `"ignoreChecks"` | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
**query['skipRebuild']** (dict) <br> **query.skip_rebuild** (Query) | **bool** | query parameter `"skipRebuild"` | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 
**query['skipVerify']** (dict) <br> **query.skip_verify** (Query) | **bool** | query parameter `"skipVerify"` | If set, the function will not be validated: it transitions to &#x60;running&#x60; without verification of it&#39;s deployment health. When a &#x60;scaleToZero&#x60; is requested or implied, it is executed at the end of the deployment job, rather than as a separate job. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RebuildPlugSyncResponseV2 \| RebuildPlugAsyncResponseV2`** |  | [RebuildPlugSyncResponseV2](RebuildPlugSyncResponseV2.md) <br> [RebuildPlugAsyncResponseV2](RebuildPlugAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
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

Remove Plug Version

Deprecate, undeploy and/or remove a <em>plug</em> version.  By default, a `DELETE`  * marks _published_ version(s) _deprecated_: they remain active, but are no longer included in listings by default. * completely removes any _draft_ version(s) (_deprecate_, _undeploy_ and _remove_)  A _deprecated_ plug version will eventually be _undeployed_ (but not _removed_) by an external background task,  once proven that no waylay rule template or task references it.  Use `?force=true` to skip the deprecation and immediately remove the version(s).  Use `?undeploy=true` to undeploy the plug version(s), but keep it registered in a `undeployed` state. An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove Plug Version
    # calls `DELETE /registry/v2/plugs/{name}/versions/{version}`
    api_response = await waylay_client.registry.plugs.remove_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'async': True
            'force': True
            'undeploy': True
            'reset': True
        },
    )
    print("The response of registry.plugs.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.remove_version: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['force']** (dict) <br> **query.force** (Query) | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  Setting this parameter is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;reset&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**query['reset']** (dict) <br> **query.reset** (Query) | **bool** | query parameter `"reset"` | If &#x60;true&#x60;, the function version will be immediately undeployed and reset to &#x60;registered&#x60; state as a _draft_. This is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;undeploy&#x3D;false&#x60;. | [optional] 
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

Remove Plug

Deprecate, undeploy and/or remove all versions of this named <em>plug</em>.  By default, a `DELETE`  * marks _published_ version(s) _deprecated_: they remain active, but are no longer included in listings by default. * completely removes any _draft_ version(s) (_deprecate_, _undeploy_ and _remove_)  A _deprecated_ plug version will eventually be _undeployed_ (but not _removed_) by an external background task,  once proven that no waylay rule template or task references it.  Use `?force=true` to skip the deprecation and immediately remove the version(s).  Use `?undeploy=true` to undeploy the plug version(s), but keep it registered in a `undeployed` state. An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove Plug
    # calls `DELETE /registry/v2/plugs/{name}`
    api_response = await waylay_client.registry.plugs.remove_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'async': True
            'force': True
            'undeploy': True
            'reset': True
        },
    )
    print("The response of registry.plugs.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.remove_versions: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['force']** (dict) <br> **query.force** (Query) | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  Setting this parameter is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;reset&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**query['reset']** (dict) <br> **query.reset** (Query) | **bool** | query parameter `"reset"` | If &#x60;true&#x60;, the function version will be immediately undeployed and reset to &#x60;registered&#x60; state as a _draft_. This is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;undeploy&#x3D;false&#x60;. | [optional] 
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
> ) -> PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2

Update Plug Asset

The provided asset will be added to the <em>plug</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the plug.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

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
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
try:
    # Update Plug Asset
    # calls `PUT /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.plugs.update_asset(
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
    print("The response of registry.plugs.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.update_asset: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/versions/{version}/content/{wildcard}
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
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [PostPlugJobSyncResponseV2](PostPlugJobSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
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
> ) -> PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2

Update Plug Assets

Update a draft <em>plug</em> function by updating its assets.      The assets for a <em>plug</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>plug</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the plug.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
try:
    # Update Plug Assets
    # calls `PUT /registry/v2/plugs/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.plugs.update_assets(
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
    print("The response of registry.plugs.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.update_assets: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;plug&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;plug&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the plug.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`, `application/tar`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `application/gzip`, `multipart/form-data`

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostPlugJobSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [PostPlugJobSyncResponseV2](PostPlugJobSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
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
> ) -> VerifyPlugSyncResponseV2 \| PostPlugJobAsyncResponseV2

Verify Health Of Plug

Verify health of plug deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.verify_plug_sync_response_v2 import VerifyPlugSyncResponseV2
try:
    # Verify Health Of Plug
    # calls `POST /registry/v2/plugs/{name}/versions/{version}/verify`
    api_response = await waylay_client.registry.plugs.verify(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'showTags': 'embed'
            'async': True
        },
    )
    print("The response of registry.plugs.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plugs.verify: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/plugs/{name}/versions/{version}/verify
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`VerifyPlugSyncResponseV2 \| PostPlugJobAsyncResponseV2`** |  | [VerifyPlugSyncResponseV2](VerifyPlugSyncResponseV2.md) <br> [PostPlugJobAsyncResponseV2](PostPlugJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Plug Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

