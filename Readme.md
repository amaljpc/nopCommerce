# Installation Instructions

Ensure you have **Python 3.7+** installed in your environment.

```bash
pip install -U pytest
pip install openpyxl
pip install selenium
```

### Running the Python Code
To execute the test script, use the following console commands based on the browser you want to use.
#### Chrome Browser:
```python
pytest -s -v testCases/test_Login.py --browser chrome
```
#### Firefox Browser:
```python
pytest -s -v testCases/test_Login.py --browser firefox
```

### Running Parallel Tests
You can run tests in parallel with multiple browser instances using the -n parameter.

For example, to run tests with 2 parallel browser instances:
```
pytest -s -v -n=2 testCases/test_Login.py --browser firefox
```

### Generating HTML Reports
Generate an HTML report for the test results and specify the report file path using the --html parameter:


```python
pytest -s -v -n=3 --html=Reports/report.html testCases/test_Login.py --browser chrome
```
choose file path from testcases



### To Run this python code use below console command

To Run Chrome browser, run below code in browser
```python
pytest -s -v testCases/test_Login.py --browser chrome
```
To Run Chrome browser, run below code in browser
```python
pytest -s -v testCases/test_Login.py --browser firefox
```

Use below commands to run parallel testing -n=2, means testing two parallel browser will start execution
```
pytest -s -v -n=2 testCases/test_Login.py --browser firefox
```
To run the tests in parallel with 3 workers and generate an HTML report, use the following command:
```python
pytest -s -v -n=3 --html=Reports/report.html testCases/test_Login.py --browser chrome
```
choose file path from testcases

#### Grouping the testcases using pytest markers
- regression<br>
- sanity<br>
- sanity or regression<br>
- sanity and regression<br>

```
pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome```