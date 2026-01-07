# Iniciando a Conectividade

O Reticulum não é um serviço ao qual você se inscreve, nem é uma única rede global que você "ingressa". É uma *pilha de rede* (networking stack); um kit de ferramentas para construir sistemas de comunicação que se alinham com seus valores específicos, requisitos e ambiente operacional. A forma como você escolhe se conectar a outros pares do Reticulum é inteiramente sua escolha.

Quando você começar a usar o Reticulum, precisará de uma forma de obter conectividade com os pares com os quais deseja comunicar - o processo de *iniciar a conectividade*. Uma vez que você tenha obtido uma ou mais definições de interface válidas, você pode adicioná-las à seção `[interfaces]` da sua configuração do Reticulum.

Esta página fornece a visão mais básica, mas para entender totalmente a flexibilidade e opções disponíveis para iniciar a conectividade, leia a seção [Iniciando a Conectividade](manual/gettingstartedfast.html#creating-a-network-with-reticulum) do manual.

## Conecte-se à Infraestrutura Distribuída

Uma infraestrutura distribuída global de Nós de Transporte do Reticulum está sendo mantida por voluntários de todo o mundo. Esta rede constitui uma coleção heterogênea de nós públicos e privados que formam uma infraestrutura de interconexão voluntária e não coordenada que atualmente fornece capacidades de transporte e interconexão global para o Reticulum.

Um bom lugar para encontrar definições de interface para iniciar a conectividade são sites mantidos pela comunidade como [directory.rns.recipes](https://directory.rns.recipes/) e [rmap.world](https://rmap.world/).

O Reticulum incentiva a abordagem de *crescimento orgânico*. Em vez de depender de conexões estáticas permanentes com servidores distantes, você pode usar conexões de inicialização temporárias para *descobrir* continuamente uma infraestrutura mais relevante ou local. Uma vez descobertos, seu sistema pode formar automaticamente ligações mais fortes e diretas com esses pares, e descartar as ligações de inicialização temporárias. Isto resulta em uma rede de conexões que são geograficamente relevantes, resilientes e eficientes.

## Construa Infraestrutura Pessoal

Incentivamos fortemente que todos, mesmo usuários domésticos, pensem em termos de construir **infraestrutura pessoal**. Não conecte cada telefone, tablet e computador em sua casa diretamente a um gateway de internet pública. Em vez disso, reaproveite um computador antigo, um Raspberry Pi, ou um roteador compatível para atuar como seu próprio **Nó de Transporte** pessoal:

* Seu Nó de Transporte local fica em sua casa, conectado ao seu WiFi e talvez a uma interface de rádio (como um RNode).
* Você configura este nó com uma interface `bootstrap_only` (talvez um túnel TCP para uma rede mais ampla) e habilita a descoberta de interfaces.
* Enquanto você dorme, trabalha ou cozinha, seu nó escuta a rede. Ele descobre outros membros da comunidade local, valida suas Identidades de Rede e estabelece automaticamente ligações diretas.
* Seus dispositivos pessoais agora se conectam ao seu nó *local*, que está integrado a uma mesh local viva e dinâmica. Seu tráfego flui através de caminhos locais fornecidos por outras pessoas reais na comunidade, em vez de ricochetear em um servidor distante.

**Não espere que outros construam as redes que você gostaria de ver**. Cada rede é importante, talvez especialmente aquelas que apoiam famílias e indivíduos. Uma vez que exista infraestrutura pessoal e local suficiente, conectá-las diretamente umas às outras, sem atravessar a Internet pública, torna-se inevitável.

<p align="right"><a href="docs_pt-br.html">Próxima Página: Leia o Manual</a></p>
