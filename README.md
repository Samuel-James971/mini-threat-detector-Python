# Mini Threat Detection Tool

## Overview
The Mini Threat Detection Tool is a Python-based program designed to monitor a folder for file changes and simulate network monitoring in safe test mode. It allows users to learn about file monitoring, alert logging, and network simulation on a personal machine in a secure and controlled environment. This tool is ideal for demonstrating basic cybersecurity monitoring techniques without impacting real systems.

---

## Features
This tool monitors file creation, modification, and deletion in a designated folder (`watched/`) and logs all alerts in both the console and a structured log file (`data/alerts.jsonl`). Additionally, it simulates network monitoring in safe test mode, generating example network alerts. The project is lightweight, Windows-compatible, and can be run safely on a personal machine.

---

## Installation
To install the Mini Threat Detection Tool, first clone the repository using `git clone https://github.com/YOUR_USERNAME/mini-threat-detector-python.git` and navigate into the project folder. Then, create a Python virtual environment by running `python -m venv .venv` and activate it with `.venv\Scripts\activate`. Once the virtual environment is active, upgrade pip and install the required dependencies using `pip install --upgrade pip` followed by `pip install -r requirements.txt`. The project is now ready to run.

---

## Running the Project
To run the tool, execute `python main.py` from the project folder with the virtual environment activated. While the program is running, you can test the file monitoring feature by adding, modifying, or deleting files in the `watched/` folder; alerts will appear in the console and be saved to `data/alerts.jsonl`. The network monitor runs in safe test mode, displaying simulated network alerts in the console, allowing safe observation of network monitoring behavior without affecting real network traffic. Press `Ctrl+C` to stop monitoring safely at any time.

---

## Example Screenshots

### File Created Alert
![image alt](https://github.com/Samuel-James971/mini-threat-detector-Python/blob/main/Screenshot%202025-08-26%20125449.png?raw=true)
*This screenshot shows the console alert generated when a new file is added to the `watched/` folder.*

### File Modified Alert
![image alt](https://github.com/Samuel-James971/Cloud-Home-Lab/blob/main/1.png?raw=true)
*This screenshot shows the console alert generated when an existing file in the `watched/` folder is modified.*

### File Deleted Alert
![image alt](https://github.com/Samuel-James971/mini-threat-detector-Python/blob/main/Screenshot%202025-08-26%20125006.png?raw=true)
*This screenshot shows the console alert generated when a file is deleted from the `watched/` folder.*

### Network Monitor Alert
![image alt](https://github.com/Samuel-James971/Cloud-Home-Lab/blob/main/1.png?raw=true)
*This screenshot shows the network monitor running in safe test mode, simulating network alerts without affecting real network traffic.*
