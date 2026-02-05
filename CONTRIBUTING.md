# Contributing to Scientific Computation

Thank you for your interest in this project! This repository is primarily a personal course assignment collection for MATH 374 (Computational Theory), but feedback and suggestions are welcome.

## 🎯 Contribution Scope

### What Contributions Are Welcome

- **Bug reports** for code errors or mathematical mistakes
- **Documentation improvements** (typos, clarity, examples)
- **Suggestions** for better implementations or algorithms
- **Questions** about the approaches used

### What This Repository Is

- **Educational**: A learning project demonstrating numerical methods
- **Personal**: Course assignments for academic credit
- **Reference**: Example implementations of computational mathematics

### What This Repository Is NOT

- A production library
- A collaborative project seeking major contributions
- Open to pull requests that complete assignments (academic integrity)

## 📝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Check existing issues** to avoid duplicates
2. **Open a new issue** with a clear title and description
3. **For bugs**, include:
   - Steps to reproduce
   - Expected vs. actual behavior
   - Python version and OS
   - Error messages/stack traces

**Example:**

```
Title: IEEE754Converter handles infinity incorrectly

Description:
The to_single() method returns wrong exponent for positive infinity.

Steps to reproduce:
1. converter = IEEE754Converter()
2. result = converter.to_single(float('inf'))
3. print(result['exponent'])

Expected: 255
Actual: 254

Python 3.12.3 on Ubuntu 22.04
```

### Suggesting Enhancements

For feature requests or improvements:

1. **Open an issue** with tag `enhancement`
2. **Describe the problem** the enhancement would solve
3. **Propose a solution** if you have one
4. **Explain why** it would be valuable

**Example:**

```
Title: Add visualization for IEEE-754 bit patterns

Description:
It would be helpful to have a visual representation of the bit layout 
(sign, exponent, mantissa) for educational purposes.

Proposed solution:
Add a method that returns an ASCII diagram or matplotlib figure showing 
the bit breakdown.

Value:
Would help students understand the structure visually, making the 
converter more valuable as a teaching tool.
```

### Code Contributions

**Note**: Pull requests for completing assignments will not be accepted (academic integrity).

**Accepted code contributions:**
- Bug fixes for existing implementations
- Additional test cases
- Documentation improvements
- New utility functions (not assignment solutions)

**Process:**

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b fix/issue-description`
3. **Make your changes** following the code style guide
4. **Test your changes** thoroughly
5. **Commit with clear messages**: `git commit -m "Fix: Issue description"`
6. **Push to your fork**: `git push origin fix/issue-description`
7. **Open a pull request** with a clear description

## 🎨 Code Style Guide

### Python Code

Follow **PEP 8** with these specifics:

#### Imports

```python
# Standard library
import math
import sys
from typing import Dict, Any

# Third-party
import numpy as np
import matplotlib.pyplot as plt

# Local
from utils import helper_function
```

#### Type Hints

Always use type hints:

```python
def function(value: float, precision: int = 32) -> Dict[str, Any]:
    """Function with type hints."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def convert_value(value: float, base: int) -> str:
    """
    Convert a floating-point value to specified base.
    
    Args:
        value: The number to convert
        base: Target base (2, 8, 10, 16)
        
    Returns:
        String representation in the target base
        
    Raises:
        ValueError: If base is not supported
        
    Example:
        >>> convert_value(15.5, 16)
        'F.8'
    """
    pass
```

#### Naming Conventions

- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **Private members**: `_leading_underscore`

```python
MAX_ITERATIONS = 100

class NumericalSolver:
    def __init__(self):
        self._tolerance = 1e-6
    
    def solve_equation(self, equation: str) -> float:
        pass
```

#### Code Formatting

- **Line length**: 88 characters (Black formatter default)
- **Indentation**: 4 spaces
- **Quotes**: Prefer double quotes for strings
- **Blank lines**: 2 before top-level functions/classes

### Markdown

- Use ATX-style headers (`#` not `===`)
- Specify language in code blocks
- Use LaTeX for math: `$inline$` or `$$display$$`
- Keep line length reasonable (80-100 characters)

### Comments

- Explain **why**, not **what**
- Use complete sentences
- Update comments when code changes

```python
# Good
# Using Horner's method to reduce floating-point errors
result = coeffs[0]
for c in coeffs[1:]:
    result = result * x + c

# Bad
# Loop through coefficients
for c in coeffs:
    result = result * x + c
```

## 🧪 Testing

### Manual Testing

Before submitting:

1. **Run all affected scripts**
2. **Verify output** matches expected results
3. **Test edge cases** (zero, infinity, very large/small numbers)
4. **Check for errors** in different scenarios

### Automated Testing (Future)

If adding tests:

- Place in `tests/` directory
- Name files `test_{module}.py`
- Use `unittest` or `pytest`
- Aim for >80% code coverage

**Example:**

```python
import unittest
from Assignment.A2_Assignment_CH1_3.A2_IEEE754Converter import IEEE754Converter

class TestIEEE754(unittest.TestCase):
    def setUp(self):
        self.converter = IEEE754Converter()
    
    def test_positive_zero(self):
        result = self.converter.to_single(0.0)
        self.assertEqual(result['sign'], 0)
        self.assertEqual(result['exponent'], 0)
        self.assertEqual(result['fraction'], 0)
```

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guide
- [ ] All tests pass (if applicable)
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No unrelated changes included

### PR Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] Documentation update
- [ ] Code refactoring
- [ ] New feature (non-assignment)

## Testing
Describe how you tested the changes

## Related Issues
Fixes #123
```

### Review Process

1. Maintainer will review within 1 week
2. Feedback will be provided if changes needed
3. Once approved, PR will be merged
4. Your contribution will be acknowledged

## 🚫 What NOT to Contribute

### Academic Integrity

**Do NOT submit:**
- Solutions to unfinished assignments
- Code that completes homework problems
- Answers to exam questions

**Rationale**: This violates academic integrity policies

### Out of Scope

**Avoid:**
- Major architectural changes (keep it simple)
- New dependencies without strong justification
- Unrelated features
- Breaking changes to existing code

## 🏆 Recognition

Contributors will be acknowledged in:
- README.md Contributors section
- Commit history
- Release notes (if applicable)

## 📞 Getting Help

### Where to Ask Questions

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For general questions (if enabled)
- **Email**: john@jakujobi.com (for private matters)

### Response Time

- **Issues**: Within 1 week
- **Pull requests**: Within 1-2 weeks
- **Email**: Within 2-3 days

## 📜 Code of Conduct

### Our Standards

- **Be respectful** and considerate
- **Be constructive** in feedback
- **Be collaborative** and helpful
- **Focus on** what is best for the project and community

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Publishing others' private information
- Spam or self-promotion

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban from contributing
3. Permanent ban

Report violations to: john@jakujobi.com

## ✅ Quick Checklist

### For Bug Reports

- [ ] Clear title describing the issue
- [ ] Steps to reproduce
- [ ] Expected vs. actual behavior
- [ ] Python version and OS
- [ ] Error messages/logs

### For Pull Requests

- [ ] Descriptive title and description
- [ ] Links to related issues
- [ ] Code follows style guide
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No academic integrity violations

## 📚 Resources

### Learning Resources

- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [Writing Good Commit Messages](https://chris.beams.io/posts/git-commit/)

### Project Documentation

- [README.md](../README.md) - Project overview
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) - System design
- [DEVELOPMENT.md](docs/DEVELOPMENT.md) - Development guide

## 🙏 Thank You!

Your contributions, whether through code, documentation, or feedback, help make this project better. Every contribution is valued and appreciated.

---

**Last Updated**: February 2025  
**Maintained By**: John Akujobi  
**Contact**: john@jakujobi.com
