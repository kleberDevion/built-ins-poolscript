import requests
import json
import logging

class RequestUtil:
    def __init__(self):
        # Session profissional: reaproveita conexões TCP (muito mais rápido)
        self.session = requests.Session()
        
        # Headers padrão: evita bloqueios e define JSON como base
        self.default_headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/plain, */*"
        }

    def _executar(self, metodo, url, headers=None, body=None, timeout=30, verify=True, **kwargs):
        """
        Mecanismo central com tratamento completo de erros e injeção de lógica.
        """
        # 1. GESTÃO DE HEADERS: Se passar arg, ignora o default. Se não, usa o default.
        request_headers = headers if headers is not None else self.default_headers

        # 2. GESTÃO DE BODY: Detecta se é dicionário (JSON) ou dado bruto
        if body is not None:
            if isinstance(body, (dict, list)):
                kwargs['json'] = body
            else:
                kwargs['data'] = body

        try:
            # 3. EXECUÇÃO COM TIMEOUT (Evita que a lang trave para sempre)
            response = self.session.request(
                method=metodo,
                url=url,
                headers=request_headers,
                timeout=timeout,
                verify=verify,
                **kwargs
            )

            # 4. TRATAMENTO DE ERROS HTTP (4xx, 5xx)
            # Retorna o erro formatado se o status não for 2xx
            response.raise_for_status()
            
            return response

        except requests.exceptions.HTTPError as errh:
            return {"error": "HTTP Error", "status": response.status_code, "message": str(errh), "details": response.text}
        except requests.exceptions.ConnectionError as errc:
            return {"error": "Connection Error", "message": "Falha na rede ou URL inexistente."}
        except requests.exceptions.Timeout as errt:
            return {"error": "Timeout Error", "message": "A requisição demorou demais para responder."}
        except requests.exceptions.RequestException as err:
            return {"error": "Unknown Error", "message": str(err)}

    # MÉTODOS PÚBLICOS
    def get(self, url, headers=None, **kwargs):
        return self._executar("GET", url, headers=headers, **kwargs)

    def post(self, url, headers=None, body=None, **kwargs):
        return self._executar("POST", url, headers=headers, body=body, **kwargs)

    def put(self, url, headers=None, body=None, **kwargs):
        return self._executar("PUT", url, headers=headers, body=body, **kwargs)

    def patch(self, url, headers=None, body=None, **kwargs):
        return self._executar("PATCH", url, headers=headers, body=body, **kwargs)

    def delete(self, url, headers=None, **kwargs):
        return self._executar("DELETE", url, headers=headers, **kwargs)

# Instância global, obs. deve importar ela 
import RequestUtil

request = RequestUtil()

Caso 1: Chamada sem headers
request.post(url, body=corpo)
👉 Envia: Content-Type: application/json e User-Agent: MinhaLang/1.0.
Caso 2: Chamada com headers
request.post(url, headers={"Chave": "Valor"}, body=corpo)
👉 Envia: APENAS {"Chave": "Valor"}. Os padrões são descartados.
Tratamento de Body:
# Se o body for um dicionário, ele envia como JSON. Se for texto puro, envia como string.