# Getting Started with Jupyter Notebook

## What is Jupyter Notebook?

Jupyter Notebook is an interactive environment for writing and running code in your web browser.

It is commonly used for:

- Learning Python
- Data science
- Machine learning
- Visualization
- Experimentation
- Teaching and tutorials

Jupyter notebooks combine:

- Code
- Text
- Images
- Charts
- Output

in a single document.

Notebook files use the extension:

```text
.ipynb
```

# 1. Install Python

Before installing Jupyter Notebook, follow the steps in [01-getting-started.md](01-getting-started.md) to install Python.

# 2. Install Jupyter Notebook

Install using `pip`.

## Windows

```bash
pip install notebook
```

## macOS/Linux

```bash
pip3 install notebook
```

You can also use:

```bash
python -m pip install notebook
```

# 3. Launch Jupyter Notebook

Start Jupyter Notebook from a terminal.

## Windows

```bash
jupyter notebook
```

## macOS/Linux

```bash
jupyter notebook
```

This will:

- Start a local server
- Open Jupyter in your browser

You should see a page similar to a file explorer.

# 4. Create Your First Notebook

1. Click:

```text
New
```

2. Select:

```text
Python 3
```

A new notebook will open.

# 5. Understanding Cells

Jupyter notebooks use cells.

## Code Cells

Run Python code.

Example:

```python
print("Hello from Jupyter!")
```

Run the cell using:

- Shift + Enter

## Markdown Cells

Used for notes and documentation.

Example:

```markdown
# My Notebook

This is a markdown cell.
```

Change cell type using the dropdown menu.

# 6. Basic Example

## Variables

```python
name = "Python"
version = 3.13

print(name)
print(version)
```

## Loops

```python
for i in range(5):
    print(i)
```

## Functions

```python
def greet(name):
    return f"Hello, {name}"

print(greet("World"))
```

# 7. Installing Packages

Install packages directly in a terminal:

```bash
pip install pandas matplotlib numpy
```

Or inside a notebook:

```python
!pip install pandas
```

# 8. Using Virtual Environments (Recommended)

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

## Windows

```bash
.venv\Scripts\activate
```

## macOS/Linux

```bash
source .venv/bin/activate
```

Install Jupyter inside it:

```bash
pip install notebook
```

# 9. Useful Notebook Shortcuts

## Run Cell

```text
Shift + Enter
```

## Add Cell Below

```text
B
```

## Add Cell Above

```text
A
```

## Delete Cell

```text
D twice
```

## Command Mode

```text
Esc
```

## Edit Mode

```text
Enter
```

# 10. Save and Export

Jupyter automatically saves notebooks periodically.

You can also manually save:

```text
Ctrl + S
```

or:

```text
Cmd + S
```

Export notebook:

```text
File -> Download As
```

Options include:

- HTML
- PDF
- Markdown
- Python script

# 11. JupyterLab (Recommended Upgrade)

JupyterLab is the modern version of Jupyter Notebook.

Install:

```bash
pip install jupyterlab
```

Launch:

```bash
jupyter lab
```

JupyterLab provides:

- Tabs
- File browser
- Terminal access
- Better UI
- Multiple notebooks

# 12. Common Data Science Packages

## NumPy

```bash
pip install numpy
```

## Pandas

```bash
pip install pandas
```

## Matplotlib

```bash
pip install matplotlib
```

## Scikit-learn

```bash
pip install scikit-learn
```

# 13. Example Data Visualization

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.show()
```

# 14. Stopping Jupyter

Return to the terminal running Jupyter and press:

```text
Ctrl + C
```

Then confirm shutdown.

# 15. Useful Resources

Official websites:

- https://jupyter.org/
- https://docs.jupyter.org/
- https://realpython.com/
