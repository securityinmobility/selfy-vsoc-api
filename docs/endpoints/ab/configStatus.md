# configstatus

- [1. [Required] Property configstatus > AB_id](#AB_id)
- [2. [Required] Property configstatus > timeStamp](#timeStamp)
- [3. [Required] Property configstatus > Enable](#Enable)
- [4. [Required] Property configstatus > Selectivemode](#Selectivemode)
- [5. [Required] Property configstatus > MINTIMETORESCAN](#MINTIMETORESCAN)
- [6. [Required] Property configstatus > JAMSIGFREQ](#JAMSIGFREQ)
- [7. [Required] Property configstatus > HEARTBEATFREQ](#HEARTBEATFREQ)
- [8. [Required] Property configstatus > AUDITTECHS](#AUDITTECHS)

**Title:** configstatus

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** Whenever VSOC requests, the AB answers with current config status

<details>
<summary>
<strong> <a name="AB_id"></a>1. [Required] Property configstatus > AB_id</strong>  

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
<strong> <a name="timeStamp"></a>2. [Required] Property configstatus > timeStamp</strong>  

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
<strong> <a name="Enable"></a>3. [Required] Property configstatus > Enable</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Enable status

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="Selectivemode"></a>4. [Required] Property configstatus > Selectivemode</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Mode of the Audit Box

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="MINTIMETORESCAN"></a>5. [Required] Property configstatus > MINTIMETORESCAN</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** MINTIMETORESCAN parameter

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="JAMSIGFREQ"></a>6. [Required] Property configstatus > JAMSIGFREQ</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** JAMSIGFREQ parameter

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="HEARTBEATFREQ"></a>7. [Required] Property configstatus > HEARTBEATFREQ</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** HEARTBEATFREQ parameter

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="AUDITTECHS"></a>8. [Required] Property configstatus > AUDITTECHS</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Parameter of which technologies to audit

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-05-28 at 13:53:54 +0200