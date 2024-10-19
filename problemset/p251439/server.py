import threading
from operator import index
from typing import Callable, Dict, List
import pickle


class OlympicsServer:
    def __init__(self):
        self.lock = threading.Lock()
        # implement the rest of the method
        self.subscribers: Dict[str, List[Callable]] = {}
        self.unsent_messages = []

    def _match_topic(self, subscribed_topic: str, published_topic: str, qos: int = 0) -> bool:
        sub_parts = subscribed_topic.split('/')
        pub_parts = published_topic.split('/')

        if len(sub_parts) < len(pub_parts):
            for _ in range(len(pub_parts) - len(sub_parts)):
                sub_parts.append('')
        elif len(sub_parts) > len(pub_parts):
            for _ in range(len(sub_parts) - len(pub_parts)):
                pub_parts.append('')

        for i in range(len(sub_parts)):
            if sub_parts[i] == pub_parts[i]:
                pass
            elif sub_parts[i] == '#':
                break
            elif (sub_parts[i] == '+') and (len(sub_parts) == i + 1):
                break
            else:
                return False
        return True

    def publish(self, topic: str, message: str, qos: int):
        with self.lock:
            for sub_topic, callbacks in self.subscribers.items():
                if self._match_topic(sub_topic, topic):
                    qos -= 1
                    for callback in callbacks:
                        callback(topic, message)
            if qos > 0:
                self.unsent_messages.append((topic, message, qos))
                try:
                    with open('messages.pkl', 'rb') as file:
                        current_list = pickle.load(file)
                except:
                    current_list = []
                with open('messages.pkl', 'wb') as file:
                    current_list.append((topic, message))
                    pickle.dump(current_list, file)

    def subscribe(self, topic: str, callback: Callable):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []
            self.subscribers[topic].append(callback)

            for m_topic, m_message, m_qos in self.unsent_messages:
                if self._match_topic(topic, m_topic, m_qos):
                    self.unsent_messages.pop(self.unsent_messages.index((m_topic, m_message, m_qos)))
                    if m_qos > 1:
                        self.unsent_messages.append((m_topic, m_message, m_qos-1))
