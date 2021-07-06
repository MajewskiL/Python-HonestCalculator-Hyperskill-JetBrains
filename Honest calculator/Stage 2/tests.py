from hstest import *

msg = ["Enter the equation",
       "Do you know what the numbers are? Focus!",
       "Yes ... an interesting math operation. Did you sleep in class?",
       "Yeah... division by zero. Smart move..."]

data = [
            (("2 + 1", "3.0"), ),
            (("2 + m", "\n".join([msg[1], msg[0]])), ("3 + 3", "6.0")),
            (("2 + m", "\n".join([msg[1], msg[0]])), ("3 n 3", "\n".join([msg[2], msg[0]])),
             ("m - 2", "\n".join([msg[1], msg[0]])), ("4 * 5", "20.0"),),
            (("2 + m", "\n".join([msg[1], msg[0]])), ("3 n 3", "\n".join([msg[2], msg[0]])),
             ("4 / 0", "\n".join([msg[3], msg[0]])), ("4 * 5.2", "20.8"),),
            (("2.0 + 1", "3.0"), ),
            (("411 - 211", "200.0"), ),

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
            if item[1] not in output:
                return CheckResult.wrong(f"Expected: ({item[1]});\nFound:    ({output.strip()})")
        if not pr.is_finished():
            return CheckResult.wrong("Your program unnecessarily waiting for input.")

        return CheckResult.correct()


if __name__ == '__main__':
    FoodBlogStage1().run_tests()
