import time
import unittest

class PerformanceTest(unittest.TestCase):

    def test(self):
        pass

    def test_perf(self):
        start_time = time.time()
        for i in range(100):
            self.test()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Test took ' + str(elapsed_time) + ' seconds.')
        # test that elapsed time is less than 10 seconds
        self.assertTrue(elapsed_time < 10.0)

if __name__ == '__main__':
    unittest.main()