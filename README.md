# Initialize the Quecpython project



I. Test Instructions:

1. Entry file: main_startup. Py

2. Files to be tested





Ii. Test Process:

1. Execute the file main_startup.py to automatically detect usb

2. Perform api_test or API_stress or function_test in turn, depending on the user configuration

3. Perform statistics according to the execution results of PY file (filter the logs in the specified format and count them in Excel for convenience of checking)



Format of log statistics (print in the script for all logs that need to be saved) :

It is divided into 4 columns:

Timestamp = timestamp

API (test interface)

Info (information, such as interface returns results or exception crash information)

Result (test result, TRUE/FALSE, TRUE will be highlighted in green, FALSE will be highlighted in red)

1. Execute log: print(' XXX; ') ## will not be counted in Excel, only recorded in the log file

Log: print(' API :: info||result_api:: result; ') ## output strictly in this format



Symbol description:

1. '; 'is used to separate, and the last character of each print is required to be At the end

2.'::' separates API and Info, Result_API and Result

3.'||' separates api&info and result



Iv. Matters needing Attention

1. Keep the return result format consistent (API ::info||result_api:: False;) If False is detected, it will be recorded in the exception message

