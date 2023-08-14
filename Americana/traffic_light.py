import time


class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change_state(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"

    def display_state(self):
        print(f"Traffic light is {self.state}")


def simulate_traffic_light():
    traffic_light = TrafficLight()

    while True:
        traffic_light.display_state()
        time.sleep(2)

        traffic_light.change_state()
        time.sleep(1)


if __name__ == "__main__":
    simulate_traffic_light()
