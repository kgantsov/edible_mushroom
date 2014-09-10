
from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint(
    'main.views',
    __name__,
    template_folder='../../templates',
    url_prefix='/',
)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')