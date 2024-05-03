import requests

cep = input('Digite o CEP que deseja consultar: ')

def getAddress(cep):
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()

        if 'erro' not in data:
            print('CEP: {}'.format(data['cep']))
            print('Logradouro: {}'.format(data['logradouro']))

            print('Complemento: {}'.format(data['complemento']))
            print('Bairro: {}'.format(data['bairro']))

            print('Localidade: {}'.format(data['localidade']))
            print('UF: {}'.format(data['uf']))

            print('IBGE: {}'.format(data['ibge']))
            print('GIA: {}'.format(data['gia']))
            print('DDD: {}'.format(data['ddd']))
            print('SIAFI: {}'.format(data['siafi']))
        else:
            print('CEP inválido!')
    else:
        print('Erro ao consultar o CEP!')

if __name__ == '__main__':
    getAddress(cep)