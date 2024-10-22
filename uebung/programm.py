
class InstanceChecker:
    def __init__(self,instanceId,notifier,thresholds):
        self.__instanceId = instanceId  # Attribute
        self.__notifier = notifier  # Attribute __ to make it private outside of described methods
        self.__tests = []
        for test, thresholds in thresholds.items():
            if test == "cpu":
                self.__tests.append(CpuTest(thresholds, self.__instanceId))
            elif test == "memory":
                self.__tests.append(MemoryTest(thresholds, self.__instanceId))
            else:
                print("test %s noch nicht implementiert" % test)

    def check_and_notify(self):
        for test in self.__tests:
            if not test.check():
                self.__notifier.notify(f"Der Test {test.name} hat für instansz {self.__instanceId} fehlgeschlagen",
                                        f"Achtung Administrator es gibt ein Problem bei.....")


class Notifier:
    def notify(self,subject,message):
        pass

class EmailNotifier:
    def __init__(self,emailAddress):
        self.__emailAddress = emailAddress # Attribute

    def notify(self,subject,message):
        print(f"Hier wurde ein Email an {self.__emailAddress} versendet.")
        print(f"Das Subject wäre: {subject}")
        print(f"Der Inhalt wäre: {message}")

class SmSNotifier:
    def __init__(self,phonenumber):
        self.__phonenumber = phonenumber # Attribute

    def notify(self,subject,message):
        print(f"Hier wurde ein SMS an {self.__phonenumber} versendet.")
        print(f"Das Subject wäre: {subject}")
        print(f"Der Inhalt wäre: {message}")

class MultiNotifier:
    def __init__(self,listOfNotifier):
        self.__listOfNotifier = listOfNotifier # Attribute

    def notify(self,subject,message):
        print(f"Hier wurde ein Email an {self.__listOfNotifier} versendet.")
        print(f"Das Subject wäre: {subject}")
        print(f"Der Inhalt wäre: {message}")

class CpuTest:
    name = "CpuTest"
    def __init__(self,thresholds,instanceId):
        self.__thresholds = thresholds # Attribute
        self.__instanceId = instanceId

    def check(self):
        return True

class MemoryTest:
    name = "MemoryTest"
    def __init__(self,thresholds,instanceId):
        self.__thresholds = thresholds # Attribute
        self.__instanceId = instanceId

    def check(self):
        return False

if __name__ == '__main__':
    # Main Code kommt hier
    smsNotifier = SmSNotifier('0793557824')
    emailNotifier = EmailNotifier('laura.dubach@edu.tbz.ch')
    multinoti_swisscom = MultiNotifier([smsNotifier, emailNotifier])

    instanzes = [
        InstanceChecker(
            instanceId='i-1235134123',
            notifier=smsNotifier,
            thresholds={'cpu': [0, 60], 'memory': [0, 90]}),
        InstanceChecker(
            instanceId='i-1235134542',
            notifier=emailNotifier,
            thresholds={'cpu': [0, 50], 'memory': [0, 95]}
        ),
        InstanceChecker(
            instanceId='i-3435134123',
            notifier=multinoti_swisscom,
            thresholds={'cpu': [0, 100], 'memory': [10, 60]})
    ]

    for instanz in instanzes:
        instanz.check_and_notify()
