from anticaptchaofficial.antinetworking import *
from anticaptchaofficial.imagecaptcha import *
import os
from dotenv import load_dotenv

_ = load_dotenv()


def solve_and_return_solution(body, solver):
    task_data = {
        "type": "ImageToTextTask",
        "body": body,
        "numeric": 1,
    }

    if solver.create_task({
        "clientKey": solver.client_key,
        "task": task_data,
        "softId": solver.soft_id
    }) == 1:
        solver.log("created task with id "+str(solver.task_id))
    else:
        solver.log("could not create task")
        solver.log(solver.err_string)
        return 0

    task_result = solver.wait_for_result(60)
    if task_result == 0:
        return 0
    else:
        return task_result["solution"]["text"]


class AnticaptchaApi:
    def __init__(self, body):
        self.body = body

    def solve(self):
        solver = antiNetworking()
        solver.set_verbose(1)
        solver.set_key(os.environ.get("ANTICAPTCHA_KEY"))

        captcha_text = solve_and_return_solution(self.body, solver)
        if captcha_text != 0:
            return captcha_text
        else:
            print("task finished with error " + solver.error_code)
            return 0
