from typing import Callable
from server import OlympicsServer


class Publisher:
    def __init__(self, server: OlympicsServer):
        self.server = server

    def publish(self, topic: str, message: str, qos: int):
        self.server.publish(topic, message, qos)


class Subscriber:
    def __init__(self, server: OlympicsServer, callback: Callable):
        self.server = server
        self.callback = callback

    def subscribe(self, topic: str):
        self.server.subscribe(topic, self.callback)


class Client:
    def __init__(self, server: OlympicsServer):
        self.server = server

    def publish(self, topic: str, message: str, qos: int):
        publisher = Publisher(self.server)
        publisher.publish(topic, message, qos)

    def subscribe(self, topic: str, callback: Callable):
        subscriber = Subscriber(self.server, callback)
        subscriber.subscribe(topic)
