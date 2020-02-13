class Human:
    def __init__(self,name):
        print('Human object creation...')
        self.name=name
        self.head=self.Head()
    class Head:
        def __init__(self):
            print('Head object creation...')
            self.brain=self.Brain()
        class Brain:
            def __init__(self):
                print('Brain object creation....')


human=Human('Surender')

