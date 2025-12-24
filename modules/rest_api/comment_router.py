from modules.rest_api.comment_view import CommentView

def register_comment_routes(app):
    comment_view = CommentView.as_view("comment_view")

    app.add_url_rule(
        "/accounts/<int:account_id>/tasks/<int:task_id>/comments",
        view_func=comment_view,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        "/accounts/<int:account_id>/tasks/<int:task_id>/comments/<int:comment_id>",
        view_func=comment_view,
        methods=["PUT", "DELETE"]
    )

