

"""

#p32页例子
# 矩阵加法与矩阵数乘都称为矩阵的线性变换
#单位矩阵相当于1
#38页例子
# 矩阵转置运算规律 p39
#具体参照p40
# 现在返回去做行列式
#利用行列式计算二元线性方程组  p2



"""
#linear algebra
import numpy as np

a = MatrixCol()

b = a.mul(Matrix(mat1.inverse_matrix()),mat3)

a.mul(Matrix(b),Matrix(mat2.inverse_matrix()))

Matrix(a.mul(mat1,mat2)).T


# 全排列
def full_permutation(n):
    if n == 1:
        return [[1]]
    else:
        sum = []
        for i in full_permutation(n - 1):
            for j in range(n):
                sum.append(i[:j] + [n] + i[j:])
        return sum


# 逆序数
def inverse_order_number(pailie):
    # 在一个排列中，当两个数的大小颠倒时，称为一个逆序
    # 逆序数就是排列中逆序的个数
    # 逆序数为奇数的排列称为奇排列，逆序数为偶数的排列称为偶排列
    sum = 0
    for i in range(len(pailie)):
        for j in range(i + 1, len(pailie)):
            if pailie[i] > pailie[j]:
                sum += 1
    return sum


class Matrix:
    def __init__(self, data: np.ndarray):
        """
        det 行列式
        """
        self.data = data
        self.square = True if self.data.shape[0] == self.data.shape[1] else False
        self.H_matrix = True if self.data.shape[0] == 1 else False
        self.W_matrix = True if self.data.shape[1] == 1 else False
        self.zero_matrix = True if self.data.all() == 0 else False
        self.diag_matrix = self._is_diag_matrix()
        self.symmetric_matrix = True if self.square and (self.data == self.data.T).all() else False
        self.unit_matrix = self._is_unit_matrix()
        self.scalar_matrix = True if self.square and (self.data == self.data[0, 0]).all() else False
        self.rank = np.linalg.matrix_rank(self.data)  # 秩
        self.trace = np.trace(self.data)  # 迹

        self.det = np.linalg.det(self.data) if self.square else None
        if self.square:
            self.values, self.vactor = np.linalg.eigh(self.data)  # 特征值 #特征向量
            self.upper_triangle_matrix = self.upper_triangle()
            self.down_triangle_matrix = self.down_triangle()

    def __repr__(self):
        return str(self.data)

    def inv(self):
        """
        inverse_matrix
        """
        assert self.square
        assert np.linalg.det(self.data) != 0
        return Matrix(np.linalg.inv(self.data))

    def T(self):
        return self.data.T

    def _is_diag_matrix(self):
        # 对角矩阵是方阵，且非对角线元素全为0
        # 也被称为diag矩阵
        if self.square:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    if i != j and self.data[i, j] != 0:
                        return False
            return True
        else:
            return False

    # 单位矩阵
    def _is_unit_matrix(self):
        # 方阵，且对角线元素全为1
        if self.square:
            for i in range(self.data.shape[0]):
                for j in range(self.data.shape[1]):
                    if i == j and self.data[i, j] != 1:
                        return False
            return True
        else:
            return False

    def upper_triangle(self):
        assert self.square
        for i in range(self.data.shape[0]):
            for j in range(i):
                if self.data[i, j] != 0:
                    return False
        return True

    def down_triangle(self):
        assert self.square
        for i in range(self.data.shape[0]):
            for j in range(i + 1, self.data.shape[1]):
                if self.data[i, j] != 0:
                    return False
        return True

    # 矩阵的幂
    def power(self, n):
        # 矩阵的幂是指把一个矩阵乘以自身n次
        # 矩阵的幂是一个方阵
        # 矩阵幂的性质类似与exp p37
        assert n > 0
        assert self.square
        if n == 1:
            return self.data
        else:
            return self.data.dot(self.power(n - 1))

    def complement_minor(self, i, j):
        # 余子式记作Aij
        assert self.square
        assert self.data.shape[0] > 1
        return np.delete(np.delete(self.data, i, axis=0), j, axis=1)

    ########

    def add(self, matrix2):
        return MatCol.add(self, matrix2)

    def sub(self, matrix2):
        return MatCol.sub(self, matrix2)

    def mul(self, matrix2):
        return MatCol.mul(self, matrix2)

    def number_mul(self, matrix2):
        return MatCol.number_mul(self, matrix2)


class MatCol:
    def same_shape(self, matrix1, matrix2):
        return True if matrix1.data.shape == matrix2.data.shape else False

    def equality(self, matrix1, matrix2):
        return True if (matrix1.data == matrix2.data).all() else False

    def change(self, matrix1, matrix2):
        return True if self.mul(matrix1, matrix2) == self.mul(matrix2, matrix1) else False

    # 矩阵加法
    @classmethod
    def add(cls, matrix1, matrix2):
        assert cls().same_shape(matrix1, matrix2)
        return Matrix(matrix1.data + matrix2.data)

    # 矩阵减法
    @classmethod
    def sub(cls, matrix1, matrix2):
        assert cls().same_shape(matrix1, matrix2)
        return Matrix(matrix1.data - matrix2.data)

    # 矩阵乘法
    @classmethod
    def mul(cls, matrix1, matrix2):
        assert matrix1.data.shape[1] == matrix2.data.shape[0]
        return Matrix(matrix1.data.dot(matrix2.data))

    @classmethod
    def number_mul(cls, number, matrix):
        return Matrix(number * matrix.data)
    # 相似矩阵


trix
# class Matrix:
#     def __init__(self,data:np.ndarray):
#         # 只接受2维
#         self.data=data
#         self.feature = {"square": self.__is_square(),
#                         'H': self.__is_H_matrix(),
#                         'W': self.__is_W_matrix(),
#                         'zero': self.__is_zero_matrix(),
#                         'diag': self.__is_diag_matrix(),
#                         'symmetric': self.__is_symmetric_matrix(),
#                         'unit': self.__is_unit_matrix(),
#                         'scalar': self.__is_scalar_matrix(),
#                         }
        self.det = self.data if self.__is_square() else None
        # self.rank = self.data if self.__is_square() else None
        # self.trace = self.data if self.__is_square() else None
        # self.inv = self.data if self.__is_square() else None
#     def __is_square(self):
#         # 行数和列数都等于n的矩阵 成为n阶矩阵 或者n阶方阵
#         if self.data.shape[0]==self.data.shape[1]:
#             return True
#         else:
#             return False

#     def __is_H_matrix(self):
#         # 只有一行的矩阵成为行矩阵
#         if self.data.shape[0]==1:
#             return True
#         else:
#             return False

#     def __is_W_matrix(self):
#         # 只有一列的矩阵成为列矩阵
#         if self.data.shape[1]==1:
#             return True
#         else:
#             return False

    # def __is_zero_matrix(self):
    #     # 全为0的矩阵称为零矩阵
    #     if self.data.all()==0:
    #         return True
    #     else:
    #         return False

    # def __is_diag_matrix(self):
    #     # 对角矩阵是方阵，且非对角线元素全为0
    #     # 也被称为diag矩阵
    #     if self.__is_square():
    #         for i in range(self.data.shape[0]):
    #             for j in range(self.data.shape[1]):
    #                 if i != j and self.data[i, j] != 0:
    #                     return False
    #         return True
    #     else:
    #         return False
    #对称矩阵
    # def __is_symmetric_matrix(self):
    #     # 方阵，且对称
    #     if self.__is_square():
    #         if (self.data==self.data.T).all():
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False
    # #单位矩阵
    # def __is_unit_matrix(self):
    #     # 方阵，且对角线元素全为1
    #     if self.__is_square():
    #         for i in range(self.data.shape[0]):
    #             for j in range(self.data.shape[1]):
    #                 if i == j and self.data[i, j] != 1:
    #                     return False
    #         return True
    #     else:
    #         return False
    # #纯量阵
    # def __is_scalar_matrix(self):
    #     #纯量阵与任何同阶方阵都是可交换的
    #     #纯量阵是一个方阵，且它的所有元素都相等
    #     if self.__is_square():
    #         if (self.data==self.data[0,0]).all():
    #             return True
    #         else:
    #             return False

    # #矩阵的幂
    # def power(self,n):
    #     #矩阵的幂是指把一个矩阵乘以自身n次
    #     #矩阵的幂是一个方阵
    #     # 矩阵幂的性质类似与exp p37
    #     assert n > 0
    #     if self.__is_square():
    #         if n==1:
    #             return self.data
    #         else:
    #             return self.data.dot(self.power(n-1))
    #     else:
    #         raise Exception("不是方阵")

    # #矩阵的转置
    # def transpose(self):
    #     return self.data.T

#     #矩阵的行列式
#     def det(self):
#         """
#         # 对角线法则只适用于2阶与3阶
#         if juzhen.shape[0]==1:
#             return juzhen[0,0]
#         elif juzhen.shape[0]==2:
#             return juzhen[0,0]*juzhen[1,1]-juzhen[0,1]*juzhen[1,0]
#         elif juzhen.shape[0]==3:
#             return juzhen[0,0]*juzhen[1,1]*juzhen[2,2]+juzhen[0,1]*juzhen[1,2]*juzhen[2,0]+juzhen[0,2]*juzhen[1,0]*juzhen[2,1]-juzhen[0,2]*juzhen[1,1]*juzhen[2,0]-juzhen[0,1]*juzhen[1,0]*juzhen[2,2]-juzhen[0,0]*juzhen[1,2]*juzhen[2,1]
#         else:
#             sum = 0
#             for i in range(juzhen.shape[0]):
#                 sum+=juzhen[0,i]*行列式的计算(行列式的余子式(juzhen,0,i))
#             return sum

#         """
#         if self.__is_square():
#             return np.linalg.det(self.data)
#         else:
#             raise Exception("不是方阵")



# # ma
# class MatrixColculation:
#     def __init__(self,matrix1:Matrix,matrix2:Matrix):
#         self.matrix1=matrix1
#         self.matrix2=matrix2

#     def __same_shape(self):
#         # 判断两个矩阵是否同型
#         if self.matrix1.data.shape==self.matrix2.data.shape:
#             return True
#         else:
#             return False

#     def __is_equality(self):
#         # 判断两个矩阵是否相等
#         if self.__same_shape():
#             if (self.matrix1.data==self.matrix2.data).all():
#                 return True
#             else:
#                 return False

    # # 矩阵加法
    # def add(self):
    #     if self.__same_shape():
    #         return self.matrix1.data+self.matrix2.data
    #     else:
    #         raise Exception("矩阵不同型")

    # # 矩阵减法
    # def sub(self):
    #     if self.__same_shape():
    #         return self.matrix1.data-self.matrix2.data
    #     else:
    #         raise Exception("矩阵不同型")

#     # 矩阵乘法
#     def mul(self):
#         if self.matrix1.data.shape[1]==self.matrix2.data.shape[0]:
#             return self.matrix1.data.dot(self.matrix2.data)
#         else:
#             raise Exception("矩阵不同型")

#     # 矩阵乘法
#     @classmethod
#     def mul2(cls, matrix1: Matrix, matrix2: Matrix):
#         if matrix1.data.shape[1] == matrix2.data.shape[0]:
#             return matrix1.data.dot(matrix2.data)
#         else:
#             raise Exception("矩阵不同型")

#     # 矩阵数乘
#     @classmethod
#     def number_mul(cls, matrix1: Matrix, n):

#     # 矩阵是否可交换
#     def is_exchange(self):
#         # 要特别注意 若有两个矩阵AB 满足AB=0 不能得出 A=0 或 B=0
#         # 若A！=0 而A（X-Y）= 0  也不能得出 X=Y的结论
#         if self.matrix1.data.shape[1]==self.matrix2.data.shape[0] and self.matrix1.data.shape[0]==self.matrix2.data.shape[1]:
#             if self.mul2(self.matrix1,self.matrix2)==self.mul2(self.matrix2,self.matrix1):
#                 return True
#             else:
#                 return False
#         else:
#             raise Exception("矩阵不同型")


if __name__ == '__main__':
    [[3, -1],
     [1, 3]]

    A = Matrix(np.array([[-2, 1, 1],
                         [0, 2, 0],
                         [-4, 1, 3]]))

    A.values

    A.vactor

    A.data