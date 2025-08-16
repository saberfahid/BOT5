import threading

class BotManager:
    def __init__(self):
        self.bots = {}

    def register_bot(self, name, handler):
        self.bots[name] = handler

    def run_all(self, user_message):
        threads = []
        for name, handler in self.bots.items():
            t = threading.Thread(target=self._run_bot, args=(name, handler, user_message))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    def _run_bot(self, name, handler, user_message):
        print(f"\n{name} Bot:")
        print(handler(user_message))
