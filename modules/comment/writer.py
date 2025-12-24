from modules.comment.types import Comment
from modules.comment.reader import COMMENTS

def create_comment(task_id, text):
    comment = Comment(len(COMMENTS)+1, task_id, text)
    COMMENTS.append(comment)
    return comment

def update_comment(comment_id, text):
    for c in COMMENTS:
        if c.id == comment_id:
            c.text = text
            return c

def delete_comment(comment_id):
    global COMMENTS
    COMMENTS = [c for c in COMMENTS if c.id != comment_id]
