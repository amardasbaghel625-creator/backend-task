from flask.views import MethodView
from flask import request, jsonify
from modules.comment.service import CommentService

class CommentView(MethodView):

    def get(self, account_id, task_id):
        comments = CommentService.get_comments(task_id)
        return jsonify([c.__dict__ for c in comments]), 200

    def post(self, account_id, task_id):
        data = request.json
        comment = CommentService.create_comment(task_id, data["text"])
        return jsonify(comment.__dict__), 201

    def put(self, account_id, task_id, comment_id):
        data = request.json
        comment = CommentService.update_comment(comment_id, data["text"])
        return jsonify(comment.__dict__), 200

    def delete(self, account_id, task_id, comment_id):
        CommentService.delete_comment(comment_id)
        return jsonify({"message": "Deleted"}), 200
