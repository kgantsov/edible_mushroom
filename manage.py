from flask.ext.script import Manager

from flask import current_app
from edible_mushroom import create_app
from edible_mushroom.modules.solution_tree.solution_tree import DATASET_LABELS
from edible_mushroom.modules.solution_tree.solution_tree import create_tree
from edible_mushroom.modules.solution_tree.solution_tree import store_tree


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)


@manager.option('-d', '--dataset', help='Mushroom Data Set')
def train(dataset):
    fr = open(dataset)
    lenses = [inst.strip().split(',') for inst in fr.readlines()]
    lenses_tree = create_tree(lenses, DATASET_LABELS)
    store_tree(lenses_tree, current_app.config['TREE_DATA_FILE_NAME'])


if __name__ == '__main__':
    manager.run()
