# vulnReport

- [1. [Required] Property vulnReport > AB_id](#AB_id)
- [2. [Required] Property vulnReport > timeStamp](#timeStamp)
- [3. [Required] Property vulnReport > VIN](#VIN)
- [4. [Required] Property vulnReport > scanType](#scanType)
- [5. [Required] Property vulnReport > result](#result)

**Title:** vulnReport

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** A vulnerability report

<details>
<summary>
<strong> <a name="AB_id"></a>1. [Required] Property vulnReport > AB_id</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** ID of the AB

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="timeStamp"></a>2. [Required] Property vulnReport > timeStamp</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the message in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="VIN"></a>3. [Required] Property vulnReport > VIN</strong>  

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
<strong> <a name="scanType"></a>4. [Required] Property vulnReport > scanType</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** The type of the requested scan

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="result"></a>5. [Required] Property vulnReport > result</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** result data

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-22 at 10:15:27 +0200