from interruptingcow import timeout

class Shell:
    def __init__(self, user, timeout = None):
        self.user = user
        self.stdout_timeout = timeout or 10
        self.machine = f"{self.user}@machine:/home/{self.user}# "

    def stdin(self):
        return input(self.machine)

    def stdout(self):
        pass

    def shell(self):
        while True:
            user_input = self.stdin()
            try:
                with timeout(self.stdout_timeout, exception=RuntimeError):
                    data = self.stdout(user_input)
                    if data:
                        print(data)
            except RuntimeError:
                print(f"machine: {user_input}: command not found")
