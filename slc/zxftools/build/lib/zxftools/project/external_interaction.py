import requests
import json
import functools

class DDMessage(object):
    """
    DingDing_POST类用于向钉钉发送POST请求。
    """
    def __init__(self,token="https://oapi.dingtalk.com/robot/send?access_token=1003a3d8a6e724e255d9b28b5d4a540cd8dbdd2d2fa2163ed09cc77f7c46841d"):
        """
        初始化DingDing_POST类。

        参数:
        token (str): 钉钉机器人的token。
        """
        self.token = token

    def send(self, content):
        """
        向钉钉发送文本消息。 要包含关键字 完成 error 或者 消息
        参数:
        content (str): 消息内容。
        返回:
        None
        """
        data = {"msgtype": "text", "text": {"content": content}}
        requests.post(self.token, data=json.dumps(data), headers={'Content-Type': 'application/json'})


def tool_qrcode(img_path:str='./small2.png'):
    """
    用来将函数输出转化为二维码图片的装饰器
    """
    import qrcode as qrcode_
    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            qr = qrcode_.QRCode(version=1, box_size=10, border=5)
            result = func(*args, **kwargs)
            qr.add_data(result)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save(img_path)
            return img
        return wrapper
    return outer_packing




