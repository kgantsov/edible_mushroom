import importlib
import os
import pkgutil


from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    # Recursively walks given path in search for blueprints
    rv = []
    for _, name, ispkg in pkgutil.iter_modules(package_path):
        if ispkg:
            register_blueprints(
                app,
                '.'.join((package_name, name)),
                [os.path.join(package_path[0], name)]
            )

        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv
