# Scientific Computation

A collection of computational mathematics assignments and implementations for MATH 374 (Computational Theory). This repository demonstrates practical applications of numerical methods, floating-point arithmetic, root-finding algorithms, and polynomial interpolation.

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Assignments Overview](#assignments-overview)
- [What This Project Demonstrates](#what-this-project-demonstrates)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## ✨ Features

This repository contains implementations and solutions for the following computational mathematics topics:

- **IEEE-754 Floating-Point Representation** ([A2_IEEE754Converter.py](Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py))
  - Single precision (32-bit) conversion
  - Double precision (64-bit) conversion
  - Handles normalized, subnormal, zeros, infinities, and NaN

- **Relative Error Bound Calculations** ([A2_Relative_Error_Bound.py](Assignment/A2-Assignment-CH1.3/A2_Relative_Error_Bound.py))
  - Machine epsilon computation
  - Floating-point error analysis

- **Numerical Analysis Topics** (detailed in assignment markdown files)
  - Maclaurin and Taylor series expansions
  - Bisection method for root finding
  - Newton's method for computing square and cube roots
  - Polynomial interpolation using divided differences

## 🏗️ Architecture

This is a course assignment repository with a simple, directory-based structure:

```
Scientific_Computation/
├── Assignment/              # All course assignments
│   ├── A1-Assignment-1.2/   # Maclaurin series, Taylor expansion
│   ├── A2-Assignment-CH1.3/ # IEEE-754 and error bounds (with Python code)
│   ├── A3-Assignment-CH3.1/ # Bisection method proofs
│   ├── A4-Assignment-CH3.2/ # Newton's method
│   ├── A5-Assignment-CH3.3/ # (Mathematical proofs)
│   ├── A6-Assignment-Ch4.1/ # Polynomial interpolation
│   ├── A7-Assignment-CH4.3/ # (Advanced topics)
│   └── A8-Assignment-CH5.1/ # (Advanced topics)
├── requirements.txt         # Python dependencies
└── streamlit_app.py        # Streamlit app entry point (references Project_1)
```

**Note**: The `streamlit_app.py` file references a `Project_1` directory that is not currently present in the repository. This may be a work in progress or moved to a separate location.

For detailed architecture information, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jakujobi/Scientific_Computation.git
cd Scientific_Computation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: The current `requirements.txt` specifies conflicting versions. Use compatible versions:
```bash
pip install streamlit matplotlib numpy
```

### Run Examples

**IEEE-754 Converter:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py
```

Expected output:
```
Value: +1.0 (1.0)
 Single Precision (32-bit):
  Binary:   00111111100000000000000000000000
  Hex:      0x3f800000
  Fields:   Sign = 0  Exponent = 127  Fraction = 0
...
```

**Relative Error Bound:**
```bash
python Assignment/A2-Assignment-CH1.3/A2_Relative_Error_Bound.py
```

Expected output:
```
Relative error bound for beta = 10 and n = 4 is 0.000500
```

## 💻 Usage

### Using the IEEE-754 Converter

```python
from Assignment.A2_Assignment_CH1_3.A2_IEEE754Converter import IEEE754Converter

converter = IEEE754Converter()

# Convert to single precision
result = converter.to_single(3.14159)
print(f"Binary: {result['binary_str']}")
print(f"Hex: {result['hex']}")

# Convert to double precision
result = converter.to_double(3.14159)
print(f"Binary: {result['binary_str']}")
```

### Using the Relative Error Bound Calculator

```python
from Assignment.A2_Assignment_CH1_3.A2_Relative_Error_Bound import relative_error_bound

# Calculate machine epsilon for base-10, 4-digit mantissa
bound = relative_error_bound(beta=10, n=4)
print(f"Relative error bound: {bound}")  # 0.0005
```

## 📁 Project Structure

```
Scientific_Computation/
├── Assignment/
│   ├── A1-Assignment-1.2/
│   │   ├── A1-Assignment-1.2.md         # Maclaurin/Taylor series problems
│   │   ├── Figure_1.png                 # Visualization
│   │   └── Figure_2.png                 # Visualization
│   ├── A2-Assignment-CH1.3/
│   │   ├── A2-Assignment-CH1.3.md       # Problem statements and solutions
│   │   ├── A2_IEEE754Converter.py       # IEEE-754 implementation
│   │   ├── A2_Relative_Error_Bound.py   # Error bound calculator
│   │   └── A2_Precision Answers.txt     # Documented results
│   ├── A3-Assignment-CH3.1/
│   │   ├── A3-Assignment-CH3.1.md       # Bisection method proofs
│   │   └── A3-Assignment-CH3.1.pdf      # PDF version
│   ├── A4-Assignment-CH3.2/
│   │   ├── A4-Assignment-CH3.2.md       # Newton's method derivations
│   │   └── A4-Assignment-CH3.2.pdf      # PDF version
│   ├── A5-Assignment-CH3.3/
│   │   ├── A5-Assignment-CH3.3.md       # Mathematical proofs
│   │   └── A5-Assignment-CH3.3.pdf      # PDF version
│   ├── A6-Assignment-Ch4.1/
│   │   ├── A6-Assignment-Ch4.1.md       # Polynomial interpolation (divided differences)
│   │   └── A6-Assignment-Ch4.1.pdf      # PDF version
│   ├── A7-Assignment-CH4.3/
│   │   ├── A7-Assignment-CH4.3.md       # Advanced topics
│   │   └── A7-Assignment-CH4.3.pdf      # PDF version
│   └── A8-Assignment-CH5.1/
│       ├── A8-Assignment-CH5.1.md       # Advanced topics
│       └── A8-Assignment-CH5.1.pdf      # PDF version
├── requirements.txt                      # Python dependencies
├── streamlit_app.py                     # Streamlit entry point
└── MATH 374 - Computational Theory.code-workspace  # VS Code workspace
```

## 📚 Assignments Overview

| Assignment | Chapter | Topics Covered | Implementation |
|------------|---------|----------------|----------------|
| **A1** | 1.2 | Maclaurin series, binomial expansion, Taylor series | Mathematical proofs only |
| **A2** | 1.3 | IEEE-754 floating-point, relative error bounds | ✅ Python implementation |
| **A3** | 3.1 | Bisection method, error analysis | Mathematical proofs only |
| **A4** | 3.2 | Newton's method for roots, convergence analysis | Mathematical derivations only |
| **A5** | 3.3 | Advanced numerical methods | Mathematical proofs only |
| **A6** | 4.1 | Polynomial interpolation, divided differences | Mathematical solutions only |
| **A7** | 4.3 | Advanced interpolation topics | Mathematical solutions only |
| **A8** | 5.1 | Numerical integration/differentiation | Mathematical solutions only |

## 🎯 What This Project Demonstrates

This repository showcases the following technical skills and knowledge areas:

### 1. **Numerical Computing & Floating-Point Arithmetic**
   - Deep understanding of IEEE-754 standard ([A2_IEEE754Converter.py](Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py))
   - Implementation of binary representation for single/double precision
   - Handling of edge cases: subnormals, infinities, NaN
   - Error analysis and machine epsilon calculations

### 2. **Algorithm Implementation**
   - Clean, well-documented Python code with type hints
   - Object-oriented design patterns (IEEE754Converter class)
   - Comprehensive error handling for special values

### 3. **Mathematical Analysis**
   - Series expansions (Maclaurin, Taylor) with convergence analysis ([A1](Assignment/A1-Assignment-1.2/))
   - Root-finding algorithms (Bisection, Newton's method) ([A3](Assignment/A3-Assignment-CH3.1/), [A4](Assignment/A4-Assignment-CH3.2/))
   - Polynomial interpolation using divided differences ([A6](Assignment/A6-Assignment-Ch4.1/))
   - Error bound derivations and convergence proofs

### 4. **Technical Documentation**
   - Clear markdown-based assignment solutions
   - Well-commented code with docstrings
   - Mathematical notation using LaTeX in markdown

### 5. **Software Engineering Practices**
   - Version control with Git
   - Dependency management (requirements.txt)
   - Modular code organization
   - VS Code workspace configuration

## ⚙️ Configuration

### Python Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest compatible | Web app framework |
| `numpy` | Latest compatible | Numerical computing |
| `matplotlib` | Latest compatible | Data visualization |

**Recommended installation:**
```bash
pip install streamlit matplotlib numpy
```

### Environment Variables

No environment variables are required for the current implementation.

## 🧪 Testing

Currently, there are no automated tests in this repository. The Python scripts include example usage in their `if __name__ == '__main__':` blocks that serve as manual tests.

**To verify the implementations:**

1. Run the IEEE-754 converter:
```bash
python Assignment/A2-Assignment-CH1.3/A2_IEEE754Converter.py
```

2. Run the relative error bound calculator:
```bash
python Assignment/A2-Assignment-CH1.3/A2_Relative_Error_Bound.py
```

## 🤝 Contributing

This is a personal course assignment repository. External contributions are not expected, but feedback and suggestions are welcome.

If you'd like to suggest improvements:
1. Open an issue describing the improvement
2. If applicable, reference the specific assignment or file

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📄 License

**Unknown** - No license file is currently present in this repository.

**TODO**: The repository owner should add an appropriate license (e.g., MIT, Apache 2.0, or specify "All Rights Reserved" for coursework).

## 🙏 Acknowledgements

- **Course**: MATH 374 - Computational Theory
- **Author**: John Akujobi ([GitHub](https://github.com/jakujobi/))
- **Institution**: Spring 2025

## 📝 Project Status

**Active Development** - This repository is being actively updated with course assignments.

**Known Issues:**
- `streamlit_app.py` references a `Project_1` directory that is not present in the current repository
- `requirements.txt` contains version conflicts (use compatible versions instead)

**Roadmap:**
- [ ] Add automated tests for numerical methods
- [ ] Implement additional numerical algorithms (pending course progress)
- [ ] Add interactive visualizations for algorithms
- [ ] Complete Project_1 integration (if applicable)

---

**Last Updated**: February 2025
