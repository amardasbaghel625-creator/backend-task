from modules.comment.types import Comment

COMMENTS = []

def get_comments_by_task(task_id):
    return [c for c in COMMENTS if c.task_id == task_id]
