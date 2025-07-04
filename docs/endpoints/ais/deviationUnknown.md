# deviationUnknown

- [1. [Required] Property deviationUnknown > type](#type)
- [2. [Required] Property deviationUnknown > spec_version](#spec_version)
- [3. [Required] Property deviationUnknown > id](#id)
- [4. [Required] Property deviationUnknown > created](#created)
- [5. [Required] Property deviationUnknown > modified](#modified)
- [6. [Required] Property deviationUnknown > name](#name)
- [7. [Required] Property deviationUnknown > description](#description)
- [8. [Required] Property deviationUnknown > indicator_types](#indicator_types)
  - [8.1. deviationUnknown > indicator_types > indicator_types items](#autogenerated_heading_2)
- [9. [Required] Property deviationUnknown > pattern](#pattern)
- [10. [Required] Property deviationUnknown > pattern_type](#pattern_type)
- [11. [Required] Property deviationUnknown > pattern_version](#pattern_version)
- [12. [Required] Property deviationUnknown > valid_from](#valid_from)
- [13. [Required] Property deviationUnknown > valid_until](#valid_until)
- [14. [Required] Property deviationUnknown > labels](#labels)
  - [14.1. deviationUnknown > labels > labels items](#autogenerated_heading_3)
- [15. [Required] Property deviationUnknown > extensions](#extensions)
  - [15.1. [Optional]Pattern Property deviationUnknown > extensions > ^extension-definition--.*$](#extensions_pattern1)
    - [15.1.1. [Required] Property deviationUnknown > extensions > ^extension-definition--.*$ > extension_type](#extensions_pattern1_extension_type)
- [16. [Required] Property deviationUnknown > source_vehicle](#source_vehicle)
- [17. [Required] Property deviationUnknown > source_ais](#source_ais)
- [18. [Required] Property deviationUnknown > source_rsu](#source_rsu)
- [19. [Required] Property deviationUnknown > src_ref](#src_ref)
- [20. [Required] Property deviationUnknown > dst_ref](#dst_ref)
- [21. [Required] Property deviationUnknown > src_port](#src_port)
- [22. [Required] Property deviationUnknown > dst_port](#dst_port)
- [23. [Required] Property deviationUnknown > protocol_type](#protocol_type)
- [24. [Required] Property deviationUnknown > service](#service)
- [25. [Required] Property deviationUnknown > flag](#flag)
- [26. [Required] Property deviationUnknown > timestamp](#timestamp)

**Title:** deviationUnknown

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** The VSOC also receives information from the AIS. For this, the function ais_deviation_unknown() to get information from the AIS for an unknown deviation. The request is a POST request from the AIS to the VSOC.

<details>
<summary>
<strong> <a name="type"></a>1. [Required] Property deviationUnknown > type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** property extension from the request (coming from the STIX format)

Specific value: `"indicator"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="spec_version"></a>2. [Required] Property deviationUnknown > spec_version</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** version of the stix format

</blockquote>
</details>

<details>
<summary>
<strong> <a name="id"></a>3. [Required] Property deviationUnknown > id</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^indicator--.*$``` [Test](https://regex101.com/?regex=%5Eindicator--.%2A%24) |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="created"></a>4. [Required] Property deviationUnknown > created</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the creation in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="modified"></a>5. [Required] Property deviationUnknown > modified</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the modification in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="name"></a>6. [Required] Property deviationUnknown > name</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"Anomaly detection"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="description"></a>7. [Required] Property deviationUnknown > description</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"An immunological algorithm detected a deviation in real-time dataset."`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="indicator_types"></a>8. [Required] Property deviationUnknown > indicator_types</strong>  

</summary>
<blockquote>

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                 | Description |
| ----------------------------------------------- | ----------- |
| [indicator_types items](#indicator_types_items) | -           |

### <a name="autogenerated_heading_2"></a>8.1. deviationUnknown > indicator_types > indicator_types items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="pattern"></a>9. [Required] Property deviationUnknown > pattern</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A specific pattern relevant to the reported case

</blockquote>
</details>

<details>
<summary>
<strong> <a name="pattern_type"></a>10. [Required] Property deviationUnknown > pattern_type</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"stix"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="pattern_version"></a>11. [Required] Property deviationUnknown > pattern_version</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"2.1"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="valid_from"></a>12. [Required] Property deviationUnknown > valid_from</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the start of the validity period in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="valid_until"></a>13. [Required] Property deviationUnknown > valid_until</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the end of the validity period in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="labels"></a>14. [Required] Property deviationUnknown > labels</strong>  

</summary>
<blockquote>

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | Yes               |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [labels items](#labels_items)   | -           |

### <a name="autogenerated_heading_3"></a>14.1. deviationUnknown > labels > labels items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="extensions"></a>15. [Required] Property deviationUnknown > extensions</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<details>
<summary>
<strong> <a name="extensions_pattern1"></a>15.1. [Optional]Pattern Property deviationUnknown > extensions > ^extension-definition--.*$</strong>  
> All properties whose name matches the regular expression
```^extension-definition--.*$``` ([Test](https://regex101.com/?regex=%5Eextension-definition--.%2A%24))
must respect the following conditions

</summary>
<blockquote>

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

<details>
<summary>
<strong> <a name="extensions_pattern1_extension_type"></a>15.1.1. [Required] Property deviationUnknown > extensions > ^extension-definition--.*$ > extension_type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="source_vehicle"></a>16. [Required] Property deviationUnknown > source_vehicle</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** VIN of the source vehicle

</blockquote>
</details>

<details>
<summary>
<strong> <a name="source_ais"></a>17. [Required] Property deviationUnknown > source_ais</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the source AIS

</blockquote>
</details>

<details>
<summary>
<strong> <a name="source_rsu"></a>18. [Required] Property deviationUnknown > source_rsu</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the source RSU

</blockquote>
</details>

<details>
<summary>
<strong> <a name="src_ref"></a>19. [Required] Property deviationUnknown > src_ref</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** IP address of the source

</blockquote>
</details>

<details>
<summary>
<strong> <a name="dst_ref"></a>20. [Required] Property deviationUnknown > dst_ref</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** IP address of the destination

</blockquote>
</details>

<details>
<summary>
<strong> <a name="src_port"></a>21. [Required] Property deviationUnknown > src_port</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Port of the source

</blockquote>
</details>

<details>
<summary>
<strong> <a name="dst_port"></a>22. [Required] Property deviationUnknown > dst_port</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Port of the destination

</blockquote>
</details>

<details>
<summary>
<strong> <a name="protocol_type"></a>23. [Required] Property deviationUnknown > protocol_type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="service"></a>24. [Required] Property deviationUnknown > service</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="flag"></a>25. [Required] Property deviationUnknown > flag</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="timestamp"></a>26. [Required] Property deviationUnknown > timestamp</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the from the AIS endpoint ISO-8601 (UTC)

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-05-28 at 13:53:54 +0200