import subprocess
import sys

def test_area_of_circle():
    result = subprocess.check_output(
        [sys.executable, "circle.py", "7"],
        text=True
    )
    assert "153.86" in result

if __name__ == "__main__":
    test_area_of_circle()
