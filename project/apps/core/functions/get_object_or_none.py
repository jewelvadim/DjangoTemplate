def get_object_or_none(class_, **kwargs):
    try:
        return class_.objects.get(**kwargs)
    except class_.DoesNotExist:
        return None
