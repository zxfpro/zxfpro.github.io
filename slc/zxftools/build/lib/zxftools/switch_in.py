import requests
import hashlib
import json
import base64
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
        向钉钉发送文本消息。
        参数:
        content (str): 消息内容。
        返回:
        None
        """
        if content.endswith('.jpeg') or content.endswith('.jpg') or content.endswith('.png'):
            # content 图片path
            msg, md5 = self._read_image_base64(content)
            data = {"msgtype": "image", "image": {"base64": msg, "md5": md5}}
        else:
            data = {"msgtype": "text", "text": {"content": content}}
        requests.post(self.token, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    def _read_image_base64(self, image_path):
        """
        读取图片并转换为base64编码。

        参数:
        image_path (str): 图片路径。

        返回:
        tuple: 包含base64编码的图片和图片的md5哈希值的元组。
        """
        with open(image_path, 'rb') as f:
            data = f.read()
            encode_str = str(base64.b64encode(data), encoding='utf-8')
            hl = hashlib.md5()
            hl.update(data)
        return encode_str, hl.hexdigest()

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




