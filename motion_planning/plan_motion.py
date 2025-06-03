import math
import matplotlib.pyplot as plt

def compute_ik(x, y, L1=100, L2=100):
    """
    Compute joint angles for a 2-link arm to reach (x, y).

    Args:
        x (float): Target x-coordinate
        y (float): Target y-coordinate
        L1 (float): Length of the first segment
        L2 (float): Length of the second segment

    Returns:
        tuple: (shoulder_angle_rad, elbow_angle_rad) or None if unreachable
    """
    dist = math.hypot(x, y)
    
    # Check reachability
    if dist > (L1 + L2) or dist < abs(L1 - L2):
        return None

    # Law of Cosines for elbow angle
    cos_angle2 = (dist**2 - L1**2 - L2**2) / (2 * L1 * L2)
    angle2 = math.acos(cos_angle2)

    # Law of Cosines for shoulder angle
    k1 = L1 + L2 * math.cos(angle2)
    k2 = L2 * math.sin(angle2)
    angle1 = math.atan2(y, x) - math.atan2(k2, k1)

    return angle1, angle2

def plot_arm(angle1, angle2, L1=100, L2=100):
    """
    Plot the 2-link arm based on joint angles.
    """
    x0, y0 = 0, 0
    x1 = L1 * math.cos(angle1)
    y1 = L1 * math.sin(angle1)
    x2 = x1 + L2 * math.cos(angle1 + angle2)
    y2 = y1 + L2 * math.sin(angle1 + angle2)

    plt.plot([x0, x1], [y0, y1], linewidth=4, label='Link 1')
    plt.plot([x1, x2], [y1, y2], linewidth=4, label='Link 2')
    plt.scatter([x0, x1, x2], [y0, y1, y2], color='red')
    plt.xlim(-L1-L2, L1+L2)
    plt.ylim(-L1-L2, L1+L2)
    plt.gca().set_aspect('equal')
    plt.title("2-Link Arm IK Simulation")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
if __name__ == "__main__":
    target_x = 120
    target_y = 50

    result = compute_ik(target_x, target_y)
    if result:
        angle1, angle2 = result
        plot_arm(angle1, angle2)
    else:
        print("Target is unreachable.")
