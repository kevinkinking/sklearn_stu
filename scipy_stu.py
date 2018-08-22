import numpy as np
from scipy import sparse

eye = np.eye(4)
print eye
sparse_eye_csr = sparse.csr_matrix(eye)
print sparse_eye_csr

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
sparse_eye_coo = sparse.coo_matrix(data, (row_indices, col_indices))
print sparse_eye_coo
print sparse_eye_coo.tocsr()

sparse_eye = sparse.eye(4)
print sparse_eye
sparse_ide = sparse.identity(4)
print sparse_ide