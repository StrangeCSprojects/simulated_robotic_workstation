
# Simulated Robotic Workstation

This project simulates a robotic workstation capable of detecting tools on a workspace and planning motion to grasp them using inverse kinematics. It includes a command-line interface and a simple Flask dashboard for interactive control and monitoring.

---

## 💡 Features

- Tool detection using OpenCV contour analysis
- 2-link arm simulation with inverse kinematics
- CLI interface for detection and motion control
- Flask web interface for browser-based monitoring
- Event logging to track robot behavior

---

## 🛠 Requirements

- Python 3.8+
- OpenCV
- Flask
- Matplotlib

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Command Line
```bash
python main.py
```

### Flask Web Dashboard
```bash
export FLASK_APP=infrastructure/dashboard.py
flask run
```
Visit: `http://localhost:5000`

---

## 📂 Project Structure

```
robotic_sim/
├── perception/
│   ├── detect_tools.py
│   └── preprocess.py
├── motion_planning/
│   └── plan_motion.py
├── infrastructure/
│   ├── dashboard.py
│   └── logger.py
├── templates/
│   ├── index.html
│   └── logs.html
├── tools/
│   └── sample_workspace.jpg
├── main.py
├── requirements.txt
└── README.md
```

---

## 📋 Logs

All actions are logged in `robot_log.txt`, including:
- Tool detection coordinates
- Movement plan results
- Errors or unreachable targets

---

## 🧠 Author Notes

This project was developed to simulate the core functionality of a workstation similar to those built at Altitude AI, focusing on perception, motion planning, and system interaction.
