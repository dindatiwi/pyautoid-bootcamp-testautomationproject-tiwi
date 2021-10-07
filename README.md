<p align="center">✨Test Automation Project✨
  <br>
  Repository purposely for pratice of selenium test automation using pytest from pyautoid bootcamp
</p>

> a script to do login test with automation using selenium pytest

> website used [Pandu Digital by Kominfo](https://pandu.kominfo.go.id/)

# Requirements
- Python 3.9.6
- pytest 6.2.5
- pytest-html v3.1.1
- ChromeDriver 94.0.4606.61
- Selenium 3.141.0
- Spirit To Learn📚

# Installation
‼️Make sure to look at the `class Prereq` and change the `mail`, `password`, `name` according to your registered account
```Python3
class Prereq:
    mail = 'bzwfdu@uniromax.com'
    password = 'f.M9V2HgSY.y6xM'
    name = 'Ronnie Gilmore'
```
###### ‼️‼️the written mail, password, and name is purposely registered for testing purpose

Run this command in commandline to run the test :
``` 
python3 -m pytest -v test_login.py 
```

Run this command in commandline to run the test with the report :
``` 
python3 -m pytest -v test_login.py --html=report.html
```

# Test Case
> Used Test Case as parameter to validate the test

<img width="1500" alt="Test Case Login Automation Project" src="https://user-images.githubusercontent.com/44132935/136389927-1e4f3d8e-017b-42d3-b578-94601adfbea9.png">

# Report
Live Test Report [here](https://dindatiwi.github.io/pyautoid-bootcamp-testautomationproject-tiwi/index.html)
>Report generated on 07-Oct-2021 at 14:09:56 by pytest-html v3.1.1
