from hstest import *

msg = ["Enter the equation",
       "Do you know what the numbers are? Focus!",
       "Yes ... an interesting math operation. Did you sleep in class?"]

data = [
            ["2 + 1", ((0, 1), ), ()],
            ["2 + m\n3 + 3", ((0, 2), (1, 1), ), ()],
            ["2 + m\n3 n 3\nm - 2\n4.7 * 5.2", ((0, 4), (1, 2), (2, 1),), ()],
            ]  # [input data, (msg sentence, number of messages), (scores)]


class FoodBlogStage1(StageTest):
    @dynamic_test(data=data)
    def test(self, arguments, answers, scores):
        pr = TestedProgram()
        output = pr.start()
        output += pr.execute(arguments)
        for answer in answers:
            if output.count(msg[answer[0]]) != answer[1]:
                return CheckResult.wrong(f"Expect the sentence '{msg[answer[0]]}' {answer[1]} {'times' if answer[1] != 1 else 'time'} "
                                         f"found {output.count(msg[answer[0]])}")

        if not pr.is_finished():
            return CheckResult.wrong("Your program unnecessarily waiting for input.")

        return CheckResult.correct()


if __name__ == '__main__':
    FoodBlogStage1().run_tests()
