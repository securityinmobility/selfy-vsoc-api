# attestationResult

- [1. Property `attestationResult > anyOf > Vehicle is OK`](#anyOf_i0)
  - [1.1. [Required] Property attestationResult > anyOf > Vehicle is OK > verifier](#anyOf_i0_verifier)
  - [1.2. [Required] Property attestationResult > anyOf > Vehicle is OK > VSOC](#anyOf_i0_VSOC)
  - [1.3. [Required] Property attestationResult > anyOf > Vehicle is OK > target_tool](#anyOf_i0_target_tool)
  - [1.4. [Required] Property attestationResult > anyOf > Vehicle is OK > state](#anyOf_i0_state)
  - [1.5. [Required] Property attestationResult > anyOf > Vehicle is OK > nonce](#anyOf_i0_nonce)
  - [1.6. [Required] Property attestationResult > anyOf > Vehicle is OK > created](#anyOf_i0_created)
  - [1.7. [Optional] Property attestationResult > anyOf > Vehicle is OK > VIN](#anyOf_i0_VIN)

**Title:** attestationResult

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** attestationResult endpoint for the RAS infrastructure

<blockquote>

| Any of(Option)             |
| -------------------------- |
| [Vehicle is OK](#anyOf_i0) |

<blockquote>

## <a name="anyOf_i0"></a>1. Property `attestationResult > anyOf > Vehicle is OK`

**Title:** Vehicle is OK

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

<details>
<summary>
<strong> <a name="anyOf_i0_verifier"></a>1.1. [Required] Property attestationResult > anyOf > Vehicle is OK > verifier</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the verifier (usually ID18)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anyOf_i0_VSOC"></a>1.2. [Required] Property attestationResult > anyOf > Vehicle is OK > VSOC</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the VSOC (usually ID08)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anyOf_i0_target_tool"></a>1.3. [Required] Property attestationResult > anyOf > Vehicle is OK > target_tool</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** ID of the tool for the RAS result

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anyOf_i0_state"></a>1.4. [Required] Property attestationResult > anyOf > Vehicle is OK > state</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** status of the attestation result

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anyOf_i0_nonce"></a>1.5. [Required] Property attestationResult > anyOf > Vehicle is OK > nonce</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** random nonce of the request

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anyOf_i0_created"></a>1.6. [Required] Property attestationResult > anyOf > Vehicle is OK > created</strong>  

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
<strong> <a name="anyOf_i0_VIN"></a>1.7. [Optional] Property attestationResult > anyOf > Vehicle is OK > VIN</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** vehicle identification number of the vehicle

</blockquote>
</details>

</blockquote>

</blockquote>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2024-10-29 at 16:00:00 +0100