import cv2

# Lendo informações da imagem

imagem = cv2.imread('manivela.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1])  # largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])  # altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)
cv2.imwrite("saida.jpg", imagem)

# Lendo informações dos pixel de cada canal de cor.

(b, g, r) = imagem[0, 0]
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# Transformando a imagem em uma cor sólida.

for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (100, 145, 100)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Gerando grades de cores

for y in range(0, imagem.shape[0]):  # percorre linhas
    for x in range(0, imagem.shape[1]):  # percorre colunas
        imagem[y, x] = (x % 125, y % 103, x % 72)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Alterando todos os pixels da imagem, gerando um padrão através da multiplicação entre x e y.

for y in range(0, imagem.shape[0], 1):  # percorre as linhas
    for x in range(0, imagem.shape[1], 1):  # percorre as colunas
        imagem[y, x] = ((x*y) % 200, 130, (x*y) % 200)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Gerando quadrados na imagem, definindo um espaço entre os pixels

imagem = cv2.imread('manivela.jpg')
for y in range(0, imagem.shape[0], 10):  # percorre linhas
    for x in range(0, imagem.shape[1], 10):  # percorre colunas
        imagem[y:y+5, x: x+5] = (150, 100, 50)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
