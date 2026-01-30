
import requests
import json

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            return {
                "Nome": dados['name'].capitalize(),
                "ID": dados['id'],
                "Tipos": [t['type']['name'] for t in dados['types']],
                "Habilidades": [h['ability']['name'] for h in dados['abilities'][:2]]
            }
        else:
            return {"Erro": "Pokémon não encontrado. Verifique o nome."}
            
    except Exception as e:
        return {"Erro": f"Falha na conexão: {e}"}

if __name__ == "__main__":
    nome_input = input("Digite o nome de um Pokémon: ")
    resultado = buscar_pokemon(nome_input)
    
    print(json.dumps(resultado, indent=4, ensure_ascii=False))