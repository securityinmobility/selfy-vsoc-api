# Locust
### Installation
First, you will need to install Locust using `pip`.
```sh
pip install locust
```
### How to use
Once the installation is finished, you can check which tests are available with `locust -l`.
```sh
locust -l

# the output will look similar to this
# Available Users:
#     SOTAUser
#     RASUser
#     ABUser
#     AISUser
```
In this case, there are four tests, each corresponding to a different VSOC endpoint.
All of them are defined inside `locustfile.py`.

You can start all the tests by running `locust`.
```sh
locust --users 4 --spawn-rate 4 --run-time 5s
```
This will start a web interface under [http://localhost:8089](http://localhost:8089)
where you can manually start the process.

It will send 10 requests per second for 5 seconds, totaling up to 50 requests, to each endpoint.

You can also run the tests automatically without the web interface by invoking the ```--headless``` flag.
```sh
locust --users 4 --spawn-rate 4 --run-time 5s --headless
```
After completion, performance information (e.g. failures) will be displayed in the console output.

If you don't want to run every test, you can explicitly specify which tests to run at the end of the command.
```sh
locust --users 2 --spawn-rate 2 --run-time 5s --headless SOTAUser RASUser
```
Note that `--users` and `--spawn-rate` should also be set to the amount of tests you are running.

Running `locust --help` will provide you with more information about the command.

### How to add tests
The tests themselves are easy to set up. If you want to add a new test, you can
add it to `locustfile.py` and look at the already existing ones as a template.