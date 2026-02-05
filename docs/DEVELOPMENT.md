# Development Guide

This guide provides information for developers working on the Scientific Computation repository.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Running Code](#running-code)
- [Testing](#testing)
- [Adding New Assignments](#adding-new-assignments)
- [Common Tasks](#common-tasks)
- [Troubleshooting](#troubleshooting)

## Development Setup

### Prerequisites

- **Python**: 3.8 or higher
- **pip**: Latest version
- **Git**: For version control
- **Code Editor**: VS Code recommended (workspace file included)

### Initial Setup

1. **Clone the repository:**
```bash
git clone https://github.com/jakujobi/Scientific_Computation.git
cd Scientific_Computation
```

2. **Create a virtual environment (recommended):**
```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies:**
```bash
# Install compatible versions (recommended)
pip install streamlit matplotlib numpy

# Or use requirements.txt (may have conflicts)
# pip install -r requirements.txt
```

4. **Verify installation:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py
```

### VS Code Setup

The repository includes a workspace file: `MATH 374 - Computational Theory.code-workspace`

**To use:**
1. Open VS Code
2. File → Open Workspace from File
3. Select `MATH 374 - Computational Theory.code-workspace`

**Recommended Extensions:**
- Python (Microsoft)
- Pylance
- Python Docstring Generator
- Markdown All in One
- Markdown Preview Enhanced

## Project Structure

```
Scientific_Computation/
├── Assignment/              # Assignment solutions
│   ├── A1-Assignment-1.2/
│   │   ├── *.md            # Markdown solutions
│   │   ├── *.pdf           # PDF exports
│   │   └── *.png           # Visualizations
│   ├── A2-Assignment-CH1.3/
│   │   ├── *.py            # Python implementations
│   │   ├── *.md            # Documentation
│   │   └── *.txt           # Test results
│   └── ...                 # Other assignments
├── docs/                   # Project documentation
│   ├── ARCHITECTURE.md
│   └── DEVELOPMENT.md
├── requirements.txt        # Python dependencies
├── streamlit_app.py       # Streamlit entry point
└── README.md              # Main documentation
```

### File Organization

- **Assignment directories**: Self-contained, one per assignment
- **Python files**: Named `A{N}_{DescriptiveName}.py`
- **Markdown files**: Named `A{N}-Assignment-{Chapter}.md`
- **PDFs**: Exported versions of markdown files

## Coding Standards

### Python Style Guide

Follow **PEP 8** conventions with these specifics:

#### File Header

Include author information and metadata:

```python
# A{N}_{ScriptName}.py
# Author: John Akujobi
# GitHub: https://github.com/jakujobi/
# Date: YYYY-MM-DD
# Version: X.Y
```

#### Docstrings

Use detailed docstrings for modules, classes, and functions:

```python
"""
Module description.

This module implements [specific functionality].

Key features:
    - Feature 1
    - Feature 2
    
Example:
    >>> from module import function
    >>> function(args)
    result
"""

def function(param: type) -> return_type:
    """
    Brief function description.
    
    Detailed explanation of what the function does.
    
    Parameters:
        param (type): Description of parameter.
        
    Returns:
        return_type: Description of return value.
        
    Examples:
        >>> function(example_input)
        expected_output
    """
    pass
```

#### Type Hints

Always use type hints for function signatures:

```python
from typing import Dict, Any, List

def convert_number(value: float, precision: int) -> Dict[str, Any]:
    """Convert number with specified precision."""
    pass
```

#### Code Organization

1. **Imports**: Standard library → Third-party → Local modules
2. **Constants**: Define at module level with UPPER_CASE
3. **Classes**: One primary class per file
4. **Functions**: Helper functions before usage
5. **Main block**: Always include for runnable scripts

```python
if __name__ == '__main__':
    main()
```

### Markdown Style Guide

#### Headers

Use ATX-style headers with descriptive titles:

```markdown
# Assignment N - Chapter X.Y

## Problem 1

### Solution

#### Step 1: [Description]
```

#### Mathematical Notation

Use LaTeX for equations:

```markdown
Inline math: $f(x) = x^2$

Display math:
$$
\int_0^1 x^2 \, dx = \frac{1}{3}
$$
```

#### Code Blocks

Always specify the language:

````markdown
```python
def function():
    pass
```

```bash
python script.py
```
````

#### Lists

Use consistent bullet styles:

```markdown
- Unordered item
- Another item
  - Nested item

1. Ordered item
2. Another item
```

## Running Code

### Running Python Scripts

**IEEE-754 Converter:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py
```

**Relative Error Bound:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_Relative_Error_Bound.py
```

### Importing as Modules

To use code from other directories:

```python
import sys
import os

# Add assignment directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Assignment', 'A2-Assignment-CH1.3'))

# Import module
from A2_IEEE754Converter import IEEE754Converter

# Use
converter = IEEE754Converter()
result = converter.to_single(3.14)
```

### Running Streamlit App (Future)

**Note**: Currently non-functional due to missing `Project_1` module.

```bash
streamlit run streamlit_app.py
```

## Testing

### Current State

**No automated tests** are currently implemented.

### Manual Testing

1. **Run the script:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py
```

2. **Verify output:**
   - Check that IEEE-754 representations match expected values
   - Compare with online converters (e.g., [h-schmidt.net/FloatConverter](https://www.h-schmidt.net/FloatConverter/IEEE754.html))
   - Verify edge cases (zero, infinity, NaN)

### Future: Adding Unit Tests

**Recommended structure:**

```
tests/
├── __init__.py
├── test_ieee754.py
├── test_error_bound.py
└── test_integration.py
```

**Example test:**

```python
import unittest
from Assignment.A2_Assignment_CH1_3.A2_IEEE754Converter import IEEE754Converter

class TestIEEE754Converter(unittest.TestCase):
    def setUp(self):
        self.converter = IEEE754Converter()
    
    def test_single_precision_one(self):
        result = self.converter.to_single(1.0)
        self.assertEqual(result['hex'], '0x3f800000')
        self.assertEqual(result['exponent'], 127)
        self.assertEqual(result['fraction'], 0)
    
    def test_special_cases(self):
        # Test infinity
        inf_result = self.converter.to_single(float('inf'))
        self.assertEqual(inf_result['exponent'], 255)
        
        # Test NaN
        nan_result = self.converter.to_single(float('nan'))
        self.assertEqual(nan_result['exponent'], 255)

if __name__ == '__main__':
    unittest.main()
```

## Adding New Assignments

### Step-by-Step Process

1. **Create assignment directory:**
```bash
mkdir "Assignment/A{N}-Assignment-{Chapter}"
cd "Assignment/A{N}-Assignment-{Chapter}"
```

2. **Create markdown file:**
```bash
touch "A{N}-Assignment-{Chapter}.md"
```

3. **Document the problem:**
```markdown
# John Akujobi - Math 374 - Spring 2025

## Problem 1

[Problem statement]

### Solution

[Your solution with mathematical derivations]
```

4. **Implement code (if needed):**
```bash
touch "A{N}_{MethodName}.py"
```

5. **Add to README:**
   - Update the assignments table
   - Add usage examples if code is included

6. **Export to PDF (for submission):**
   - Use VS Code markdown PDF export
   - Or use Pandoc: `pandoc input.md -o output.pdf`

### Assignment Checklist

- [ ] Create directory following naming convention
- [ ] Write markdown solution with clear explanations
- [ ] Implement code if required
- [ ] Test code thoroughly
- [ ] Add docstrings and type hints
- [ ] Export to PDF
- [ ] Update README.md
- [ ] Commit with clear message

## Common Tasks

### Exporting Markdown to PDF

**Using VS Code:**
1. Install "Markdown PDF" extension
2. Open markdown file
3. Ctrl+Shift+P → "Markdown PDF: Export (pdf)"

**Using Pandoc (command line):**
```bash
pandoc Assignment/A1-Assignment-1.2/A1-Assignment-1.2.md -o Assignment/A1-Assignment-1.2/A1-Assignment-1.2.pdf
```

### Creating Visualizations

**Using matplotlib:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 2, 100)
y = x**2

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function')
plt.legend()
plt.grid(True)

# Save
plt.savefig('Assignment/A1-Assignment-1.2/figure.png', dpi=300, bbox_inches='tight')
plt.close()
```

### Updating Dependencies

1. **Check current versions:**
```bash
pip list
```

2. **Update specific package:**
```bash
pip install --upgrade streamlit
```

3. **Update requirements.txt:**
```bash
pip freeze > requirements.txt
```

**Note**: Edit to remove unnecessary packages and ensure compatibility.

### Git Workflow

1. **Check status:**
```bash
git status
```

2. **Add files:**
```bash
git add Assignment/A{N}-*
```

3. **Commit with descriptive message:**
```bash
git commit -m "Add Assignment {N}: {Brief description}"
```

4. **Push to remote:**
```bash
git push origin main
```

## Troubleshooting

### Dependency Conflicts

**Problem**: `requirements.txt` has incompatible versions

**Solution**: Install without version pins:
```bash
pip install streamlit matplotlib numpy
```

### Import Errors

**Problem**: Cannot import modules from assignment directories

**Solution**: Add directory to Python path:
```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Assignment', 'A2-Assignment-CH1.3'))
```

### Streamlit App Not Working

**Problem**: `streamlit_app.py` references missing `Project_1` module

**Status**: Known issue - module not in repository

**Workaround**: Comment out or remove streamlit_app.py if not needed

### Python Version Issues

**Problem**: Code requires Python 3.8+ features (type hints, etc.)

**Solution**: Upgrade Python:
```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install python3.12

# On macOS with Homebrew
brew install python@3.12

# On Windows
# Download from python.org
```

### Mathematical Notation Not Rendering

**Problem**: LaTeX math not displaying in markdown preview

**Solution**:
- Use VS Code with "Markdown Preview Enhanced" extension
- Or export to PDF where LaTeX is properly rendered
- GitHub will render math in `.md` files automatically

## Development Tips

### Code Reusability

Consider extracting common functionality:

```python
# utils/numerical_methods.py
def relative_error(approximate: float, exact: float) -> float:
    """Calculate relative error."""
    return abs(approximate - exact) / abs(exact)
```

### Documentation

- Document **why**, not just **what**
- Include mathematical background in docstrings
- Add examples for complex functions
- Link to relevant textbook sections or papers

### Performance

For numerical methods:
- Profile code to find bottlenecks
- Use NumPy for array operations
- Consider algorithmic improvements before micro-optimizations

### Collaboration

- Use clear commit messages
- Keep changes focused and atomic
- Document any non-obvious decisions
- Add TODO comments for future improvements

---

## Additional Resources

### Python Resources

- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

### Mathematical Computing

- [IEEE-754 Standard](https://standards.ieee.org/standard/754-2019.html)
- [Numerical Recipes](http://numerical.recipes/)
- [SciPy Lectures](https://scipy-lectures.org/)

### Tools

- [VS Code](https://code.visualstudio.com/)
- [Pandoc](https://pandoc.org/)
- [LaTeX Math Reference](https://katex.org/docs/supported.html)

---

**Document Version**: 1.0  
**Last Updated**: February 2025  
**Maintained By**: John Akujobi
