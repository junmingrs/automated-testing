# This is purely for linux

```
TEST_BROWSER=chrome
```

``` 
python -m pytest tests/test_member_1.py --browser-channel $TEST_BROWSER --headed --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py::test_login_with_correct_details --browser-channel $TEST_BROWSER --headed --slowmo 300 --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py::test_login_with_incorrect_password --browser-channel $TEST_BROWSER --headed --slowmo 300 --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py --browser-channel $TEST_BROWSER --headed --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m playwright codegen --channel $TEST_BROWSER --target python-pytest -o recordings/member-1/recorded_task.py https://demo.playwright.dev/todomvc/
```

```
python -m pytest recordings/member-1/recorded_task.py --browser-channel $TEST_BROWSER --headed --slowmo 300 --output test-results/member-1/recording-run --screenshot on --junitxml=reports/member-1/recording.xml --html=reports/member-1/recording.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py --browser-channel $TEST_BROWSER --headed --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py::test_active_filter_shows_unfinished_task --browser-channel $TEST_BROWSER --headed --slowmo 300 --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```

```
python -m pytest tests/test_member_1.py::test_delete_task --browser-channel $TEST_BROWSER --headed --slowmo 300 --output test-results/member-1/current-run --screenshot on --junitxml=reports/member-1/results.xml --html=reports/member-1/results.html --self-contained-html
```













