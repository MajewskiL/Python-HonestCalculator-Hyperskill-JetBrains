from hstest import *

msg = ["Enter the equation",
       "Do you know what the numbers are? Focus!",
       "Yes ... an interesting math operation. Did you sleep in class?",
       "Yeah... division by zero. Smart move...",
       "Do you want to remember the result (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly, it's just one number! Add to memory? (y / n)",
       "Last chance! Do you want to be ashamed for the rest of your days? (y / n)"
]


def add_enter(txt):
    return "\n".join([txt, msg[0]])


def add_memory(txt):
    return "\n".join([txt, msg[4]])


data = [(("4 * 5", "\n".join([msg[9] + msg[6], add_memory("20.0")])), ("y", msg[5]), ("n", "")),
        (("225 / 15", add_memory("15.0")), ("y", msg[5]), ("y",msg[0]),
         ("1 * 5", "\n".join([msg[9] + msg[6] + msg[7], add_memory("5.0")])), ("y", msg[10]), ("y", msg[11]), ("n", msg[5]), ("y", msg[0]),
        ("M - 10", add_memory("5.0")), ("y", msg[10]), ("y", msg[11]), ("y", msg[12]), ("y", msg[5]), ("y", msg[0]),
         ("M / M",  "\n".join([msg[9] + msg[6], add_memory("1.0")])), ("n", msg[5]), ("n", "")),
       ]  # (input data, msg sentence])


class FoodBlogStage1(StageTest):
    @dynamic_test(data=data)
    def test(self, *items):
        pr = TestedProgram()
        output = pr.start()
        if msg[0] not in output:
            return CheckResult.wrong(f"Expected: ({msg[0]});\nFound:    ({output.strip()})")
        for item in items:
            output = pr.execute(item[0])
            if item[1] != output.strip():
                return CheckResult.wrong(f"Expected:\n{item[1]}\nFound:\n{output.strip()}")
        if not pr.is_finished():
            return CheckResult.wrong("Your program unnecessarily waiting for input.")
        return CheckResult.correct()


if __name__ == '__main__':
    FoodBlogStage1().run_tests()
