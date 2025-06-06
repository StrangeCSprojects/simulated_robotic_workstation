import cv2
from perception.preprocess import preprocess_image
from perception.detect_tools import detect_tools
from motion_planning.plan_motion import compute_ik, plot_arm
from infrastructure.logger import log_event

def run_detection(image_path="tools/tools_list.png"):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return []

    preprocessed = preprocess_image(image)
    tools = detect_tools(preprocessed)

    # Show detection result
    for (x, y, w, h) in tools:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Detected Tools", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for (x, y, w, h) in tools:
        center_x = x + w // 2
        center_y = y + h // 2
        log_event("TOOL_DETECTED", {"center": (center_x, center_y)})

    return tools

def move_to_tool(x, y):
    result = compute_ik(x, y)
    if result:
        angle1, angle2 = result
        log_event("MOTION_PLAN_SUCCESS", {"target": (x, y), "angles": [angle1, angle2]})
        plot_arm(angle1, angle2)
    else:
        log_event("MOTION_PLAN_FAILED", {"target": (x, y)})
        print("Target is unreachable.")

def main():
    tools = []
    print("Welcome to the Robotic Workstation CLI")
    while True:
        command = input("\nCommands: detect, move, logs, exit\n> ").strip().lower()
        if command == "detect":
            tools = run_detection()
        elif command == "move":
            if not tools:
                print("No tools detected. Run 'detect' first.")
                continue
            for i, (x, y, w, h) in enumerate(tools):
                print(f"[{i}] Tool at ({x + w//2}, {y + h//2})")
            index = input("Enter tool number to move to: ").strip()
            if index.isdigit() and 0 <= int(index) < len(tools):
                (x, y, w, h) = tools[int(index)]
                center_x = x + w // 2
                center_y = y + h // 2
                move_to_tool(center_x, center_y)
            else:
                print("Invalid tool index.")
        elif command == "logs":
            with open("robot_log.txt", "r") as f:
                print(f.read())
        elif command == "exit":
            print("Exiting CLI.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
