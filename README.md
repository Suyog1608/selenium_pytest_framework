<h2>Python Automation Testing Framework using Pytest and Selenium</h2>

<p><b>Notes :</b></p>
<ol>
    <li><b>pytest</b> : Command to run all the test cases</li>
    <li><b>pytest -v -s</b> : Command to run the test cases with details</li>

<h3>Grouping in Pytest</h3>
<li>Run all test cases in a specific file:
<ol>
<pre>
pytest tests\test_grouping.py -v -s </pre>
</ol>
</li>
<li>Run a specific test case in a file:
<ol>
<pre>
pytest tests\test_grouping.py::Test_groups::test_tc01 -v -s
</pre>
</ol>
</li>

<h3>Ordering in Pytest</h3>
    <li>Install order plugin: <b>pip install pytest-order</b></li>
    <li>Use annotation on function level: <b>@pytest.mark.order(&lt;order_number&gt;)</b></li>
    <li>Tests will run according to the given order number (use the same command as in grouping).</li>
    <li>Skip a test case: <b>@pytest.mark.skip</b></li>

<h3>Grouping using ini file & markers</h3>
    <li>Use annotation on function level: <b>@pytest.mark.&lt;marker_name&gt;</b></li>
    <li>Example markers in <b>pytest.ini</b>:
<pre>
markers =
    smoke
    sanity
    regression
</pre>
Command to run smoke tests: 
<pre>
<b>pytest -v -s -m smoke
</b></pre>

<h3>Generating Test Case Reports</h3>
<li>Command:
<pre>
pytest -v -s --html=report.html
</pre>
</ol>

<h3>Parallel Test Execution</h3>
    <li>Command: 
<pre>
    pytest -v -s -n 2 .\test_parallel.py
</pre>
<i>Note:</i> Provide the correct file path if inside a folder.
    </li>

<h3>Running Test Cases Using Addoption</h3>
<li>Example function:
<pre>
    def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser name (chrome or edge)')
</pre>
</li>
    <li>Explanation:
        <ol>
            <li><b>pytest_addoption</b> → Pytest hook for adding custom command-line arguments.</li>
            <li><b>parser.addoption('--browser', ...)</b> → Defines a new command-line option.</li>
            <li><b>action='store'</b> → Stores the provided value (e.g., chrome/edge).</li>
            <li><b>default='chrome'</b> → Chrome is used if no browser is specified.</li>
            <li><b>help='...'</b> → Shows help text in <code>pytest --help</code>.</li>
        </ol>
    </li>
    <br>
    <li>Command to run:
<pre>
    <b>pytest -v -s .\test_fixtureWith_addoption.py --browser=edge</b>
</pre>
        <ol>
            <li><b>pytest</b> → Runs Pytest framework.</li>
            <li><b>-v</b> → Verbose mode (detailed output).</li>
            <li><b>-s</b> → Displays print statements in terminal.</li>
            <li><b>.\test_fixtureWith_addoption.py</b> → Specifies the test file.</li>
            <li><b>--browser=edge</b> → Sets browser to Edge.</li>
        </ol>
    </li>

