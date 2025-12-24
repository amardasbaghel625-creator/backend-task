from modules.comment.reader import get_comments_by_task
from modules.comment.writer import create_comment, update_comment, delete_comment

class CommentService:

    @staticmethod
    def get_comments(task_id):
        return get_comments_by_task(task_id)

    @staticmethod
    def create_comment(task_id, text):
        return create_comment(task_id, text)

    @staticmethod
    def update_comment(comment_id, text):
        return update_comment(comment_id, text)

    @staticmethod
    def delete_comment(comment_id):
        delete_comment(comment_id)
