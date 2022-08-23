from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self._email = email

    def notify(self, message):
        print(f'Send "{message}" to {self._email}')


class Sms(Notification):
    def __init__(self, phone):
        self._phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self._phone}')


class Contact:
    def __init__(self, name, email, phone):
        self._name = name
        self._email = email
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    @property
    def notification(self):
        return self._notification

    @notification.setter
    def notification(self, value):
        if not value:
            raise ValueError('The notification cannot be empty')

        self._notification = value

    def send(self, message):
        self._notification.notify(message)


if __name__ == '__main__':
    contact = Contact('Kevin Daniel Guzman Delgadillo', 'kevocde@gmail.com', '+573183995668')

    sms = Sms(contact.phone)
    email = Sms(contact.email)

    manager = NotificationManager(sms)
    manager.send('Hello Kevin, welcome to our family')

    manager.notification = email
    manager.send('Hello Kevin, this is your confirmation email.')


