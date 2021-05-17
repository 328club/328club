import django_filters
# from django_mysql.models import JSONField
from django_jsonfield_backport.models import JSONField


def get_custom_filter_class(model_class, filter_fields=None, extra_fileds=None):
    class ModelFilter(django_filters.FilterSet):
        class Meta:
            model = model_class
            if filter_fields:
                fields = filter_fields
            else:
                fields = [item.name for item in model._meta.fields]
            if extra_fileds:
                fields.extend(extra_fileds)
            filter_overrides = {
                JSONField: {
                    'filter_class': django_filters.CharFilter,
                    'extra': lambda f: {
                        'lookup_expr': 'icontains',
                    },
                },
            }

    return ModelFilter
