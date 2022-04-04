class Logger:
    _instance = None
    _messages = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log_save(self):
        with open(f'logs.txt', 'a+') as fp:
            for message in self._messages:
                fp.write(f'{str(message)}\n')
            fp.write(f'---END OF EXECUTION!---\n')

    def log_message(self, data: dict):
        self._messages.append(data)

logger = Logger()
