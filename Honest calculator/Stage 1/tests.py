from hstest import *

msg = ["Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?"]

data = [
            (("2 + 1.1", ""), ),
            (("2 + m", "\n".join([msg[1], msg[0]])), ("3 + 3", "")),
            (("2 + m", "\n".join([msg[1], msg[0]])), ("3 n 3", "\n".join([msg[2], msg[0]])),
             ("m - 2", "\n".join([msg[1], msg[0]])), ("4 * 5.2", "")),

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
                return CheckResult.wrong(f"Expected: ({item[1]});\nFound:    ({output.strip()})")
        if not pr.is_finished():
            return CheckResult.wrong("Your program unnecessarily waiting for input.")
        return CheckResult.correct()


if __name__ == '__main__':
    FoodBlogStage1().run_tests()
