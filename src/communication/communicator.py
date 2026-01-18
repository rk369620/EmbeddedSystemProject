import requests

class Communicator:
    def __init__(self, pi_ip):
        self.pi_ip = pi_ip

    def send_alert(self, action="activate"):

        url = f"http://{self.pi_ip}/buzzer/{action}"
        try:
            response = requests.get(url, timeout=2)
            return response.status_code == 200
        except requests.RequestException:
            return False
