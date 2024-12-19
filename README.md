# Course Playwright Python

### Learn Playwright and master web automation!
This repository contains the course materials and exercises for a comprehensive Playwright course.<br>
It covers everything from the basics to advanced techniques, making it ideal for both beginners and experienced testers.<br> 
The full course, including in-depth theory (delivered through PowerPoint presentations), assignments, and Q&A sessions, will take approximately 4 hours to complete.<br>
**Please contact me for more information.**

### Key Topics:
- **Introduction to Playwright**: Understand the core concepts and capabilities of Playwright.
- **Web Element Interaction**: Learn how to locate and interact with web elements.
- **Assertions**: Master the art of verifying expected behavior in your tests.
- **Waiting Mechanisms**: Learn how to handle dynamic web elements and asynchronous operations.
- **Cross-Browser Testing**: Execute tests across different browsers and platforms.
- **Advanced Techniques**: Explore advanced scenarios like multi-tab, multi-origin, and multi-user testing.
- **Playwright Tooling**: Utilize powerful tools like Codegen, UI mode, and Trace Viewer.
- **CI/CD Integration**: Learn how to integrate Playwright into your CI/CD pipeline.

### Who Should Attend:
- Software Testers
- Developers
- DevOps Engineers
- Technical Leads/Managers
- Anyone interested in web testing

### Prerequisites:
- Programming skills: **Python**
- Basic understanding of **GIT** (You should be able to clone this repo) + **PYTEST**

### This repository provides:
- Practical exercises
- Code examples

>Let's dive into the world of Playwright and build robust, reliable web applications!

## Getting started

**Step 1: Download and Install Python**
1. Download Python:
    - Go to the official Python website: https://www.python.org/downloads/
    - Download the latest version of Python for your operating system.

2. Install Python:
    - Run the installer and follow the installation instructions.
    - Make sure to check the box that says "Add Python to PATH" during the installation process.

**Step 2: Install Git**
1. Download Git:
    - Go to the official Git website: https://git-scm.com/
    - Click on "Download" and select the version for your operating system.

2. Run the Installer:
    - Locate the downloaded `.exe` file and run it.
    - Follow the installation prompts. You can use the default settings for most options.

3. Verify Installation:
    - Open Command Prompt.
    - Type the following command and press Enter:

        ```Bash 
        > git --version
        ```

**Step 3: Clone the Repository**
1. **Open a Terminal or Command Prompt:**
    - On Windows, you can open Command Prompt or PowerShell.
    - On macOS or Linux, open the Terminal.

2. **Clone the repo:**
    ```Bash
    git clone https://github.com/RobbertChampagne/course-playwright-python.git
    ```

3. **Run the following command to create a virtual environment:**
    ```Bash
    python -m venv pythonenv
    ```

4. **Activate the virtual environment:**
    ```Bash
    pythonenv\Scripts\activate
    ```

5. **Install packages:**
    ```Bash
    pip install pytest playwright pytest-playwright python-dotenv pytest-html 
    ```

6. **Install playwright browsers:**
    ```Bash
    playwright install
    ```

7. **Export the installed packages to a requirements.txt file:**
    ```Bash
    pip freeze > requirements.txt
    ```

**Done? -> Deactivate the virtual environment:**
```Bash
deactivate
```

**Install packages from requirements.txt:**
```Bash
pip install -r requirements.txt
```

**To list all virtual environments created using venv or other tools like virtualenv, you can use:**
```Bash
dir /s /b activate
or
Get-ChildItem -Recurse -Name -Filter activate
```

---

### Modifying the PYTHONPATH environment variable:
Setting the PYTHONPATH environment variable using set PYTHONPATH=%cd% in the Command Prompt or $env:PYTHONPATH=$(pwd) in PowerShell **will only apply to the current terminal session**.<br> 
Once you close the terminal, the environment variable will no longer be set.<br>

Because running tests from the root folder, the relative imports in your `conftest.py` file are not resolving correctly.<br> 
When running tests from the root folder, Python needs to know where to find the modules and packages in your project.<br> 

By modifying the **PYTHONPATH** environment variable or **sys.path**, you ensure that Python can locate the necessary modules and packages,<br>
regardless of where the tests are run from.

**PYTHONPATH**:
- Is an environment variable that specifies the search path for Python modules. 
When you run a Python script, Python uses the directories listed in **PYTHONPATH** to locate modules and packages.
- By setting **PYTHONPATH** to the current directory, you ensure that Python can find the modules and packages in your project.

**%cd%**:
- Is a Windows command prompt variable that represents the current directory. 
When you use **%cd%** in a command, it is replaced with the full path of the current directory.
- For example, if your current directory is `C:\Users\..\..\..\course-playwright-python`, **%cd%** will be replaced with `C:\Users\..\..\..\course-playwright-python`.

```Bash
cd C:\Users\..\..\..\course-playwright-python
set PYTHONPATH=%cd%
```

**Relative Imports**:<br>
Specify the path to the module relative to the current module's location.<br>
They use dots (`..`) to indicate the current and parent directories.

In the `course-playwright-python\tests\standalone_test_scripts\conftest.py` file, you are using an absolute import.<br>
This works because the core directory is at the top level of your project,<br> 
and Python can resolve this path correctly when the **PYTHONPATH** or **sys.path** includes the project's root directory.
```Python
from core.loggingSetup import setup_logging
```

In the `course-playwright-python\tests\playwright\module_a\conftest.py` file, you are using a relative import.<br>
This is necessary because the `conftest.py` file is nested within the `module_a` directory,<br> 
and you need to navigate up one level to access the core directory.
```Python
from ..core.loggingSetup import setup_logging
```

---

### Running tests:

Running all tests in a directory:
```Bash
pytest tests/module_a
```

Running all tests in a file:
```Bash
pytest tests/module_a/test_marks.py 
```

Running a specific tests in a file:
```Bash
pytest tests/module_a/tests/test_marks.py::test_get_user_parametrize 
```

Running a specific mark from a file:
```Bash
pytest tests/api/module_a/tests/test_marks.py -m custom_mark
```

Running all the marks from the project:
```Bash
pytest -m custom_mark
```
Running mobile emulation:
```Bash
pytest tests/playwright/module_a/tests/test_text.py --device="Galaxy S9+"
```

Running tests on a browser other than the one specified in the `pytest.ini` file:
```Bash
pytest tests/playwright/module_a/tests/test_text.py --browser=webkit  
```

Codegen:
```Bash
playwright codegen https://robbertchampagne.com/
```

Trace viewer:
```Bash
playwright show-trace tests/playwright/traces/module_b/trace_example.zip
```

---

### Reports:

```Bash
# Install pytest-html
pip install pytest-html

# Run tests and generate an HTML report
pytest --html=report.html

# Install pytest-json-report
pip install pytest-json-report

# Run tests and generate a JSON report
pytest --json-report --json-report-file=report.json
```

---

<br>

> **Note**: 
<br>This repository is designed to supplement a structured course.<br> 
For the full learning experience, consider attending the complete course.