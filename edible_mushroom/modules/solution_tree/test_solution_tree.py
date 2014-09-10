from flask import current_app
from edible_mushroom import create_app
from flask.ext.testing import TestCase

from edible_mushroom.modules.solution_tree.solution_tree import grab_tree
from edible_mushroom.modules.solution_tree.solution_tree import classify
from edible_mushroom.modules.solution_tree.solution_tree import DATASET_LABELS


class SolutionTreeTest(TestCase):
    def setUp(self):
        self.tree_data = grab_tree(current_app.config['TREE_DATA_FILE_NAME'])

    def tearDown(self):
        self.tree_data = {}

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'SECRET KEY'
        return app

    def test_classify(self):
        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'x,s,g,f,n,f,w,b,k,t,e,s,s,w,w,p,w,o,e,n,a,g'.split(',')
            ),
            'e'
        )

        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'x,y,n,t,p,f,c,n,w,e,e,s,s,w,w,p,w,o,p,n,s,u'.split(',')
            ),
            'p'
        )

        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'f,f,g,f,n,f,w,b,n,t,e,f,f,w,w,p,w,o,e,n,a,g'.split(',')
            ),
            'e'
        )

        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'f,f,n,f,n,f,w,b,h,t,e,s,s,w,w,p,w,o,e,n,a,g'.split(',')
            ),
            'e'
        )

        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'x,f,g,f,f,f,c,b,p,e,b,k,k,b,b,p,w,o,l,h,v,p'.split(',')
            ),
            'p'
        )

        self.assertEqual(
            classify(
                self.tree_data,
                DATASET_LABELS,
                'x,y,g,f,f,f,c,b,p,e,b,k,k,b,b,p,w,o,l,h,y,g'.split(',')
            ),
            'p'
        )
