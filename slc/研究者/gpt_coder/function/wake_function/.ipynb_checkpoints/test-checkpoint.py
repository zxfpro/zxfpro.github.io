import unittest

class TestWakeFunction(unittest.TestCase):
    
    def test_wake_function_with_high_decibels(self):
        input_decibels = 80  # 假设80是阈值
        result = wake_function(input_decibels, "no_wake_word")
        self.assertEqual(result.sound, "bi")
        self.assertEqual(result.light, "on")
        self.assertEqual(result.status, "working")
        self.assertEqual(result.duration, 3600)  # 秒
    
    def test_wake_function_with_low_decibels(self):
        input_decibels = 50  # 阈值以下
        result = wake_function(input_decibels, "no_wake_word")
        self.assertEqual(result.sound, "none")
        self.assertEqual(result.light, "off")
        self.assertEqual(result.status, "idle")
        self.assertEqual(result.duration, 0)
    
    def test_wake_function_with_wake_word(self):
        input_decibels = 40  # 阈值以下
        result = wake_function(input_decibels, "wake_word")
        self.assertEqual(result.sound, "bi")
        self.assertEqual(result.light, "on")
        self.assertEqual(result.status, "working")
        self.assertEqual(result.duration, 3600)  # 秒
    
    def test_wake_function_with_no_wake_word(self):
        input_decibels = 40  # 阈值以下
        result = wake_function(input_decibels, "no_wake_word")
        self.assertEqual(result.sound, "none")
        self.assertEqual(result.light, "off")
        self.assertEqual(result.status, "idle")
        self.assertEqual(result.duration, 0)
    
    def test_wake_function_with_high_decibels_and_wake_word(self):
        input_decibels = 80  # 假设80是阈值
        result = wake_function(input_decibels, "wake_word")
        self.assertEqual(result.sound, "bi")
        self.assertEqual(result.light, "on")
        self.assertEqual(result.status, "working")
        self.assertEqual(result.duration, 3600)  # 秒
    
    def test_wake_function_on_threshold(self):
        input_decibels = 80  # 正好等于阈值
        result = wake_function(input_decibels, "no_wake_word")
        self.assertEqual(result.sound, "bi")
        self.assertEqual(result.light, "on")
        self.assertEqual(result.status, "working")
        self.assertEqual(result.duration, 3600)  # 秒

if __name__ == '__main__':
    unittest.main()
