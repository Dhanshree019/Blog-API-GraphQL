import graphene
from graphene_django.types import DjangoObjectType
from .models import *
from .services import *

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, description, author):
        post = create_post(title, description, author)
        return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id,title=None,description=None,author=None):
        post = update_post(id, title, description, author)
        return UpdatePost(post=post)
    
class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int(required=True)
        text = graphene.String(required=True)
        author = graphene.String(required=True)

    comment = graphene.Field(CommentType)

    def mutate(self, info, post_id, text, author):
        comment = create_comment(post_id, text, author)
        return CreateComment(comment=comment)

class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        delete_comment(id)
        return DeleteComment(success=True)

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.Int(required=True))

    def resolve_posts(self, info):
        return get_all_posts()

    def resolve_post(self, info, id):
        return get_post_by_id(id)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
