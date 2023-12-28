import datetime

nascimento = input('Entre com a data (dd/mm/aaaa): ')

nascimento_list = nascimento.split('/')
nascimento_data = datetime.date(
    int(nascimento_list[2]),
    int(nascimento_list[1]),
    int(nascimento_list[0])
)

print(nascimento_data)
print(type(nascimento_data))