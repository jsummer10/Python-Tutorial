# Getting Started with Python

## What is Python?

Python is a popular programming language used for:

- Automation
- Web development
- Data science
- Scripting
- APIs and servers
- AI and machine learning
- Desktop applications

Python is designed to be readable and beginner-friendly.

Example:

```python
print("Hello, world!")
```

# 1. Download Python

Go to the official Python website:

https://www.python.org/downloads/

Download the latest stable version for your operating system:

- Windows
- macOS
- Linux

# 2. Install Python

## Windows

1. Run the installer
2. IMPORTANT: Check the box:

```text
Add Python to PATH
```

3. Click:

```text
Install Now
```

4. Wait for installation to complete

Verify installation:

```bash
python --version
```

or:

```bash
py --version
```

## macOS

### Option 1 (Recommended): Install from python.org

https://www.python.org/downloads/macos/

Verify installation:

```bash
python3 --version
```

### Option 2: Install with Homebrew

```bash
brew install python
```

Verify:

```bash
python3 --version
```

## Linux

Check installed version:

```bash
python3 --version
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install python3
```

### Fedora

```bash
sudo dnf install python3
```

### Arch Linux

```bash
sudo pacman -S python
```

# 3. Run Python

## Interactive Mode (REPL)

### Windows

```bash
python
```

or:

```bash
py
```

### macOS/Linux

```bash
python3
```

Example:

```python
print("Hello!")
```

Exit:

```python
exit()
```

# 4. Create Your First Python File

Create:

```text
hello.py
```

Contents:

```python
print("Hello, world!")
```

# 5. Run a Python File

## Windows

```bash
python hello.py
```

or:

```bash
py hello.py
```

## macOS/Linux

```bash
python3 hello.py
```

# 6. Install Packages

```bash
pip install requests
```

or:

```bash
pip3 install requests
```

Example:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

# 7. Virtual Environments

Create:

```bash
python -m venv .venv
```

Activate:

## Windows

```bash
.venv\Scripts\activate
```

## macOS/Linux

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

# 8. Recommended Editors

- VS Code
- PyCharm
- Vim
- Neovim

# 9. Useful Commands

## Check Version

```bash
python --version
```

## Run File

```bash
python script.py
```

## Install Package

```bash
pip install package_name
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```
