from neomodel import (StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom)


class Person(StructuredNode):
    first_name = StringProperty()
    last_name = StringProperty()
    # age = models.IntegerProperty()
    job_title = StringProperty()
    # email = EmailProperty()
    # blog = models.URLProperty()


# class Organization(models.NodeModel):
#     name = models.StringProperty()

#     industry = models.Relationship('Industry',
#                                    rel_type='classification',
#                                    single=False,
#                                    related_name='organizations'
#                                    )


# class Industry(models.NodeModel):
#     name = models.StringProperty()


class TwitterUser(StructuredNode):
    username = StringProperty()
    twitter_id = StringProperty()
    company = StringProperty()

    followed_by = RelationshipFrom('TwitterUser', 'FOLLOWED_BY')
    following = RelationshipTo('TwitterUser', 'FOLLOWING')
    person = RelationshipTo('Person', 'OWNED_BY')


# class Tweet(models.NodeModel):
#     full_text = models.StringProperty()

