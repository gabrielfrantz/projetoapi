<h1 align="center">API desenvolvida em Python e Flask, na qual se comunica com um banco de dados PostgreSQL, ambos em containers separados</h1>

<h2 align="left">Cada container possui seu Dockerfile específico, e ambos os arquivos são criados através de um Docker-compose.yaml</h2>

<h3 align="left">Teste de rota da API no container, através de um GET e seu Dockerfile</h3>

![image](https://github.com/gabrielfrantz/projetodevops/assets/33354703/79ed05cf-8525-4c9c-b378-423eef33237d)

![image](https://github.com/gabrielfrantz/projetodevops/assets/33354703/7ee997e7-2309-4a5e-9b0c-3c1a284f371c)

<h3 align="left">Banco de Dados PostgreSQL no container e seu Dockerfile</h3>

![image](https://github.com/gabrielfrantz/projetodevops/assets/33354703/f5136a5e-29cd-4f59-9b1b-92a50728189a)

![image](https://github.com/gabrielfrantz/projetodevops/assets/33354703/362d2cce-3f30-4912-ab13-e826cdb3cc3c)

<h3 align="left">Estrutura do Docker-compose</h3>

![image](https://github.com/gabrielfrantz/projetodevops/assets/33354703/e65ec5e6-16de-4691-84cc-1ac9a832d1ac)

<h3 align="left">Ambos estão rodando na mesma rede, em modo Bridge, para poderem se comunicar entre si</h3>
