algoritmo "fibonacci"
// Autor : Eduardo Henrique
// Data : 29/03/2022
// Se��o de Declara��es 
// =================================================================================
// Pesquisa sobre s�rie de Fibonacci e implementa��o no algoritmo pedido abaixoSabemos que
// os dois primeiros n�meros da s�rie de Fibonacci s�o o n�mero 1 e que a partir deles,
// calculamos o n�mero subsequente sempre fazendo a soma dos dois �ltimos. Fa�a um
// que imprima os 20 primeiros n�meros da s�rie de Fibonacci.
// Obs: f�rmula de forma��o da s�rie de Fibonaci abaixo utilize no algoritmo
// P=Posi��o; (n)=Numero; P(1)=P(2)=1; P(n)=P(n-1)+P(n-2)
// ==================================================================================
Var
v: vetor[0..2] de inteiro
limite, cont: inteiro
Inicio
escreva("Digite um limite: ")
leia(limite)
v[0] <- -1
v[1] <- 1
cont <- 0

enquanto cont < limite faca
v[2] <- v[0] + v[1]
v[0] <- v[1]
v[1] <- v[2]
escreva(v[2])
cont <- cont+1
fimenquanto
Fimalgoritmo
