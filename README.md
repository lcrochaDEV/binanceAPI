### Para Instalação no Windows 10 foi criado um Ambiente Virtual

### Instalação do ambiente Virtual

```shell
python -m venv .venv
```


### Ativação do ambiente virtual no Windows

```shell
.venv/Scripts/activate
```

### Para Instalação no Debia 12 foi criado um Ambiente Virtual
 #### Crie um ambiente virtual usando venv ou virtual env Certifique-se venv de que esteja instalado executando:
```shell
sudo apt install python3-venv
```
#### Para criar um novo ambiente virtual em um **diretório chamado env**, execute:
```shell
python3 -m venv env
```
#### Para ativar este ambiente virtual (que modifica a PATH variável de ambiente), execute:
```shell
source env/bin/activate
```
#### Agora você pode instalar uma biblioteca neste ambiente virtual:
```shell
pip install XYZ
```
Os arquivos serão instalados no env/diretório.

Se quiser sair do ambiente virtual, você pode executar:
```shell
deactivate

### Instalação de Bibliotecas:
pip install python-binance
pip install python-dotenv
```

```py
#ORIGIAL
import pandas as pd

        df = self.tabela()
        compra = False
        # ESTRATÉGIA DE COMPRA E VENDA
        acumulados = (df.Open.pct_change() +1).cumprod() -1
        if not compra:
            if acumulados.iloc[-1] < -0.002:
                ordem = client.create_order(symbol=self.criptoPar, side='SIDE_BUY', type='ORDER_TYPE_MARKET', quantity=0.0001)
                print('Compra Realizada com Sucesso!')
                compra = True
            else:
                print('Sem Ordens nos últimos 30 minutos')

        if compra:
            while True:
                df = self.tabela(2, ["date_open", "Open"])

                ordem_executada = df.loc[df.index > pd.to_datetime(ordem['transactTime'], unit='ms')]
 
                if len(ordem_executada) > 0:
                    retorno_ordem_executada = (df.Open.pct_change() + 1).cumprod() -1
                    retorno_ordem_executada[-1] > 0.0015 or retorno_ordem_executada[-1] > -0.0015
                    ordem = client.create_order(symbol=self.criptoPar, side='SIDE_SELL', type='ORDER_TYPE_MARKET', quantity=0.0001)
                    print('Venda Realizada com Sucesso!')
                    break
```