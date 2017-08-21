# -*- coding: utf-8 -*-

from pygsp import utils
from pygsp.graphs import NNGraph  # prevent circular import in Python < 3.5


class Bunny(NNGraph):
    r"""
    Create a graph of the Stanford bunny.

    References
    ----------
    See :cite:`turk1994zippered`.

    Examples
    --------
    >>> from pygsp import graphs
    >>> G = graphs.Bunny()

    """

    def __init__(self, **kwargs):

        data = utils.loadmat('pointclouds/bunny')

        plotting = {'vertex_size': 10,
                    'vertex_color': (1, 1, 1, 1),
                    'edge_color': (.5, .5, .5, 1)}

        super(Bunny, self).__init__(Xin=data['bunny'], epsilon=0.2,
                                    NNtype='radius', plotting=plotting,
                                    gtype='Bunny', **kwargs)
