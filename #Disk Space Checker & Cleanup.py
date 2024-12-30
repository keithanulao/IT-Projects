#Disk Space Checker & Cleanup (Bash Translation)

import os
import subprocess

def check_disk_space(threshold=10):
  """Checks disk space usage and sends a notification if below the threshold."""
  try:
    output = subprocess.check_output(['df', '-h']).decode('utf-8')
    lines = output.split('\n')
    for line in lines:
      if '/dev/sda1' in line:  # Adjust this to match your root partition
        parts = line.split()
        usage = float(parts[4].strip('%'))
        if usage < threshold:
          print(f"WARNING: Low disk space detected! Only {usage}% free.")
          # Uncomment and install `libnotify-bin` for notifications
          # subprocess.run(['notify-send', 'Low Disk Space Warning', f'Only {usage}% disk space free.']) 
  except Exception as e:
    print(f"Error checking disk space: {e}")

def clean_temp_files():
  """Cleans up temporary files from the user's temp directory."""
  try:
    temp_dir = os.getenv('TEMP') 
    for filename in os.listdir(temp_dir):
      file_path = os.path.join(temp_dir, filename)
      try:
        if os.path.isfile(file_path):
          os.remove(file_path)
          print(f"Removed: {file_path}")
      except Exception as e:
        print(f"Error removing file: {file_path}, {e}") 

    print("Temporary files in user's temp directory cleaned.")
  except Exception as e:
    print(f"Error cleaning temporary files: {e}")

if __name__ == "__main__":
  check_disk_space()
  clean_temp_files()
  check_disk_space()