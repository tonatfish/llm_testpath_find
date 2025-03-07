import argparse
from dotenv import load_dotenv
import os, shutil

# load .env for sensitive info
load_dotenv()

from controller import testpath_find

def main():
    # setup environment & variables
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="apk path", dest="apk_path", default="E:/class/grad/project/llm_testpath_find/input/app-debug.apk")
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
    
    print("start process")
    testpath_find(apk_path, test_path)

if __name__ == '__main__':
    main()