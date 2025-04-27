from collections import defaultdict
from typing import Type, Callable

class EventDispatcher:
    
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type: Type, handler: Callable):
        self._subscribers[event_type].append(handler)

    def publish(self, event):
        event_type = type(event)
        if event_type in self._subscribers:
            for handler in self._subscribers[event_type]:
                handler(event)


dispatcher = EventDispatcher()
