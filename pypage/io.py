"""Data input and output handling
"""

import numpy as np
import pandas as pd


class ExpressionProfile:
    """Container for a Sample Expression Profile

    Attributes
    ==========
    genes: np.ndarray
        the sorted list of genes found in the expression profile
    bins: np.ndarray
        the sorted list of bins found in the expression profile
    n_genes: int
        the number of genes found
    n_bins: int
        the number of bins found
    bool_array: np.ndarray
        a (n_bins, n_genes) bit array representing the bin-position of each gene
    bin_array: np.ndarray
        a (n_genes, ) array where each value represents the bin index of that gene
    bin_sizes: np.ndarray
        a (n_bins, ) array where each value represents the number of genes in that bin index

    Methods
    -------
    get_gene_subset:
        returns a subset of the `bin_array` for the provided gene list
    """
    def __init__(
            self,
            expression_profile: pd.DataFrame):
        """
        Parameters
        ==========
        expression_profile: pd.DataFrame
            a two column dataframe where the first column is the gene and the
            second column is the bin that gene belongs to

        """

        genes = {n: idx for idx, n in enumerate(np.sort(expression_profile.gene.unique()))}
        bins = {n: idx for idx, n in enumerate(np.sort(expression_profile.bin.unique()))}

        self.genes = np.array(list(genes.keys()))
        self.bins= np.array(list(bins.keys()))

        self.n_genes = self.genes.size
        self.n_bins = self.bins.size


        # builds bool array
        self.bool_array = np.zeros((self.n_bins, self.n_genes), dtype=int)
        for g, b in expression_profile.values:
            self.bool_array[bins[b]][genes[g]] += 1

        # builds bin array
        self.bin_array = np.argmax(self.bool_array, axis=0)
        
        self.bin_sizes = self.bool_array.sum(axis=1)

    def __repr__(
            self) -> str:
        s = ""
        s += "Expression Profile\n"
        s += f">> num_genes: {self.n_genes}\n"
        s += f">> num_bins: {self.n_bins}\n"
        s += f">> bin_sizes: {' '.join(self.bin_sizes.astype(str))}\n"
        return s

    def get_gene_subset(
            self,
            gene_subset: np.ndarray) -> np.ndarray:
        """
        Index the bin-array for the required gene subset. 
        Expects the subset to be sorted
        
        Parameters
        ==========
        gene_subset: np.ndarray
            a list of genes to subset the bin_array to

        Returns
        =======
        np.ndarray
            the bin_array subsetted to the indices of the `gene_subset`
        """
        mask = np.isin(self.genes, gene_subset)
        return self.bin_array[mask]


class GeneOntology:
    """Container for a Set of Pathways

    Attributes
    ==========
    genes: np.ndarray
        the sorted list of genes found in the pathways
    pathways: np.ndarray
        the sorted list of pathways found in the index
    n_genes: int
        the number of genes found
    n_pathways: int
        the number of pathways found
    bool_array: np.ndarray
        a (n_pathways, n_genes) bit array representing the bin-position of each gene
    pathway_sizes: np.ndarray
        a (n_pathways, ) array where each value represents the number of genes in that pathway index
    avg_p_size: float
        the mean number of genes across pathways

    Methods
    -------
    get_gene_subset:
        returns a subset of the `bool_array` for the provided gene list
    """
    def __init__(
            self,
            index_filename: str):
        """
        Parameters
        ==========
        index_filename: str 
            filepath of a a two column dataframe where the first column is the gene 
            and the second column is the pathway that gene belongs to
        """

        self.index_filename = index_filename

        # load files
        self._load_index()

    def _load_index(self):
        """
        loads the index file representing the gene to pathway mapping
        """
        index = pd.read_csv(
                self.index_filename, 
                sep="\t",
                header=None,
                names=["gene", "pathway"])
        
        pathways = {n: idx for idx, n in enumerate(np.sort(index.pathway.unique()))}
        genes = {n: idx for idx, n in enumerate(np.sort(index.gene.unique()))}

        self.genes = np.array(list(genes.keys()))
        self.pathways = np.array(list(pathways.keys()))

        self.n_genes = self.genes.size
        self.n_pathways = self.pathways.size

        # builds bool array
        self.bool_array = np.zeros((self.n_pathways, self.n_genes), dtype=int)
        for g, p in index.values:
            self.bool_array[pathways[p]][genes[g]] += 1

        self.pathway_sizes = self.bool_array.sum(axis=1)
        self.avg_p_size = self.pathway_sizes.mean()

    def get_gene_subset(
            self,
            gene_subset: np.ndarray) -> np.ndarray:
        """
        Index the bool-array for the required gene subset. 
        Expects the subset to be sorted
        
        Parameters
        ==========
        gene_subset: np.ndarray
            a list of genes to subset the bin_array to

        Returns
        =======
        np.ndarray
            the bool_array subsetted to the indices of the `gene_subset`
        """
        mask = np.isin(self.genes, gene_subset)
        return self.bool_array[:, mask]
    
    def __repr__(self) -> str:
        """
        """
        s = ""
        s += "Gene Ontology\n"
        s += f">> num_genes: {self.n_genes}\n"
        s += f">> num_pathways: {self.n_pathways}\n"
        s += ">> avg_pathway_size: {:.2f}\n".format(self.avg_p_size)
        return s


