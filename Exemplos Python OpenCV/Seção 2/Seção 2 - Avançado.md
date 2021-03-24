# **Seção 2 - Avançado**


## **Espaço de cores**

Existem alguns espaços de cores que podem ser utilizados no openCV, alguns exemplos desses canais são o “Preto e Branco”, lab, HSV e o BGR (o BGR difere do tradicional RGB apenas pela ordenação das cores).
Para converter uma imagem de BGR (padrão do OpenCV) para outros espaços de cores faz se necessário a utilização da função cvtColor(),que recebe como parâmetro a imagem que se deseja alterar e o espaço de cores no qual a imagem se encontra e para qual se deseja mudar. 


**Exemplos:**

```
# BGR para Escala de Cinza
gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='Escala de cinza', mat=gray)

# BGR para HSV
hsv = cv.cvtColor(src=img, code=cv.COLOR_BGR2HSV)
cv.imshow(winname='HSV', mat=hsv)

# BGR para L*a*b
lab = cv.cvtColor(src=img, code=cv.COLOR_BGR2LAB)
cv.imshow(winname='LAB', mat=lab)

# BGR para RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow(winname='RGB', mat=rgb)

# L*a*b para BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow(winname='LAB para BGR', mat=lab_bgr)
```

## **Canais de cores**

Imagens em BGR possuem três canais de cores, uma para a cor azul (“blue”), uma para a cor verde (“green”) e uma outra para a cor vermelha (“red”). Utilizando OpenCv esses três canais podem ser separados e visualizados individualmente. Para realizar essa separação pode-se usar a função split(), que é responsável por separar os canais.

```
# Carregando uma imagem
img = cv.imread(filename=path)

# Utilizando o cv.split para conseguir obter cada imagens em escala # de cinza de cada cor separadamente 
b,g,r = cv.split(img)

# Exibindo das imagens adquiridas 
cv2.imshow("Azul", b)
cv2.imshow("Verde", g)
cv2.imshow("Vermelho", r)

cv2.waitKey(0)
```
> Para unir os canais novamente, basta usar a função  merge() especificando os canais.

```
merged = cv.merge([b, g, r])
cv.imshow(“Merged”, merged)
```


> Existe também outra forma para fazer isso, onde as imagens aparecem com cores, com as cores originais (azul, vermelho e verde),  ao invés de escalas de cinza.

```
img = cv.imread(path)

blank = np.imread(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

# Utilizar o merge na imagem Azul em Escala de cinza com duas outras # imagens vazias e repetir o mesmo processo com o verde e vermelho
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


# Exibir o resultado da utilização do merge
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
```

(O uint é um tipo de dado não assinalado, ou seja, um tipo de dado que não considera o sinal, o uint8 é uma variação que possui capacidade de armazenamento de 0 a 255.)


> Ao mesclar esses três resultados, você obterá a imagem original novamente.


## **Suavização e desfoque**
Em alguns casos, a câmera, os sensores e as circunstâncias em que o ambiente se encontra, podem causar ruído na imagem, fazendo-se assim, necessário suavizá-la e/ou reduzir o ruído.
(Um método de desfoque muito conhecido e usado é o Gaussiano, apesar de não ser completo.)


### **Média**
Basicamente, o método da média define uma janela no Kernel sobre uma parte específica da imagem, que irá computar a intensidade do pixel central como sendo a média dos pixels ao redor. Esse processo é repetido até que todos os pixels sejam computados. Quanto maior o tamanho do kernel definido, maior será o desfoque produzido. Isso é feito utilizando a função blur.

```
average = cv.blur(img, (3,3))
cv.imshow('Average Blur’, average)
```

> Os parâmetros são a imagem a ser suavizada e a janela de suavização, o tamanho de kernel. No exemplo acima, a “caixa” usada para causar o borrão é 3x3.


### **Gaussiano**
O método Gaussiano é semelhante ao método anterior, difere apenas por, ao invés de pegar a média de toda a intensidade dos pixels ao redor, cada pixel vizinho recebe um valor diferente e a média do produto desses pixels gera o novo valor para o pixel centra.
Apesar de tender a ficar mais desfocado do que no método anterior, as imagens ficam mais “naturais”.

```
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussiano Blur’, gauss)
```

> Os Parâmetros são a imagem, o tamanho de kernel, no caso acima 3x3 e o desvio padrão nos eixos X e Y, que no exemplo acima é igual a zero.


### **Mediana**
Similar ao método gaussiano, difere apenas por não pegar a média dos pixels vizinhos e sim a mediana. O método tende a ser mais eficaz na redução de ruído do que o método gaussiano e da média.

```
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur’, median) 
```

> Os parâmetros utilizados são a imagem e, diferentemente dos outros métodos, não é preciso dizer uma tupla e sim apenas um número e o tamanho do kernel será interpretado, no exemplo acima foi colocado um 3, ou seja, o tamanho é 3x3.


### **Bilateral**

É o método mais avançado, utilizado em projetos avançados de visão computacional. Têm como uma das vantagens a preservação das bordas.

```
bilateral = cv.bilateralFilter(img, 5, 15)
cv.imshow('Bilateral’, bilateral)
```

> Os parâmetros são a imagem, o diâmetro da vizinhança do pixel (não mais o tamanho do kernel como nos outros métodos) e um outro número, sigma, que indica a distância dos pixels da vizinhança que serão levadas em conta no cálculo do desfoque 


## **Operadores bit a bit**

Os operadores funcionam de maneira binária, se um pixel tiver o valor 0 ele é desligado se tiver o valor 1, ele é ligado. Existem 4 operadores básicos: and, or, xor e not. Eles são muito usados no processamento de imagens, principalmente quando se está trabalhando com máscara.


Para a demonstração, é essencial que criemos imagens vazias com formas geométricas em seu escopo:

```
# Cria uma imagem vazia
blank = np.zeros(shape=(400,400), dtype='uint8')

# Cria um objeto retangular branco em uma imagem vazia
rectangle = cv.rectangle(img=blank.copy(), pt1=(30,30), pt2=(370,370), color=255, thickness=-1)

# Cria um objeto circular branco em uma imagem vazia
circle = cv.circle(img=blank.copy(), center=(200,200), radius=200, color=255, thickness=-1)

# Exibe as duas imagens criadas
cv.imshow(winname='Retangulo', mat=rectangle)
cv.imshow(winname='Circulo', mat=circle)
```

> Após a criação das imagens, podemos utilizar as seguintes operações bit a bit:


* and: retorna o cruzamento, pode-se dizer que a interseção das duas imagens

```
# bitwise AND --> intersecta as regiões
bitwise_and = cv.bitwise_and(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise AND', mat=bitwise_and)
```

* or: retorna a soma das imagens, uma imagem sobreposta a outra

```
# bitwise OR --> União das regiões
bitwise_or = cv.bitwise_or(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise OR', mat=bitwise_or)
```

* xor: retorna apenas as partes que não se intersectam, como o resultado de uma subtração

```
# bitwise XOR --> Regiões não intersectadas
bitwise_xor = cv.bitwise_xor(src1=rectangle, src2=circle)
cv.imshow(winname='Bitwise XOR', mat=bitwise_xor)
```

* not: inverte as cores.

```
# bitwise NOT --> Região não preenchida
bitwise_not = cv.bitwise_not(src=circle)
cv.imshow(winname='Circle NOT', mat=bitwise_not)
```


## **Mascaramento** 

Nas operações de Mascaramento(Masking - do inglês), o valor de cada pixel de uma imagem é recalculado com base em uma determinada matriz de máscara, isto é conhecido como o Kernel. O mascaramento é conhecido como filtragem. Em termos simples, uma máscara nos permite focar apenas nas porções da imagem que nos interessam.
No nosso exemplo utilizaremos as operações bit a bit para realizar um mascaramento. Realizaremos novamente o processo inicial para criar formas geométricas em imagens vazias e criaremos uma forma que será utilizada no nosso mascaramento. Também carregamos uma imagem, será nela que aplicamos o mascaramento:

```
# Carregando e exibindo uma imagem
img = cv.imread(filename=path)
cv.imshow(winname='Nome da imagem', mat=img)

# Criando uma imagem vazia e a exibe
blank = np.zeros(shape=(img.shape[0],img.shape[1]), dtype='uint8')
cv.imshow(winname='Imagem Vazia', mat=blank)

# Criando um objeto circular branco em uma imagem vazia
circle = cv.circle(img=blank.copy(), center=(img.shape[1]//2 + 40, img.shape[0]//2), radius=100, color=255, thickness=-1)

# Criando um objeto retangular branco em uma imagem vazia
rectangle = cv.rectangle(img=blank.copy(), pt1=(30,30), pt2=(370,370), color=255, thickness=-1)

# Realizando uma operação bit a bit “and” entre “circle” e 
# “rectangle” e a exibindo
weird_shape = cv.bitwise_and(src1=circle, src2=rectangle)
cv.imshow(winname='Mascaramento', mat=weird_shape)
```

> Após termos nossa forma criada. Mais uma vez realizaremos uma operação bit a bit, na qual a nossa imagem carregada no início do problema será utilizada como argumento para scr1 e scr2 e utilizamos o argumento mask, atribuindo a ele o formato que fizemos “weird_shape”. Desse modo criamos uma máscara para nossa imagem.

```
# Criando uma máscara através operação bit a bit “and” com a imagem 
# carregada inicialmente e a forma criada “weird_shape”
masked = cv.bitwise_and(src1=img, src2=img, mask=weird_shape)
cv.imshow(winname='Imagem Mascarada com o Mascaramento', mat=masked)
```

## **Histogramas**

Histogramas são contagens de dados coletados e organizados em um conjunto de caixas pré-definidas. Com um histograma podemos visualizar as intensidades das cores de nossa imagem, mas também explorar outras características da imagem que queremos medir (isto é, gradientes, direções, etc.). O histograma é um gráfico, no qual o eixo x representa a intensidade do pixel e o eixo y representa a quantidade.

```
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Carregando e exibindo uma imagem
img =cv.imread(filename=path)
cv.imshow(winname='Nome da imagem', mat=img)

# Criando uma imagem vazia do tamanho da imagem carregada
blank = np.zeros(shape=(img.shape[0],img.shape[1]), dtype='uint8')

# Convertendo a imagem para Escala de cinza
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Criando um círculo numa imagem vazia
mask = cv.circle(img=blank,center=(img.shape[1]//2,img.shape[0]//2), radius=100, color=255, thickness=-1)

# Criando uma máscara utilizando o círculo criado como forma
masked = cv.bitwise_and(src1=img,src2=img,mask=mask)
cv.imshow(winname='Mask', mat=masked)

# GRayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Plotando o histograma de cores
plt.figure()
plt.title(label='Colour Histogram')
plt.xlabel(xlabel='Bins')
plt.ylabel(ylabel='# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist(images=[img], channels=[i], mask=mask, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

# Exibindo o plot
plt.show()

cv.waitKey(0)
```

## **Thresholding/Binarização**

O thresholding é o método mais simples de segmentar as imagens. A partir de uma imagem em escala de cinza, o thresholding pode ser usado para criar imagens binárias. Para cada pixel, é aplicado o mesmo valor limite. Se o valor do pixel for menor que o limite, ele é ajustado para 0, caso contrário, é ajustado para um valor máximo. A função cv.threshold é utilizada para aplicar o threshold. O primeiro argumento é a imagem de origem, que deve ser uma imagem em escala de cinza.

Portanto, inicialmente carregamos uma imagem e a converteremos para a escala de cinza:

```
# Carregando e exibindo uma imagem
img = cv.imread(filename=path)
cv.imshow(winname='Nome da imagem', mat=img)

# Convertendo BGR para Escala de cinza
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow(winname='Escala de cinza', mat=gray)
```

> Em seguida, aplicamos uma técnica de binarização simples utilizando o cv.threshold:

```
# Thresholding simples
threshold, thresh = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY )
cv.imshow(winname='Thresholded Simples', mat=thresh)

threshold, thresh_inv = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV )
cv.imshow(winname='Thresholded Simples Inverso', mat=thresh_inv)
```

> Se uma imagem tem condições de iluminação diferentes em áreas diferentes. Nesse caso, o thresholding adaptável pode ajudar:

```
# Thresholding adaptativo
adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=9)
cv.imshow(winname='Thresholding Adaptativo', mat=adaptive_thresh)
```

## **Detecção de Borda**

A detecção de borda, ou “Edge Detection”, é uma técnica de processamento de imagem e visão computacional para determinar pontos de uma imagem digital em que a intensidade luminosa muda repentinamente. Mudanças repentinas em imagens geralmente refletem eventos importantes no cenário, como a descontinuação da profundidade (transição entre o objeto e o fundo), descontinuação da orientação da superfície, mudança das propriedades do material ou variações na iluminação da cena.

> Primeiramente carregamos nossa imagem e a converteremos para escala de cinza:

```
# Carregando e exibindo uma imagem
img = cv.imread(filename=path)
cv.imshow(winname='Nome da imagem', mat=img)

# Convertendo BGR para Escala de cinza
gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
cv.imshow(winname='Gray', mat=gray)
```

> O OpenCV fornece três tipos de filtros gradientes, que podem ser utilizados para detecção de gradientes ou bordas de uma imagem. São eles o Sobel, Scharr e Laplacian. 


> O Sobel é uma operação conjunta de suavização e diferenciação da Gaussiana, por isso é mais resistente ao ruído. Em opencv, podemos utilizar a função cv.Sobel().

```
# Utilizando o Sobel 
sobelx = cv.Sobel(src=gray, ddeph=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddeph=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_or(src1=sobelx, src2=sobely)

# Exibindo o Sobel combinado
cv.imshow(winname='Sobel X', mat=sobelx)
cv.imshow(winname='Sobel Y', mat=sobely)
cv.imshow(winname='Combined Sobel', mat=combined_sobel)
```

> No Laplacian é calculado o filtro laplaciano da imagem, onde cada derivada é encontrada utilizando as derivadas do Sobel. Em opencv, podemos utilizar a função cv.Laplacian().

```
# Utilizando o Laplacian
lap = cv.Laplacian(src=gray, ddeph=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow(winname='Laplacian', mat=lap)
```

> Além dos gradientes, podemos utilizar também a detecção de borda de Canny, que é um dos algoritmos mais populares para realização desse tratamento. Ela é capaz de reduzir ruídos, encontrar o gradiente de intensidade da imagem, realizar uma supressão não-máxima etc. No opencv, podemos utilizar a função cv.Canny() para explorar esse algoritmo.

```
# Utilizando a detecção de borda de Canny
canny = cv.Canny(image=gray, threshold1=150, threshold2=175)
cv.imshow(winname='Canny', mat=canny)

cv.waitKey(0)
```

## **Referências**

1. OpenCV Course - Full Tutorial with Python, Curso do Jason Dsouza
2. https://docs.opencv.org/master/d6/d00/tutorial_py_root.html