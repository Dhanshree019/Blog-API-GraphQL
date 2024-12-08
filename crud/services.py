import logging
from .models import *

logger = logging.getLogger("custom_logger")

def create_post(title, description, author):
    try:
        post = Post.objects.create(
            title=title,
            description=description,
            author=author
        )

        logger.info(f"Post created: {post.title} by {post.author}")

        return post
    
    except Exception as e:
        logger.error(f"Error creating post: {str(e)}")
        raise

def update_post(post_id, title, description, author):
    try:
        post = Post.objects.get(id=post_id)
        
        if title:
            post.title=title
        if description:
            post.description = description
        if author:
            post.author = author

        post.save()

        logger.info(f"Post updated: {post.title}")

        return post
    
    except Post.DoesNotExist:
        logger.error(f"Post with id {post_id} does not exist.")
        raise

    except Exception as e:
        logger.error(f"Error updating post: {str(e)}")
        raise

def create_comment(post_id, text, author):
    try:
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, text=text, author=author)

        logger.info(f"Comment created by {author} on post {post.title}")

        return comment
    
    except Post.DoesNotExist:
        logger.error(f"Post with id {post_id} does not exist.")
        raise

    except Exception as e:
        logger.error(f"Error creating comment: {str(e)}")
        raise

def delete_comment(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()

        logger.info(f"Comment deleted: {comment_id}")

    except Comment.DoesNotExist:
        logger.error(f"Comment with id {comment_id} does not exist.")
        raise

    except Exception as e:
        logger.error(f"Error deleting comment: {str(e)}")
        raise

def get_all_posts():
    try:
        posts = Post.objects.all()

        logger.info(f"Retrieved all posts: {len(posts)} found.")

        return posts
    
    except Exception as e:
        logger.error(f"Error retrieving posts: {str(e)}")
        raise Exception("An error occurred while retrieving posts.")
    
def get_post_by_id(post_id):
    try:
        post = Post.objects.get(id=post_id)

        logger.info(f"Retrieved post with id {post_id}: {post.title}")

        return post
    
    except Post.DoesNotExist:
        logger.error(f"Post with id {post_id} not found.")
        raise Exception("Post not found")
    
    except Exception as e:
        logger.error(f"Error retrieving post with id {post_id}: {str(e)}")
        raise Exception("An error occurred while retrieving the post.")