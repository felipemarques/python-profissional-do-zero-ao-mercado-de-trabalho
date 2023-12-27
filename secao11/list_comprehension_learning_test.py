userData = [
    {
        'id': 100,
        'name': 'Felipe Marques',
        'email': 'contato@felipemarques.com.br',
        'roles': [1,2,3,4,5]
    },
    {
        'id': 200,
        'name': 'Jocemarina Marques',
        'email': 'jocemarina@gmail.com',
        'roles': [100,200,300,400,500]
    }

]

[[[print(roles) for roles in user['roles']] for key in user] for user in userData]