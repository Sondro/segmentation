# flake8: noqa
from catalyst.dl import registry

# add experiment
from .experiment import Experiment
from .runner import ModelRunner as Runner
from . import callbacks

registry.CALLBACKS.add_from_module(callbacks)
