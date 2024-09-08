# updateInfo

- [1. [Required] Property updateInfo > selfy_id](#selfy_id)
- [2. [Required] Property updateInfo > timeStamp](#timeStamp)
- [3. [Required] Property updateInfo > message](#message)
  - [3.1. [Required] Property updateInfo > message > action](#message_action)
  - [3.2. [Required] Property updateInfo > message > vin](#message_vin)
  - [3.3. [Required] Property updateInfo > message > deviceID](#message_deviceID)
  - [3.4. [Required] Property updateInfo > message > status](#message_status)
  - [3.5. [Optional] Property updateInfo > message > deviceMetadata](#message_deviceMetadata)

**Title:** updateInfo

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** updateInfo endpoint for the SOTA infrastructure

<details>
<summary>
<strong> <a name="selfy_id"></a>1. [Required] Property updateInfo > selfy_id</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** ID of the SOTA endpoint

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="timeStamp"></a>2. [Required] Property updateInfo > timeStamp</strong>  

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
<strong> <a name="message"></a>3. [Required] Property updateInfo > message</strong>  

</summary>
<blockquote>

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

**Description:** containg message information

<details>
<summary>
<strong> <a name="message_action"></a>3.1. [Required] Property updateInfo > message > action</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** action flag; e.g. 1 for update

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="message_vin"></a>3.2. [Required] Property updateInfo > message > vin</strong>  

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
<strong> <a name="message_deviceID"></a>3.3. [Required] Property updateInfo > message > deviceID</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the device

</blockquote>
</details>

<details>
<summary>
<strong> <a name="message_status"></a>3.4. [Required] Property updateInfo > message > status</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** status of the update

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 2 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="message_deviceMetadata"></a>3.5. [Optional] Property updateInfo > message > deviceMetadata</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Metadata about the update

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-09-09 at 01:13:35 +0200