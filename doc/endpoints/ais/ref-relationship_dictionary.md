# relationship_dictionary

- [1. [Required] Property relationship_dictionary > type](#type)
- [2. [Required] Property relationship_dictionary > spec_version](#spec_version)
- [3. [Required] Property relationship_dictionary > id](#id)
- [4. [Required] Property relationship_dictionary > created](#created)
- [5. [Required] Property relationship_dictionary > modified](#modified)
- [6. [Required] Property relationship_dictionary > relationship_type](#relationship_type)
- [7. [Required] Property relationship_dictionary > source_ref](#source_ref)
- [8. [Required] Property relationship_dictionary > target_ref](#target_ref)

**Title:** relationship_dictionary

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

<details>
<summary>
<strong> <a name="type"></a>1. [Required] Property relationship_dictionary > type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** property extension from the request (coming from the STIX format)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="spec_version"></a>2. [Required] Property relationship_dictionary > spec_version</strong>  

</summary>
<blockquote>

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

**Description:** version of the stix format

Specific value: `"relationship"`

</blockquote>
</details>

<details>
<summary>
<strong> <a name="id"></a>3. [Required] Property relationship_dictionary > id</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^relationship--.*$``` [Test](https://regex101.com/?regex=%5Erelationship--.%2A%24) |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="created"></a>4. [Required] Property relationship_dictionary > created</strong>  

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
<strong> <a name="modified"></a>5. [Required] Property relationship_dictionary > modified</strong>  

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
<strong> <a name="relationship_type"></a>6. [Required] Property relationship_dictionary > relationship_type</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** relationship type of the deviation

</blockquote>
</details>

<details>
<summary>
<strong> <a name="source_ref"></a>7. [Required] Property relationship_dictionary > source_ref</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** reference to the source indicator

| Restrictions                      |                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^indicator--.*$``` [Test](https://regex101.com/?regex=%5Eindicator--.%2A%24) |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="target_ref"></a>8. [Required] Property relationship_dictionary > target_ref</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** reference to the target indicator

| Restrictions                      |                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------- |
| **Must match regular expression** | ```^indicator--.*$``` [Test](https://regex101.com/?regex=%5Eindicator--.%2A%24) |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-08-05 at 08:54:51 +0200