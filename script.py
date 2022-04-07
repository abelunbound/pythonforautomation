# House for our automated terminal logic
# Subprocess is a library that allows our python script to interact wiht the commandline interface or shell

import subprocess
for i in range(0,5):
    subprocess.check_call(['python','example.py'])