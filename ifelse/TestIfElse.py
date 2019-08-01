class Hello:
    color = 'Purple'

    def traffic_signal(self, color):
        self.color = color
        if color == 'red':
            return 'Stop'
        elif color == 'green':
            return 'Go'
        elif color == 'yellow':
            return 'ready to go'


h1 = Hello()
signal = h1.traffic_signal('green')
print(h1.color+' #{}'.format(signal))

