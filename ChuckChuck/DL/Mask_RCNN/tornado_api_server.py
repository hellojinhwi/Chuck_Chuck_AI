import tornado.ioloop
import tornado.web
import tornado.concurrent
from concurrent.futures import ThreadPoolExecutor

import os
import sys
sys.path.append("./Mask_RCNN")
import uuid
import predict
import time


# MAX_PROCESS = 0 : auto count cpu, process
MAX_PROCESS = 1

# worker thread pool size
MAX_WORKERS = 4

# system port
PORT = 5000

# meta data
IMAGE_DIR = os.path.join(os.getcwd(), "image_temp\\")
HTML_PATH = "templates/"
REDIRECT_URL = "http://localhost:8000/imageResult/" # text 검색을 하는 페이지 URL
REDIRECT_HOME = "http://localhost:8000/error" # 이미지 검색 오류시 사용자에게 재시도를 권하는 오류 페이지


class MainHandler(tornado.web.RequestHandler): # URL 또는 URL 패턴을 RequestHandler에 서브클래스로 매핑함.
    def get(self): # get 방식의 request
        print('client !')
        self.render(HTML_PATH + "index.html") # html 파일을 화면에 띄워줌. html파일이 .py 파일과 동일 경로.


class ImageHandler(tornado.web.RequestHandler):

    executor = tornado.concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)

    @tornado.concurrent.run_on_executor
    def run_classification(self, image_path):
        label = predict.classify(image_path)
        return label

    @tornado.gen.coroutine
    def upload_file(self, file, f_name):
        with open(os.path.join(IMAGE_DIR + f_name), 'wb') as save_file:
            save_file.write(file['body'])

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        request_file = self.request.files['uploadFile'][0]

        if request_file:
            extension = os.path.splitext(request_file.filename)[1]
            file_name = str(uuid.uuid4()) + extension
            yield self.upload_file(request_file, file_name)
            time.sleep(0.5)
            print("upload !")
            image_path = IMAGE_DIR + file_name
            print(image_path)
            try:
                label = yield self.run_classification(image_path)
                time.sleep(0.5)
            except:
                os.remove(image_path)
                return self.redirect(REDIRECT_HOME) 
            time.sleep(0.5)
            os.remove(image_path)
            return self.redirect(REDIRECT_URL +label)

        else:
            return self.redirect(REDIRECT_HOME)


def make_app():
    return tornado.web.Application([
        ("/", MainHandler),
        ("/upload", ImageHandler),
         (r"/(.*)",tornado.web.StaticFileHandler, {"path": "./static"},),
        (r"/css/(.*)",tornado.web.StaticFileHandler, {"path": "./static/css"},),
        (r"/img/core-img/(.*)",tornado.web.StaticFileHandler, {"path": "./static/img/core-img"},),
        (r"/img/icons/(.*)",tornado.web.StaticFileHandler, {"path": "./static/img/icons"},),
        (r"/img/bg-img/(.*)",tornado.web.StaticFileHandler, {"path": "./static/img/bg-img"},),
        (r"/js/(.*)",tornado.web.StaticFileHandler, {"path": "./static/js"},),
        (r"/fonts/(.*)",tornado.web.StaticFileHandler, {"path": "./static/fonts"},),
        (r"/assets/js/(.*)",tornado.web.StaticFileHandler, {"path": "./static/assets/js"},),
    ],debug=True)


if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(PORT)
    server.start(MAX_PROCESS)  # forks one process per cpu 0
    print('Tornado Server Start !')
    tornado.ioloop.IOLoop.current().start()
