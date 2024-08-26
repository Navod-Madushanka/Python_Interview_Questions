class Observer:
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received message: {message}')


# Example usage
if __name__ == "__main__":
    subject = Subject()

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    subject.add_observer(observer1)
    subject.add_observer(observer2)

    subject.notify_observers("This is a notification.")
    # Output:
    # Observer 1 received message: This is a notification.
    # Observer 2 received message: This is a notification.

    subject.remove_observer(observer1)
    subject.notify_observers("Another notification.")
    # Output:
    # Observer 2 received message: Another notification.
