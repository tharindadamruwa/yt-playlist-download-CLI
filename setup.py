import os
import subprocess
import sys

# Function to run system commands like apt update and apt upgrade
def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(stdout.decode())
        else:
            print(f"Error: {stderr.decode()}")
    except Exception as e:
        print(f"Failed to execute command: {str(e)}")

# Function to install required Python packages from requirements.txt
def install_python_requirements():
    try:
        print("Installing Python dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Python dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Python dependencies: {e}")

# Function to update and upgrade the system
def update_system():
    print("Updating system...")
    run_command("sudo apt update -y")
    run_command("sudo apt upgrade -y")

# Function to install necessary system packages (like ffmpeg)
def install_system_dependencies():
    print("Installing system dependencies (e.g., ffmpeg)...")
    run_command("sudo apt install -y ffmpeg")

# Main function to set up everything
def main():
    # Step 1: Update and upgrade the system
    update_system()

    # Step 2: Install system dependencies like ffmpeg
    install_system_dependencies()

    # Step 3: Install Python dependencies from requirements.txt
    install_python_requirements()

    print("Setup completed successfully.")

if __name__ == "__main__":
    main()