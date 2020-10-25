# insights-survey-analysis
Small tool to analyse survey results from the Insights App

## Prerequisites
It is recommended to create a [virtual environment](https://docs.python.org/3/library/venv.html) to
avoid any dependency conflicts with other projects. The project needs to run Python 3.6 version. 

To create the virtual environment Using `venv` with Python 3.6 you can create a virtual environment as follows:

```
$ python3 -m venv ENV_DIR
```

Activate your environment according to instructions above.

Upgrade to the most recent version of pip by calling:

```
$ pip install --upgrade pip
```

Another alternative is using `virtualenv` as described
[here](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/virtualenv.html#creating-a-virtualenv).
 ## Installing

For this step, please checkout the repository and activate your virtual environment.
**For developers (i.e. if you will edit the source code), please install using:**

```
pip install -e .
```

All depending packages are installed in the virtual environment, but the actual source code of this
package is copied to the site-packages folder. You should edit and run the code from the
checked-out source directory.

For users **who do not intend to edit the source code**, run:

```
pip install .
```


For installing test dependencies, run: 
```
pip install .[testing]
```
## Running
