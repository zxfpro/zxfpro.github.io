

def interpret_intent(statement: str) -> str:
    """
    根据给定的语句和背景信息推断用户真正的意图。
    """
    # 根据语句和背景信息进行意图推断的逻辑
    inferred_intent = """
用户希望编写一个软件著作权的申请书,但是我们还需要编写主体,相关材料等信息
    """
    inferred_intent = input(statement)
    # cache 一下内容  statement : inferred_intent

    # cache 整合策略点 带点

    return inferred_intent


def gather_required_info(ask: str) -> str:
    """
    可以根据这个函数来向用户索要相关的信息
    """
    result = input(ask)
    return result

