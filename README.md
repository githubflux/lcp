# ASTRID Local Control Plane

In each local agent, the control plane is responsible for programmability, i.e., changing the behaviour of the data plane at run-time.

---

- [ASTRID Local Control Plane](#astrid-local-control-plane)
- [Installation](#installation)
- [Usage](#usage)
  - [Display help](#display-help)
  - [Production environment](#production-environment)
  - [Debug enabled in Development environment](#debug-enabled-in-development-environment)
- [Extra](#extra)

---

# Installation

1. Prerequisite

- python3
- pip3

2. Clone the repository.

```bash
git clone https://gitlab.com/astrid-repositories/wp2/astrid-local-control-plane.git
cd astrid-local-control-plane
```

3. Install the dependencies.

```bash
pip3 install -r requirements.txt
```

# Usage

## Display help

```bash
python3 main.py -h
```

## Production environment

```bash
python3 main.py -n production
```

## Debug enabled in Development environment

```bash
python3 main.py --debug -n development
```

# Extra

See the **Issues** for *features* in development.
