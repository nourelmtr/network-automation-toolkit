# Network Automation Toolkit

A Python-based network automation toolkit designed to simplify network administration tasks through automation.

The project provides a unified solution for inventory management, network monitoring, SSH automation, configuration backups, reporting, REST API services, and a modern web dashboard.

---

## Overview

Network Automation Toolkit automates repetitive network administration tasks and provides an intuitive dashboard for monitoring network devices.

The application includes:

- Network inventory management
- ICMP reachability testing
- SSH device management
- Configuration backup automation
- CSV report generation
- REST API with FastAPI
- Interactive web dashboard
- Logging
- Command-line interface
- Automated testing

---

## Features

- Load device inventory from YAML
- Ping network devices
- Connect to Cisco devices via SSH
- Backup running configurations
- Generate CSV reports
- REST API built with FastAPI
- Interactive dashboard
- Real-time statistics
- Device latency visualization
- Application logging
- Command-line interface
- Unit testing with pytest

---

## Architecture

*Architecture diagram will be added.*

![Architecture](assets/architecture.png)

---

## Project Structure

```text
network-automation-toolkit/
│
├── api/
├── assets/
├── backup/
├── cli/
├── configuration/
├── frontend/
├── inventory/
├── logs/
├── ping/
├── reports/
├── services/
├── ssh/
├── tests/
├── utils/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Python | Core application |
| FastAPI | REST API |
| HTML | Dashboard |
| CSS | User interface |
| JavaScript | Frontend logic |
| Chart.js | Data visualization |
| Paramiko | SSH communication |
| Netmiko | Cisco device automation |
| PyYAML | Inventory parsing |
| pytest | Unit testing |
| Git | Version control |

---

## Installation

Clone the repository

```bash
git clone https://github.com/nourelmtr/network-automation-toolkit.git
```

Move into the project

```bash
cd network-automation-toolkit
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the complete workflow

```bash
python main.py --all
```

Ping devices

```bash
python main.py --ping
```

Create configuration backups

```bash
python main.py --backup
```

Generate reports

```bash
python main.py --report
```

---

## REST API

Start the API server

```bash
uvicorn api.app:app --reload
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

Available endpoint

```
GET /devices
```

Example response

```json
[
  {
    "name": "Router1",
    "ip": "192.168.1.1",
    "device_type": "cisco_ios",
    "reachable": true,
    "latency": "5 ms"
  }
]
```

---

## Dashboard

Open

```
frontend/index.html
```

The dashboard provides:

- Network overview
- Online and offline device statistics
- Average latency
- Interactive charts
- Device table
- Live data from the REST API

---

## Testing

Run all tests

```bash
pytest
```

Example output

```text
=========================
3 passed
=========================
```

---

## Roadmap

- [x] Inventory Management
- [x] Network Reachability Testing
- [x] SSH Automation
- [x] Configuration Backup
- [x] CSV Reporting
- [x] Logging
- [x] REST API
- [x] Interactive Dashboard
- [x] Charts
- [x] Unit Testing
- [ ] PDF Report Export
- [ ] Configuration Difference Viewer
- [ ] Network Topology Visualization
- [ ] Authentication
- [ ] Multi-vendor Device Support

---

## License

This project is licensed under the MIT License.

---

## Author

**Nour El Houda Mastour**

Cybersecurity and Network Engineering Student

GitHub: https://github.com/nourelmtr