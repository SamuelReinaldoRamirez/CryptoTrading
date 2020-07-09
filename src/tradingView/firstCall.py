import json
import shutil
import tempfile
import time
import urllib
from urllib.request import urlopen


def main():
    # listAssets = []
    # try:
    #     api_data = urlopen("https://docs.python.org/3/howto/urllib2.html").read()
    #     print(api_data)
    #     print("a")
    #     jsonResult = json.loads(api_data)
    #     print("b")
    #     print(jsonResult)
    #     for asset in jsonResult["result"]:
    #         listAssets.append(asset)
    # except Exception:
    #     print("error in getListAssets")
    # return listAssets
    with urllib.request.urlopen('http://python.org/') as response:
        print(response)
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            print(tmp_file)
            shutil.copyfileobj(response, tmp_file)
    with open(tmp_file.name) as html:
        print(html)
        time.sleep(5)
        pass


if __name__ == "__main__":
    main()