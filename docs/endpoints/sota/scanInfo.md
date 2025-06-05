# scanInfo

- [1. [Required] Property scanInfo > toolId](#toolId)
- [2. [Required] Property scanInfo > timeStamp](#timeStamp)
- [3. [Required] Property scanInfo > VIN](#VIN)
- [4. [Required] Property scanInfo > action](#action)
- [5. [Required] Property scanInfo > status](#status)

**Title:** scanInfo

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** scanInfo endpoint for the SOTA Binary Tool scanning result

<details>
<summary>
<strong> <a name="toolId"></a>1. [Required] Property scanInfo > toolId</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** The tool ID of SOTA

</blockquote>
</details>

<details>
<summary>
<strong> <a name="timeStamp"></a>2. [Required] Property scanInfo > timeStamp</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** Timestamp of the scan information

</blockquote>
</details>

<details>
<summary>
<strong> <a name="VIN"></a>3. [Required] Property scanInfo > VIN</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Vehicle Identification Number

</blockquote>
</details>

<details>
<summary>
<strong> <a name="action"></a>4. [Required] Property scanInfo > action</strong>  

</summary>
<blockquote>

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | Yes                 |

**Description:** Action performed. It only accepts value 1 for update.

Must be one of:
* 1

</blockquote>
</details>

<details>
<summary>
<strong> <a name="status"></a>5. [Required] Property scanInfo > status</strong>  

</summary>
<blockquote>

|              |                     |
| ------------ | ------------------- |
| **Type**     | `enum (of integer)` |
| **Required** | Yes                 |

**Description:** The status of the binary scanning tool

Must be one of:
* 1
* 2
* 3

**Examples:** 

```json
1
```
```json
2
```
```json
3
```

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-05-28 at 13:53:54 +0200