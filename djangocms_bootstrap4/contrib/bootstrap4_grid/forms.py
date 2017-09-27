# -*- coding: utf-8 -*-
from django.forms import models, IntegerField, BooleanField
from django.utils.translation import ugettext_lazy as _

from ...utils import IntegerRangeField
from ...constants import DEVICE_SIZES

from .models import GRID_SIZE, Bootstrap4GridRow, Bootstrap4GridColumn


class Bootstrap4GridRowForm(models.ModelForm):
    create = IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create when saving.'),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )

    class Meta:
        pass


class Bootstrap4GridColumnBaseForm(models.ModelForm):
    class Meta:
        model = Bootstrap4GridColumn
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


extra_fields_column = {}
for size in DEVICE_SIZES:
    extra_fields_column['{}_col'.format(size)] = IntegerField(
        label='col-{}'.format(size),
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_order'.format(size)] = IntegerField(
        label='order-{}'.format(size),
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_ml'.format(size)] = BooleanField(
        label='ml-{}-auto'.format(size),
        required=False,
    )
    extra_fields_column['{}_mr'.format(size)] = BooleanField(
        label='mr-{}-auto'.format(size),
        required=False,
    )

Bootstrap4GridColumnForm = type(
    str('Bootstrap4GridColumnBaseForm'),
    (Bootstrap4GridColumnBaseForm,),
    extra_fields_column,
)