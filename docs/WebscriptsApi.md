# waylay.services.registry.WebscriptsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](WebscriptsApi.md#create) | **POST** /registry/v2/webscripts/ | Create Version
[**delete_asset**](WebscriptsApi.md#delete_asset) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Delete Asset
[**get_archive**](WebscriptsApi.md#get_archive) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content | Get Archive
[**get_asset_by_role**](WebscriptsApi.md#get_asset_by_role) | **GET** /registry/v2/webscripts/{name}/versions/{version}/{assetRole} | Get Asset By Role
[**get_asset**](WebscriptsApi.md#get_asset) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Get Asset
[**get_latest**](WebscriptsApi.md#get_latest) | **GET** /registry/v2/webscripts/{name} | Get Latest
[**get**](WebscriptsApi.md#get) | **GET** /registry/v2/webscripts/{name}/versions/{version} | Get Version
[**jobs**](WebscriptsApi.md#jobs) | **GET** /registry/v2/webscripts/{name}/versions/{version}/jobs | List Jobs
[**list_versions**](WebscriptsApi.md#list_versions) | **GET** /registry/v2/webscripts/{name}/versions | List Versions
[**list**](WebscriptsApi.md#list) | **GET** /registry/v2/webscripts/ | List
[**patch_manifest**](WebscriptsApi.md#patch_manifest) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/manifest | Patch Manifest
[**patch_metadata**](WebscriptsApi.md#patch_metadata) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/metadata | Patch Metadata
[**protect_versions**](WebscriptsApi.md#protect_versions) | **POST** /registry/v2/webscripts/{name}/protect | Protect
[**protect**](WebscriptsApi.md#protect) | **POST** /registry/v2/webscripts/{name}/versions/{version}/protect | Protect Version
[**publish**](WebscriptsApi.md#publish) | **POST** /registry/v2/webscripts/{name}/versions/{version}/publish | Publish Draft
[**rebuild**](WebscriptsApi.md#rebuild) | **POST** /registry/v2/webscripts/{name}/versions/{version}/rebuild | Rebuild
[**remove_version**](WebscriptsApi.md#remove_version) | **DELETE** /registry/v2/webscripts/{name}/versions/{version} | Remove Version
[**remove_versions**](WebscriptsApi.md#remove_versions) | **DELETE** /registry/v2/webscripts/{name} | Remove
[**update_asset_by_role**](WebscriptsApi.md#update_asset_by_role) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/{assetRole} | Update Asset By Role
[**update_asset**](WebscriptsApi.md#update_asset) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Update Asset
[**update_assets**](WebscriptsApi.md#update_assets) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content | Update Assets
[**verify**](WebscriptsApi.md#verify) | **POST** /registry/v2/webscripts/{name}/versions/{version}/verify | Verify Health

# **create**
> create(
> query: CreateQuery,
> files,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Create Version

Creates a new <em>webscript</em> function by uploading its assets.      The assets for a <em>webscript</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>webscript</em> in the <code>copy</code> argument</li>   </ul>    The required <code>webscript.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=webscripts</code>).    For each <em>runtime</em> other files will be required or supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Create Version
    # calls `POST /registry/v2/webscripts/`
    api_response = await waylay_client.registry.webscripts.create(
        # query parameters:
        query = {
            'showTags': 'embed'
            'deploy': True
            'scaleToZero': False
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'dryRun': True
            'async': True
            'draft': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = None # object | The assets for a <em>webscript</em> function can be provided as   <ul>     <li>A single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>Separate files in a <code>multipart/form-data</code> request</li>     <li>A reference to the assets of another <em>webscript</em> in the <code>copy</code> argument</li>   </ul>    The required <code>webscript.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=webscripts</code>).    For each <em>runtime</em> other files will be required or supported.  (optional)
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/gzip', 'application/json', 'application/octet-stream', 'application/tar', 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'multipart/form-data', 
        headers = {
            'content-type': '*/*+json'
        },
    )
    print("The response of registry.webscripts.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.create: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | **object** | json request body | The assets for a &lt;em&gt;webscript&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;webscript&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;webscript.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;webscripts&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;webscript&lt;/em&gt; function can be provided as   &lt;ul&gt;     &lt;li&gt;A single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;Separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;     &lt;li&gt;A reference to the assets of another &lt;em&gt;webscript&lt;/em&gt; in the &lt;code&gt;copy&lt;/code&gt; argument&lt;/li&gt;   &lt;/ul&gt;    The required &lt;code&gt;webscript.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;webscripts&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deprecatePrevious']** (dict) <br> **query.deprecate_previous** (Query) | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions when creating a new non-draft version or publishing a draft version. | [optional] 
**query['dryRun']** (dict) <br> **query.dry_run** (Query) | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['version']** (dict) <br> **query.version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, the function version will be an increment of the latest existing version that satisfies the &#x60;version&#x60; range. Note that this increment always takes precedence over an explicit &#x60;version&#x60; in the function manifest. | [optional] 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | If set, the value will be used as the function name instead of the one specified in the manifest. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. | [optional] [default False]
**query['runtime']** (dict) <br> **query.runtime** (Query) | **str** | query parameter `"runtime"` | If set, the created function will use the indicated runtime (latest version within specified range).  This takes precedence over the runtime specified in a function manifest (copied or from request body). | [optional] 
**query['copy']** (dict) <br> **query.copy_from** (Query) | [**CreateModelsCopyParameter**](.md) | query parameter `"copy"` | Indicates the _source_ of initial assets for a _new function_.  When using this query parameter, the request body does not need to contain assets, but any assets in the request body will overwrite the copied assets.  #### Selection of _assets_ source  * If set as &#x60;&lt;sourceName&gt;[@&lt;sourceVersionRange&gt;]&#x60;, the _new function_ will be created with copied assets of the selected _source function_. * If set as &#x60;!example&#x60;, a &#x60;runtime&#x60; query parameter is required, and the _new function_ will be initialized with assets of the _runtime example_.  #### Selection of the _source function_  When &#x60;&lt;sourceVersionRange&gt;&#x60; is a range (or is not given), the latest _published_ version (in that range) is used.  If no _published_ version exists, the latest _draft_ is selected.  If no versions in the range exist, a &#x60;404&#x60; _Not Found_ error is returned.  #### The &#x60;name&#x60; of the _new function_  If a &#x60;name&#x60; is NOT specified (either as query parameter, or in an optional manifest asset in the request body), the &#x60;name&#x60; of the _new function_ will be that of the _source function_.  #### The &#x60;version&#x60; of the _new function_  When the _target_ and _source_ name are equal, the &#x60;version&#x60; query parameters is defaulted to &#x60;&lt;sourceVersionRange&gt;&#x60; (&#x60;~&lt;sourceVersionRange&gt;&#x60; when it&#39;s an exact version)  The version of the _new function_ will be: * If a &#x60;version&#x60; is NOT specified (either as query parameter, in an optional manifest asset, or as &#x60;&lt;sourceVersionRange&gt;&#x60; _default_)    * a **patch increment** (&#x60;&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;+1&#x60;) of the latest **existing version** with the target &#x60;name&#x60;    * **&#x60;1.0.0&#x60;** otherwise  * If a &#x60;version&#x60; is specified:    * the **lowest version** in that range **if no existing version** is in that range.    * an **increment** of the latest existing version, **at the highest level** (_major_,_minor_,_patch_) allowed by that range.    * otherwise, if all allowed versions already exist, a **&#x60;409&#x60; _Duplicate_ error** is raised.  #### Deployment overrides  The new function will use the deployment overrides of the copied function, unless a _manifest_ was specified in the request body. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `*/*+json`, `application/gzip`, `application/json`, `application/octet-stream`, `application/tar`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `multipart/form-data`

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: */*+json, application/gzip, application/json, application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployed |  -  |
**202** | Webscript Deployment Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(
> name: str,
> version: str,
> wildcard: str,
> query: DeleteAssetQuery,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Delete Asset

Delete an asset from the webscript's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Delete Asset
    # calls `DELETE /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.webscripts.delete_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'showTags': 'embed'
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
    )
    print("The response of registry.webscripts.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.delete_asset: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployed |  -  |
**202** | Webscript Deployment Initiated |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive**
> get_archive(
> name: str,
> version: str,
> query: GetArchiveQuery,
> headers
> ) -> bytearray

Get Archive

Get the specification archive of a webscript.

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
    # Get Archive
    # calls `GET /registry/v2/webscripts/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.webscripts.get_archive(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.webscripts.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.get_archive: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions/{version}/content
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
 - **Accept**: application/gzip, application/json, application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_role**
> get_asset_by_role(
> name: str,
> version: str,
> asset_role: GetAssetByRoleModelsAssetRoleParameter,
> query: GetAssetByRoleQuery,
> headers
> ) -> bytearray

Get Asset By Role

Get asset content or metadata from the archive of a webscript by name.

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
    # Get Asset By Role
    # calls `GET /registry/v2/webscripts/{name}/versions/{version}/{assetRole}`
    api_response = await waylay_client.registry.webscripts.get_asset_by_role(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        waylay.services.registry.GetAssetByRoleModelsAssetRoleParameter(), # asset_role | path param "assetRole"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.webscripts.get_asset_by_role:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.get_asset_by_role: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions/{version}/{assetRole}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**asset_role** | [**GetAssetByRoleModelsAssetRoleParameter**](.md) | path parameter `"assetRole"` | Role name of the asset. The mapping to a concrete asset path depends on the runtime. Only asset roles with a fixed asset path for the runtime are supported. | 
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
 - **Accept**: application/gzip, application/json, application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar

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

Get Asset

Get asset content or metadata from the archive of a webscript by name.

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
    # Get Asset
    # calls `GET /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.webscripts.get_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.webscripts.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.get_asset: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}
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
 - **Accept**: application/gzip, application/json, application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar

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
> ) -> GetWebscriptResponseV2

Get Latest

Fetch the latest version of a <em>webscript</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>webscript version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2
try:
    # Get Latest
    # calls `GET /registry/v2/webscripts/{name}`
    api_response = await waylay_client.registry.webscripts.get_latest(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'includeDraft': True
            'includeDeprecated': True
            'includeUndeployed': True
            'showTags': 'embed'
        },
    )
    print("The response of registry.webscripts.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.get_latest: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions can be selected as latest version. If set to &#x60;false&#x60;, draft versions are **excluded**. (similar to a &#x60;draft&#x3D;false&#x60; filter) | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions can be selected as latest version. If set to &#x60;false&#x60;, deprecated versions are **excluded**. (similar to a &#x60;deprecated&#x3D;false&#x60; filter) | [optional] 
**query['includeUndeployed']** (dict) <br> **query.include_undeployed** (Query) | **bool** | query parameter `"includeUndeployed"` | Configures the inclusion of _undeployed_ versions when selecting latest versions per name. By default, undeployed versions are only considered when no other versions are available. If set to &#x60;true&#x60;, undeployed versions can be selected as latest version. If set to &#x60;false&#x60;, undeployed versions are **excluded** (similar to a &#x60;status&#x3D;-undeployed&#x60; filter) | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetWebscriptResponseV2`** |  | [GetWebscriptResponseV2](GetWebscriptResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> name: str,
> version: str,
> query: GetQuery,
> headers
> ) -> GetWebscriptResponseV2

Get Version

Get the webscript version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2
try:
    # Get Version
    # calls `GET /registry/v2/webscripts/{name}/versions/{version}`
    api_response = await waylay_client.registry.webscripts.get(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
        },
    )
    print("The response of registry.webscripts.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions/{version}
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
Literal[""] _(default)_  | False _(default)_ | **`GetWebscriptResponseV2`** |  | [GetWebscriptResponseV2](GetWebscriptResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> jobs(
> name: str,
> version: str,
> query: JobsQuery,
> headers
> ) -> JobsForWebscriptResponseV2

List Jobs

List the ongoing and completed operations on a specific webscript.

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
from waylay.services.registry.models.jobs_for_webscript_response_v2 import JobsForWebscriptResponseV2
try:
    # List Jobs
    # calls `GET /registry/v2/webscripts/{name}/versions/{version}/jobs`
    api_response = await waylay_client.registry.webscripts.jobs(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
        },
    )
    print("The response of registry.webscripts.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.jobs: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions/{version}/jobs
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
Literal[""] _(default)_  | False _(default)_ | **`JobsForWebscriptResponseV2`** |  | [JobsForWebscriptResponseV2](JobsForWebscriptResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Jobs Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> list_versions(
> name: str,
> query: ListVersionsQuery,
> headers
> ) -> WebscriptVersionsResponseV2

List Versions

List all deployed versions of a webscript.

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
from waylay.services.registry.models.status_filter import StatusFilter
from waylay.services.registry.models.webscript_versions_response_v2 import WebscriptVersionsResponseV2
try:
    # List Versions
    # calls `GET /registry/v2/webscripts/{name}/versions`
    api_response = await waylay_client.registry.webscripts.list_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'deprecated': True
            'draft': True
            'showTags': 'embed'
            'includeDraft': True
            'includeDeprecated': True
            'includeUndeployed': True
            'createdBy': '@me'
            'updatedBy': '@me'
        },
    )
    print("The response of registry.webscripts.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.list_versions: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/{name}/versions
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
**query['status']** (dict) <br> **query.status** (Query) | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['tags']** (dict) <br> **query.tags** (Query) | [**TagsFilter**](.md) | query parameter `"tags"` | Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions can be selected as latest version. If set to &#x60;false&#x60;, draft versions are **excluded**. (similar to a &#x60;draft&#x3D;false&#x60; filter) | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions can be selected as latest version. If set to &#x60;false&#x60;, deprecated versions are **excluded**. (similar to a &#x60;deprecated&#x3D;false&#x60; filter) | [optional] 
**query['includeUndeployed']** (dict) <br> **query.include_undeployed** (Query) | **bool** | query parameter `"includeUndeployed"` | Configures the inclusion of _undeployed_ versions when selecting latest versions per name. By default, undeployed versions are only considered when no other versions are available. If set to &#x60;true&#x60;, undeployed versions can be selected as latest version. If set to &#x60;false&#x60;, undeployed versions are **excluded** (similar to a &#x60;status&#x3D;-undeployed&#x60; filter) | [optional] 
**query['version']** (dict) <br> **query.version** (Query) | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`WebscriptVersionsResponseV2`** |  | [WebscriptVersionsResponseV2](WebscriptVersionsResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Versions Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> LatestWebscriptsResponseV2

List

List the (latest) versions of available <em>webscripts</em>.  ### List Latest Webscript Versions By default, the result includes the latest non-deprecated, non-draft version for each name, among the webscript versions that satisfy the query filters. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   ### Related Webscript Versions Each listed _latest_ <em>webscript version</em> contains HAL references to the latest _draft_  or _published_ version of the same name,  if they exist and are different from the selected _latest_ version. These linked versions might not satisfy other query filters.  Use the query parameter `showRelated` to change the representation of linked versions:  * `showRelated=link`: (default) include links (`entities[]._links.draft`,`entities[]._links.published`) * `showRelated=embed`: include  a full representation (`entities[]._embedded.draft`,`entities[]._embedded.published`) * `showRelated=none`: do not include related versions.  ### List All Webscript Versions When using `latest=false` the listing contains _all_  <em>webscripts</em> versions that satisfy the query, possibly multiple versions per named <em>webscripts</em>. No HAL links are provided.  #### Filter on _status_ By default <em>webscript versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list (a page of) _ALL_ versions known to the function registry. 

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
from waylay.services.registry.models.latest_webscripts_response_v2 import LatestWebscriptsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List
    # calls `GET /registry/v2/webscripts/`
    api_response = await waylay_client.registry.webscripts.list(
        # query parameters:
        query = {
            'includeDraft': True
            'includeDeprecated': True
            'includeUndeployed': True
            'deprecated': True
            'draft': True
            'showTags': 'embed'
            'createdBy': '@me'
            'updatedBy': '@me'
            'latest': True
        },
    )
    print("The response of registry.webscripts.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/webscripts/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** (dict) <br> **query.page** (Query) | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['showRelated']** (dict) <br> **query.show_related** (Query) | [**ShowLinkOrEmbedding**](.md) | query parameter `"showRelated"` | Sets the representation of related function versions (like the _latest_ draft and/or published) in the response. Ignored (forced to &#x60;none&#x60;) when any of the _version filter_ query params are used. - &#x60;embed&#x60;: as full summary representation (in &#x60;_embedded&#x60;). - &#x60;link&#x60;: as HAL link in (in &#x60;_links&#x60;). - &#x60;none&#x60;: omitted.  Defaults to &#x60;link&#x60; unless &#x60;latest&#x3D;false&#x60;, in which case related versions are omitted. | [optional] 
**query['includeDraft']** (dict) <br> **query.include_draft** (Query) | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions can be selected as latest version. If set to &#x60;false&#x60;, draft versions are **excluded**. (similar to a &#x60;draft&#x3D;false&#x60; filter) | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions can be selected as latest version. If set to &#x60;false&#x60;, deprecated versions are **excluded**. (similar to a &#x60;deprecated&#x3D;false&#x60; filter) | [optional] 
**query['includeUndeployed']** (dict) <br> **query.include_undeployed** (Query) | **bool** | query parameter `"includeUndeployed"` | Configures the inclusion of _undeployed_ versions when selecting latest versions per name. By default, undeployed versions are only considered when no other versions are available. If set to &#x60;true&#x60;, undeployed versions can be selected as latest version. If set to &#x60;false&#x60;, undeployed versions are **excluded** (similar to a &#x60;status&#x3D;-undeployed&#x60; filter) | [optional] 
**query['deprecated']** (dict) <br> **query.deprecated** (Query) | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** (dict) <br> **query.draft** (Query) | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['nameVersion']** (dict) <br> **query.name_version** (Query) | [**List[str]**](str.md) | query parameter `"nameVersion"` | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['tags']** (dict) <br> **query.tags** (Query) | [**TagsFilter**](.md) | query parameter `"tags"` | Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
**query['wql']** (dict) <br> **query.wql** (Query) | **str** | query parameter `"wql"` | Query filter using the &#39;wql&#39; query language.  This is a unstable preview feature, currently supporting the following _match terms_: * &#x60;tag:&lt;name&gt;&#x60; entity has a tag that fully matches &#x60;&lt;name&gt;&#x60; (case insensitive). * &#x60;tag:&lt;name1&gt;,&lt;name2&gt;&#x60; entity has a tag that fully matches any of &#x60;&lt;name1&gt;&#x60;, &#x60;&lt;name2&gt;&#x60; (case insensitive). * &#x60;tag:inIgnoreCase(&lt;name1&gt;,&lt;name2&gt;)&#x60; is the fully specified format for the previous statements.   &#x60;inIgnoreCase&#x60; is the _default match predicate_. * &#x60;tag:in(&lt;name1&gt;,&lt;name2&gt;)&#x60; entity has a tag matches one of &#x60;&lt;name1&gt;&#x60;,&#x60;&lt;name2&gt;&#x60; (case sensitive) * &#x60;tag:equals(&lt;name&gt;)&#x60; entity has a tag matches &#x60;&lt;name&gt;&#x60; (case sensitive) * &#x60;tag:like(&lt;pattern&gt;)&#x60; entity has a tag that matches &#x60;&lt;pattern&gt;&#x60; (case insensitive),    where &#x60;&lt;pattern&gt;&#x60; can contain &#x60;*&#x60; (multiple characters) and &#x60;?&#x60; (single character) wildcards.  Each _argument_ of a _match term_ (like &#x60;&lt;name&gt;&#x60; above) can either be a * a _quoted match argument_, quoted using &#x60;\&quot;&#x60;, can contain any character except &#x60;\&quot;&#x60;: &#x60;tag:\&quot;Status:In Review\&quot;&#x60;. * a _safe match argument_ can only contain alpha-numeric characters or &#x60;_&#x60;: &#x60;tag:Status_In_Review&#x60;.  Multiple _match term_s can be combined in a boolean predicate using the &#x60;AND&#x60;, &#x60;OR&#x60; and &#x60;NOT&#x60; operators: * &#x60;tag:abc AND tag:\&quot;My Demo\&quot; AND tag:like(\&quot;prj:*\&quot;)&#x60;: entity has a tag matching &#x60;abc&#x60; **AND** a tag matching &#x60;\&quot;My Demo\&quot;&#x60; **AND**    a tag that has the &#x60;prj:&#x60; prefix * &#x60;tag:abc tag:\&quot;My Demo\&quot; tag:like(\&quot;prj:*\&quot;)&#x60;: same as the previous statement: a (space-deliminated) list of terms is     implicitly combined with &#x60;AND&#x60;. * &#x60;tag:abc OR tag:\&quot;My Demo\&quot;&#x60;: entity has a tag matching &#x60;abc&#x60; **OR** a tag matching &#x60;\&quot;My Demo\&quot;&#x60; * &#x60;NOT tag:abc&#x60;: entity **does not have** a tag matching &#x60;abc&#x60;  Round brackets can be used to combine predicates with different operators: * &#x60;(tag:abc OR tag:\&quot;My Demo\&quot;) AND tag:like(\&quot;prj:*\&quot;)&#x60;: entity has a tag &#x60;abc&#x60; or a tag &#x60;My Demo&#x60;, and a tag with prefix &#x60;prj:*&#x60;  For a _multi-valued attribute_ like &#x60;tag&#x60;, each _match term_ tests the existence of a matching tag assigned to the entity. When _multiple match predicates on the **same** tag_ need to be specified, the boolean operators &#x60;not&#x60;, &#x60;all&#x60;, &#x60;any&#x60; can be used _within_ the match term:  * &#x60;tag:all(like(\&quot;prj:*\&quot;),not(like(\&quot;*:Done\&quot;)))&#x60;: entity has a tag that starts with &#x60;prj:&#x60; and does NOT end with &#x60;:Done&#x60;. * &#x60;tag:not(Done)&#x60;: entity has a tag that does not match &#x60;Done&#x60; (this excludes entities without tags, and with a single &#x60;Done&#x60; tag!). * &#x60;NOT tag:not(in(abc,def))&#x60;: each tag of the entity is in &#x60;abc&#x60; or &#x60;def&#x60; (matches entities without tags!) * &#x60;tag:any(like(\&quot;prj:*\&quot;),not(done)))&#x60;: entity has a tag that either starts with &#x60;prj:&#x60; or does not match &#x60;done&#x60;. | [optional] 
**query['version']** (dict) <br> **query.version** (Query) | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
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
**query['latest']** (dict) <br> **query.latest** (Query) | **bool** | query parameter `"latest"` | When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`LatestWebscriptsResponseV2`** |  | [LatestWebscriptsResponseV2](LatestWebscriptsResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscripts Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_manifest**
> patch_manifest(
> name: str,
> version: str,
> query: PatchManifestQuery,
> headers
> ) -> PostWebscriptJobAsyncResponseV2 \| PostWebscriptJobSyncResponseV2

Patch Manifest

The provided json content will be merged with the existing as <code>webscript.json</code> manifest asset.   Please note that it is not allowed to change the any of the <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_webscript_job_async_response_v2 import PostWebscriptJobAsyncResponseV2
from waylay.services.registry.models.webscript_manifest_patch import WebscriptManifestPatch
try:
    # Patch Manifest
    # calls `PATCH /registry/v2/webscripts/{name}/versions/{version}/manifest`
    api_response = await waylay_client.registry.webscripts.patch_manifest(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.WebscriptManifestPatch() # WebscriptManifestPatch |  (optional)
    )
    print("The response of registry.webscripts.patch_manifest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.patch_manifest: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/webscripts/{name}/versions/{version}/manifest
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**WebscriptManifestPatch**](WebscriptManifestPatch.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobAsyncResponseV2 \| PostWebscriptJobSyncResponseV2`** |  | [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md) <br> [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployment Initiated |  -  |
**202** | Webscript Deployed |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metadata**
> patch_metadata(
> name: str,
> version: str,
> query: PatchMetadataQuery,
> headers
> ) -> GetWebscriptResponseV2

Patch Metadata

Patch the metadata of a webscript version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2
from waylay.services.registry.models.update_metadata_request_v2 import UpdateMetadataRequestV2
try:
    # Patch Metadata
    # calls `PATCH /registry/v2/webscripts/{name}/versions/{version}/metadata`
    api_response = await waylay_client.registry.webscripts.patch_metadata(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdateMetadataRequestV2() # UpdateMetadataRequestV2 |  (optional)
    )
    print("The response of registry.webscripts.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.patch_metadata: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/webscripts/{name}/versions/{version}/metadata
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**UpdateMetadataRequestV2**](UpdateMetadataRequestV2.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetWebscriptResponseV2`** |  | [GetWebscriptResponseV2](GetWebscriptResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_versions**
> protect_versions(
> name: str,
> query: ProtectVersionsQuery,
> headers
> ) -> ProtectByNameResponseV2

Protect

Enable/disable protection for all <em>webscript</em> versions. Enabling protection requires ownership for draft versions.

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
    # Protect
    # calls `POST /registry/v2/webscripts/{name}/protect`
    api_response = await waylay_client.registry.webscripts.protect_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'chown': False
            'showTags': 'embed'
            'enable': True
        },
    )
    print("The response of registry.webscripts.protect_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.protect_versions: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/{name}/protect
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
**200** | Protection changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect**
> protect(
> name: str,
> version: str,
> query: ProtectQuery,
> headers
> ) -> GetWebscriptResponseV2

Protect Version

Enable/disable protection for a <em>webscript</em> version. Enabling protection requires ownership for draft versions.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2
try:
    # Protect Version
    # calls `POST /registry/v2/webscripts/{name}/versions/{version}/protect`
    api_response = await waylay_client.registry.webscripts.protect(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'chown': False
            'showTags': 'embed'
            'enable': True
        },
    )
    print("The response of registry.webscripts.protect:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.protect: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/{name}/versions/{version}/protect
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
Literal[""] _(default)_  | False _(default)_ | **`GetWebscriptResponseV2`** |  | [GetWebscriptResponseV2](GetWebscriptResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> publish(
> name: str,
> version: str,
> query: PublishQuery,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Publish Draft

Mark the <em>webscript</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>webscript</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Publish Draft
    # calls `POST /registry/v2/webscripts/{name}/versions/{version}/publish`
    api_response = await waylay_client.registry.webscripts.publish(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
            'chown': False
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'async': True
        },
    )
    print("The response of registry.webscripts.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.publish: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/{name}/versions/{version}/publish
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['deprecatePrevious']** (dict) <br> **query.deprecate_previous** (Query) | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions when creating a new non-draft version or publishing a draft version. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Published |  -  |
**202** | Webscript Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> rebuild(
> name: str,
> version: str,
> query: RebuildQuery,
> headers
> ) -> RebuildWebscriptSyncResponseV2 \| RebuildWebscriptAsyncResponseV2

Rebuild

Rebuild and deploy a webscript with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.rebuild_policy import RebuildPolicy
from waylay.services.registry.models.rebuild_request_v2 import RebuildRequestV2
from waylay.services.registry.models.rebuild_webscript_sync_response_v2 import RebuildWebscriptSyncResponseV2
try:
    # Rebuild
    # calls `POST /registry/v2/webscripts/{name}/versions/{version}/rebuild`
    api_response = await waylay_client.registry.webscripts.rebuild(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'dryRun': True
            'async': True
            'showTags': 'embed'
            'upgrade': 'patch'
            'forceDeploy': True
            'ignoreChecks': True
            'skipRebuild': True
            'skipVerify': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.RebuildRequestV2() # RebuildRequestV2 |  (optional)
    )
    print("The response of registry.webscripts.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.rebuild: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/{name}/versions/{version}/rebuild
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
**query['forceDeploy']** (dict) <br> **query.force_deploy** (Query) | **bool** | query parameter `"forceDeploy"` | By default, a redeploy is skipped if there are no build/deploy argument changes. If this flag is set, a redeployment is forced in that case (with the unchanged build and deploy arguments). | [optional] 
**query['ignoreChecks']** (dict) <br> **query.ignore_checks** (Query) | **bool** | query parameter `"ignoreChecks"` | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
**query['skipRebuild']** (dict) <br> **query.skip_rebuild** (Query) | **bool** | query parameter `"skipRebuild"` | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 
**query['skipVerify']** (dict) <br> **query.skip_verify** (Query) | **bool** | query parameter `"skipVerify"` | If set, the function will not be validated: it transitions to &#x60;running&#x60; without verification of it&#39;s deployment health. When a &#x60;scaleToZero&#x60; is requested or implied, it is executed at the end of the deployment job, rather than as a separate job. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RebuildWebscriptSyncResponseV2 \| RebuildWebscriptAsyncResponseV2`** |  | [RebuildWebscriptSyncResponseV2](RebuildWebscriptSyncResponseV2.md) <br> [RebuildWebscriptAsyncResponseV2](RebuildWebscriptAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Rebuild Ignored |  -  |
**202** | Webscript Rebuild Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_version**
> remove_version(
> name: str,
> version: str,
> query: RemoveVersionQuery,
> headers
> ) -> UndeployedResponseV2 \| UndeploySubmittedResponseV2

Remove Version

Deprecate, undeploy and/or remove a <em>webscript</em> version.    By default, a `DELETE`    * _deprecates_ the webscript version(s): they are no longer included in listings by default.   * _undeploys_ the webscript version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the webscript version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove Version
    # calls `DELETE /registry/v2/webscripts/{name}/versions/{version}`
    api_response = await waylay_client.registry.webscripts.remove_version(
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
    print("The response of registry.webscripts.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.remove_version: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/webscripts/{name}/versions/{version}
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
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  Setting this parameter is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;reset&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
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
**200** | Undeployed |  -  |
**202** | Undeployment Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_versions**
> remove_versions(
> name: str,
> query: RemoveVersionsQuery,
> headers
> ) -> UndeployedResponseV2 \| UndeploySubmittedResponseV2

Remove

Deprecate, undeploy and/or remove all versions of this named <em>webscript</em>.    By default, a `DELETE`    * _deprecates_ the webscript version(s): they are no longer included in listings by default.   * _undeploys_ the webscript version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the webscript version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove
    # calls `DELETE /registry/v2/webscripts/{name}`
    api_response = await waylay_client.registry.webscripts.remove_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'async': True
            'force': True
            'undeploy': True
            'reset': True
        },
    )
    print("The response of registry.webscripts.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.remove_versions: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/webscripts/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['force']** (dict) <br> **query.force** (Query) | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**query['undeploy']** (dict) <br> **query.undeploy** (Query) | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  Setting this parameter is incompatible with &#x60;force&#x3D;true&#x60; or &#x60;reset&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
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
**200** | Undeployed |  -  |
**202** | Undeployment Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_by_role**
> update_asset_by_role(
> name: str,
> version: str,
> asset_role: GetAssetByRoleModelsAssetRoleParameter,
> query: UpdateAssetByRoleQuery,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Update Asset By Role

The provided asset will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing asset with the same _role_.    Please note that it is not allowed to update the    <em>manifest</em>    json file with a changed value for any of the  <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.   For each <em>runtime</em> other files are supported.   

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
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Update Asset By Role
    # calls `PUT /registry/v2/webscripts/{name}/versions/{version}/{assetRole}`
    api_response = await waylay_client.registry.webscripts.update_asset_by_role(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        waylay.services.registry.GetAssetByRoleModelsAssetRoleParameter(), # asset_role | path param "assetRole"
        # query parameters:
        query = {
            'showTags': 'embed'
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
    print("The response of registry.webscripts.update_asset_by_role:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.update_asset_by_role: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/webscripts/{name}/versions/{version}/{assetRole}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**asset_role** | [**GetAssetByRoleModelsAssetRoleParameter**](.md) | path parameter `"assetRole"` | Role name of the asset. The mapping to a concrete asset path depends on the runtime. Only asset roles with a fixed asset path for the runtime are supported. | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | A single asset file. | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployed |  -  |
**202** | Webscript Deployment Initiated |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> update_asset(
> name: str,
> version: str,
> wildcard: str,
> query: UpdateAssetQuery,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Update Asset

The provided asset will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing asset with the same _name_.    Please note that it is not allowed to update the    <code>webscript.json</code>    json file with a changed value for any of the  <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.   For each <em>runtime</em> other files are supported.   

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
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Update Asset
    # calls `PUT /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.webscripts.update_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'showTags': 'embed'
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
    print("The response of registry.webscripts.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.update_asset: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | A single asset file. | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
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
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployed |  -  |
**202** | Webscript Deployment Initiated |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assets**
> update_assets(
> name: str,
> version: str,
> query: UpdateAssetsQuery,
> files,
> headers
> ) -> PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Update Assets

Update a draft <em>webscript</em> function by updating its assets.      The assets for a <em>webscript</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the webscript.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
try:
    # Update Assets
    # calls `PUT /registry/v2/webscripts/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.webscripts.update_assets(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'showTags': 'embed'
            'scaleToZero': False
            'deploy': True
            'chown': False
            'async': True
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/octet-stream', 'application/tar', 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'multipart/form-data', 
        headers = {
            'content-type': 'application/gzip'
        },
    )
    print("The response of registry.webscripts.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.update_assets: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/webscripts/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;webscript&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;webscript&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the webscript.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['showTags']** (dict) <br> **query.show_tags** (Query) | [**ShowInlineOrEmbedding**](.md) | query parameter `"showTags"` | Instructs how tag (objects) should be rendered in responses. The tags are show at the &#x60;tags&#x60; property of the manifest (legacy: the &#x60;metadata.tags&#x60; property) - &#x60;inline&#x60;: Show full tag objects in the manifest. - &#x60;embed&#x60;: Show tag references in the manifest.          Referenced full tag objects are included in a separate &#x60;_embedded&#x60; HAL section. - &#x60;none&#x60;: Show tag references in the manifest. Do not render tag objects.  The default behaviour depends on deployment settings. | [optional] 
**query['scaleToZero']** (dict) <br> **query.scale_to_zero** (Query) | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['deploy']** (dict) <br> **query.deploy** (Query) | **bool** | query parameter `"deploy"` | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default True]
**query['chown']** (dict) <br> **query.chown** (Query) | **bool** | query parameter `"chown"` | If set, ownership of a draft function is transferred to the current user. | [optional] [default False]
**query['comment']** (dict) <br> **query.comment** (Query) | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['author']** (dict) <br> **query.author** (Query) | **str** | query parameter `"author"` | Optionally changes the author metadata when updating a function. | [optional] 
**query['async']** (dict) <br> **query.var_async** (Query) | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/gzip`, `application/octet-stream`, `application/tar`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `multipart/form-data`

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`PostWebscriptJobSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [PostWebscriptJobSyncResponseV2](PostWebscriptJobSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/gzip, application/octet-stream, application/tar, application/tar+gzip, application/x-gzip, application/x-tar, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Deployed |  -  |
**202** | Webscript Deployment Initiated |  -  |
**403** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> verify(
> name: str,
> version: str,
> query: VerifyQuery,
> headers
> ) -> VerifyWebscriptSyncResponseV2 \| PostWebscriptJobAsyncResponseV2

Verify Health

Verify health of webscript deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.verify_webscript_sync_response_v2 import VerifyWebscriptSyncResponseV2
try:
    # Verify Health
    # calls `POST /registry/v2/webscripts/{name}/versions/{version}/verify`
    api_response = await waylay_client.registry.webscripts.verify(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'scaleToZero': True
            'showTags': 'embed'
            'async': True
        },
    )
    print("The response of registry.webscripts.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscripts.verify: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/webscripts/{name}/versions/{version}/verify
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
Literal[""] _(default)_  | False _(default)_ | **`VerifyWebscriptSyncResponseV2 \| PostWebscriptJobAsyncResponseV2`** |  | [VerifyWebscriptSyncResponseV2](VerifyWebscriptSyncResponseV2.md) <br> [PostWebscriptJobAsyncResponseV2](PostWebscriptJobAsyncResponseV2.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webscript Health Verified |  -  |
**202** | Webscript Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

