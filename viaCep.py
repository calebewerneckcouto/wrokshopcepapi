import requests

def consulta_cep(cep):
    # Verifica se o CEP tem 8 dígitos
    if len(cep) != 8:
        print("CEP inválido. O CEP deve ter exatamente 8 dígitos numéricos.")
        return

    # Faz a requisição à API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    # Verifica o status da resposta
    if response.status_code == 200:
        data = response.json()

        # Verifica se o CEP retornou dados válidos
        if "erro" in data:
            print("CEP não encontrado.")
        else:
            print(f"CEP: {data.get('cep')}")
            print(f"Logradouro: {data.get('logradouro')}")
            print(f"Bairro: {data.get('bairro')}")
            print(f"Cidade: {data.get('localidade')}")
            print(f"Estado: {data.get('uf')}")
            print(f"Complemento: {data.get('complemento', 'Não informado')}")
    else:
        print("Erro ao acessar a API. Verifique sua conexão com a Internet.")

if __name__ == "__main__":
    # Solicita o CEP ao usuário
    cep_usuario = input("Digite o CEP (somente números e 8 dígitos): ")
    consulta_cep(cep_usuario)
