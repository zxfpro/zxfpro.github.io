import unittest


class TKNodeTests(unittest.TestCase):

    def test_SuperReActOutputParser(self):
        pass


    def test_ReactAgentMaker(self):
        pass


# import unittest
#
# class_level Test_utils(unittest.TestCase):
#
#     def test_prinf(self):
#         print('123')


import requests
import httpx
def release_task(priority, content):
    url = "http://localhost:8000/add_task"  # 替换为正确的URL
    payload = {
        "priority": priority,
        "content": content,
        "task_id": 12,
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Task added successfully")
    else:
        print("Failed to add task")
        print()

release_task(1,'what is weather')


# import os
# import diskcache
#
# # Define a dummy function for testing
# def dummy_function(**kwargs):
#     return "Result"
#
# # Create an instance of OptConfig
# optconfig = OptConfig("dummy_function")
#
# # Create a cache1 decorator with exact_match type
# @cache1(optconfig, type='exact_match')
# def decorated_function(**kwargs):
#     return dummy_function(**kwargs)
#
# # Test the decorated function
# result = decorated_function(key1='value1', key2='value2')
# print(result)  # Expected output: "Result"
#
# # Create a cache1 decorator with fuzzy_match type
# @cache1(optconfig, type='fuzzy_match')
# def decorated_function2(**kwargs):
#     return dummy_function(**kwargs)
#
# # Test the decorated function with fuzzy_match type
# result2 = decorated_function2(key1='value1', key2='value2')
# print(result2)  # Expected output: "Result"



class AgentMakerTests(unittest.TestCase):

    def test_SuperReActOutputParser(self):
        pass


    def test_ReactAgentMaker(self):
        pass


    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    # 测试异常
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            pass
            # add(1, "two")


class AgentMakerTests(unittest.TestCase):

    def test_SuperReActOutputParser(self):
        pass

    def test_ReactAgentMaker(self):
        pass

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    # 测试异常
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            pass
            # add(1, "two")


class AgentMakerTests(unittest.TestCase):

    def test_SuperReActOutputParser(self):
        pass

    def test_ReactAgentMaker(self):
        pass

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    # 测试异常
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            pass
            # add(1, "two")


class AgentAPIServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = AgentAPIService()

    def test_add_mission(self):
        self.service.add_mission(1, "mission content", 1, "http://localhost:8000")
        self.assertEqual(len(self.service.missions), 1)
        self.assertEqual(self.service.missions[0].priority, 1)
        self.assertEqual(self.service.missions[0].content, "mission content")
        self.assertEqual(self.service.missions[0].mission_id, 1)
        self.assertEqual(self.service.missions[0].release_ip, "http://localhost:8000")

    def test_recall_mission(self):
        mission = Mission(1, "mission content", 1, "http://localhost:8000")
        self.service.hang_missions[1] = mission
        self.service.recall_mission("result", 1)
        self.assertEqual(len(self.service.missions), 1)
        self.assertEqual(self.service.missions[0].priority, 1)
        self.assertEqual(self.service.missions[0].content, "mission content")
        self.assertEqual(self.service.missions[0].mission_id, 1)
        self.assertEqual(self.service.missions[0].release_ip, "http://localhost:8000")
        self.assertEqual(self.service.missions[0].recall_message, "result")

    def test_release_mission(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            result = self.service.release_mission(1, "mission content", "weather_expert")
            self.assertEqual(result, "await")
            mock_post.assert_called_once_with('http://localhost:8001/add_mission', json={
                "priority": 1,
                "content": "mission content",
                "mission_id": self.service.release_mission_id,
                "release_ip": "http://localhost:8000"
            })

    def test_handle_mission(self):
        mission = Mission(1, "mission content", 1, "http://localhost:8000")
        agent = Agent()
        result = self.service.handle_mission(mission, agent)
        self.assertEqual(result, mission)

    def test_callback(self):
        mission = Mission(1, "mission content", 1, "http://localhost:8000")
        mission.result = "result"
        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            self.service.callback(mission, human=False, parents_url='http://localhost:7999')
            mock_post.assert_called_once_with('http://localhost:7999/get_result', json={
                "result": "result",
                "mission_id": 1
            })

# ChatMemoryBuffer
# 运行所有测试
if __name__ == '__main__':
    unittest.main()