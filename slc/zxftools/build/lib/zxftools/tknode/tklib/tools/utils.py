import os
import time

def human_inter_with_txt(self, text: str) -> str:
    """
    inter with human
    :param text:
    :return:
    """
    if not os.path.exists('.temp.txt'):
        with open('.temp.txt', 'w') as file:
            file.write('')
    print(text)
    while True:
        with open('.temp.txt', 'r') as file:
            result = file.read()
        if result:
            break

        time.sleep(0.5)  # Wait for specified time before checking again

    os.remove('.temp.txt')

    return result


# 人工交互
def human_2_0_inp(self):
    input_value = input('Please input: ')
    with open('.temp.txt', 'w') as file:
        file.write(input_value)