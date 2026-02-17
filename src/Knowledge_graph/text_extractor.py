import re

from llm import chat_completion

# This is the variable containing the text you pasted above
latex_content = r"""
\section*{MATRICES}

\section*{The essence of Mathematics lies in its freedom．－CANTOR}

\section*{3．1 Introduction}

The knowledge of matrices is necessary in various branches of mathematics．Matrices are one of the most powerful tools in mathematics．This mathematical tool simplifies our work to a great extent when compared with other straight forward methods．The evolution of concept of matrices is the result of an attempt to obtain compact and simple methods of solving system of linear equations．Matrices are not only used as a representation of the coefficients in system of linear equations，but utility of matrices far exceeds that use．Matrix notation and operations are used in electronic spreadsheet programs for personal computer，which in turn is used in different areas of business and science like budgeting，sales projection，cost estimation，analysing the results of an experiment etc．Also，many physical operations such as magnification，rotation and reflection through a plane can be represented mathematically by matrices．Matrices are also used in cryptography．This mathematical tool is not only used in certain branches of sciences，but also in genetics，economics，sociology，modern psychology and industrial management．

In this chapter，we shall find it interesting to become acquainted with the fundamentals of matrix and matrix algebra．

\section*{3．2 Matrix}

Suppose we wish to express the information that Radha has 15 notebooks．We may express it as［15］with the understanding that the number inside［ ］is the number of notebooks that Radha has．Now，if we have to express that Radha has 15 notebooks and 6 pens．We may express it as［15 6］with the understanding that first number inside［ ］is the number of notebooks while the other one is the number of pens possessed by Radha．Let us now suppose that we wish to express the information of possession
of notebooks and pens by Radha and her two friends Fauzia and Simran which is as follows:

\begin{tabular}{llllll} 
Radha & has & 15 & notebooks & and & 6 pens, \\
Fauzia & has & 10 & notebooks & and & 2 pens, \\
Simran & has & 13 & notebooks & and & 5 pens.
\end{tabular}

Now this could be arranged in the tabular form as follows:

\begin{tabular}{lcc} 
& Notebooks & Pens \\
Radha & 15 & 6 \\
Fauzia & 10 & 2 \\
Simran & 13 & 5
\end{tabular}
and this can be expressed as
![](https://cdn.mathpix.com/cropped/ff5fa1a1-4942-472a-b762-16ec8077ff68-02.jpg?height=396&width=630&top_left_y=959&top_left_x=526)
or

\begin{tabular}{lccc} 
& Radha & Fauzia & Simran \\
Notebooks & 15 & 10 & 13 \\
Pens & 6 & 2 & 5
\end{tabular}
which can be expressed as:
![](https://cdn.mathpix.com/cropped/ff5fa1a1-4942-472a-b762-16ec8077ff68-02.jpg?height=296&width=775&top_left_y=1677&top_left_x=456)

In the first arrangement the entries in the first column represent the number of note books possessed by Radha, Fauzia and Simran, respectively and the entries in the second column represent the number of pens possessed by Radha, Fauzia and Simran,
respectively. Similarly, in the second arrangement, the entries in the first row represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively. The entries in the second row represent the number of pens possessed by Radha, Fauzia and Simran, respectively. An arrangement or display of the above kind is called a matrix. Formally, we define matrix as:
Definition 1 A matrix is an ordered rectangular array of numbers or functions. The numbers or functions are called the elements or the entries of the matrix.

We denote matrices by capital letters. The following are some examples of matrices:
$$
\mathrm{A}=\left[\begin{array}{cc}
-2 & 5 \\
0 & \sqrt{5} \\
3 & 6
\end{array}\right], \mathrm{B}=\left[\begin{array}{ccc}
2+i & 3 & -\frac{1}{2} \\
3.5 & -1 & 2 \\
\sqrt{3} & 5 & \frac{5}{7}
\end{array}\right], \mathrm{C}=\left[\begin{array}{ccc}
1+x & x^{3} & 3 \\
\cos x & \sin x+2 & \tan x
\end{array}\right]
$$

In the above examples, the horizontal lines of elements are said to constitute, rows of the matrix and the vertical lines of elements are said to constitute, columns of the matrix. Thus A has 3 rows and 2 columns, B has 3 rows and 3 columns while C has 2 rows and 3 columns.

\subsection*{3.2.1 Order of a matrix}

A matrix having $m$ rows and $n$ columns is called a matrix of order $m \times n$ or simply $m \times n$ matrix (read as an $m$ by $n$ matrix). So referring to the above examples of matrices, we have A as $3 \times 2$ matrix, B as $3 \times 3$ matrix and C as $2 \times 3$ matrix. We observe that A has $3 \times 2=6$ elements, B and C have 9 and 6 elements, respectively.

In general, an $m \times n$ matrix has the following rectangular array:
$$
\left[\begin{array}{ccccccc}
a_{11} & a_{12} & a_{13} & \ldots & a_{1 j} & \ldots & a_{1 n} \\
a_{21} & a_{22} & a_{23} & \ldots & a_{2 j} & \ldots & a_{2 n} \\
\dot{\dot{a}}_{i 1} & \dot{\dot{a}}_{i 2} & \dot{a}_{i 3} & \ldots & \dot{a}_{i j} & \ldots & \dot{a}_{i n} \\
\dot{\dot{a}}_{m 1} & \dot{\dot{a}}_{m 2} & \dot{a}_{m 3} & \ldots & \dot{a}_{m j} & \ldots & \dot{a}_{m n}
\end{array}\right]_{m \times n}
$$
or $\mathrm{A}=\left[a_{i j}\right]_{m \times n}, 1 \leq i \leq m, 1 \leq j \leq n \quad i, j \in \mathrm{~N}$
Thus the $i^{\text {th }}$ row consists of the elements $a_{i 1}, a_{i 2}, a_{i 3}, \ldots, a_{i n}$, while the $j^{\text {th }}$ column consists of the elements $a_{1 j}, a_{2 j}, a_{3 j}, \ldots, a_{m j}$,

In general $a_{i j}$, is an element lying in the $i^{\text {th }}$ row and $j^{\text {th }}$ column. We can also call it as the $(i, j)^{\text {th }}$ element of A . The number of elements in an $m \times n$ matrix will be equal to $m n$.

\section*{Note In this chapter}
1. We shall follow the notation, namely $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ to indicate that A is a matrix of order $m \times n$.
2. We shall consider only those matrices whose elements are real numbers or functions taking real values.

We can also represent any point $(x, y)$ in a plane by a matrix (column or row) as $\left[\begin{array}{l}x \\ y\end{array}\right]$ (or $[x, y]$ ). For example point $\mathrm{P}(0,1)$ as a matrix representation may be given as
$$
\mathrm{P}=\left[\begin{array}{l}
0 \\
1
\end{array}\right] \text { or }\left[\begin{array}{ll}
0 & 1
\end{array}\right] .
$$

Observe that in this way we can also express the vertices of a closed rectilinear figure in the form of a matrix. For example, consider a quadrilateral ABCD with vertices $\mathrm{A}(1,0), \mathrm{B}(3,2), \mathrm{C}(1,3), \mathrm{D}(-1,2)$.

Now, quadrilateral ABCD in the matrix form, can be represented as
$$
\mathrm{X}=\begin{array}{cccc}
\mathrm{A} & \mathrm{~B} & \mathrm{C} & \mathrm{D} \\
{\left[\begin{array}{cccr}
1 & 3 & 1 & -1 \\
0 & 2 & 3 & 2
\end{array}\right]_{2 \times 4}}
\end{array}
$$
$$
\text { or } \quad Y=\begin{aligned}
& A \\
& B \\
& C \\
& D
\end{aligned}\left[\begin{array}{rr}
1 & 0 \\
3 & 2 \\
1 & 3 \\
-1 & 2
\end{array}\right]_{4 \times 2}
$$

Thus, matrices can be used as representation of vertices of geometrical figures in a plane.

Now, let us consider some examples.
Example 1 Consider the following information regarding the number of men and women workers in three factories I, II and III

\begin{tabular}{lcc} 
& Men workers & Women workers \\
I & 30 & 25 \\
II & 25 & 31 \\
III & 27 & 26
\end{tabular}

Represent the above information in the form of a $3 \times 2$ matrix. What does the entry in the third row and second column represent?

Solution The information is represented in the form of a $3 \times 2$ matrix as follows:
$$
A=\left[\begin{array}{ll}
30 & 25 \\
25 & 31 \\
27 & 26
\end{array}\right]
$$

The entry in the third row and second column represents the number of women workers in factory III.

Example 2 If a matrix has 8 elements, what are the possible orders it can have?
Solution We know that if a matrix is of order $m \times n$, it has $m n$ elements. Thus, to find all possible orders of a matrix with 8 elements, we will find all ordered pairs of natural numbers, whose product is 8 .
Thus, all possible ordered pairs are $(1,8),(8,1),(4,2),(2,4)$
Hence, possible orders are $1 \times 8,8 \times 1,4 \times 2,2 \times 4$
Example 3 Construct a $3 \times 2$ matrix whose elements are given by $a_{i j}=\frac{1}{2}|i-3 j|$.
Solution In general a $3 \times 2$ matrix is given by $\mathrm{A}=\left[\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22} \\ a_{31} & a_{32}\end{array}\right]$.
Now
$$
a_{i j}=\frac{1}{2}|i-3 j|, i=1,2,3 \text { and } j=1,2 .
$$

Therefore
$$
\begin{array}{ll}
a_{11}=\frac{1}{2}|1-3 \times 1|=1 & a_{12}=\frac{1}{2}|1-3 \times 2|=\frac{5}{2} \\
a_{21}=\frac{1}{2}|2-3 \times 1|=\frac{1}{2} & a_{22}=\frac{1}{2}|2-3 \times 2|=2 \\
a_{31}=\frac{1}{2}|3-3 \times 1|=0 & a_{32}=\frac{1}{2}|3-3 \times 2|=\frac{3}{2}
\end{array}
$$

Hence the required matrix is given by $\mathrm{A}=\left[\begin{array}{cc}1 & \frac{5}{2} \\ \frac{1}{2} & 2 \\ 0 & \frac{3}{2}\end{array}\right]$.

\subsection*{3.3 Types of Matrices}

In this section, we shall discuss different types of matrices.
(i) Column matrix

A matrix is said to be a column matrix if it has only one column.
For example, $\mathrm{A}=\left[\begin{array}{c}0 \\ \sqrt{3} \\ -1 \\ 1 / 2\end{array}\right]$ is a column matrix of order $4 \times 1$.
In general, $\mathrm{A}=\left[a_{i j}\right]_{m \times 1}$ is a column matrix of order $m \times 1$.
(ii) Row matrix

A matrix is said to be a row matrix if it has only one row.
For example, $\mathrm{B}=\left[\begin{array}{llll}-\frac{1}{2} & \sqrt{5} & 2 & 3\end{array}\right]_{1 \times 4}$ is a row matrix.
In general, $\mathrm{B}=\left[b_{i j}\right]_{1 \times n}$ is a row matrix of order $1 \times n$.
(iii) Square matrix

A matrix in which the number of rows are equal to the number of columns, is said to be a square matrix. Thus an $m \times n$ matrix is said to be a square matrix if $m=n$ and is known as a square matrix of order ' $n$ '.

For example $\mathrm{A}=\left[\begin{array}{ccc}3 & -1 & 0 \\ \frac{3}{2} & 3 \sqrt{2} & 1 \\ 4 & 3 & -1\end{array}\right]$ is a square matrix of order 3 .
In general, $\mathrm{A}=\left[a_{i j}\right]_{m \times m}$ is a square matrix of order $m$.
□ Note If $\mathrm{A}=\left[a_{i j}\right]$ is a square matrix of order $n$, then elements (entries) $a_{11}, a_{22}, \ldots, a_{n n}$ are said to constitute the diagonal, of the matrix A . Thus, if $\mathrm{A}=\left[\begin{array}{ccc}1 & -3 & 1 \\ 2 & 4 & -1 \\ 3 & 5 & 6\end{array}\right]$.
Then the elements of the diagonal of A are $1,4,6$.
(iv) Diagonal matrix

A square matrix $\mathrm{B}=\left[b_{i j}\right]_{m \times m}$ is said to be a diagonal matrix if all its non diagonal elements are zero, that is a matrix $\mathrm{B}=\left[b_{i j}\right]_{m \times m}$ is said to be a diagonal matrix if $b_{i j}=0$, when $i \neq j$.
For example, $\mathrm{A}=[4], \mathrm{B}=\left[\begin{array}{cc}-1 & 0 \\ 0 & 2\end{array}\right], \mathrm{C}=\left[\begin{array}{ccc}-1.1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3\end{array}\right]$, are diagonal matrices of order $1,2,3$, respectively.
(v) Scalar matrix

A diagonal matrix is said to be a scalar matrix if its diagonal elements are equal, that is, a square matrix $\mathrm{B}=\left[b_{i j}\right]_{n \times n}$ is said to be a scalar matrix if
$$
\begin{aligned}
& b_{i j}=0, \quad \text { when } i \neq j \\
& b_{i j}=k, \quad \text { when } i=j, \text { for some constant } k .
\end{aligned}
$$

For example
$$
\mathrm{A}=[3], \quad \mathrm{B}=\left[\begin{array}{cc}
-1 & 0 \\
0 & -1
\end{array}\right], \quad \mathrm{C}=\left[\begin{array}{ccc}
\sqrt{3} & 0 & 0 \\
0 & \sqrt{3} & 0 \\
0 & 0 & \sqrt{3}
\end{array}\right]
$$
are scalar matrices of order 1, 2 and 3, respectively.

\section*{(vi) Identity matrix}

A square matrix in which elements in the diagonal are all 1 and rest are all zero is called an identity matrix. In other words, the square matrix $\mathrm{A}=\left[a_{i j}\right]_{n \times n}$ is an identity matrix, if $a_{i j}=\left\{\begin{array}{ll}1 & \text { if } \quad i=j \\ 0 & \text { if } \quad i \neq j\end{array}\right.$.
We denote the identity matrix of order $n$ by $\mathrm{I}_{n}$. When order is clear from the context, we simply write it as I.

For example [1], [ $\left.\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right],\left[\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right]$ are identity matrices of order 1, 2 and 3, respectively.
Observe that a scalar matrix is an identity matrix when $k=1$. But every identity matrix is clearly a scalar matrix.

\section*{(vii) Zero matrix}

A matrix is said to be zero matrix or null matrix if all its elements are zero.
For example, $[0],\left[\begin{array}{ll}0 & 0 \\ 0 & 0\end{array}\right],\left[\begin{array}{lll}0 & 0 & 0 \\ 0 & 0 & 0\end{array}\right],[0,0]$ are all zero matrices. We denote zero matrix by O . Its order will be clear from the context.

\subsection*{3.3.1 Equality of matrices}

Definition 2 Two matrices $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ are said to be equal if
(i) they are of the same order
(ii) each element of A is equal to the corresponding element of B , that is $a_{i j}=b_{i j}$ for all $i$ and $j$.
For example, $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ and $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ are equal matrices but $\left[\begin{array}{ll}3 & 2 \\ 0 & 1\end{array}\right]$ and $\left[\begin{array}{ll}2 & 3 \\ 0 & 1\end{array}\right]$ are not equal matrices. Symbolically, if two matrices A and B are equal, we write $\mathrm{A}=\mathrm{B}$.

If $\left[\begin{array}{cc}x & y \\ z & a \\ b & c\end{array}\right]=\left[\begin{array}{cc}-1.5 & 0 \\ 2 & \sqrt{6} \\ 3 & 2\end{array}\right]$, then $x=-1.5, y=0, z=2, a=\sqrt{6}, b=3, c=2$
Example 4 If $\left[\begin{array}{ccc}x+3 & z+4 & 2 y-7 \\ -6 & a-1 & 0 \\ b-3 & -21 & 0\end{array}\right]=\left[\begin{array}{ccc}0 & 6 & 3 y-2 \\ -6 & -3 & 2 c+2 \\ 2 b+4 & -21 & 0\end{array}\right]$
Find the values of $a, b, c, x, y$ and $z$.
Solution As the given matrices are equal, therefore, their corresponding elements must be equal. Comparing the corresponding elements, we get
$$
\begin{array}{rlrl}
x+3=0, & z+4=6, & 2 y-7=3 y-2 \\
a-1=-3, & 0=2 c+2 & b-3=2 b+4
\end{array}
$$

Simplifying, we get
$$
a=-2, b=-7, c=-1, x=-3, y=-5, z=2
$$

Example 5 Find the values of $a, b, c$, and $d$ from the following equation:
$$
\left[\begin{array}{cc}
2 a+b & a-2 b \\
5 c-d & 4 c+3 d
\end{array}\right]=\left[\begin{array}{cc}
4 & -3 \\
11 & 24
\end{array}\right]
$$

Solution By equality of two matrices, equating the corresponding elements, we get
$$
\begin{array}{rlrl}
2 a+b & =4 & 5 c-d & =11 \\
a-2 b & =-3 & 4 c+3 d & =24
\end{array}
$$

Solving these equations, we get
$$
a=1, b=2, c=3 \text { and } d=4
$$

\section*{EXERCISE 3.1}
1. In the matrix $\mathrm{A}=\left[\begin{array}{cccc}2 & 5 & 19 & -7 \\ 35 & -2 & \frac{5}{2} & 12 \\ \sqrt{3} & 1 & -5 & 17\end{array}\right]$, write:
(i) The order of the matrix,
(ii) The number of elements,
(iii) Write the elements $a_{13}, a_{21}, a_{33}, a_{24}, a_{23}$.
2. If a matrix has 24 elements, what are the possible orders it can have? What, if it has 13 elements?
3. If a matrix has 18 elements, what are the possible orders it can have? What, if it has 5 elements?
4. Construct a $2 \times 2$ matrix, $\mathrm{A}=\left[a_{i j}\right]$, whose elements are given by:
(i) $a_{i j}=\frac{(i+j)^{2}}{2}$
(ii) $a_{i j}=\frac{i}{j}$
(iii) $a_{i j}=\frac{(i+2 j)^{2}}{2}$
5. Construct a $3 \times 4$ matrix, whose elements are given by:
(i) $a_{i j}=\frac{1}{2}|-3 i+j|$
(ii) $a_{i j}=2 i-j$
6. Find the values of $x, y$ and $z$ from the following equations:
(i) $\left[\begin{array}{ll}4 & 3 \\ x & 5\end{array}\right]=\left[\begin{array}{ll}y & z \\ 1 & 5\end{array}\right]$
(ii) $\left[\begin{array}{cc}x+y & 2 \\ 5+z & x y\end{array}\right]=\left[\begin{array}{ll}6 & 2 \\ 5 & 8\end{array}\right]$
(iii) $\left[\begin{array}{c}x+y+z \\ x+z \\ y+z\end{array}\right]=\left[\begin{array}{l}9 \\ 5 \\ 7\end{array}\right]$
7. Find the value of $a, b, c$ and $d$ from the equation:
$$
\left[\begin{array}{cc}
a-b & 2 a+c \\
2 a-b & 3 c+d
\end{array}\right]=\left[\begin{array}{cc}
-1 & 5 \\
0 & 13
\end{array}\right]
$$
8. $\mathrm{A}=\left[a_{i j}\right]_{m \times n!}$ is a square matrix, if
(A) $m<n$
(B) $m>n$
(C) $m=n$
(D) None of these
9. Which of the given values of $x$ and $y$ make the following pair of matrices equal $\left[\begin{array}{cc}3 x+7 & 5 \\ y+1 & 2-3 x\end{array}\right],\left[\begin{array}{cc}0 & y-2 \\ 8 & 4\end{array}\right]$
(A) $x=\frac{-1}{3}, y=7$
(B) Not possible to find
(C) $y=7, x=\frac{-2}{3}$
(D) $x=\frac{-1}{3}, y=\frac{-2}{3}$
10. The number of all possible matrices of order $3 \times 3$ with each entry 0 or 1 is:
(A) 27
(B) 18
(C) 81
(D) 512

\subsection*{3.4 Operations on Matrices}

In this section, we shall introduce certain operations on matrices, namely, addition of matrices, multiplication of a matrix by a scalar, difference and multiplication of matrices.

\subsection*{3.4.1 Addition of matrices}

Suppose Fatima has two factories at places A and B . Each factory produces sport shoes for boys and girls in three different price categories labelled 1,2 and 3 . The quantities produced by each factory are represented as matrices given below:

\begin{tabular}{ccc} 
& \multicolumn{2}{c}{ Factory at A } \\
& Boys & Gactory at B \\
1 \\
2 \\
3
\end{tabular}$\left[\begin{array}{cc}80 & 60 \\
75 & 65 \\
90 & 85\end{array}\right] \quad$\begin{tabular}{c} 
Boys \\
Girls
\end{tabular}$\quad$\begin{tabular}{c}
1 \\
2 \\
3
\end{tabular}$\left[\begin{array}{cc}90 & 50 \\
70 & 55 \\
75 & 75\end{array}\right]$.

Suppose Fatima wants to know the total production of sport shoes in each price category. Then the total production

In category 1 : for boys $(80+90)$, for girls $(60+50)$
In category 2 : for boys $(75+70)$, for girls $(65+55)$
In category 3 : for boys $(90+75)$, for girls $(85+75)$
This can be represented in the matrix form as $\left[\begin{array}{ll}80+90 & 60+50 \\ 75+70 & 65+55 \\ 90+75 & 85+75\end{array}\right]$.

This new matrix is the sum of the above two matrices. We observe that the sum of two matrices is a matrix obtained by adding the corresponding elements of the given matrices. Furthermore, the two matrices have to be of the same order.

Thus, if $\mathrm{A}=\left[\begin{array}{ccc}a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23}\end{array}\right]$ is a $2 \times 3$ matrix and $\mathrm{B}=\left[\begin{array}{lll}b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23}\end{array}\right]$ is another $2 \times 3$ matrix. Then, we define $\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}a_{11}+b_{11} & a_{12}+b_{12} & a_{13}+b_{13} \\ a_{21}+b_{21} & a_{22}+b_{22} & a_{23}+b_{23}\end{array}\right]$.

In general, if $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ are two matrices of the same order, say $m \times n$. Then, the sum of the two matrices A and B is defined as a matrix $\mathrm{C}=\left[c_{i j}\right]_{m \times n}$, where $c_{i j}=a_{i j}+b_{i j}$, for all possible values of $i$ and $j$.

Example 6 Given $\mathrm{A}=\left[\begin{array}{ccc}\sqrt{3} & 1 & -1 \\ 2 & 3 & 0\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ccc}2 & \sqrt{5} & 1 \\ -2 & 3 & \frac{1}{2}\end{array}\right]$, find $\mathrm{A}+\mathrm{B}$
Since A , B are of the same order $2 \times 3$. Therefore, addition of A and B is defined and is given by
$$
A+B=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 1-1 \\
2-2 & 3+3 & 0+\frac{1}{2}
\end{array}\right]=\left[\begin{array}{ccc}
2+\sqrt{3} & 1+\sqrt{5} & 0 \\
0 & 6 & \frac{1}{2}
\end{array}\right]
$$

\section*{Note}
1. We emphasise that if A and B are not of the same order, then $\mathrm{A}+\mathrm{B}$ is not defined. For example if $\mathrm{A}=\left[\begin{array}{ll}2 & 3 \\ 1 & 0\end{array}\right], \mathrm{B}=\left[\begin{array}{lll}1 & 2 & 3 \\ 1 & 0 & 1\end{array}\right]$, then $\mathrm{A}+\mathrm{B}$ is not defined.
2. We may observe that addition of matrices is an example of binary operation on the set of matrices of the same order.

\subsection*{3.4.2 Multiplication of a matrix by a scalar}

Now suppose that Fatima has doubled the production at a factory A in all categories (refer to 3.4.1).

Previously quantities (in standard units) produced by factory A were

1
2
3 \begin{tabular}{cc} 
Boys & Girls \\
{$\left[\begin{array}{c}80 \\
75 \\
90\end{array}\right.$} & $\left.\begin{array}{c}60 \\
65 \\
85\end{array}\right]$
\end{tabular}

Revised quantities produced by factory A are as given below:

Boys Girls
$$
\begin{aligned}
& 1 \\
& 2 \\
& 3
\end{aligned}\left[\begin{array}{ll}
2 \times 80 & 2 \times 60 \\
2 \times 75 & 2 \times 65 \\
2 \times 90 & 2 \times 85
\end{array}\right]
$$

This can be represented in the matrix form as $\left[\begin{array}{cc}160 & 120 \\ 150 & 130 \\ 180 & 170\end{array}\right]$. We observe that the new matrix is obtained by multiplying each element of the previous matrix by 2 .

In general, we may define multiplication of a matrix by a scalar as follows: if $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ is a matrix and $k$ is a scalar, then $k \mathrm{~A}$ is another matrix which is obtained by multiplying each element of A by the scalar $k$.

In other words, $k \mathrm{~A}=k\left[a_{i j}\right]_{m \times n}=\left[k\left(a_{i j}\right)\right]_{m \times n}$, that is, $(i, j)^{\text {th }}$ element of $k \mathrm{~A}$ is $k a_{i j}$ for all possible values of $i$ and $j$.

For example, if $\quad \mathrm{A}=\left[\begin{array}{ccc}3 & 1 & 1.5 \\ \sqrt{5} & 7 & -3 \\ 2 & 0 & 5\end{array}\right]$, then
$$
3 \mathrm{~A}=3\left[\begin{array}{ccc}
3 & 1 & 1.5 \\
\sqrt{5} & 7 & -3 \\
2 & 0 & 5
\end{array}\right]=\left[\begin{array}{ccc}
9 & 3 & 4.5 \\
3 \sqrt{5} & 21 & -9 \\
6 & 0 & 15
\end{array}\right]
$$

Negative of a matrix the negative of a matrix is denoted by -A . We define $-\mathrm{A}=(-1) \mathrm{A}$.

For example, let
$$
\begin{aligned}
\mathrm{A} & =\left[\begin{array}{cc}
3 & 1 \\
-5 & x
\end{array}\right], \text { then }-\mathrm{A} \text { is given by } \\
-\mathrm{A} & =(-1) \mathrm{A}=(-1)\left[\begin{array}{cc}
3 & 1 \\
-5 & x
\end{array}\right]=\left[\begin{array}{cc}
-3 & -1 \\
5 & -x
\end{array}\right]
\end{aligned}
$$

Difference of matrices If $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right]$ are two matrices of the same order, say $m \times n$, then difference $\mathrm{A}-\mathrm{B}$ is defined as a matrix $\mathrm{D}=\left[d_{i j}\right]$, where $d_{i j}=a_{i j}-b_{i j}$, for all value of $i$ and $j$. In other words, $\mathrm{D}=\mathrm{A}-\mathrm{B}=\mathrm{A}+(-1) \mathrm{B}$, that is sum of the matrix A and the matrix -B .
Example 7 If $\mathrm{A}=\left[\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{rrr}3 & -1 & 3 \\ -1 & 0 & 2\end{array}\right]$, then find $2 \mathrm{~A}-\mathrm{B}$.
Solution We have
$$
\begin{aligned}
2 A-B & =2 \begin{array}{ccc}
1 & 2 & 3 \\
2 & 3 & 1
\end{array}-\begin{array}{rrr}
3 & -1 & 3 \\
-1 & 0 & 2
\end{array} \\
& =\left[\begin{array}{lll}
2 & 4 & 6 \\
4 & 6 & 2
\end{array}\right]+\left[\begin{array}{ccc}
-3 & 1 & -3 \\
1 & 0 & -2
\end{array}\right] \\
& =\left[\begin{array}{ccc}
2-3 & 4+1 & 6-3 \\
4+1 & 6+0 & 2-2
\end{array}\right]=\left[\begin{array}{ccc}
-1 & 5 & 3 \\
5 & 6 & 0
\end{array}\right]
\end{aligned}
$$

\subsection*{3.4.3 Properties of matrix addition}

The addition of matrices satisfy the following properties:
(i) Commutative Law If $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right]$ are matrices of the same order, say $m \times n$, then $\mathrm{A}+\mathrm{B}=\mathrm{B}+\mathrm{A}$.
Now
$$
\begin{aligned}
\mathrm{A}+\mathrm{B} & =\left[a_{i j}\right]+\left[b_{i j}\right]=\left[a_{i j}+b_{i j}\right] \\
& =\left[b_{i j}+a_{i j}\right] \text { (addition of numbers is commutative) } \\
& =\left(\left[b_{i j}\right]+\left[a_{i j}\right]\right)=\mathrm{B}+\mathrm{A}
\end{aligned}
$$
(ii) Associative Law For any three matrices $\mathrm{A}=\left[a_{i j}\right], \mathrm{B}=\left[b_{i j}\right], \mathrm{C}=\left[c_{i j}\right]$ of the same order, say $m \times n,(\mathrm{~A}+\mathrm{B})+\mathrm{C}=\mathrm{A}+(\mathrm{B}+\mathrm{C})$.
Now
$$
\begin{aligned}
(\mathrm{A}+\mathrm{B})+\mathrm{C} & =\left(\left[a_{i j}\right]+\left[b_{i j}\right]\right)+\left[c_{i j}\right] \\
& =\left[a_{i j}+b_{i j}\right]+\left[c_{i j}\right]=\left[\left(a_{i j}+b_{i j}\right)+c_{i j}\right] \\
& =\left[a_{i j}+\left(b_{i j}+c_{i j}\right)\right] \quad(\text { Why? }) \\
& =\left[a_{i j}\right]+\left[\left(b_{i j}+c_{i j}\right)\right]=\left[a_{i j}\right]+\left(\left[b_{i j}\right]+\left[c_{i j}\right]\right)=\mathrm{A}+(\mathrm{B}+\mathrm{C})
\end{aligned}
$$
(iii) Existence of additive identity Let $\mathrm{A}=\left[a_{i j}\right]$ be an $m \times n$ matrix and O be an $m \times n$ zero matrix, then $\mathrm{A}+\mathrm{O}=\mathrm{O}+\mathrm{A}=\mathrm{A}$. In other words, O is the additive identity for matrix addition.
(iv) The existence of additive inverse Let $\mathrm{A}=\left[a_{i j}\right]_{m \times n}$ be any matrix, then we have another matrix as $-\mathrm{A}=\left[-a_{i j}\right]_{m \times n}$ such that $\mathrm{A}+(-\mathrm{A})=(-\mathrm{A})+\mathrm{A}=\mathrm{O}$. So -A is the additive inverse of A or negative of A .

\subsection*{3.4.4 Properties of scalar multiplication of a matrix}

If $\mathrm{A}=\left[a_{i j}\right]$ and $\mathrm{B}=\left[b_{i j}\right]$ be two matrices of the same order, say $m \times n$, and $k$ and $l$ are scalars, then
(i) $k(\mathrm{~A}+\mathrm{B})=k \mathrm{~A}+k \mathrm{~B}$, (ii) $(k+l) \mathrm{A}=k \mathrm{~A}+l \mathrm{~A}$
(ii) $k(\mathrm{~A}+\mathrm{B})=k\left(\left[a_{i j}\right]+\left[b_{i j}\right]\right)$
$$
\begin{aligned}
& =k\left[a_{i j}+b_{i j}\right]=\left[k\left(a_{i j}+b_{i j}\right)\right]=\left[\left(k a_{i j}\right)+\left(k b_{i j}\right)\right] \\
& =\left[k a_{i j}\right]+\left[k b_{i j}\right]=k\left[a_{i j}\right]+k\left[b_{i j}\right]=k \mathrm{~A}+k \mathrm{~B}
\end{aligned}
$$
(iii) $(k+l) \mathrm{A}=(k+l)\left[a_{i j}\right]$
$$
=\left[(k+l) a_{i j}\right]+\left[k a_{i j}\right]+\left[l a_{i j}\right]=k\left[a_{i j}\right]+l\left[a_{i j}\right]=k \mathrm{~A}+l \mathrm{~A}
$$

Example 8 If $\mathrm{A}=\left[\begin{array}{cc}8 & 0 \\ 4 & -2 \\ 3 & 6\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{cc}2 & -2 \\ 4 & 2 \\ -5 & 1\end{array}\right]$, then find the matrix X , such that $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$.

Solution We have $2 \mathrm{~A}+3 \mathrm{X}=5 \mathrm{~B}$
or
$$
2 A+3 X-2 A=5 B-2 A
$$
or
$$
2 A-2 A+3 X=5 B-2 A
$$
(Matrix addition is commutative)
or
$$
O+3 X=5 B-2 A
$$
( -2 A is the additive inverse of 2 A )
or
$$
3 X=5 B-2 A
$$
( O is the additive identity)
or
$$
X=\frac{1}{3}(5 B-2 A)
$$
or
$$
\mathrm{X}=\frac{1}{3}\left(5\left[\begin{array}{cc}
2 & -2 \\
4 & 2 \\
-5 & 1
\end{array}\right]-2\left[\begin{array}{cc}
8 & 0 \\
4 & -2 \\
3 & 6
\end{array}\right]\right)=\frac{1}{3}\left(\left[\begin{array}{cc}
10 & -10 \\
20 & 10 \\
-25 & 5
\end{array}\right]+\left[\begin{array}{cc}
-16 & 0 \\
-8 & 4 \\
-6 & -12
\end{array}\right]\right)
$$
$$
=\frac{1}{3}\left[\begin{array}{cc}
10-16 & -10+0 \\
20-8 & 10+4 \\
-25-6 & 5-12
\end{array}\right]=\frac{1}{3}\left[\begin{array}{cc}
-6 & -10 \\
12 & 14 \\
-31 & -7
\end{array}\right]=\left[\begin{array}{cc}
-2 & \frac{-10}{3} \\
4 & \frac{14}{3} \\
\frac{-31}{3} & \frac{-7}{3}
\end{array}\right]
$$

Example 9 Find X and Y , if $\mathrm{X}+\mathrm{Y}=\left[\begin{array}{ll}5 & 2 \\ 0 & 9\end{array}\right]$ and $\mathrm{X}-\mathrm{Y}=\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
Solution We have $(\mathrm{X}+\mathrm{Y})+(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{cc}5 & 2 \\ 0 & 9\end{array}\right]+\left[\begin{array}{cc}3 & 6 \\ 0 & -1\end{array}\right]$.
or
$$
\begin{aligned}
(\mathrm{X}+\mathrm{X})+(\mathrm{Y}-\mathrm{Y}) & =\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \Rightarrow 2 \mathrm{X}=\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right] \\
\mathrm{X} & =\frac{1}{2}\left[\begin{array}{ll}
8 & 8 \\
0 & 8
\end{array}\right]=\left[\begin{array}{ll}
4 & 4 \\
0 & 4
\end{array}\right]
\end{aligned}
$$
or
$$
(\mathrm{X}+\mathrm{Y})-(\mathrm{X}-\mathrm{Y})=\left[\begin{array}{ll}
5 & 2 \\
0 & 9
\end{array}\right]-\left[\begin{array}{rr}
3 & 6 \\
0 & -1
\end{array}\right]
$$

Also
$$
(\mathrm{X}-\mathrm{X})+(\mathrm{Y}+\mathrm{Y})=\left[\begin{array}{cc}
5-3 & 2-6 \\
0 & 9+1
\end{array}\right] \Rightarrow 2 \mathrm{Y}=\left[\begin{array}{ll}
2 & -4 \\
0 & 10
\end{array}\right]
$$
or
$$
\mathrm{Y}=\frac{1}{2}\left[\begin{array}{rr}
2 & -4 \\
0 & 10
\end{array}\right]=\left[\begin{array}{rr}
1 & -2 \\
0 & 5
\end{array}\right]
$$

Example 10 Find the values of $x$ and $y$ from the following equation:
$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{rr}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

Solution We have
$$
2\left[\begin{array}{cc}
x & 5 \\
7 & y-3
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right] \Rightarrow\left[\begin{array}{cc}
2 x & 10 \\
14 & 2 y-6
\end{array}\right]+\left[\begin{array}{cc}
3 & -4 \\
1 & 2
\end{array}\right]=\left[\begin{array}{cc}
7 & 6 \\
15 & 14
\end{array}\right]
$$

\begin{table}
\begin{tabular}{|l|l|}
\hline or & $\left[\begin{array}{cc}2 x+3 & 10-4 \\ 14+1 & 2 y-6+2\end{array}\right]=\left[\begin{array}{cc}7 & 6 \\ 15 & 14\end{array}\right] \Rightarrow\left[\begin{array}{cc}2 x+3 & 6 \\ 15 & 2 y-4\end{array}\right]=\left[\begin{array}{cc}7 & 6 \\ 15 & 14\end{array}\right]$ \\
\hline or & $2 x+3=7$ \\
\hline or & $2 x=7-3$ \\
\hline or & $x=\frac{4}{2}$ \\
\hline i.e. & $x=2$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{September Sales (in Rupees)}
\end{table}

Example 11 Two farmers Ramkishan and Gurcharan Singh cultivates only three varieties of rice namely Basmati, Permal and Naura. The sale (in Rupees) of these varieties of rice by both the farmers in the month of September and October are given by the following matrices A and B .
$$
\mathrm{A}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
10,000 & 20,000 & 30,000 \\
50,000 & 30,000 & 10,000
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$

October Sales (in Rupees)
$$
\mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$
(i) Find the combined sales in September and October for each farmer in each variety.
(ii) Find the decrease in sales from September to October.
(iii) If both farmers receive $2 \%$ profit on gross sales, compute the profit for each farmer and for each variety sold in October.

\section*{Solution}
(i) Combined sales in September and October for each farmer in each variety is given by
$$
\mathrm{A}+\mathrm{B}=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
15,000 & 30,000 & 36,000 \\
70,000 & 40,000 & 20,000
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$
(ii) Change in sales from September to October is given by
$$
A-B=\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 24,000 \\
30,000 & 20,000 & 0
\end{array}\right] \begin{aligned}
& \text { Ramkishan } \\
& \text { Gurcharan Singh }
\end{aligned}
$$
(iii) $2 \%$ of $\mathrm{B}=\frac{2}{100} \times \mathrm{B}=0.02 \times \mathrm{B}$
$$
\begin{aligned}
& =0.02\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
5000 & 10,000 & 6000 \\
20,000 & 10,000 & 10,000
\end{array}\right] \begin{array}{l}
\text { Ramkishan } \\
\text { Gurcharan Singh }
\end{array} \\
& =\left[\begin{array}{ccc}
\text { Basmati } & \text { Permal } & \text { Naura } \\
100 & 200 & 120 \\
400 & 200 & 200
\end{array}\right] \begin{array}{l}
\text { Ramkishan } \\
\text { Gurcharan Singh }
\end{array}
\end{aligned}
$$

Thus, in October Ramkishan receives ₹ 100 , ₹ 200 and ₹ 120 as profit in the sale of each variety of rice, respectively, and Grucharan Singh receives profit of ₹400, ₹ 200 and ₹ 200 in the sale of each variety of rice, respectively.

\subsection*{3.4.5 Multiplication of matrices}

Suppose Meera and Nadeem are two friends. Meera wants to buy 2 pens and 5 story books, while Nadeem needs 8 pens and 10 story books. They both go to a shop to enquire about the rates which are quoted as follows:
$$
\text { Pen - ₹ } 5 \text { each, story book - ₹ } 50 \text { each. }
$$

How much money does each need to spend? Clearly, Meera needs ₹ ( $5 \times 2+50 \times 5$ ) that is ₹260, while Nadeem needs $(8 \times 5+50 \times 10)$ ₹, that is ₹ 540 . In terms of matrix representation, we can write the above information as follows:
Requirements Prices per piece (in Rupees) Money needed (in Rupees)
$$
\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right] \quad\left[\begin{array}{c}
5 \\
50
\end{array}\right] \quad\left[\begin{array}{l}
5 \times 2+5 \times 50 \\
8 \times 5+10 \times 50
\end{array}\right]=\left[\begin{array}{c}
260 \\
540
\end{array}\right]
$$

Suppose that they enquire about the rates from another shop, quoted as follows:
$$
\text { pen - ₹ } 4 \text { each, story book - ₹ } 40 \text { each. }
$$

Now, the money required by Meera and Nadeem to make purchases will be respectively ₹ $(4 \times 2+40 \times 5)=₹ 208$ and ₹ $(8 \times 4+10 \times 40)=₹ 432$

Again, the above information can be represented as follows:

\section*{Requirements Prices per piece (in Rupees) Money needed (in Rupees)}
$$
\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right] \quad\left[\begin{array}{c}
4 \\
40
\end{array}\right] \quad\left[\begin{array}{c}
4 \times 2+40 \times 5 \\
8 \times 4+10 \times 40
\end{array}\right]=\left[\begin{array}{c}
208 \\
432
\end{array}\right]
$$

Now, the information in both the cases can be combined and expressed in terms of matrices as follows:

\section*{Requirements Prices per piece (in Rupees) Money needed (in Rupees)}
$$
\begin{gathered}
{\left[\begin{array}{cc}
2 & 5 \\
8 & 10
\end{array}\right] \quad\left[\begin{array}{cc}
5 & 4 \\
50 & 40
\end{array}\right] \quad\left[\begin{array}{ll}
5 \times 2+5 \times 50 & 4 \times 2+40 \times 5 \\
8 \times 5+10 \times 50 & 8 \times 4+10 \times 40
\end{array}\right]} \\
=\left[\begin{array}{cc}
260 & 208 \\
540 & 432
\end{array}\right]
\end{gathered}
$$

The above is an example of multiplication of matrices. We observe that, for multiplication of two matrices A and B , the number of columns in A should be equal to the number of rows in B . Furthermore for getting the elements of the product matrix, we take rows of A and columns of B , multiply them element-wise and take the sum. Formally, we define multiplication of matrices as follows:

The product of two matrices A and B is defined if the number of columns of A is equal to the number of rows of B . Let $\mathrm{A}=\left[a_{i j}\right]$ be an $m \times n$ matrix and $\mathrm{B}=\left[b_{j k}\right]$ be an $n \times p$ matrix. Then the product of the matrices A and B is the matrix C of order $m \times p$. To get the $(i, k)^{\text {th }}$ element $c_{i k}$ of the matrix C , we take the $i^{\text {th }}$ row of A and $k^{\text {th }}$ column of B , multiply them elementwise and take the sum of all these products. In other words, if $\mathrm{A}=\left[a_{i j}\right]_{m \times n}, \mathrm{~B}=\left[b_{j k}\right]_{n \times p}$, then the $i^{\text {th }}$ row of A is $\left[a_{i 1} a_{i 2} \ldots a_{i n}\right]$ and the $k^{\text {th }}$ column of B is $\left[\begin{array}{c}b_{1 k} \\ b_{2 k} \\ \vdots \\ \vdots \\ b_{n k}\end{array}\right]$, then $c_{i k}=a_{i 1} b_{1 k}+a_{i 2} b_{2 k}+a_{i 3} b_{3 k}+\ldots+a_{i n} b_{n k}=\sum_{j=1}^{n} a_{i j} b_{j k}$.

The matrix $\mathrm{C}=\left[c_{i k}\right]_{m \times p}$ is the product of A and B .
For example, if $\mathrm{C}=\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]$ and $\mathrm{D}=\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]$, then the product CD is defined
and is given by $\mathrm{CD}=\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]$. This is a $2 \times 2$ matrix in which each entry is the sum of the products across some row of C with the corresponding entries down some column of D. These four computations are
$\begin{aligned} & \text { Entry in } \\ & \text { first row } \\ & \text { first column }\end{aligned}\left[\begin{array}{ccc}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{cc}(1)(2)+(-1)(-1)+(2)(5) & ? \\ ? & ?\end{array}\right]$ Entry in
first row
second column $\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{cc}13 & (1)(7)+(-1)(1)+2(-4) \\ ? & ?\end{array}\right]$
$\begin{aligned} & \text { Entry in } \\ & \text { second row } \\ & \text { first column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{ll}13 & -2 \\ 0(2)+3(-1)+4(5) & ?\end{array}\right] \begin{aligned} & \text { Entry in } \\ & \text { second row } \\ & \text { second column }\end{aligned}\left[\begin{array}{rrr}1 & -1 & 2 \\ 0 & 3 & 4\end{array}\right]\left[\begin{array}{rr}2 & 7 \\ -1 & 1 \\ 5 & -4\end{array}\right]=\left[\begin{array}{ll}13 & -2 \\ 17 & 0(7)+3(1)+4(-4)\end{array}\right]$

Thus $\mathrm{CD}=\left[\begin{array}{ll}13 & -2 \\ 17 & -13\end{array}\right]$
Example 12 Find AB , if $\mathrm{A}=\left[\begin{array}{ll}6 & 9 \\ 2 & 3\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{lll}2 & 6 & 0 \\ 7 & 9 & 8\end{array}\right]$.
Solution The matrix A has 2 columns which is equal to the number of rows of B . Hence AB is defined. Now
$$
\begin{aligned}
\mathrm{AB} & =\left[\begin{array}{lll}
6(2)+9(7) & 6(6)+9(9) & 6(0)+9(8) \\
2(2)+3(7) & 2(6)+3(9) & 2(0)+3(8)
\end{array}\right] \\
& =\left[\begin{array}{ccc}
12+63 & 36+81 & 0+72 \\
4+21 & 12+27 & 0+24
\end{array}\right]=\left[\begin{array}{ccc}
75 & 117 & 72 \\
25 & 39 & 24
\end{array}\right]
\end{aligned}
$$

Remark If AB is defined, then BA need not be defined. In the above example, AB is defined but BA is not defined because B has 3 column while A has only 2 (and not 3 ) rows. If $\mathrm{A}, \mathrm{B}$ are, respectively $m \times n, k \times l$ matrices, then both AB and BA are defined if and only if $n=k$ and $l=m$. In particular, if both A and B are square matrices of the same order, then both AB and BA are defined.

\section*{Non-commutativity of multiplication of matrices}

Now, we shall see by an example that even if AB and BA are both defined, it is not necessary that $\mathrm{AB}=\mathrm{BA}$.

Example 13 If $\mathrm{A}=\left[\begin{array}{rrr}1 & -2 & 3 \\ -4 & 2 & 5\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}2 & 3 \\ 4 & 5 \\ 2 & 1\end{array}\right]$, then find $\mathrm{AB}, \mathrm{BA}$. Show that $\mathrm{AB} \neq \mathrm{BA}$.

Solution Since A is a $2 \times 3$ matrix and B is $3 \times 2$ matrix. Hence AB and BA are both defined and are matrices of order $2 \times 2$ and $3 \times 3$, respectively. Note that
and
$$
\begin{aligned}
& \mathrm{AB}=\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]=\left[\begin{array}{cc}
2-8+6 & 3-10+3 \\
-8+8+10 & -12+10+5
\end{array}\right]=\left[\begin{array}{cc}
0 & -4 \\
10 & 3
\end{array}\right] \\
& \mathrm{BA}=\left[\begin{array}{ll}
2 & 3 \\
4 & 5 \\
2 & 1
\end{array}\right]\left[\begin{array}{rrr}
1 & -2 & 3 \\
-4 & 2 & 5
\end{array}\right]=\left[\begin{array}{ccc}
2-12 & -4+6 & 6+15 \\
4-20 & -8+10 & 12+25 \\
2-4 & -4+2 & 6+5
\end{array}\right]=\left[\begin{array}{ccc}
-10 & 2 & 21 \\
-16 & 2 & 37 \\
-2 & -2 & 11
\end{array}\right]
\end{aligned}
$$

Clearly $\mathrm{AB} \neq \mathrm{BA}$
In the above example both AB and BA are of different order and so $\mathrm{AB} \neq \mathrm{BA}$. But one may think that perhaps AB and BA could be the same if they were of the same order. But it is not so, here we give an example to show that even if AB and BA are of same order they may not be same.

Example 14 If $\mathrm{A}=\left[\begin{array}{rr}1 & 0 \\ 0 & -1\end{array}\right]$ and $\mathrm{B}=\left[\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right]$, then $\mathrm{AB}=\left[\begin{array}{rr}0 & 1 \\ -1 & 0\end{array}\right]$.
and
$$
\mathrm{BA}=\left[\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right] . \text { Clearly } \mathrm{AB} \neq \mathrm{BA} .
$$

Thus matrix multiplication is not commutative.
"""

import re
import json
# from llm import chat_completion # Assuming this is your wrapper

# --- 1. Robust Chunking Function ---
def chunk_latex(text):
    # Improved Regex: Handles \section and \section* (optional asterisk)
    # Group 1: 'sub' (optional)
    # Group 2: Title
    pattern = r'\\(sub)?section\*?\{(.*?)\}'
    
    parts = re.split(pattern, text)
    chunks = {}
    
    # Capture introduction (text before the first section)
    if parts[0].strip():
        chunks["Introduction"] = parts[0].strip()
        
    # re.split returns: [content, 'sub'?, 'Title', content, 'sub'?, 'Title'...]
    # We step by 3 because there are 2 capturing groups + the content chunk
    i = 1
    while i < len(parts) - 1:
        is_sub = parts[i]  # captures 'sub' or None
        title = parts[i+1] # captures the title
        content = parts[i+2] # captures the text content
        
        # Create a unique key like "3.2 Matrix" or "Sub-Order of a Matrix"
        full_title = f"{'Sub-' if is_sub else ''}{title}"
        chunks[full_title] = content
        i += 3
        
    return chunks

# --- 2. Processing Loop ---

# Run the chunker
sections = chunk_latex(latex_content)
all_results = []

print(f"Found {len(sections)} sections. Starting extraction...\n")

for title, text_content in sections.items():
    # Skip very short chunks (e.g., just whitespace)
    if len(text_content) < 50:
        continue

    print(f"Processing: {title}...")

    # Dynamic Prompt for this specific chunk
    # Notice the f""" and passing text_content, not the whole dictionary
    prompt = f"""
    You are a Mathematician and Knowledge Graph Engineer.
    Task: Extract knowledge from the provided LaTeX text chunk.
    
    Input Text:
    {text_content}
    
    Rules:
    1. NODES: Identify Concepts (e.g., "Square Matrix"), Symbols (e.g., "$A=[a_{{ij}}]$"), and Properties.
    2. EDGES: Use relations like [DEFINED_AS, IS_A, HAS_PROPERTY, REQUIRES, EXAMPLE_OF].
    3. MATH: Keep equations in strict LaTeX format (e.g., use $...$).
    4. OUTPUT: Return strictly valid JSON only. No markdown formatting.
    
    Return JSON format:
    [{{"head": "Entity", "relation": "RELATION", "tail": "Entity"}}]
    """
    
    # Call your LLM function
    # Note: Ensure chat_completion returns a string
    try:
        response = chat_completion(prompt)
        
        # Attempt to parse the response as JSON to ensure it's valid
        # (LLMs sometimes add ```json at the start, stripping that helps)
        clean_response = response.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_response)
        
        # Tag the data with the source section and save it
        for item in data:
            item['source'] = title
            all_results.append(item)
            
    except Exception as e:
        print(f"Error processing {title}: {e}")


import json
from pathlib import Path

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

output_file = OUTPUT_DIR / "knowledge_triples.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print(f"Saved {len(all_results)} triples to {output_file}")


# --- 3. View Results ---
print(f"\nExtraction complete. Extracted {len(all_results)} triples.")
# Example: Print first 3 triples
print(json.dumps(all_results[:3], indent=2))