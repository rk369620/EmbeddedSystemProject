from flask import Flask
try:
    import RPi.GPIO as GPIO
except ImportError:

    from unittest.mock import Mock
    GPIO = Mock()

app = Flask(__name__)
BUZZER_PIN = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

@app.route('/buzzer/<action>')
def buzzer_action(action):

    if action == "activate":
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
    else:
        GPIO.output(BUZZER_PIN, GPIO.LOW)
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
