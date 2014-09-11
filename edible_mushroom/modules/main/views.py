from flask import g, request, session
from flask import current_app
from flask import Blueprint, render_template

from edible_mushroom.core import babel
from edible_mushroom.modules.main.form import MushroomFeaturesForm
from edible_mushroom.modules.solution_tree.solution_tree import grab_tree
from edible_mushroom.modules.solution_tree.solution_tree import classify
from edible_mushroom.modules.solution_tree.solution_tree import DATASET_LABELS

bp = Blueprint(
    'main.views',
    __name__,
    template_folder='../../templates',
    url_prefix='/',
)


@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale

    return request.accept_languages.best_match(['en', 'ru'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = MushroomFeaturesForm()
    result = None

    if form.validate_on_submit():
        tree_data = grab_tree(current_app.config['TREE_DATA_FILE_NAME'])
        data = [
            form.cap_shape.data,
            form.cap_surface.data,
            form.cap_color.data,
            form.bruises.data,
            form.odor.data,
            form.gill_attachment.data,
            form.gill_spacing.data,
            form.gill_size.data,
            form.gill_color.data,
            form.stalk_shape.data,
            form.stalk_root.data,
            form.stalk_surface_above_ring.data,
            form.stalk_surface_below_ring.data,
            form.stalk_color_above_ring.data,
            form.stalk_color_below_ring.data,
            form.veil_type.data,
            form.veil_color.data,
            form.ring_number.data,
            form.ring_type.data,
            form.spore_print_color.data,
            form.population.data,
            form.habitat.data
        ]

        result = classify(tree_data, DATASET_LABELS, data)

    return render_template('main/index.html', form=form, result=result)
