import subprocess
import sys
import os

def run_tests():
    """Run all test cases with HTML report and output results to the terminal."""
    os.makedirs("logs", exist_ok=True)
    result = subprocess.run([
        'python', '-m', 'pytest', 'tests/', '-v', '--html=logs/report.html'
    ])
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_tests()
