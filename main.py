import string

from flask import Flask
from flask_restful import Api , Resource , reqparse , abort


from app import hello_world

app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def HelloWorld(Resource):
#     return 'hello world'

names = {"tim": {"age":19 , "gender":'male'},
         "bill":{"age":20 , "gender":'male'}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str ,help= "Name of the Video" ,required = True)
video_put_args.add_argument("views",type=int ,help= "Views of the Video",required = True)
video_put_args.add_argument("likes",type=int ,help= "likes of the Video",required = True)

videos = {}

def abort_if_video_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video {} doesn't exist".format(video_id))

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409, message="Video {} already exist".format(video_id))

class HelloWorld(Resource):
    def get(self,name):
        # return {"data":f"Hello {name}","test":test}
    
        return names[name]
    def post(self):
        return "post success"

class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_not_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        # print(request.form)
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self,video_id):
        abort_if_video_id_not_exist(video_id)
        del videos[video_id]
        return 'Method Deleted', 204

    def post(self,video_id):
        abort_if_video_id_not_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video,'/video/<int:video_id>')
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)