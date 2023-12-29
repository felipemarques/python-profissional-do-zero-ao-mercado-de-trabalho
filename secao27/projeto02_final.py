# Documentação: https://pypi.org/project/qrcode/
# pip install qrcode[pil]

import qrcode

dados = input("Digite a informação que deseja gerar o QRCode: ")

img = qrcode.make(dados)

arquivo = input("Digite o nome do arquivo para salvar o QRCode: ")

img.save(arquivo)
