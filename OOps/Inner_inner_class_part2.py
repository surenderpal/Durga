class Human:
    def __init__(self,name):
        print('Human object creation....')
        # self.name=name
        self.head=self.Head()
    # def info(self):
    #     print('Hello, Myself:',self.name)
    #     print("I'm full busy with...")
    #     self.head.talk()
    #     self.head.brain.think()
    class Head:
        def __init__(self):
            print('Head object creation....')
            self.brain=self.Brain()
        # def talk(self):
        #     print('Talking...')
        class Brain:
            def __init__(self):
                print('Brain object creation...')
            # def think(self):
            #     print('thinking....')

human=Human('surender')
# human.info()
  