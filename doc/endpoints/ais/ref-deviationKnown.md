# deviationKnown

- [1. [Required] Property deviationKnown > relationships](#relationships)
  - [1.1. deviationKnown > relationships > relationships items](#autogenerated_heading_2)
- [2. [Required] Property deviationKnown > indicator](#indicator)

**Title:** deviationKnown

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** The VSOC also receives information from the AIS. For this, the function ais_deviation_known() to get information from the AIS for an known deviation. The request is a POST request from the AIS to the VSOC.

<details>
<summary>
<strong> <a name="relationships"></a>1. [Required] Property deviationKnown > relationships</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [relationships items](#relationships_items) | -           |

### <a name="autogenerated_heading_2"></a>1.1. deviationKnown > relationships > relationships items

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="indicator"></a>2. [Required] Property deviationKnown > indicator</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-08-03 at 16:07:26 +0200