import argparse
from dotenv import load_dotenv
import os, shutil

# load .env for sensitive info
load_dotenv()

import sys

class Tee:
    def __init__(self, *outputs):
        self.outputs = outputs

    def write(self, message):
        for output in self.outputs:
            try:
                output.write(message)
                output.flush()  # 確保即時寫入
            except ValueError:
                # 有些 output（例如已關閉的 file）不能 flush，忽略即可
                pass
            

    def flush(self):
        for output in self.outputs:
            try:
                output.flush()
            except ValueError:
                # 有些 output（例如已關閉的 file）不能 flush，忽略即可
                pass


from controller import test_process

def main():
    # setup environment & variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="apk path", dest="apk_path", default="E:/class/grad/project/llm_testpath_find/input/app-debug_1_6_2_b.apk")
    parser.add_argument("-t", "--test", help="test step file", dest="test_path", default="E:/class/grad/project/llm_testpath_find/input")
    args = parser.parse_args()
    apk_path = args.apk_path
    test_path = args.test_path
    print("apk path:", apk_path)
    print("test path:", test_path)

    # setup tmp folder for screenshots
    tmp_path = os.getenv("TMP_PATH")
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
    os.mkdir(tmp_path)

    # setup output folder for record
    output_path = os.getenv("OUTPUT_PATH")
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    # 用 with 保證 file 正確開關
    with open(output_path + "/output.log", "w") as log_file:
        sys.stdout = Tee(sys.__stdout__, log_file)  # __stdout__ 是原始 terminal stdout

        print("start process")
        test_process(apk_path, test_path)


if __name__ == '__main__':
    main()
