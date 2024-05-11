from ..utils import get_db
from django import template
from bson.objectid import ObjectId

register = template.Library()


@register.filter
def author(_id):
    db = get_db()
    author = db.authors.find_one({"_id": ObjectId(_id)})
    return author['fullname']
