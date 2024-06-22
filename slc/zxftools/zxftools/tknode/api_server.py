from flask import Flask, Response, request
import numpy as np
import json
import time

def inner(x):
    time.sleep(x)
    print('end')


def verbose_func(info, verbose=True):
    if verbose:
        print(info)

def convert_to_chinese_time(second):
    if second < 60:
        chinese_time = "{}秒".format(second)
    else:
        minutes = second // 60
        hours = minutes // 60
        remaining_minutes = minutes % 60
        chinese_time = "{}小时{}分钟".format(hours, remaining_minutes)
    return chinese_time


def computation(history_spend):
    time = int(np.array(history_spend).mean())
    chinese_time = convert_to_chinese_time(time)
    return chinese_time



class API_manager():
    def __init__(self, **kwargs):
        """
        kwargs 包括
        """

        self.app = Flask(__name__)
        self.token = '57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd'
        self.open_guard_token = True  # 是否开启token鉴权
        self.db_list = []
        self.answer = None
        self.answer_dict = {}
        self.function_kwargs = kwargs

    def guard_token(self, type='get'):
        try:
            if type == 'get':
                token = request.args.get('token', default=None, type=None)
            elif type == 'post':
                data = request.get_data()
                data_dict = json.loads(data)
                token = data_dict.get('token')
            else:
                raise Exception("type error")
            assert token == self.token
            return None
        except:
            if self.open_guard_token:
                return self.response_info(f"token未授权", 500, '')
            else:
                return None

    def get_data(self, type='post'):
        if type == 'post':
            data = request.get_data()
            data_dict = json.loads(data)
        return data_dict

    def response_info(self, msg: str, code: int, data):
        dicts = {
            "msg": msg,
            "code": code,
            "data": data
        }
        return Response(json.dumps(dicts, ensure_ascii=False), mimetype='application/json')

    def response_generate(self, generate):
        # TODO

        return Response(generate(), mimetype='text/plain')

    def start(self, server_name='0.0.0.0', server_port=9000, run=True, **kwargs):

        @self.app.route('/live', methods=['GET', 'POST'])
        def live():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return self.response_info("success", 200, '')

            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                text = data_dict.get('data')
                return self.response_info(f"机器人收到任务: {text}\n预计花费: 25分钟", 200, data_dict)

        @self.app.route('/sweep', methods=['GET', 'POST'])
        def sweep():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return self.response_info("success", 200, '')

            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                text = data_dict.get('text')
                # TODO
                spend_time = '25分钟'

                history_spend = [300, 500, 1200, 233, 600, 700]

                spend_time = computation(history_spend)
                # 执行异步函数
                # append history_spend
                inner(x=3)
                history_spend.append(3)

                return self.response_info(f"机器人收到任务: {text}\n预计花费: {spend_time}", 200, data_dict)

        @self.app.route('/code', methods=['GET', 'POST'])
        def code():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return self.response_info("success", 200, '')

            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                text = data_dict.get('text')
                # TODO
                spend_time = '25分钟'

                history_spend = [300, 500, 1200, 233, 600, 700]

                spend_time = computation(history_spend)
                # 执行异步函数
                # append history_spend
                inner(x=3)
                history_spend.append(3)

                return self.response_info(f"机器人收到任务: {text}\n预计花费: {spend_time}", 200, data_dict)

        @self.app.route('/environment', methods=['GET', 'POST'])
        def environment():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return self.response_info("success", 200, '')

            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                text = data_dict.get('text')
                # TODO
                spend_time = '25分钟'

                history_spend = [300, 500, 1200, 233, 600, 700]

                spend_time = computation(history_spend)
                # 执行异步函数
                # append history_spend
                inner(x=3)
                history_spend.append(3)

                return self.response_info(f"机器人收到任务: {text}\n预计花费: {spend_time}", 200, data_dict)

        @self.app.route('/information', methods=['GET', 'POST'])
        def information():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return self.response_info("success", 200, '')

            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                text = data_dict.get('text')
                # TODO
                spend_time = '25分钟'

                history_spend = [300, 500, 1200, 233, 600, 700]

                spend_time = computation(history_spend)
                # 执行异步函数
                # append history_spend
                inner(x=3)
                history_spend.append(3)

                return self.response_info(f"机器人收到任务: {text}\n预计花费: {spend_time}", 200, data_dict)

        if run:
            self.app.run(host=server_name, port=server_port, **kwargs)


class API_massage2(API_manager):
    def start(self, server_name='0.0.0.0', server_port=9000, **kwargs):
        super().start(run=False)
        # custom code

        # custom code end
        self.app.run(host=server_name, port=server_port, **kwargs)


# API_massage2().start()