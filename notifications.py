import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "HYDRATE!",
            message = "It has been an hour. Drink water!",
            timeout = 10
        )
        time.sleep(3600)