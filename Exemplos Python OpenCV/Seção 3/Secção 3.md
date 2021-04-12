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
### Treinando
Muito bem agora que temos um detector de faces, vamos fazer um reconhecedor de faces.
Para isso vamos precisar fazer esse reconhecedor funcionar corretamente, primeiro temos que treiná-lo, logo precisaremos de fotos do rosto alvo que queremos reconhecer, então precisamos acessar todas essas fotos e se possível armazenar o nome da pasta que essa fotos estaram (nome do(s) alvo(s)).
```sh
DIR = r'Exemplos Python OpenCV/Resources/Faces/train'
people = []
for i in os.listdir(DIR):
    people.append(i)
```
Pronto após isso já podemos criar nosso treino para o reconhecedor.
```sh
haar_cascade = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

features = []
labels = []
def createTrain():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
createTrain()
```
Para começar precisamos carregar o arquivo para detecção de faces e criar duas listas que usaremos para armazenar as caracteristicas e nome das pessoas nas fotos, respectivamente.
Feito essa inicialização de variáveis podemos finalmente fazer a função de criar treino. Ela será responsavel por ler cada foto presente(s) na(s) pasta(s), armazenar o nome na lista 'labels' e armazenar na lista 'features' as características.
Feito isso agora podemos salvar esses dados que conseguimos em matrizes, e usá-las para então criar um arquivo que contem todos essas informações para usarmos no reconhecimento.
```sh
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer= cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels) #treinando o reconhcedor

face_recognizer.save('Exemplos Python OpenCV/Seção 3/face_trained.yml')
np.save('Exemplos Python OpenCV/Seção 3/features.npy', features)
np.save('Exemplos Python OpenCV/Seção 3/labels.npy', labels)
```
### Reconhecendo
Visto que temos todas as informações necessárias para o reconhecimento podemos testar seu funcionamento. Primeiramente temos que iniciar todos os dados que adiquirimos através do treinamento. Então iremos carregar a imagem/foto que iremos usar para o teste do reconhecedor, sempre lembrando de convertê-la para preto e branco. 
```sh
haar = cv.CascadeClassifier('Exemplos Python OpenCV/Seção 3/haar_face.xml')

features = np.load('Exemplos Python OpenCV/Seção 3/features.npy', allow_pickle=True)
labels = np.load('Exemplos Python OpenCV/Seção 3/labels.npy', allow_pickle=True)

face_recognizer= cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Exemplos Python OpenCV/Seção 3/face_trained.yml')

img = cv.imread('Exemplos Python OpenCV/Resources/Faces/val/ben_afflek/2.jpg')# Coloque aqui o caminho até a imagem/foto que deseja testar
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Pessoa', gray)
```
Com tudo isso a postos, vamos repetir a lógica do código que usamos para detecção de rostos.
```sh
faces_detected = haar.detectMultiScale(gray, 1.1 , 4)

for (x,y,a,b) in faces_detected:
    face_roi = gray[y:y+b, x:x+a]

    label, confindence  = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+a,y+b), (0,255,0), thickness=2)

cv.imshow('Detected', img)
```
Comparando diretamente com aquilo que fizemos na parte de #detecção, claramente existeM diferenças, mas não muitas. Existem duas diferenças, apenas, a primeira delas é que temos a introdução do 'face_recognizer.predict()' essa é a função que retorna as informações, ela faz todo processo de reconhecer a pessoa baseado nas informações que inicializamos com os arquivos .yml e .np, com isso feito podemos imprimir o resultado na tela e mostrar o quão confiante esse é esse reconhecimento além de desenhar na imagem o retangulo, como fizemos na detecção, e o nome.

### Notas
É importante estar atento que o reconhecimento pode falhar, para perceber isso é observar o valor da confiança e o nome da pessoa. Para diminuir o número de falhas sempre tente passar o maior número de fotos para treinar o programa para torná-lo mais robusto e completo

