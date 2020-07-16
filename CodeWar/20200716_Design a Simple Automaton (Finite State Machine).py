# 문제
# Design a Simple Automaton (Finite State Machine)

# 나의 풀이
class Automaton(object):

    def __init__(self):
        self.states = ["q1"]

    def read_commands(self, commands):
        for i in commands:
            if self.states[-1] == 'q1' and i == '1':
                self.states.append("q2")
            elif self.states[-1] == 'q2' and i == '0':
                self.states.append("q3")
            elif self.states[-1] == 'q3':
                self.states.append("q2")
        return True if self.states[-1] == 'q2' else False
my_automaton = Automaton()

# 다른 사람의 풀이
class Automaton1(object):

    def __init__(self):
        self.automata = {('q1', '1'): 'q2', ('q1', '0'): 'q1',
                         ('q2', '0'): 'q3', ('q2', '1'): 'q2',
                         ('q3', '0'): 'q2', ('q3', '1'): 'q2'}
        self.state = "q1"

    def read_commands(self, commands):
        for c in commands:
            self.state = self.automata[(self.state, c)]
        return self.state=="q2"

my_automaton1 = Automaton1()

if __name__ == '__main__':
    print(my_automaton.read_commands(["1"]), True)
    print(my_automaton.read_commands(["1", "0", "0", "1"]), True)