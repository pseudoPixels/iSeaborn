import numpy as np


__all__ = ["barplot"]


class _CategoricalPlotter(object):

    width = .8
    default_palette = "light"







def barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
            estimator=np.mean, ci=95, n_boot=1000, units=None,
            orient=None, color=None, palette=None, saturation=.75,
            errcolor=".26", errwidth=None, capsize=None, dodge=True,
            ax=None, **kwargs):
    pass