### Setting up Locust tests
The [Locust docs](https://docs.locust.io/en/stable/) are a great source of information on how to set up everything.

A simple `locustfile.py` was derived from them, filled with valid **VSOC JSON requests** and could then be
deployed with the **Locust pip package**.

The explanation for the command flags that is provided with
`locust --help` was enough to find the most fitting runtime arguments.

Lastly, a `README.md` was created to ease the set-up and testing process.