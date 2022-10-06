import keyboard
import pygsheets


class Listener():
    client = pygsheets.authorize(service_account_file="service-account-credentials.json")
    sh = None

    def __init__(self, title, attempt):
        self.attempt = attempt
        self.sh = self.client.open(title).sheet1

    def recordHits(self, hits):
        print(hits)
        self.sh.update_value('A'+str(self.attempt), hits)
        self.attempt+=1

if __name__ == '__main__':
    docName = 'Progress Bars'
    startingCell = 3
    l = Listener(docName, startingCell)

    keyboard.add_hotkey('ctrl+0', lambda: l.recordHits(0))
    keyboard.add_hotkey('ctrl+1', lambda: l.recordHits(1))
    keyboard.add_hotkey('ctrl+2', lambda: l.recordHits(2))
    keyboard.add_hotkey('ctrl+3', lambda: l.recordHits(3))
    keyboard.add_hotkey('ctrl+4', lambda: l.recordHits(4))
    keyboard.add_hotkey('ctrl+5', lambda: l.recordHits(5))
    keyboard.add_hotkey('ctrl+6', lambda: l.recordHits(6))
    keyboard.add_hotkey('ctrl+7', lambda: l.recordHits(7))

    keyboard.wait()
