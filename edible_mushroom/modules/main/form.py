# coding: utf-8

from flask_wtf import Form
from flask.ext.babel import lazy_gettext as _
from wtforms import SubmitField, SelectField


class MushroomFeaturesForm(Form):
    cap_shape = SelectField(
        _(u'Cap shape'),
        choices=[
            ('b', _('Bell')),
            ('c', _('Conical')),
            ('x', _('Convex')),
            ('f', _('Flat')),
            ('k', _('Knobbed')),
            ('s', _('Sunken'))
        ]
    )
    cap_surface = SelectField(
        _(u'Cap surface'),
        choices=[
            ('f', _('Fibrous')),
            ('g', _('Grooves')),
            ('y', _('Scaly')),
            ('s', _('Smooth'))
        ]
    )
    cap_color = SelectField(
        _(u'Cap color'),
        choices=[
            ('n', _('Brown')),
            ('b', _('Buff')),
            ('c', _('Cinnamon')),
            ('g', _('Gray')),
            ('r', _('Green')),
            ('p', _('Pink')),
            ('u', _('Purple')),
            ('e', _('Red')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    bruises = SelectField(
        _(u'Bruises'),
        choices=[('t', _('Bruises')), ('f', _('No'))]
    )
    odor = SelectField(
        _(u'Odor'),
        choices=[
            ('a', _('Almond')),
            ('l', _('Anise')),
            ('c', _('Creosote')),
            ('y', _('Fishy')),
            ('f', _('Foul')),
            ('m', _('Musty')),
            ('n', _('None')),
            ('p', _('Pungent')),
            ('s', _('Spicy'))
        ]
    )
    gill_attachment = SelectField(
        _(u'Gill attachment'),
        choices=[
            ('a', _('Attached')),
            ('d', _('Descending')),
            ('f', _('Free')),
            ('n', _('Notched'))
        ]
    )
    gill_spacing = SelectField(
        _(u'Gill spacing'),
        choices=[
            ('c', _('Close')),
            ('w', _('Crowded')),
            ('d', _('Distant'))
        ]
    )
    gill_size = SelectField(
        _(u'Gill size'),
        choices=[('b', _('Broad')), ('n', _('Narrow'))]
    )
    gill_color = SelectField(
        _(u'Gill color'),
        choices=[
            ('k', _('Black')),
            ('n', _('Brown')),
            ('b', _('Buff')),
            ('h', _('Chocolate')),
            ('g', _('Gray')),
            ('r', _('Green')),
            ('o', _('Orange')),
            ('p', _('Pink')),
            ('u', _('Purple')),
            ('e', _('Red')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    stalk_shape = SelectField(
        _(u'Stalk shape'),
        choices=[('e', _('Enlarging')), ('t', _('Tapering'))]
    )
    stalk_root = SelectField(
        _(u'Stalk root'),
        choices=[
            ('b', _('Bulbous')),
            ('c', _('Club')),
            ('u', _('Cup')),
            ('e', _('Equal')),
            ('z', _('Rhizomorphs')),
            ('r', _('Rooted')),
            ('?', _('Missing'))
        ]
    )
    stalk_surface_above_ring = SelectField(
        _(u'Stalk surface above ring'),
        choices=[
            ('f', _('Fibrous')),
            ('y', _('Scaly')),
            ('k', _('Silky')),
            ('s', _('Smooth'))
        ]
    )
    stalk_surface_below_ring = SelectField(
        _(u'Stalk surface below ring'),
        choices=[
            ('f', _('Fibrous')),
            ('y', _('Scaly')),
            ('k', _('Silky')),
            ('s', _('Smooth'))
        ]
    )
    stalk_color_above_ring = SelectField(
        _(u'Stalk color above ring'),
        choices=[
            ('n', _('Brown')),
            ('b', _('Buff')),
            ('c', _('Cinnamon')),
            ('g', _('Gray')),
            ('o', _('Orange')),
            ('p', _('Pink')),
            ('e', _('Red')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    stalk_color_below_ring = SelectField(
        _(u'Stalk color below ring'),
        choices=[
            ('n', _('Brown')),
            ('b', _('Buff')),
            ('c', _('Cinnamon')),
            ('g', _('Gray')),
            ('o', _('Orange')),
            ('p', _('Pink')),
            ('e', _('Red')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    veil_type = SelectField(
        _(u'Veil type'),
        choices=[('p', _('Partial')), ('u', _('Universal'))]
    )
    veil_color = SelectField(
        _(u'Veil color'),
        choices=[
            ('n', _('Brown')),
            ('o', _('Orange')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    ring_number = SelectField(
        _(u'Ring number'),
        choices=[
            ('n', _('None')), ('o', _('One')), ('t', _('Two'))
        ]
    )
    ring_type = SelectField(
        _(u'Ring type'),
        choices=[
            ('c', _('Cobwebby')),
            ('e', _('Evanescent')),
            ('f', _('Flaring')),
            ('l', _('Large')),
            ('n', _('None')),
            ('p', _('Pendant')),
            ('s', _('Sheathing')),
            ('z', _('Zone'))
        ]
    )
    spore_print_color = SelectField(
        _(u'Spore print color'),
        choices=[
            ('k', _('Black')),
            ('n', _('Brown')),
            ('b', _('Buff')),
            ('h', _('Chocolate')),
            ('r', _('Green')),
            ('o', _('Orange')),
            ('u', _('Purple')),
            ('w', _('White')),
            ('y', _('Yellow'))
        ]
    )
    population = SelectField(
        _(u'Population'),
        choices=[
            ('a', _('Abundant')),
            ('c', _('Clustered')),
            ('n', _('Numerous')),
            ('s', _('Scattered')),
            ('v', _('Several')),
            ('y', _('Solitary'))
        ]
    )
    habitat = SelectField(
        _(u'Habitat'),
        choices=[
            ('g', _('Grasses')),
            ('l', _('Leaves')),
            ('m', _('Meadows')),
            ('p', _('Paths')),
            ('u', _('Urban')),
            ('w', _('Waste')),
            ('d', _('Woods'))
        ]
    )
    submit = SubmitField(_(u"Check mushroom"))

    def __init__(self, *args, **kwargs):
        super(MushroomFeaturesForm, self).__init__(*args, **kwargs)
