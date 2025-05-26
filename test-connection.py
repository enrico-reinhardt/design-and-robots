import socket
import time

# UR5 robot IP and port
UR5_IP = "192.168.8.24"  # Change this to your robot's IP
PORT = 30002             # Secondary client interface (real-time)

def connect_to_ur5(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("Connected to UR5")
        return s
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def send_urscript(sock, script):
    try:
        sock.sendall(script.encode('utf-8'))
        print("URScript sent")
    except Exception as e:
        print(f"Sending failed: {e}")

def main():
    sock = connect_to_ur5(UR5_IP, PORT)
    if not sock:
        return

    # Example: Move to a point (joint angles in radians)
    move_cmd = "movej([0, -1.57, 1.57, 0, 1.57, 0], a=1.2, v=0.25)\n"

    send_urscript(sock, move_cmd)

    time.sleep(2)  # Wait for move to finish (adjust as needed)
    sock.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
