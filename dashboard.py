from flask import Flask, render_template, request, redirect, url_for, jsonify
import cv2
import os
from simulated_robotic_workstation.perception.preprocess import preprocess_image
from simulated_robotic_workstation.perception.detect_tools import detect_tools
from simulated_robotic_workstation.motion_planning.plan_motion import compute_ik, plot_arm
from simulated_robotic_workstation.infrastructure.logger import log_event

app = Flask(__name__)
IMAGE_PATH = "tools/tools_list.png"
DETECTED_TOOLS = []

@app.route("/")
def index():
    return render_template("index.html", tools=DETECTED_TOOLS)

@app.route("/detect")
def detect():
    global DETECTED_TOOLS
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        return "Image not found.", 404

    preprocessed = preprocess_image(image)
    DETECTED_TOOLS = detect_tools(preprocessed)

    # Log and send detection results
    for (x, y, w, h) in DETECTED_TOOLS:
        center_x = x + w // 2
        center_y = y + h // 2
        log_event("TOOL_DETECTED", {"center": (center_x, center_y)})

    return redirect(url_for('index'))

@app.route("/move/<int:index>")
def move(index):
    if 0 <= index < len(DETECTED_TOOLS):
        (x, y, w, h) = DETECTED_TOOLS[index]
        center_x = x + w // 2
        center_y = y + h // 2
        result = compute_ik(center_x, center_y)

        if result:
            angle1, angle2 = result
            log_event("MOTION_PLAN_SUCCESS", {"target": (center_x, center_y), "angles": [angle1, angle2]})
            plot_arm(angle1, angle2)
            return redirect(url_for("index"))
        else:
            log_event("MOTION_PLAN_FAILED", {"target": (center_x, center_y)})
            return "Target unreachable", 400
    return "Invalid tool index", 400

@app.route("/logs")
def logs():
    if os.path.exists("robot_log.txt"):
        with open("robot_log.txt", "r") as f:
            log_data = f.readlines()
        return render_template("logs.html", logs=log_data)
    return "No logs found.", 404

if __name__ == "__main__":
    app.run(debug=True)
