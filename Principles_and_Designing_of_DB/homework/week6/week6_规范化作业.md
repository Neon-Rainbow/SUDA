> 2127405048 方浩楠 规范化作业

# 8.1

> Suppose that we decompose the schema $R = (A, B, C, D, E)$ into 
> $$
> (A, B, C) \\
> (A, D, E)
> $$
> Show that this decomposition is a lossless decomposition if the following
> set $F$ of functional dependencies holds: 
> $$
> A \rightarrow BC   \\
> CD \rightarrow E  \\
> B \rightarrow D  \\
> E \rightarrow A  \\
> $$

answer:

$$
\begin{aligned}
&A\rightarrow BC,B\rightarrow D \Rightarrow A \rightarrow D \newline
&A\rightarrow BC,A\rightarrow D \Rightarrow A \rightarrow CD \newline
&A\rightarrow CD,CD\rightarrow E \Rightarrow A \rightarrow E \newline
&综上所述,A \rightarrow ABCDE,(A)^+ = ABCDE \newline
&令R_1 = (A,B,C),R_2 = (A,D,E) \newline 
&因为R_1 \cap R_2 = A,A \rightarrow ABC \\
&因此R_1 \cap R_2 \rightarrow R_1 成立 \\
&综上所述,该分解是无损分解
\end{aligned}
$$



# 8.6

> Compute the closure of the following set $F$ of functional dependencies 
> for relation schema $R = (A, B, C, D, E)$. 
> $$
> A \rightarrow BC \\ 
> CD \rightarrow E \\ 
> B \rightarrow D \\
> E \rightarrow A 
> $$
>
> List the candidate keys for $R$. 

$$
\begin{aligned}
&由8.1得,A是候选码 \\
&E \rightarrow A \Rightarrow E \rightarrow ABCDE \qquad 因此E是候选码 \\
&CD \rightarrow E \Rightarrow CD \rightarrow ABCDE \qquad 因此CD是候选码\\
&B \rightarrow D \Rightarrow BC \rightarrow CD \\
&BC \rightarrow CD,CD \rightarrow E \Rightarrow BC \rightarrow E \Rightarrow BC \rightarrow ABCDE \qquad 因此BC是候选码\\
&候选码:A,BC,CD,E \\
&令\alpha为{A,B,C,D,E}中的任意一种组合,*表示F中任意一种属性 \\
&F^+ = \left\{A* \rightarrow \alpha,BC* \rightarrow \alpha,CD* \rightarrow \alpha,E \rightarrow \alpha,B \rightarrow B,B \rightarrow D,BD \rightarrow B,BD \rightarrow D,BD \rightarrow BD,C \rightarrow C,D \rightarrow D\right\}
\end{aligned}
$$


# 8.13

> Show that the decomposition in Exercise 8.1 is not a dependency-preserving decomposition.

answer:

有几个函数依赖在分解后未能保持.例如$B\rightarrow D$在$R_1$和$R_2$上均未保留,因此不是保持依赖的分解

# 8.30

> Consider the following set $F$ of functional dependencies on the relation 
> schema $(A, B, C, D, E, G)$: 
>$$
> A \rightarrow BCD \\
> BC \rightarrow DE \\
> B \rightarrow D \\
> D \rightarrow A \\
> $$
> 
>a. Compute $B^+$.
> 
>b. Prove (using Armstrong's axioms) that $AG$ is a superkey. 
> 
>c. Compute a canonical cover for this set of functional dependencies $F$; give
> each step of your derivation with an explanation. 
> 
>d. Give a 3NF decomposition of the given schema based on a canonical cover. 
> 
>e. Give a BCNF decomposition of the given schema using the original set $F$ 
> of functional dependencies. 

## a

$B^+ = \left\{A,B,C,D,E\right\} $

## b

$$
A \rightarrow BCD \Rightarrow A \rightarrow BC \tag{合并率} \\
$$

$$
A \rightarrow BC,BC \rightarrow DE \Rightarrow A \rightarrow DE \tag{传递律} \\
$$

$$
A \rightarrow BC,A \rightarrow DE \Rightarrow A \rightarrow BCDE \tag{合并律} \\
$$

$$
A \subset A \Rightarrow A \rightarrow A \tag{自反律} \\
$$

$$
A \rightarrow A,A \rightarrow BCDE \Rightarrow A \rightarrow ABCDE \tag{合并律} \\
$$

$$
A \rightarrow ABCDE \Rightarrow AG \rightarrow ABCDEG \tag{增补律} \\
$$

$$
(AG)^+ = ABCDEG \\
综上,AG是超码
$$



## c

$$
\begin{aligned}
&D在A \rightarrow BCD中无关,因为F逻辑蕴涵(F-\left\{A \rightarrow BCD\right\})\cup\left\{A \rightarrow BC\right\}.此断言为真,因为A \rightarrow BC,BC \rightarrow DE,所以(A)^+中包括D\\
&D在BC \rightarrow DE中无关,因为F逻辑蕴涵(F-\left\{BC \rightarrow DE\right\})\cup\left\{BC \rightarrow E\right\}.此断言为真,因为B \rightarrow D,所以(BC)^+中包括D\\
&综上,F的正则覆盖Fc = \left\{A \rightarrow BC,BC \rightarrow E,B \rightarrow D,D \rightarrow A\right\} \\
\end{aligned}
$$



## d

$$
\begin{aligned}
&A \rightarrow ABCDE \Rightarrow AG \rightarrow ABCDEG \\
&(AG)^+ = ABCDEG \\
&因此AG是R的一个候选码 \\
&Fc = \left\{A \rightarrow BC,BC \rightarrow E,B \rightarrow D,D \rightarrow A\right\} \\
&R_1 = ABC,R_2 = BCE,R_3 = BD,R_4 = DA \ 其中不包含候选码,所以添加R_5 = AG \\
&因此3NF分解为\left\{ABC,BCE,BD,DA,AG\right\} \\
\end{aligned}
$$



## e

$$
\begin{aligned}
&候选码:AG,BG,DG \quad F中不满足\alpha\rightarrow\beta是平凡的函数依赖或\alpha是超码,因此F不符合BCNF \\
&F=\left\{A\rightarrow BCD,BC \rightarrow DE,B\rightarrow D,D\rightarrow A\right\} \quad R=\left\{A,B,C,D,E,G\right\}\\
&result=\left\{R\right\}=\left\{R(A,B,C,D,E,G)\right\}\\
&B\rightarrow D不符合BCNF \\
&result=\left\{R_1,R_2\right\}=\left\{R_1(B,D),R_2(A,B,C,E,G)\right\}\\
&R_1(B,D)符合BCNF,因为B\rightarrow D,其中(B)^+ =\left\{B,D\right\},B是R_1的超码  \\
&R_2(A,B,C,E,G)不符合BCNF,因为其中A\rightarrow BC不满足\\
&result=\left\{R_1,R_2,R_3\right\} = \left\{R_1(B,D),R_2(A,B,C),R_3(A,E,G)\right\}\\
&R_2(A,B,C)符合BCNF,因为A\rightarrow BC,其中(A)^+ = \left\{ABC\right\},A是R_2的超码\\
&R_3(A,E,G)不符合BCNF,因为R_3中A\rightarrow E不满足\\
&result=\left\{R_1,R_2,R_3,R_4\right\} = \left\{R_1(B,D),R_2(A,B,C),R_3(A,E),R_4(A,G)\right\}\\
&其中result中的所有关系均满足BCNF \\
&F的BCNF分解的结果:result=\left\{R_1(B,D),R_2(A,B,C),R_3(A,E),R_4(A,G)\right\} \\
\end{aligned}
$$



# 8.31

> Consider the schema $R = (A,B,C,D,E,G)$ and the set $F$ of functional dependencies: 
> $$
> AB \rightarrow CD  \\
> B \rightarrow D  \\
> DE \rightarrow B \\
> DEG \rightarrow AB \\
> AC \rightarrow DE  \\
> $$
>
> $R$ is not in BCNF for many reasons, one of which arises from the functional 
> dependency $AB \rightarrow CD$. Explain why $AB \rightarrow CD$ shows that 
> $R$ is not in BCNF and then use the BCNF decomposition algorithm starting with 
> $AB \rightarrow CD$ to generate a BCNF decomposition of $R$. Once that is done, 
> determine whether your result is or is not dependency preserving, and explain 
> your reasoning.

+ R的BCNF分解

$$
\begin{aligned}
&R=(A,B,C,D,E,G)\\
&F=\left\{AB\rightarrow CD,B\rightarrow D,DE \rightarrow B,DEG \rightarrow AB,AC \rightarrow DE\right\}\\
&AB\rightarrow CD不是平凡的函数依赖,且(AB)^+中不包括G,因此AB不是超码,所以AB\rightarrow CD不满足BCNF\\
&result=\left\{R\right\}=\left\{R(A,B,C,D,E,G)\right\}\\
&R中AB\rightarrow CD不符合BCNF,分解R为R(A,B,C,D),R(A,B,E,G)\\
&result=\left\{R_1,R_2\right\}=\left\{R_1(A,B,C,D),R_2(A,B,E,G)\right\}\\
&R_1中B\rightarrow D不符合BCNF,分解R_1为R(B,D),R(A,B,C)\\
&result=\left\{R_1,R_2,R_3\right\}=\left\{R_1(B,D),R_2(A,B,C),R_3(A,B,E,G)\right\}\\
&R_3中AB\rightarrow E不符合BCNF,分解R_3为R(A,B,E),R(A,B,G)\\
&result=\left\{R_1,R_2,R_3,R_4\right\}=\left\{R_1(B,D),R_2(A,B,C),R_3(A,B,E),R_4(A,B,G)\right\}\\
&此时result中的每个关系都符合BCNF,因此R的BCNF为:\\
&result=\left\{R_1,R_2,R_3,R_4\right\}=\left\{R_1(B,D),R_2(A,B,C),R_3(A,B,E),R_4(A,B,G)\right\}\\
\end{aligned}
$$

+ BCNF分解的结果是否保持依赖

BCNF的结果不保持依赖,例如$DE \rightarrow B$的函数依赖不存在在分解之后的任何一个关系R中
