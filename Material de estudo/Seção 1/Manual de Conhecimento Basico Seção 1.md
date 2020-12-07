# Seção 1 - Básico

Os códigos de apoio numerados por episódio estão disponíveis no Git do projeto.

## Introdução - Instalação do Python e bibliotecas

Pyhton é uma linguagem de programação com muitas aplicações devido as bibliotecas criadas pela comunidade. Para instalar Python entre no link, Download Python | Python.org, sempre instale a versão mais recente do programa.
Para instalar as bibliotecas no seu computador existem dois modos, instalar usando o terminal ou instalar colocando as pastas da biblioteca no mesmo domínio dos seus códigos.  

No primeiro modo você deve abrir seu terminal(CMD), digitar no terminal o comando “pip install opencv-contrib-python”, use também “pip install caer” para funções nas partes avançadas. Caso ocorra um erro no uso do comando pip, vá até Sistema>Propriedade dos Sistema>Variáveis de Ambiente e coloque em variáveis para o usuário uma nova variável com o nome “pip” com valor “C:Users/[nome_do_ usuário]/AppData/Local/Programs/Python/[nome_da_pasta_python]/Scripts”. Você pode achar essa pasta “Scripts” e copiar o local e colar no valor da variável.

No segundo caso basta apenas baixar a biblioteca com uma pasta zip e extrair essa pasta para a mesma pasta do seus códigos, mas saiba que as importações só funcionaram nesta pasta.

## Episódio 1 - Leitura de imagens e vídeos

A leitura de imagens e vídeos com a biblioteca Open CV é feita através das funções `cv2.imread('arquivo de imagem')` e `cv2.VideroCapture('arquivo de vídeo')`. Para garantir que a mídia seja encontrada, o seu respectivo arquivo deve ter o caminho especificado.
A função `cv2.imshow(‘Nome de exibição’, imagem)` exibirá a imagem atribuída no segundo parâmetro da função. Por outro lado, a exibição de vídeos exige o uso da estrutura de repetição while. Esse loop deve conter as funções `.read()` para captura de cada frame do vídeo e `cv2.imshow('Nome de exibição', imagem)` para apresentá-los em sequência.
Funções usadas:

* `retval = cv.imread( filename[, flags] )`
  * Carrega a imagem em um arquivo e tem como parâmetros: o nome do arquivo a ser carregado (uso obrigatório) e uma flag1 (uso optativo) [1].
* `<VideoCapture object> = cv.VideoCapture()`
  * Método construtor responsável por criar um objeto da classe VideoCapture, tendo três tipos distintos de construtores dependentes do parâmetro passado.
    * `<VideoCapture object> = cv.VideoCapture( )`
      * Construtor padrão.
      * `<VideoCapture object> = cv.VideoCapture( filename[, apiPreference] )`
        * Abre um arquivo de vídeo, uma ferramenta de captura ou IP video stream ao usar a API de preferência. Tem como parâmetros obrigatórios: o nome do arquivo de vídeo a ser carregado, a sequência de imagens e a URL da Stream de vídeo ou a GSTream pipeline string(caso esteja usando GStreamer), e tendo como parâmetro optativo a Capture API, caso o usuário tenha interesse em usar como backend.
      * `<VideoCapture object> =        cv.VideoCapture(        index[, apiPreference]        )`
        * Abre uma câmera para captura de vídeo. Tendo como parâmetro obrigatório a id da câmera que será usada, e parâmetro optativo a Capture API, que o usuário tenha interesse em usar como backend.
  * Caso deseje usar APIs, recomendo dar uma olhada no link no rodapé[2].
* `retval, image = cv.VideoCapture.read( [, image])`
  * Esse método irá, pegar decodificar e retornar o próximo frame do nosso objeto da classe VideoCapture. [out] Tem como parâmetro optativo o frame que será retornado.
* `None = cv.VideoCapture.release( )`
  * Fecha o arquivo de vídeo ou ferramenta de captura.
* `None = cv.imshow( winname, mat )`
  * Irá mostrar uma imagem numa janela específica. Caso a janela não tenha sido criada uma nova será criada. Tem como parâmetros obrigatórios nome da janela e da imagem.
* `retval = cv.waitKey( [, delay] )`
  * Aguarda uma tecla ser pressionada. Tem como parâmetro o delay em milissegundos do tempo que deve aguardar, caso o valor passado seja menor ou igual a 0, ele irá aguardar indefinidamente.
* `None = cv.destroyAllWindows( )`
  * Irá destruir todas janelas HighGUI que foram abertas.

## Episódio 2 - Redimensionamento de frames

Existem vários motivos para se querer redimensionar um frame no tratamento de imagens, seja por o OpenCV não fazer isso por default(padrão), ou por motivos de imagens menores poderem significar melhora no desempenho de algumas funções, ou até mesmo por a imagem não estar cabendo corretamente na tela.
Dentre os métodos de redimensionamento de imagens e vídeos, o redimensionamento de frame pode ser feito ao se definir uma função `rescaleFrame(frame, scale)`,
A qual consiste em pegar um frame, e redimensionar usando a função `cv2.resize(frame, dimension, interpolation=cv.INTER_AREA)` para retornar o frame no novo tamanho desejado. Sendo este método especialmente eficaz por ser possível usar tanto em imagens, vídeos e lives.  
Outro método, exclusivo para live videos, é definindo uma função `changeRes(width, height)`, que irá mudar as dimensões do live video para os valores passados no parâmetro.

Funções usadas:

* `def rescaleFrame(frame, scale=0.75) : ...`
  * Função o qual podemos definir para alterar a escala do video. Onde teremos como parâmetros o frame ou imagem que queremos reescalar e a escala que desejamos em relação às dimensões do frame.
* `dst = cv.resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] )`
  * A função resize redimensiona a imagem para o tamanho informado. Tendo como parâmetros obrigatórios, a imagem a ser redimensionada e as dimensões desejadas, e como opcionais a imagem de saída, fatores de escalas e o método de interpolação usado para redimensionar a imagem, sendo o INTER_LINEAR o default.
* `def changeRes(width, height) : ...`
  * Função que irá modificar a resolução do live video que o programa está lendo, através da função set(n, value) para redefinir os parâmetros do objeto da classe Video Capture. Sendo o n = 3 a largura  e o n = 4 a altura. Tem como parâmetros obrigatórios a largura e altura desejada.  

## Episódio 3: Desenhando formas e Inserindo textos

Com o OpenCV é possível modificar imagens de diversas formas, incluindo, pintar uma parte da imagem, ou ela toda de uma cor, desenhar retângulos, círculos e linhas, e até inserir textos nas imagem.Para demonstração também usaremos a biblioteca NumPy para gerarmos uma imagem vazia. E então podemos desenhar usando as funções abaixo:

* `numpy.zeros(shape, dtype=float, order='C')`
  * A função zeros, irá retornar uma array completamente preenchida por 0s. Tem como parâmetro obrigatório as dimensões do quadro que a gente deseja criar, e como optativo o tipo dos dados dentro da função e como esses dados estarão armazenados na memória.
* `array[n:m, x:y] = b, g, r`
  * É possível desenhar diretamente na imagem aos especificar quais elementos ou conjunto de elementos da array você deseja alterar o valor, sendo esse valor a 3-upla que representa a cor desejada no padrão rgb.
* `img = cv.rectangle(..)`
  * Essa função é usada para desenhar um retângulo na imagem.
    * `img = cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])`
      * Ao ser declarada dessa forma, ela tem como parâmetros obrigatórios, a imagem o qual receberá o desenho, os eixos opositores que delimitaram a área do retângulo e a cor. E tendo como parâmetros opcionais, a grossura das paredes do retângulo, se -1 irá preencher todo retângulo, o tipo de linhas e o número de fractional bits na coordenada, onde o shift pode atuar para definir escala do desenho.
    * `img = cv.rectangle(img, rec, color[, thickness[, lineType[, shift]]])`
      * Ao ser declarada dessa forma será similar a forma de cima com exceção dos eixos opositores, que aqui será passado o valor do tipo Rect, como alternativa aos dois valores de eixo.
* `img = cv.circle(img, center, radius, color[, thickness[, lineType[, shift]]])`
  * Função usada para desenhar um círculo na imagem. Tendo como parâmetro obrigatório a imagem a ser desenhada, 2-upla informando centro do círculo e a cor do círculo. Tendo como parâmetros opcionais, a grossura das paredes do círculo, se -1 irá preencher todo retângulo, o tipo de linhas e o número de fractional bits na coordenada, onde o shift pode atuar para definir escala do desenho.
* `img = cv.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])`
  * Função usada para desenhar um segmento de linha que vai de um ponto a outro. Tendo como parâmetro obrigatório a imagem a ser desenhada, os dois pontos que definem o início e fim do segmento de linha e a cor da linha. Tendo como parâmetros opcionais, a grossura da linha, o tipo da linha e o número de fractional bits na coordenada, onde o shift pode atuar para definir escala do desenho.
* `img = cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])`
  * A função acima irá desenhar uma string de texto na imagem. Tendo como parâmetro obrigatório a imagem a ser desenhada, a string de texto, a posição onde a base esquerda do texto estará, o tipo de fonte usada, o tamanho da fonte e a cor do texto. Sendo parâmetro opcional, a espessura dos caracteres do texto, o tipo de linha, e se a imagem tem seus organizados a começar pelo inferior esquerdo ou superior esquerdo, sendo True para inferior esquerdo.

## Episódio 4: Funções básicas do OpenCV

Dentre as funções básicas de tratamento de imagem do OpenCV, é importante ressaltar as seguintes funções que podem alterar propriedades básicas das imagens, capaz de mudar esquemas de cores, aplicar blur, traçar as linhas de cascata entre outras.

* `dst= cv.cvtColor( src, code[, dst[, dstCn]] )`
  * Essa função irá converter o espaço de cores da imagem de um espaço para outro, podendo ser usado para converter imagem para escala de cinza, padrões de cores diferentes do BGR, entre outros. Recomendo a leitura da nota[3]. Tendo como parâmetro obrigatório a imagem a ser convertida e o código de conversão, segue a seguir a lista de códigos[4]. E como parâmetros optativos, o arquivo de saída, e o número de canais na saída.
* `dst = cv.GaussianBlur(  src, ksize, sigmaX[, dst[, sigmaY[, borderType]]] )`
  * Borra(efeito Blur) a imagem usando filtro Gaussiano. Tem como parâmetros obrigatórios, a imagem a ser borrada, o kernel Gaussiano, e o desvio no eixo X. Sendo parâmetros facultativos a imagem de saída, o desvio no eixo y e o tipo de borda.
* edges = cv.Canny( … )
  * Função usada para encontrar as bordas de usando o algoritmo de detecção de bordas de Canny.[5]
    * `edges = cv.Canny( image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]] )`
      * Essa implementação tem como parâmetros obrigatórios, a imagem, o primeiro e segundo threshold, usados para o processo de hysteresis. Tendo como opcional o conjunto de bordas de saída, o tamanho da abertura de Sobel e uma flag indicando a acurácia ao calcular a magnitude do gradiente.
      * `edges = cv.Canny( dx, dy, threshold1, threshold2[, edges[, L2gradient]] )`
        * Essa implementação é usada para imagens com magnitude de gradiente modificados, tendo como parâmetros, a derivada em x da imagem de entrada, a derivada em y da imagem de entrada e o primeiro e segundo threshold, usados para o processo de hysteresis.Tendo como opcional o conjunto de bordas de saída e uma flag indicando a acurácia ao calcular a magnitude do gradiente.
* `dst = cv.dilate( src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )`
  * A função irá dilatar a imagem usando uma estruturação de elementos específica, o qual pode conferir no link do rodapé[6]. Tendo como parâmetros obrigatórios a imagem a ser dilatada e os elementos usados para estruturação, e como parâmetro facultativo imagem de saída, a âncora usada pelo elemento, o número de iterações que serão feitas, o tipo de bordas, e o valor da borda, caso seja uma borda constante.
* `dst = cv.erode( src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]] )`
  * A função erode irá realizar a erosão da imagem que é o processo oposto ao de dilatação de imagem, como pode conferir na nota de rodapé[7].Tendo como parâmetros obrigatórios a imagem a ser dilatada e os elementos usados para estruturação, e como parâmetro facultativo imagem de saída, a âncora usada pelo elemento, o número de iterações que serão feitas, o tipo de bordas, e o valor da borda, caso seja uma borda constante.
* `dst = img[X, Y]`
  * Para cortar uma imagem basta você associar a parte da imagem que você quer a um vetor, copiando os valores usando operador [], passando como parâmetro o intervalo de X, e o intervalo de Y que serão copiados.

## Episódio 5: Transformações de imagem

Dentre as funções e ações que se pode fazer com o OpenCV estão as transformações de Imagem, que envolve, transladar, rotacionar, cortar, redimensionar a imagem, espelhar e entre outros, através das seguintes funções.

* `def translate(img, x, y): …`
  * A função definida pode ser usada para transladar a imagem no eixo x e y. Tendo como parâmetro, a imagem, e os valores em x e y do quanto será transladado.
* `dst = cv.warpAffine( src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]] )`
  * Função usada para aplicar uma transformação afim na imagem. Tem como parâmetros obrigatórios, a imagem a ser transformada, a matrix específica usada para transformação, e as dimensões da imagem de saída. Como parâmetro facultativo temos a imagem de saída, uma flag[8] para especificar o método de interpolação usado, o método de extrapolação de pixel, e o valor da borda para o caso de uma borda constante.
* `def rotate(img, angle, rotPoint=None): …`
  * Uma função definida para realizar a rotação da imagem. Tendo como parâmetros obrigatórios a imagem a ser rotacionada e o ângulo de rotação em sentido anti horário, e como parâmetro facultativo o centro de rotação, sendo o centro da imagem o valor padrão.
* `retval = cv.getRotationMatrix2D( center, angle, scale )`
  * A função irá retornar a matriz afim de rotação, tendo como parâmetros obrigatórios o centro da rotação, o ângulo de rotação, e o fator de escala isotrópica.
* `dst = cv.flip( src, flipCode[, dst] )`
  * Função usada para “inverter”(flip) uma imagem, na vertical e/ou horizontal, tendo como parâmetros obrigatórios a imagem a ser invertida, e um número que irá determinar o sentido da inversão, sendo 0 para inverter no eixo x, qualquer número positivo para inverter no eixo y e qualquer número negativo para inverter nos dois eixos, tendo também como parâmetro facultativo a imagem de saída.

## Episódio 6: Detecção de contornos

Através do OpenCV uma funcionalidade importante é a identificação de contornos na imagem, “Onde são as linhas que borda de um objeto, ou seja as linhas que denotam os limites de um objeto.” Para isso introduziremos duas funções importantes, uma para determinar os contornos da imagem, e outra para desenhar os contornos obtidos.

* `contours, hierarchy = cv.findContours( image, mode, method[, contours[, hierarchy[, offset]]])`
  * Função que irá encontrar e retornar os contornos e hierarquias de uma imagem binária, como as imagem de saída da função `cv.Canny(...)` ou outras. Tendo como parâmetro a imagem binária a ser obtida os contornos, o modo de coleta dos contornos[9] e o método de aproximação de contornos[10]. Tendo como parâmetros facultativos os contornos de saída, cada contorno é armazenado como um vetor de pontos, a saída de hierarquias dos contornos o qual descreve a topologia dos contornos, e um offset que pode ser usado para shift os pontos de contorno, prático para o caso de analisar região de interesse e contextualizar na imagem completa.
* `image = cv.drawContours( image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]] )`
  * Função usada para desenhar contornos, podendo ser preenchidas ou apenas linhas de borda. Tendo como parâmetros obrigatórios a imagem de destino a ser desenhada, todos contornos de entrada onde cada contorno armazenado em um vetor de pontos, parâmetro que indica quais contornos devem ser desenhado, usando valor negativo para desenhar todos contornos, e também a cor dos contornos, e tendo como parâmetro facultativo, a espessura do contorno, valor negativo para preencher o contorno, os tipos de linha do contorno, as informações a respeito da hierarquia dos contornos, o nível máximo de desenho do contorno e o shift nos contornos de acordo com offset informado.
Dentre os métodos de gerar imagens binárias no OpenCV para usarmos para encontrar contornos é importante citar o thresholding, o qual pode ser encontrado no OpenCV através de algumas funções como.
* `retval, dst = cv.threshold( src, thresh, maxval, type[, dst] )`
  * Aplica um nível fixo de threshold para cada elemento da array(no nosso caso um frame ou imagem), podendo gerar a imagem binária a partir de uma escala de cinzas ou remover ruídos de imagens coloridas. Tendo como parâmetros obrigatórios a array de entrada, o valor para threshold, valor máximo a ser usado com os tipos de thresholding THRESH_BINARY e THRESH_BINARY_INV e o tipo de thresholding[11] a ser usado, tendo como parâmetro facultativo a array de saída do mesmo tamanho da de entrada.
* `dst = cv.adaptiveThreshold( src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst] )`
  * Função que gera um thresholding adaptativo de uma imagem em escala de cinza a partir de uma determinada fórmula,( conferir na documentação) [12], onde tem como parâmetros obrigatórios a imagem de entrada em escala de cinza, o valor máximo de thresholding, o algoritmo usado como método[13], o tipo de threshold¹¹ a ser usado, o tamanho da vizinhança usada para calcular o valor do threshold, e o valor subtraído da média ou média ponderada.

________________
[1] "Image file reading and writing - OpenCV." <https://docs.opencv.org/4.5.0/d4/da8/group__imgcodecs.html>. Accessed 18 Nov. 2020.  
[2] "Flags for video I/O - OpenCV." <https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html>. Accessed 18 Nov. 2020.  
[3] "Color conversions - OpenCV." <https://docs.opencv.org/4.5.0/de/d25/imgproc_color_conversions.html>. Accessed 18 Nov. 2020.  
[4] "Color Space Conversions - OpenCV." <https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html>. Accessed 18 Nov. 2020.
[5] "Canny edge detector - Wikipedia." <https://en.wikipedia.org/wiki/Canny_edge_detector>. Accessed 18 Nov. 2020.  
[6] "Image Filtering - OpenCV." <https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html>. Accessed 23 Nov. 2020.  
[7] "Image Filtering - OpenCV." <https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html>. Accessed 23 Nov. 2020.  
[8] "Geometric Image Transformations - OpenCV." <https://docs.opencv.org/4.5.0/da/d54/group__imgproc__transform.html>. Accessed 23 Nov. 2020.  
[9] "Structural Analysis and Shape Descriptors - OpenCV." <https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html>. Accessed 24 Nov. 2020.  
[10] "Structural Analysis and Shape Descriptors - OpenCV." <https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html>. Accessed 24 Nov. 2020.  
[11] "Miscellaneous Image Transformations - OpenCV." <https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html>. Accessed 24 Nov. 2020.  
[12] "Miscellaneous Image Transformations - OpenCV." <https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html>. Accessed 24 Nov. 2020.  
[13] "Miscellaneous Image Transformations - OpenCV." <https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html>. Accessed 24 Nov. 2020.  
