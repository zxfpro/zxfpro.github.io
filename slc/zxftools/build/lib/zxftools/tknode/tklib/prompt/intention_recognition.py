# Intention recognition
intention_recognition = """
你是一个意图判断器,你会对用户的每个输入进行判断,并归类到,给予消息 ,接收信息 这两类中
for example:
    user:老唐是一个脱口秀演员 assistant: 要求接收消息
    user:唐宇者是一个智者 assistant: 要求接收消息
    user:老唐是谁 assistant: 要求给予消息
------------------
{input}
"""

intention_recognition_example = """
Text: 谁是王忠伟? Sentiment: information_exchange
"""

intention_recognition2 = """
Classify the text into information_exchange deep_thinking Intuitive_answer. // 将文本按信息交流、深入思考或直觉回复进行分类
for example:
{example}

---------------
Text: {input}.
Sentiment:
"""

