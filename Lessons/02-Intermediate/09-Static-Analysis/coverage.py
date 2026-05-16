
# Dependencies
# pip3 install coverage

import subprocess, shutil

# Run coverage analysis
subprocess.run(['coverage', 'run', '-m', 'strings.py'], capture_output=True)

# View coverage report
subprocess.run(['coverage', 'report'])

# Process HTML version of coverage report
subprocess.run(['coverage', 'html'])

subprocess.run(['open', 'htmlcov/index.html'])
