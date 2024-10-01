# heartbeat

- [1. [Required] Property heartbeat > AB_id](#AB_id)
- [2. [Required] Property heartbeat > timeStamp](#timeStamp)
- [3. [Required] Property heartbeat > DTCs](#DTCs)
- [4. [Required] Property heartbeat > lastResetTimeStamp](#lastResetTimeStamp)
- [5. [Required] Property heartbeat > lastResetCause](#lastResetCause)

**Title:** heartbeat

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** A heartbeat signal

<details>
<summary>
<strong> <a name="AB_id"></a>1. [Required] Property heartbeat > AB_id</strong>  

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
<strong> <a name="timeStamp"></a>2. [Required] Property heartbeat > timeStamp</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** timestamp of the heartbeat in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="DTCs"></a>3. [Required] Property heartbeat > DTCs</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** List of DTCs

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastResetTimeStamp"></a>4. [Required] Property heartbeat > lastResetTimeStamp</strong>  

</summary>
<blockquote>

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

**Description:** in ISO-8601 (UTC)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastResetCause"></a>5. [Required] Property heartbeat > lastResetCause</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-01 at 15:17:02 +0200