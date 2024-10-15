### Sources
- [How to use Bayesian Inference for predictions in Python](https://towardsdatascience.com/how-to-use-bayesian-inference-for-predictions-in-python-4de5d0bc84f3)
- [BayesPy: Variational Bayesian Inference in Python](https://www.jmlr.org/papers/volume17/luttinen16a/luttinen16a.pdf)
- [BayesPy GitHub](https://github.com/bayespy/bayespy)
- [Markov Chain Monte Carlo in Python](https://towardsdatascience.com/markov-chain-monte-carlo-in-python-44f7e609be98)
- [Dempster-Shafer Theory for Classification using Python](https://bennycheung.github.io/dempster-shafer-theory-for-classification)
### Identified requirements
- Score needs to be calculated in a range from 0 - 1
- Score is (ideally) added to a trace when ingested into Elasticsearch (Ingest Pipeline?)
- Score needs to reflect changes from the environment, e.g. information from the SOTA or AIS unit
- Score should be calculated using different fields depending on the trace
- Score should be inferred using Bayesian Variational Inference since the sample size is large enough to support it (+ efficient calculation using BayesPy)
### Development
- For development purposes the indexdump tool (dump.py) can be used which will retrieve the specified index into a file with newline delimited JSON objects
- The interesting fields are located under the labels object, e.g:
```json
	...,
	"labels": {
      "sota_updateInfo_timestamp": "2024-07-23T10:08:30Z",
      "sota_updateInfo_toolid": "8",
      "sota_updateInfo_vin": "1FAHP2E89FG123598",
      "telemetry_auto_version": "0.43b0"
    },
    ...
```
- In this specific case taking the VIN into consideration for the trust score calculation makes sense since there will likely be information attributed to it from previous traces
- The trust score calculation should ideally be done from a component outside of the main Flask app since it would ideally take previous data into consideration
- For the start it can be added manually to the traces from inside app.py and calculated on a single point of data
- A rough implementation could also assign static weights to each possible value of the fields and calculate the score from that (e.g. a status of 2 => +0.2)
- To make the score calculation more dynamic a statistic model needs to be created using BayesPy which can then infer the scores based on previous observations
### Next steps
- Identify interesting fields for the trust score calculation for each trace type
- Construct a model using BayesPy that uses these fields for inference
- Find a preprocessor solution that can mark the traces with a trust score before being indexed into Elasticsearch