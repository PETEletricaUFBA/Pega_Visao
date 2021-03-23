# Reconhecendo rostos e criando parametros
Agora que ja sabemos o básico do opencv podemos usar a parte importante para o projeto. Estaremos agora reconhecendo o rosto de pessoas em fotos e criando parametros a partir das análises de fotos.
## Detectando
Para detectar se existe um rosto(s) em uma foto primeiro precisamos de um arquivo .xml criado pela intel, nesse arquivo encontraremos vários parametros para decidir se existe ou não um rosto em uma imagem. Para acessar as informações desse aquivo temos que usar a função .CascadeClassifier('pasta/arquivo.xml') associada com uma váriavel.
```sh
haar_cascade = cv..CascadeClassifier('haar_face.xml')
```
Antes de tentarmos visualizar o resultado precisamos também, carregar uma imagem e transformá-la em preto/branco (grayscale).
```sh
img = cv.imread('Photos/group 2.jpg')
cv.imshow('IMG', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
```
Agora que temos tudo pronto podemos detectar rostos e para fazer isso precisamos apenas de uma linha de código.
```sh
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)
```
Bem você pode estar se perguntando, o que está acontecendo nessa linha ?
Estámos usando a variável que criamos 'haar_cascade' juntamente com a função 'detectMultiScale()', no caso estamos passando informações armazenadas na variável para a função então usar para descubrir se na imagem preto e branco que passamos têm ou não um rosto/face.

Para vizualizarmos o resultado podemos imprimir o tamanho de 'faces_rect' ou então determinar na imagem a localização da face usando o desenho de um retângulo.
```sh
print(f'Number of faces found = {len(faces_rect)}') 

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
cv.imshow('IMG', img)
```

## Criando parametros e Reconhecendo faces
