from interruptingcow import timeout
from os.path import join as path_join

class LinuxShell:
    def __init__(self, user, timeout = None):
        self.user = user
        self.pwd = ""
        self.stdout_timeout = timeout or 10
        self.machine = f"{self.user}@machine:/home/{self.user}# "
        self.configure()

    def stdin(self):
        return input(self.machine)

    def stdout(self):
        return None

    def configure(self):
        runtime_error = False
        type_error = False

        try:
            with timeout(self.stdout_timeout, exception=RuntimeError):
                self.pwd = self.stdout("pwd")
                self.refresh(self.pwd)
        except RuntimeError:
            runtime_error = True
        except TypeError:
            type_error = True
            raise TypeError("Standard output function is not configured")
        if not self.pwd:
            if self.user == "root":
                self.pwd = "/root"
                self.refresh(self.pwd)
            elif not runtime_error and not type_error:
                self.pwd = f"/home/{self.user}"
                self.refresh(self.pwd)
        if not self.user:
            self.user = "www-data"

    def refresh(self, pwd):
        self.machine = f"{self.user}@machine:{pwd}# "

    def interact(self):
        while True:
            user_input = self.stdin().strip(' ')
            if user_input.startswith('cd '):
                temporary = user_input.split('cd ')[-1].strip(' ')
                if '/' in temporary and temporary.startswith('/'):
                    self.pwd = temporary
                else:
                    self.pwd = path_join(self.pwd, temporary)
                self.refresh(self.pwd)
            elif user_input == 'pwd':
                self.refresh(self.pwd)
            try:
                with timeout(self.stdout_timeout, exception=RuntimeError):
                    data = self.stdout(user_input)
                    if data:
                        print(data)
            except RuntimeError:
                print(f"machine: {user_input}: command not found")
