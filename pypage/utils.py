"""Utility functions
"""

import numpy as np
import numba as nb
from scipy.stats import hypergeom
from .hist import (
        hist1D,
        hist2D,
        hist3D)

@nb.jit(nopython=True)
def shuffle_bin_array(
        bin_array: np.ndarray) -> np.ndarray:
    """Shuffles the bin identities for a provided bin array
    """
    shuf = bin_array.copy()
    np.random.shuffle(shuf)
    return shuf


@nb.jit(nopython=True)
def empirical_pvalue(
        array: np.ndarray,
        value: float) -> float:
    """Calculates the empirical pvalue of a value given a distribution
    """
    m = array.max()
    if value > m:
        return 0.
    else:
        return np.mean(array >= value)


def hypergeometric_test(
        e_bins: np.ndarray, 
        o_bool: np.ndarray) -> np.ndarray:
    """
    translating from: https://ars.els-cdn.com/content/image/1-s2.0-S1097276509008570-mmc1.pdf
    
    m = n: number of genes in the pathway
    x = k: number of genes in the bin which are also in the pathway
    n = N: number of genes in the bin
    N = M: total number of genes
    """
    n_bins = e_bins.max() + 1
    ct = hist2D(e_bins, o_bool, n_bins, 2)
    n = o_bool.sum()
    k = ct[:, 1]
    N = ct.sum(axis=1)
    M = o_bool.size

    # parameterize hypergeometric distribution
    hg = hypergeom(M, n, N)
    
    # measure overrepresentation
    sf = hg.sf(k)
    
    # measure underrepresentation
    cdf = hg.cdf(k)
    
    return np.stack([sf, cdf])


def benjamini_hochberg(
        p: np.ndarray) -> np.ndarray:
    """
    Benjamini-Hochberg p-value correction for multiple hypothesis testing.
    https://stackoverflow.com/a/33532498
    """
    p = np.asfarray(p)
    by_descend = p.argsort()[::-1]
    by_orig = by_descend.argsort()
    steps = float(len(p)) / np.arange(len(p), 0, -1)
    q = np.minimum(1, np.minimum.accumulate(steps * p[by_descend]))
    return q[by_orig]
