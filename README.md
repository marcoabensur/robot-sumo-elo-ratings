# Elo Ratings Sumô de Robôs Brasil

## Sumário

**[Introdução](#introdução)**<br>
**[O que é Rating Elo?](#o-que-é-rating-elo)**<br>
**[Instruções](#instruções)**<br>
**[Premissas](#premissas)**<br>
**[Ranking Times Sumô 3kg Autônomo](#ranking-times-sumô-3kg-autônomo)**<br>
**[Ranking Robôs Sumô 3kg Autônomo](#ranking-robôs-sumô-3kg-autônomo)**<br>
**[Ranking Times Sumô 3kg Rádio-Controlado](#ranking-times-sumô-3kg-rádio-controlado)**<br>
**[Ranking Robôs Sumô 3kg Rádio-Controlado](#ranking-robôs-sumô-3kg-rádio-controlado)**<br>



## Introdução
No cenário competitivo de robótica, historicamente, há apenas um ranking nacional existente que é considerado relevante às equipes brasileiras, que é o ranking da [Robocore](https://www.robocore.net/modules.php?name=GR_Equipes) (organizadora de competições ao redor do país). Entretanto, o maior defeito deste ranking é o seu caráter **puramente cumulativo de resultados**, ou seja, um troféu de ouro conquistado em 2010 terá mesmo peso na pontuação da equipe que um troféu conquistado em 2022. Além disso, é interessante notar que com apenas a participação do robô em dada competição, é garantida no mínimo uma pontuação somada equivalente a $\frac{1}{Participantes na categoria}$, e nunca há situação em que a equipe tem sua pontuação deduzida, o que faz com que equipes com maior tempo de existência possuam uma vantagem enorme em relação às novas equipes.

Com isso, este projeto tem como intuito **projetar um ranking mais justo em relação à competitividade de robôs e equipes nas categorias Sumô 3kg (RC e Auto) no decorrer do tempo**. Para isso, foi utilizada uma simulação com base em pontuação de "Rating Elo".

## O que é Rating Elo?
O Rating Elo é um método estatístico que é conhecido por ser utilizado no Xadrez e em outros esportes competitivos, com o intuito de rankear os melhores jogadores, atribuindo a cada um deles uma pontuação numérica. Com base na pontuação numérica, é possível quantificar a "força" de cada competidor, o que faz com que uma vitória contra um competidor "forte" (ou seja, com Elo alto) seja mais recompensada em relação a uma vitória contra um competidor "fraco" (com Elo baixo). Esta mesma lógica também funciona para derrotas, porém em lógica reversa, ou seja, uma derrota contra um competidor "forte" deduz menos pontos, enquanto uma derrota contra um competidor "fraco" deduz mais pontos.

Para mais informações técnicas a respeito da aritmética por trás desse método, consulte a [Wikipedia](https://pt.wikipedia.org/wiki/Rating_Elo).

Para esse projeto, foi considerado que todo robô inicia com pontuação de elo igual a **1500**.

## Instruções

### Como rodar o programa?
Para rodar o programa (feito em Python), utilize o comando:

> python elo.py <rc/auto> <robot/team> <true/false>

Em que:
- rc/auto: determina se será feita a análise para a categoria 3kg RC (rc) ou 3kg Auto (auto);
- robot/team: determina se a análise será feita de acordo com times (team) ou robôs (robot);
- true/false: determina se os dados serão mostrados a cada competição (true) ou apenas a cada ano (false).

### Como atualizar as planilhas?
Para atualizar a planilha, é necessário criar um novo item correspondente à competição que deseja adicionar. Os dados básicos que devem ser fornecidos (com o intuito de facilitar a posterior verificação) são:
- Nome da competição (campo "name")
- Data da competição (campo "date"). Obs: para o primeiro teste, foi considerado sempre o último dia de competição.
- Link das chaves (campo "link")

Além disso, devem ser fornecidas as partidas em ordem cronológica (do mais antigo ao mais recente) com a seguinte sintaxe:

> ["Equipe Vencedora", "Equipe Derrotada"]

E que devem ser adicionadas no campo "matches". Já para os robôs, a sintaxe é bem similar, e devem ser adicionados no campo "matches-robot":

> ["Robô Vencedor", "Robô Derrotado"]

Para mais detalhes, consulte um arquivo .json presente nas pastas "rc" ou "auto".

## Premissas
Em relação às partidas listadas nos arquivos, foram considerados que:

- Partidas só possuem como resultado vitória/derrota, não importando o placar (o que inclui partidas que resultaram em W.O.). Isso ocorre devido à falta de informação para competições com chaveamento no sistema Robocore, que apenas indica o vencedor de cada luta;
- W.O.s em sua grande maioria são tratados como lutas disputadas, como descrito acima. Consideramos justo ser atribuído derrota a robôs que nao conseguiram ser finalizados com devida manutenção a tempo de lutar;
- O único caso exclusivo a essas afirmativas sobre o W.O. se dá para competições em que a equipe declarou ausência prévia na competição, e mesma assim seus robôs foram mantidos nas chaves por motivo desconhecido (por exemplo: ThundeRatz na IRON Cup 2022). Neste caso, foi considerado que as partidas não foram disputadas (ou seja, nenhuma equipe/robô teve seu elo alterado devido a essas partidas em específico);
- Partidas entre robôs de mesma equipe foram desconsideradas nos cálculos. Isso se deve ao fato de serem poucos os casos em que as partidas de fato ocorrem, além de que, matematicamente, irá punir a própria equipe, reduzindo seu Elo.

Na tentativa de se fazer um ranking mais justo e que reflita as reais habilidades dos competidores, algumas considerações foram realizadas para o ranking:

- Optou-se por **não se contabilizar equipes com menos de 10 partidas** no **ranking geral** e times com **menos de 5 partidas** no **ranking anual**. Isso porque para um elo ser mais representativo, um número maior de amostras se faz necessário;
- Para o **ranking geral** de robôs, considerou-se um mínimo de **8 partidas**. E, um mínimo de **5 partidas para o ranking anual**;
- Robôs estrangeiros não entram na classificação por se tratar de um ranking brasileiro.
- Optou-se por **não se contabilizar competições com menos de 4 robôs participantes**. Isso se deve ao fato de que, com poucos competidores, a pontuação de Elo se torna muito volátil, e não reflete a real habilidade dos competidores.

Dessa forma, as posições denominadas com "*" significam que o time ou o robô não atingiu o limite mínimo para ser contabilizado ou é estrangeiro, entretanto seu "Elo" ja é calculado e consta em ordem decrescente na lista. Por fim, é interessante notar que nos rankings a seguir, além de cada elo, estão contabilizados os números de Vitória e Derrota de cada equipe/robô, embora esta contabilização não seja utilizada diretamente no cálculo final de cada elo, e sirva apenas como um dado adicional a ser apresentado.

## Ranking Times Sumô 3kg Autônomo

<details>
<summary>Ranking Geral 2017-2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 155 / 042 | 1782 | KIMAUÁNISSO
| #02 | 026 / 017 | 1630 | Raijū
| #03 | 097 / 066 | 1624 | ThundeRatz
| #04 | 048 / 052 | 1585 | Equipe-Paralela
| #05 | 011 / 008 | 1554 | Robrow-Team
| #06 | 021 / 020 | 1552 | RioBotz
|  *  | 008 / 005 | 1551 | Sumomasters
|  *  | 005 / 002 | 1549 | Roshi-Team
| #07 | 017 / 013 | 1529 | SALVADOR-VIPERS
|  *  | 006 / 006 | 1525 | Team-Fiuna
| #08 | 009 / 006 | 1522 | PatoBots
|  *  | 002 / 003 | 1500 | SIRE-UB
| #09 | 007 / 010 | 1496 | Instituto-RSM
| #10 | 005 / 006 | 1496 | Expert-Robots
| #11 | 034 / 041 | 1496 | MinervaBots
|  *  | 001 / 002 | 1494 | Club-Robótica-IST-TUNGURAHUA
|  *  | 001 / 002 | 1494 | Autobots
|  *  | 003 / 004 | 1494 | BrBots
|  *  | 001 / 002 | 1492 | Cupim-do-aço
| #12 | 031 / 031 | 1491 | Equipe-Phoenix
|  *  | 001 / 002 | 1491 | ZOW-E
|  *  | 001 / 002 | 1490 | DragBotz
|  *  | 001 / 002 | 1489 | RoboCamp
|  *  | 001 / 002 | 1488 | Uai!rrior
|  *  | 000 / 002 | 1486 | Luison-Roboteam
|  *  | 000 / 002 | 1486 | ATIM
|  *  | 000 / 002 | 1486 | Netuno
| #13 | 022 / 028 | 1485 | Trincabotz
|  *  | 002 / 004 | 1485 | WickedBotz
|  *  | 000 / 002 | 1484 | Senai-SC
|  *  | 002 / 004 | 1483 | Ztronics-Unip
|  *  | 001 / 004 | 1483 | RAS-UFRB
|  *  | 003 / 006 | 1481 | Phoenix
|  *  | 000 / 002 | 1481 | Crossbots
|  *  | 000 / 002 | 1480 | Engetonica
|  *  | 000 / 002 | 1480 | GROM
|  *  | 000 / 002 | 1480 | EniacChallengers
|  *  | 000 / 002 | 1480 | EquipePUCPR
|  *  | 000 / 002 | 1480 | Vortex
|  *  | 000 / 002 | 1480 | GREAT
|  *  | 000 / 002 | 1480 | Machine-Eagle
| #14 | 008 / 012 | 1478 | WestBots
| #15 | 051 / 064 | 1472 | RobotBulls
|  *  | 000 / 004 | 1468 | UDITECH
|  *  | 002 / 006 | 1463 | UFBATS
| #16 | 002 / 008 | 1461 | Cupim-do-Aço
| #17 | 003 / 008 | 1455 | DotBotz
|  *  | 004 / 010 | 1452 | Polybot-Grenoble
| #18 | 003 / 010 | 1446 | Robótica-TERA
|  *  | 000 / 006 | 1443 | Ball-Robotics
| #19 | 037 / 053 | 1438 | FEG-Robótica
| #20 | 066 / 092 | 1437 | OMEGABOTZ
| #21 | 005 / 014 | 1427 | UERJBotz
</details>

<details>
<summary>2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 006 / 002 | 1537 | KIMAUÁNISSO
| #02 | 007 / 004 | 1531 | ThundeRatz
| #03 | 003 / 004 | 1492 | RobotBulls
|  *  | 000 / 002 | 1480 | Netuno
|  *  | 000 / 002 | 1480 | OMEGABOTZ
|  *  | 000 / 002 | 1480 | RioBotz
</details>

<details>
<summary>2024</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 024 / 005 | 1649 | KIMAUÁNISSO
| #02 | 008 / 002 | 1552 | RioBotz
|  *  | 005 / 000 | 1551 | Roshi-Team
| #03 | 021 / 018 | 1530 | Equipe-Paralela
| #04 | 019 / 015 | 1523 | ThundeRatz
| #05 | 007 / 006 | 1519 | Raijū
|  *  | 003 / 004 | 1496 | Team-Fiuna
| #06 | 005 / 006 | 1494 | MinervaBots
|  *  | 001 / 002 | 1492 | Autobots
|  *  | 001 / 002 | 1490 | Cupim-do-aço
|  *  | 001 / 002 | 1490 | Club-Robótica-IST-TUNGURAHUA
|  *  | 001 / 002 | 1489 | RAS-UFRB
|  *  | 001 / 002 | 1487 | PatoBots
| #07 | 002 / 004 | 1482 | Trincabotz
|  *  | 000 / 002 | 1481 | ATIM
| #08 | 004 / 006 | 1479 | OMEGABOTZ
| #09 | 002 / 004 | 1479 | Instituto-RSM
| #10 | 003 / 006 | 1474 | Phoenix
| #11 | 002 / 006 | 1466 | FEG-Robótica
|  *  | 000 / 004 | 1460 | UDITECH
| #12 | 008 / 020 | 1416 | RobotBulls

</details>

<details>
<summary>2023</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 028 / 008 | 1637 | KIMAUÁNISSO
| #02 | 010 / 003 | 1567 | Raijū
|  *  | 003 / 002 | 1513 | Team-Fiuna
| #03 | 012 / 012 | 1508 | ThundeRatz
|  *  | 002 / 002 | 1503 | Instituto-RSM
| #04 | 006 / 008 | 1502 | RobotBulls
| #05 | 004 / 004 | 1502 | MinervaBots
| #06 | 004 / 004 | 1497 | RioBotz
|  *  | 001 / 002 | 1492 | Equipe-Phoenix
| #07 | 011 / 012 | 1489 | Equipe-Paralela
| #08 | 004 / 006 | 1486 | Trincabotz
|  *  | 000 / 002 | 1483 | Luison-Roboteam
|  *  | 000 / 002 | 1483 | Robótica-TERA
|  *  | 000 / 002 | 1483 | Polybot-Grenoble
|  *  | 000 / 002 | 1481 | Roshi-Team
|  *  | 000 / 002 | 1480 | UERJBotz
| #09 | 001 / 004 | 1474 | OMEGABOTZ
| #10 | 002 / 005 | 1462 | FEG-Robótica
| #11 | 002 / 008 | 1448 | Cupim-do-Aço

</details>


<details>
<summary>2022</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 023 / 010 | 1575 | KIMAUÁNISSO
|  *  | 008 / 005 | 1536 | Sumomasters
| #02 | 013 / 012 | 1518 | RobotBulls
| #03 | 007 / 006 | 1516 | Raijū
| #04 | 006 / 006 | 1506 | Equipe-Paralela
| #05 | 004 / 003 | 1505 | FEG-Robótica
|  *  | 002 / 002 | 1502 | RioBotz
|  *  | 002 / 002 | 1500 | Equipe-Phoenix
| #06 | 010 / 011 | 1498 | ThundeRatz
| #07 | 006 / 006 | 1497 | Trincabotz
|  *  | 002 / 003 | 1492 | SIRE-UB
|  *  | 001 / 002 | 1489 | Robótica-TERA
|  *  | 001 / 002 | 1489 | Uai!rrior
|  *  | 000 / 002 | 1482 | RAS-UFRB
|  *  | 000 / 002 | 1479 | UERJBotz
| #08 | 008 / 013 | 1473 | OMEGABOTZ
| #09 | 000 / 006 | 1443 | MinervaBots

</details>

<details>
<summary>2021</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 008 / 003 | 1548 | ThundeRatz
| #02 | 005 / 002 | 1528 | KIMAUÁNISSO
| #03 | 006 / 004 | 1517 | Equipe-Paralela
| #04 | 004 / 004 | 1501 | RobotBulls
|  *  | 002 / 002 | 1500 | FEG-Robótica
|  *  | 001 / 002 | 1490 | SALVADOR-VIPERS
| #05 | 001 / 004 | 1468 | Equipe-Phoenix
| #06 | 002 / 008 | 1448 | OMEGABOTZ

</details>

<details>
<summary>2020</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 005 / 000 | 1550 | RioBotz
| #02 | 006 / 003 | 1528 | ThundeRatz
| #03 | 004 / 004 | 1500 | MinervaBots
|  *  | 002 / 002 | 1499 | Equipe-Paralela
| #04 | 003 / 004 | 1492 | RobotBulls
|  *  | 001 / 002 | 1491 | DotBotz
|  *  | 000 / 002 | 1480 | Senai-SC
|  *  | 000 / 002 | 1480 | Trincabotz
|  *  | 000 / 002 | 1479 | UFBATS

</details>

<details>
<summary>2019</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 031 / 006 | 1666 | KIMAUÁNISSO
| #02 | 018 / 010 | 1572 | ThundeRatz
| #03 | 014 / 010 | 1552 | RobotBulls
| #04 | 005 / 002 | 1532 | Robrow-Team
| #05 | 004 / 002 | 1518 | PatoBots
| #06 | 006 / 004 | 1517 | WestBots
|  *  | 002 / 002 | 1506 | Raijū
| #07 | 006 / 006 | 1501 | Trincabotz
| #08 | 003 / 004 | 1495 | RSM-Robótica
| #09 | 017 / 017 | 1493 | MinervaBots
| #10 | 003 / 004 | 1492 | SALVADOR-VIPERS
|  *  | 001 / 002 | 1490 | Robótica-TERA
|  *  | 001 / 002 | 1490 | UFBATS
|  *  | 001 / 002 | 1490 | DragBotz
|  *  | 001 / 002 | 1490 | RoboCamp
|  *  | 000 / 002 | 1482 | Crossbots
|  *  | 000 / 002 | 1480 | DotBotz
|  *  | 000 / 002 | 1480 | Polybot-Grenoble
|  *  | 000 / 002 | 1480 | Ball-Robotics
| #11 | 001 / 004 | 1474 | UERJBotz
| #12 | 004 / 008 | 1471 | Equipe-Phoenix
|  *  | 000 / 004 | 1461 | RioBotz
| #13 | 002 / 008 | 1459 | Equipe-Paralela
| #14 | 032 / 034 | 1447 | OMEGABOTZ
| #15 | 007 / 018 | 1431 | FEG-Robótica

</details>

<details>
<summary>2018</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 020 / 010 | 1593 | KIMAUÁNISSO
| #02 | 010 / 011 | 1557 | Equipe-Phoenix
| #03 | 010 / 006 | 1551 | ThundeRatz
| #04 | 000 / 003 | 1540 | SALVADOR-VIPERS
| #05 | 010 / 017 | 1511 | OMEGABOTZ
| #06 | 000 / 002 | 1510 | BrBots
| #07 | 010 / 012 | 1509 | FEG-Robótica
| #08 | 000 / 006 | 1508 | Robrow-Team
|  *  | 000 / 002 | 1502 | MinervaBots
|  *  | 000 / 002 | 1501 | Trincabotz
| #09 | 000 / 004 | 1494 | Expert-Robots
|  *  | 000 / 002 | 1491 | Ztronics-Unip
|  *  | 000 / 002 | 1491 | ZOW-E
|  *  | 000 / 002 | 1490 | UFBATS
|  *  | 000 / 002 | 1490 | Robótica-TERA
|  *  | 000 / 002 | 1488 | WestBots
| #10 | 000 / 004 | 1482 | Polybot-Grenoble
|  *  | 000 / 002 | 1481 | WickedBotz
|  *  | 000 / 002 | 1481 | RobotBulls
| #11 | 000 / 004 | 1481 | UERJBotz
|  *  | 000 / 002 | 1480 | Ball-Robotics
| #12 | 000 / 004 | 1480 | RioBotz
| #13 | 000 / 004 | 1480 | DotBotz
|  *  | 000 / 002 | 1480 | EquipePUCPR
|  *  | 000 / 002 | 1480 | Machine-Eagle
|  *  | 000 / 002 | 1480 | Equipe-Paralela
|  *  | 000 / 002 | 1480 | Vortex
|  *  | 000 / 002 | 1480 | GREAT

</details>

<details>
<summary>2017</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 015 / 001 | 1622 | KIMAUÁNISSO
| #02 | 007 / 004 | 1529 | ThundeRatz
| #03 | 004 / 002 | 1520 | PatoBots
| #04 | 006 / 004 | 1519 | SALVADOR-VIPERS
| #05 | 005 / 004 | 1512 | Equipe-Phoenix
| #06 | 009 / 007 | 1507 | FEG-Robótica
|  *  | 002 / 002 | 1502 | WickedBotz
|  *  | 002 / 002 | 1501 | MinervaBots
|  *  | 002 / 002 | 1500 | UERJBotz
|  *  | 002 / 002 | 1499 | Trincabotz
|  *  | 002 / 002 | 1499 | Expert-Robots
|  *  | 002 / 002 | 1499 | Polybot-Grenoble
|  *  | 001 / 002 | 1493 | Ztronics-Unip
| #07 | 004 / 008 | 1482 | OMEGABOTZ
|  *  | 000 / 002 | 1482 | RioBotz
|  *  | 000 / 002 | 1481 | BrBots
|  *  | 000 / 002 | 1481 | Robótica-TERA
|  *  | 000 / 002 | 1480 | Ball-Robotics
|  *  | 000 / 002 | 1480 | Engetonica
|  *  | 000 / 002 | 1480 | GROM
|  *  | 000 / 002 | 1480 | EniacChallengers
| #08 | 001 / 006 | 1453 | WestBots

</details>


## Ranking Robôs Sumô 3kg Autônomo


<details>
<summary>Ranking Geral 2017-2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 068 / 018 | 1729 | Eleven
| #02 | 029 / 011 | 1653 | Charizard
| #03 | 033 / 008 | 1652 | Paçoca
| #04 | 030 / 020 | 1606 | Galena
| #05 | 026 / 017 | 1605 | Raijū
| #06 | 015 / 004 | 1584 | Frank
|  *  | 007 / 000 | 1571 | Dolgorsuren
|  *  | 007 / 001 | 1567 | Masakrator
| #07 | 011 / 004 | 1564 | Stonehenge-Auto
| #08 | 019 / 012 | 1561 | Aldebaran+
| #09 | 020 / 012 | 1558 | Golem
|  *  | 005 / 000 | 1558 | Virus-MX
| #10 | 020 / 014 | 1556 | Coelho-Escovado
| #11 | 016 / 011 | 1544 | Drakkar
| #12 | 014 / 012 | 1537 | Itiban
| #13 | 009 / 008 | 1536 | Kamex
| #14 | 056 / 042 | 1531 | Moai
|  *  | 005 / 002 | 1531 | Salomão
|  *  | 003 / 001 | 1529 | Gyarados
| #15 | 009 / 006 | 1528 | MÔZÓVS
| #16 | 026 / 025 | 1525 | Bullbasauro-Descontrolado
|  *  | 004 / 002 | 1519 | KokiBot
|  *  | 003 / 002 | 1518 | Mbaretech-2.0
|  *  | 003 / 002 | 1512 | Odyssay
|  *  | 003 / 002 | 1511 | Paladino
| #17 | 007 / 007 | 1510 | Doge
|  *  | 003 / 002 | 1509 | Rancor
| #18 | 005 / 004 | 1509 | Cinnamon-Breaker
|  *  | 003 / 002 | 1508 | Cocha
| #19 | 006 / 005 | 1508 | Lobo
| #20 | 013 / 013 | 1507 | MetalGarurumon
| #21 | 009 / 010 | 1505 | Bullbasaur
| #22 | 006 / 006 | 1505 | Mensageiro-do-Caos
|  *  | 002 / 002 | 1505 | ExcaliBull
| #23 | 008 / 007 | 1505 | Traga-a-Vasilha
| #24 | 004 / 004 | 1503 | Daltonomo
|  *  | 002 / 002 | 1502 | Bender-II
|  *  | 002 / 002 | 1502 | Jean-Michel
| #25 | 012 / 012 | 1501 | Auterna
| #26 | 020 / 020 | 1501 | Atena
|  *  | 002 / 002 | 1500 | Bernadete
|  *  | 002 / 002 | 1500 | Hulk
|  *  | 003 / 004 | 1495 | Mbaretech
|  *  | 001 / 002 | 1494 | Optimus-prime
|  *  | 001 / 002 | 1494 | Amostradinho
|  *  | 001 / 002 | 1494 | Rabanete
|  *  | 003 / 004 | 1494 | JPLSM
|  *  | 001 / 002 | 1494 | TicoMia
|  *  | 002 / 003 | 1494 | SIRE-UB
|  *  | 001 / 002 | 1492 | SIGMA
|  *  | 001 / 002 | 1491 | PLC-ROBOT
|  *  | 001 / 002 | 1491 | Ciclope
|  *  | 001 / 002 | 1491 | PL-CH
|  *  | 001 / 002 | 1491 | Tanos
|  *  | 001 / 002 | 1490 | Optimus
|  *  | 001 / 002 | 1490 | Carvão
|  *  | 001 / 002 | 1490 | Judith
|  *  | 001 / 002 | 1490 | Brutus
|  *  | 001 / 002 | 1490 | Kakaroto
|  *  | 003 / 004 | 1490 | Catuaba
|  *  | 001 / 002 | 1490 | Gurizinho
|  *  | 001 / 002 | 1489 | ZOW-E
|  *  | 001 / 002 | 1489 | Locomotiva
| #27 | 004 / 006 | 1488 | Dinamite-Auto
|  *  | 000 / 002 | 1487 | Topotoropo
|  *  | 001 / 002 | 1487 | Roberto
|  *  | 000 / 002 | 1486 | Georges
|  *  | 002 / 004 | 1485 | Projeto-X
|  *  | 002 / 004 | 1485 | Bullvidoso
|  *  | 000 / 002 | 1485 | Bruxão
|  *  | 000 / 002 | 1485 | BULUC-CHABTAN
| #28 | 004 / 006 | 1484 | Bullvidoso-Descontrolado
|  *  | 000 / 002 | 1484 | Ganon
|  *  | 000 / 002 | 1483 | Ártemis
|  *  | 001 / 003 | 1482 | Shiny
|  *  | 000 / 002 | 1482 | Luison
|  *  | 000 / 002 | 1482 | Toro
|  *  | 002 / 004 | 1482 | Jack-Chumbo
|  *  | 000 / 002 | 1482 | Sumozão
|  *  | 000 / 002 | 1482 | Sindrome
|  *  | 000 / 002 | 1481 | CaLipe
|  *  | 001 / 004 | 1481 | SENAI-KOMBAT-23
|  *  | 000 / 002 | 1481 | Unit-One
|  *  | 000 / 002 | 1481 | Robotnik
|  *  | 000 / 002 | 1481 | Tohru
|  *  | 000 / 002 | 1481 | Sumo-EquipePUCPR1
|  *  | 000 / 002 | 1480 | Javelin
|  *  | 000 / 002 | 1480 | Panelinha
|  *  | 000 / 002 | 1480 | Cthulhu
|  *  | 000 / 002 | 1480 | Ariticum
|  *  | 000 / 002 | 1480 | Shenbong-Auto
|  *  | 000 / 002 | 1480 | BLL
|  *  | 000 / 002 | 1480 | Bot-Lee
|  *  | 000 / 002 | 1480 | Weng-Weng-2
|  *  | 000 / 002 | 1480 | Titan
|  *  | 000 / 002 | 1480 | Challenger
|  *  | 000 / 002 | 1480 | Facão-de-Pau
|  *  | 000 / 002 | 1480 | Rhinoceros
| #29 | 003 / 006 | 1480 | Skoll
|  *  | 002 / 004 | 1480 | Expert
|  *  | 000 / 002 | 1480 | Coiote+
|  *  | 000 / 002 | 1480 | Zerum
| #30 | 007 / 011 | 1476 | Ronda
| #31 | 006 / 008 | 1475 | PitBull
|  *  | 001 / 004 | 1475 | Golden-Boy
|  *  | 002 / 005 | 1474 | Bullvidoso+Controlado
|  *  | 000 / 003 | 1473 | Bender
|  *  | 001 / 004 | 1472 | Sr.Tarugo
|  *  | 001 / 004 | 1472 | Anchieta-Warrior
|  *  | 001 / 004 | 1471 | Zeidan
| #32 | 018 / 024 | 1467 | Hariyama
|  *  | 000 / 004 | 1466 | AngryBull
| #33 | 002 / 006 | 1466 | C3+
| #34 | 019 / 030 | 1463 | Kuro-Usagi
|  *  | 000 / 004 | 1463 | Tòbias
|  *  | 000 / 004 | 1462 | Totoro
| #35 | 002 / 006 | 1462 | Thanos
|  *  | 000 / 004 | 1461 | Sumo-BALL
| #36 | 004 / 009 | 1458 | Loba
| #37 | 007 / 014 | 1458 | Mooncake
| #38 | 020 / 031 | 1455 | RiscaFaca
| #39 | 008 / 015 | 1452 | Hachiko
| #40 | 006 / 013 | 1447 | Shiryu
| #41 | 002 / 009 | 1443 | Valeska
</details>

<details>
<summary>2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 006 / 002 | 1538 | Galena
|  *  | 003 / 001 | 1522 | Gyarados
|  *  | 003 / 001 | 1519 | Charizard
|  *  | 002 / 002 | 1500 | ExcaliBull
|  *  | 001 / 002 | 1490 | Bullbasauro-Descontrolado
|  *  | 001 / 002 | 1490 | Moai
|  *  | 000 / 002 | 1480 | Ártemis
|  *  | 000 / 002 | 1480 | Ganon
|  *  | 000 / 002 | 1480 | Aldebaran+
</details>


<details>
<summary>2024</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 012 / 002 | 1593 | Charizard
| #02 | 012 / 003 | 1582 | Eleven
| #03 | 008 / 002 | 1553 | Aldebaran+
|  *  | 005 / 000 | 1550 | Virus-MX
| #04 | 012 / 008 | 1534 | Galena
| #05 | 011 / 008 | 1525 | Coelho-Escovado
| #06 | 009 / 008 | 1517 | Kamex
| #07 | 007 / 006 | 1516 | Raijū
|  *  | 003 / 002 | 1513 | Mbaretech-2.0
| #08 | 006 / 006 | 1500 | Bullbasauro-Descontrolado
| #09 | 007 / 007 | 1499 | Moai
|  *  | 001 / 002 | 1492 | Optimus-prime
| #10 | 005 / 006 | 1492 | Atena
|  *  | 001 / 002 | 1490 | Cinnamon-Breaker
|  *  | 001 / 002 | 1490 | Kuro-Usagi
|  *  | 001 / 002 | 1490 | Ciclope
|  *  | 001 / 002 | 1490 | Tanos
|  *  | 001 / 002 | 1489 | Amostradinho
| #11 | 002 / 004 | 1483 | Skoll
| #12 | 002 / 004 | 1482 | Hariyama
| #13 | 004 / 006 | 1482 | RiscaFaca
| #14 | 002 / 004 | 1481 | Dinamite-Auto
|  *  | 000 / 002 | 1481 | Topotoropo
|  *  | 000 / 002 | 1480 | Mbaretech
|  *  | 000 / 002 | 1480 | BULUC-CHABTAN
| #15 | 002 / 004 | 1480 | Bullvidoso
|  *  | 000 / 002 | 1480 | AngryBull
|  *  | 000 / 002 | 1480 | Loba
|  *  | 000 / 002 | 1480 | Bullvidoso-Descontrolado
|  *  | 000 / 002 | 1480 | Bot-Lee
| #16 | 003 / 006 | 1474 | Mooncake
| #17 | 000 / 006 | 1443 | PitBull

</details>

<details>
<summary>2023</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 015 / 004 | 1591 | Eleven
| #02 | 010 / 003 | 1566 | Charizard
| #03 | 010 / 003 | 1565 | Raijū
| #04 | 009 / 006 | 1525 | Coelho-Escovado
| #05 | 008 / 006 | 1523 | Galena
|  *  | 003 / 001 | 1520 | Frank
|  *  | 003 / 002 | 1510 | Mbaretech
| #06 | 006 / 006 | 1508 | Bullbasauro-Descontrolado
|  *  | 002 / 002 | 1502 | Dinamite-Auto
| #07 | 004 / 004 | 1501 | Atena
| #08 | 004 / 004 | 1498 | Aldebaran+
|  *  | 001 / 002 | 1491 | Mooncake
|  *  | 001 / 002 | 1491 | Skoll
|  *  | 000 / 001 | 1490 | Hachiko
|  *  | 001 / 002 | 1489 | Loba
| #09 | 004 / 006 | 1485 | Hariyama
| #10 | 004 / 006 | 1483 | Moai
|  *  | 000 / 002 | 1482 | Georges
|  *  | 000 / 002 | 1481 | Sindrome
|  *  | 000 / 002 | 1481 | Shenbong-Auto
|  *  | 000 / 002 | 1480 | Luison
|  *  | 000 / 002 | 1480 | Bullvidoso+Controlado
|  *  | 000 / 002 | 1480 | Totoro
| #11 | 001 / 004 | 1473 | SENAI-KOMBAT-23
| #12 | 001 / 004 | 1472 | Anchieta-Warrior
| #13 | 001 / 004 | 1472 | RiscaFaca
| #14 | 002 / 006 | 1461 | Kuro-Usagi

</details>

<details>
<summary>2022</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 014 / 004 | 1574 | Eleven
|  *  | 007 / 001 | 1561 | Masakrator
| #02 | 011 / 009 | 1527 | Bullbasauro-Descontrolado
| #03 | 006 / 003 | 1526 | Paçoca
| #04 | 007 / 006 | 1513 | Raijū
|  *  | 002 / 001 | 1509 | Loba
| #05 | 006 / 006 | 1506 | Kuro-Usagi
| #06 | 004 / 004 | 1504 | Galena
|  *  | 002 / 002 | 1501 | Aldebaran+
|  *  | 002 / 002 | 1500 | Mooncake
| #07 | 003 / 003 | 1499 | Charizard
|  *  | 002 / 002 | 1498 | Hachiko
| #08 | 006 / 006 | 1496 | Hariyama
| #09 | 006 / 007 | 1491 | Moai
| #10 | 002 / 003 | 1491 | Bullvidoso+Controlado
|  *  | 002 / 003 | 1491 | SIRE-UB
|  *  | 001 / 002 | 1490 | Shiny
|  *  | 001 / 002 | 1490 | Roberto
|  *  | 001 / 002 | 1490 | Locomotiva
| #11 | 008 / 011 | 1483 | RiscaFaca
|  *  | 000 / 002 | 1482 | Bruxão
|  *  | 000 / 002 | 1480 | Shiryu
|  *  | 000 / 002 | 1480 | Valeska
|  *  | 000 / 002 | 1479 | Javelin
|  *  | 000 / 002 | 1479 | Totoro
|  *  | 000 / 004 | 1460 | Atena

</details>

<details>
<summary>2021</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 008 / 003 | 1549 | Moai
|  *  | 004 / 000 | 1539 | Eleven
| #02 | 006 / 004 | 1519 | Kuro-Usagi
| #03 | 004 / 004 | 1501 | Bullvidoso-Descontrolado
|  *  | 002 / 002 | 1500 | Hachiko
|  *  | 001 / 002 | 1490 | Charizard
|  *  | 001 / 002 | 1490 | Traga-a-Vasilha
|  *  | 000 / 001 | 1489 | Shiny
| #04 | 002 / 004 | 1481 | RiscaFaca
|  *  | 000 / 003 | 1471 | Shiryu
| #05 | 001 / 004 | 1471 | Mooncake

</details>

<details>
<summary>2020</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 005 / 000 | 1549 | Aldebaran+
| #02 | 004 / 001 | 1530 | Stonehenge-Auto
| #03 | 003 / 002 | 1510 | Atena
|  *  | 002 / 002 | 1501 | Moai
|  *  | 002 / 002 | 1501 | Bullbasauro-Descontrolado
|  *  | 002 / 002 | 1499 | Kuro-Usagi
|  *  | 001 / 001 | 1499 | Auterna
|  *  | 001 / 002 | 1491 | Golden-Boy
|  *  | 000 / 001 | 1490 | Valeska
|  *  | 001 / 002 | 1490 | PitBull
|  *  | 000 / 002 | 1480 | Hariyama
|  *  | 000 / 002 | 1480 | Thanos
|  *  | 000 / 002 | 1480 | Toro
</details>


<details>
<summary>2019</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 015 / 003 | 1610 | Eleven
| #02 | 012 / 003 | 1571 | Frank
| #03 | 005 / 000 | 1550 | PitBull
| #04 | 009 / 004 | 1543 | Itiban
| #05 | 007 / 003 | 1540 | Stonehenge-Auto
|  *  | 004 / 000 | 1539 | Paçoca
| #06 | 008 / 004 | 1536 | Atena
| #07 | 011 / 007 | 1534 | Moai
| #08 | 005 / 002 | 1529 | Salomão
| #09 | 004 / 002 | 1517 | Cinnamon-Breaker
| #10 | 006 / 004 | 1515 | Doge
| #11 | 003 / 002 | 1509 | Rancor
| #12 | 003 / 002 | 1508 | Cocha
|  *  | 002 / 002 | 1504 | Raijū
|  *  | 002 / 002 | 1501 | MÔZÓVS
| #13 | 006 / 006 | 1499 | Hariyama
| #14 | 009 / 010 | 1497 | Bullbasaur
| #15 | 003 / 004 | 1495 | JPLSM
| #16 | 003 / 004 | 1495 | Golem
| #17 | 005 / 006 | 1493 | RiscaFaca
| #18 | 005 / 006 | 1493 | Drakkar
| #19 | 007 / 007 | 1493 | Auterna
|  *  | 001 / 002 | 1491 | Traga-a-Vasilha
|  *  | 001 / 002 | 1490 | SIGMA
|  *  | 001 / 002 | 1490 | Brutus
|  *  | 001 / 002 | 1490 | Thanos
|  *  | 001 / 002 | 1490 | Jack-Chumbo
| #20 | 006 / 008 | 1487 | Shiryu
| #21 | 002 / 004 | 1483 | Projeto-X
|  *  | 000 / 002 | 1481 | Tòbias
|  *  | 000 / 002 | 1481 | CaLipe
|  *  | 000 / 002 | 1480 | Golden-Boy
|  *  | 000 / 002 | 1480 | Coiote+
|  *  | 000 / 002 | 1480 | Aldebaran+
|  *  | 000 / 002 | 1480 | Sumo-BALL
| #22 | 004 / 006 | 1479 | Hachiko
|  *  | 000 / 002 | 1479 | Zerum
| #23 | 001 / 004 | 1475 | Loba
| #24 | 001 / 004 | 1472 | Sr.Tarugo
| #25 | 001 / 004 | 1472 | Ronda
| #26 | 001 / 004 | 1471 | Zeidan
| #27 | 002 / 006 | 1463 | Valeska
|  *  | 000 / 004 | 1461 | MetalGarurumon
| #28 | 002 / 008 | 1454 | Kuro-Usagi

</details>

<details>
<summary>2018</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 007 / 000 | 1569 | Dolgorsuren
| #02 | 011 / 005 | 1557 | Drakkar
| #03 | 013 / 006 | 1556 | Golem
| #04 | 012 / 006 | 1549 | Moai
| #05 | 010 / 006 | 1542 | Paçoca
| #06 | 008 / 004 | 1537 | Eleven
| #07 | 009 / 006 | 1535 | MetalGarurumon
|  *  | 003 / 001 | 1521 | Traga-a-Vasilha
| #08 | 004 / 002 | 1520 | MÔZÓVS
| #09 | 003 / 002 | 1511 | Odyssay
| #10 | 003 / 002 | 1510 | Paladino
| #11 | 005 / 005 | 1504 | Ronda
| #12 | 006 / 006 | 1501 | Mensageiro-do-Caos
|  *  | 002 / 002 | 1501 | Jean-Michel
|  *  | 002 / 002 | 1501 | Auterna
|  *  | 002 / 002 | 1500 | Daltonomo
|  *  | 002 / 002 | 1499 | Lobo
|  *  | 001 / 002 | 1491 | Jack-Chumbo
|  *  | 001 / 002 | 1491 | PL-CH
|  *  | 001 / 002 | 1490 | Optimus
|  *  | 001 / 002 | 1490 | Judith
|  *  | 001 / 002 | 1490 | Carvão
|  *  | 001 / 002 | 1490 | Catuaba
|  *  | 001 / 002 | 1490 | ZOW-E
|  *  | 001 / 002 | 1490 | Thanos
|  *  | 001 / 002 | 1489 | Kakaroto
|  *  | 000 / 002 | 1481 | Sumozão
|  *  | 000 / 002 | 1481 | AngryBull
|  *  | 000 / 002 | 1481 | Doge
|  *  | 000 / 002 | 1480 | Tohru
|  *  | 000 / 002 | 1480 | Sumo-EquipePUCPR1
|  *  | 000 / 002 | 1480 | Robotnik
| #13 | 002 / 004 | 1480 | C3+
|  *  | 000 / 002 | 1480 | BLL
|  *  | 000 / 002 | 1480 | Kuro-Usagi
|  *  | 000 / 002 | 1480 | Weng-Weng-2
|  *  | 000 / 002 | 1480 | Tòbias
|  *  | 000 / 002 | 1480 | Expert
| #14 | 004 / 007 | 1479 | Itiban
|  *  | 000 / 003 | 1473 | Bender
|  *  | 000 / 004 | 1462 | Hachiko
</details>

<details>
<summary>2017</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 013 / 001 | 1608 | Paçoca
| #02 | 007 / 004 | 1525 | Moai
| #03 | 004 / 002 | 1522 | Golem
|  *  | 002 / 000 | 1521 | Eleven
| #04 | 004 / 002 | 1519 | KokiBot
| #05 | 003 / 002 | 1511 | Traga-a-Vasilha
| #06 | 003 / 002 | 1509 | MÔZÓVS
| #07 | 004 / 003 | 1509 | Lobo
| #08 | 004 / 003 | 1509 | MetalGarurumon
|  *  | 001 / 001 | 1503 | Doge
|  *  | 002 / 002 | 1502 | Bender-II
|  *  | 001 / 001 | 1501 | Itiban
|  *  | 002 / 002 | 1500 | Bernadete
|  *  | 002 / 002 | 1500 | Auterna
|  *  | 002 / 002 | 1500 | Expert
|  *  | 002 / 002 | 1500 | Catuaba
|  *  | 002 / 002 | 1500 | Daltonomo
|  *  | 002 / 002 | 1500 | Hulk
|  *  | 001 / 002 | 1494 | Rabanete
|  *  | 001 / 002 | 1494 | TicoMia
|  *  | 001 / 002 | 1491 | PLC-ROBOT
|  *  | 001 / 002 | 1490 | Gurizinho
|  *  | 001 / 002 | 1490 | Ronda
|  *  | 000 / 002 | 1481 | Unit-One
|  *  | 000 / 002 | 1481 | C3+
|  *  | 000 / 002 | 1480 | Sumo-BALL
|  *  | 000 / 002 | 1480 | Panelinha
|  *  | 000 / 002 | 1480 | Cthulhu
|  *  | 000 / 002 | 1480 | Ariticum
|  *  | 000 / 002 | 1480 | Titan
|  *  | 000 / 002 | 1480 | Challenger
|  *  | 000 / 002 | 1480 | Facão-de-Pau
|  *  | 000 / 002 | 1480 | Rhinoceros

</details>


## Ranking Times Sumô 3kg Rádio-Controlado

<details>
<summary>Ranking Geral 2017-2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 198 / 049 | 1843 | KIMAUÁNISSO
| #02 | 131 / 081 | 1647 | ThundeRatz
| #03 | 063 / 046 | 1643 | Equipe-Paralela
| #04 | 022 / 018 | 1577 | Raijū
|  *  | 005 / 002 | 1562 | Roshi-Team
| #05 | 015 / 009 | 1543 | UFFight
| #06 | 020 / 015 | 1532 | Imperial-Botz
| #07 | 018 / 024 | 1517 | RioBotz
|  *  | 002 / 002 | 1510 | Club-Robótica-IST-TUNGURAHUA
| #08 | 005 / 006 | 1507 | Instituto-RSM
| #09 | 028 / 033 | 1504 | Trincabotz
|  *  | 001 / 002 | 1501 | SIRE-UB
| #10 | 005 / 006 | 1501 | Robótica-TERA
|  *  | 001 / 002 | 1496 | CEEPTRON
|  *  | 001 / 002 | 1495 | PinoyFlash
|  *  | 001 / 002 | 1495 | GERSE
|  *  | 003 / 004 | 1493 | Quantum-team
| #11 | 009 / 011 | 1492 | SALVADOR-VIPERS
|  *  | 001 / 002 | 1491 | Expert-Robots
| #12 | 046 / 065 | 1490 | Phoenix
|  *  | 000 / 002 | 1488 | INTACTUZ
|  *  | 000 / 002 | 1487 | Spark-Team
|  *  | 000 / 002 | 1487 | Netuno
|  *  | 000 / 002 | 1486 | GEAR-EST
|  *  | 000 / 002 | 1486 | Quantum-Team
| #13 | 017 / 026 | 1486 | Uai!rrior
|  *  | 002 / 004 | 1486 | UFFight-Robotica
|  *  | 000 / 002 | 1485 | Titans
|  *  | 000 / 002 | 1483 | Star-Bots
| #14 | 038 / 053 | 1481 | MinervaBots
|  *  | 000 / 002 | 1480 | GER
|  *  | 000 / 002 | 1480 | BrBots
|  *  | 000 / 002 | 1478 | GaudérioBotz
| #15 | 043 / 067 | 1477 | RobotBulls
|  *  | 002 / 005 | 1474 | DragonBotz
|  *  | 000 / 004 | 1467 | ERA
|  *  | 000 / 004 | 1465 | OVERLOAD
|  *  | 000 / 004 | 1464 | DotBotz
|  *  | 000 / 004 | 1462 | Haka
|  *  | 000 / 006 | 1461 | UDITECH
| #16 | 062 / 107 | 1459 | OMEGABOTZ
|  *  | 001 / 006 | 1456 | UERJBotz
|  *  | 001 / 008 | 1451 | RSM-Robótica
| #17 | 002 / 008 | 1451 | TamanduTech
| #18 | 001 / 010 | 1450 | Equipe-Atena-SEMEAR
|  *  | 000 / 006 | 1445 | Bodetronic
| #19 | 003 / 024 | 1355 | ESC-Escola-de-Robótica-São-Caetano
</details>

<details>
<summary>2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 007 / 000 | 1565 | KIMAUÁNISSO
| #02 | 003 / 002 | 1508 | Instituto-RSM
| #03 | 004 / 004 | 1502 | ThundeRatz
| #04 | 003 / 004 | 1492 | RobotBulls
|  *  | 001 / 002 | 1491 | RioBotz
|  *  | 000 / 002 | 1481 | Netuno
|  *  | 000 / 004 | 1461 | OMEGABOTZ

</details>


<details>
<summary>2024</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 035 / 010 | 1672 | KIMAUÁNISSO
| #02 | 025 / 015 | 1577 | ThundeRatz
| #03 | 021 / 016 | 1551 | Equipe-Paralela
|  *  | 005 / 002 | 1533 | Roshi-Team
| #04 | 005 / 004 | 1516 | RioBotz
| #05 | 007 / 006 | 1508 | Raijū
|  *  | 002 / 002 | 1501 | Robótica-TERA
|  *  | 002 / 002 | 1501 | Club-Robótica-IST-TUNGURAHUA
| #06 | 004 / 006 | 1492 | MinervaBots
|  *  | 001 / 002 | 1491 | CEEPTRON
| #07 | 003 / 004 | 1491 | Trincabotz
|  *  | 000 / 002 | 1483 | Spark-Team
|  *  | 000 / 002 | 1482 | Equipe-Atena-SEMEAR
| #08 | 002 / 004 | 1482 | Instituto-RSM
|  *  | 000 / 002 | 1481 | GEAR-EST
|  *  | 000 / 002 | 1481 | Quantum-Team
| #09 | 002 / 004 | 1480 | UFFight-Robotica
|  *  | 000 / 002 | 1479 | UERJBotz
| #10 | 007 / 012 | 1471 | OMEGABOTZ
| #11 | 002 / 007 | 1457 | Phoenix
|  *  | 000 / 006 | 1444 | UDITECH
| #12 | 010 / 021 | 1427 | RobotBulls

</details>


<details>
<summary>2023</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 018 / 004 | 1616 | KIMAUÁNISSO
| #02 | 008 / 004 | 1534 | Raijū
| #03 | 010 / 008 | 1518 | Equipe-Paralela
| #04 | 003 / 002 | 1511 | RioBotz
|  *  | 002 / 002 | 1500 | Uai!rrior
| #05 | 006 / 007 | 1497 | ThundeRatz
| #06 | 003 / 004 | 1490 | Trincabotz
|  *  | 001 / 002 | 1489 | Equipe-Atena-SEMEAR
| #07 | 005 / 008 | 1483 | Phoenix
|  *  | 000 / 002 | 1480 | UERJBotz
| #08 | 003 / 006 | 1475 | MinervaBots
| #09 | 001 / 004 | 1472 | TamanduTech
| #10 | 001 / 004 | 1470 | OMEGABOTZ
| #11 | 002 / 006 | 1465 | RobotBulls

</details>

<details>
<summary>2022</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 043 / 008 | 1718 | KIMAUÁNISSO
| #02 | 022 / 017 | 1540 | ThundeRatz
| #03 | 008 / 006 | 1527 | Equipe-Paralela
| #04 | 009 / 009 | 1511 | Phoenix
|  *  | 002 / 002 | 1505 | RioBotz
| #05 | 006 / 006 | 1503 | Raijū
|  *  | 002 / 002 | 1500 | Robótica-TERA
|  *  | 001 / 002 | 1492 | SIRE-UB
|  *  | 001 / 002 | 1491 | GERSE
|  *  | 001 / 002 | 1491 | PinoyFlash
|  *  | 001 / 002 | 1489 | UERJBotz
| #06 | 010 / 013 | 1487 | OMEGABOTZ
|  *  | 001 / 002 | 1485 | UFFight
| #07 | 008 / 011 | 1484 | Uai!rrior
| #08 | 009 / 013 | 1482 | RobotBulls
|  *  | 000 / 002 | 1482 | Titans
|  *  | 000 / 002 | 1479 | Star-Bots
| #09 | 004 / 007 | 1476 | Trincabotz
| #10 | 001 / 004 | 1468 | TamanduTech
|  *  | 000 / 004 | 1467 | Equipe-Atena-SEMEAR
|  *  | 000 / 004 | 1465 | ERA
| #11 | 004 / 013 | 1436 | MinervaBots

</details>

<details>
<summary>2021</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 010 / 003 | 1566 | KIMAUÁNISSO
| #02 | 006 / 004 | 1520 | ThundeRatz
| #03 | 006 / 004 | 1518 | Equipe-Paralela
|  *  | 002 / 002 | 1501 | Trincabotz
| #04 | 006 / 008 | 1486 | Phoenix
| #05 | 005 / 007 | 1481 | OMEGABOTZ
| #06 | 003 / 005 | 1479 | Uai!rrior
|  *  | 000 / 002 | 1478 | SALVADOR-VIPERS
| #07 | 001 / 004 | 1471 | RobotBulls
</details>

<details>
<summary>2020</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 006 / 002 | 1539 | Trincabotz
| #02 | 004 / 001 | 1529 | UFFight
| #03 | 004 / 004 | 1501 | ThundeRatz
|  *  | 002 / 002 | 1500 | Equipe-Paralela
|  *  | 002 / 002 | 1500 | Uai!rrior
| #04 | 003 / 003 | 1499 | RobotBulls
|  *  | 001 / 002 | 1490 | RioBotz
| #05 | 003 / 005 | 1482 | MinervaBots
|  *  | 000 / 002 | 1480 | DotBotz
|  *  | 000 / 002 | 1480 | ESC-Escola-de-Robótica-São-Caetano
</details>

<details>
<summary>2019</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 036 / 009 | 1680 | KIMAUÁNISSO
| #02 | 028 / 009 | 1624 | ThundeRatz
| #03 | 014 / 008 | 1560 | Equipe-Paralela
| #04 | 003 / 002 | 1512 | SALVADOR-VIPERS
| #05 | 012 / 012 | 1509 | RobotBulls
|  *  | 002 / 002 | 1500 | UFFight
| #06 | 017 / 017 | 1498 | MinervaBots
|  *  | 001 / 002 | 1496 | Raijū
| #07 | 006 / 008 | 1490 | Trincabotz
|  *  | 001 / 002 | 1490 | Quantum-team
|  *  | 001 / 002 | 1489 | Uai!rrior
|  *  | 000 / 002 | 1482 | OVERLOAD
|  *  | 000 / 002 | 1480 | DotBotz
|  *  | 000 / 002 | 1479 | GaudérioBotz
|  *  | 000 / 004 | 1462 | RioBotz
| #08 | 031 / 044 | 1456 | OMEGABOTZ
| #09 | 000 / 006 | 1447 | RSM-Robótica
| #10 | 008 / 014 | 1443 | Phoenix
| #11 | 001 / 014 | 1394 | ESC-Escola-de-Robótica-São-Caetano
</details>

<details>
<summary>2018</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 030 / 011 | 1622 | KIMAUÁNISSO
| #02 | 022 / 011 | 1597 | ThundeRatz
| #03 | 005 / 004 | 1511 | SALVADOR-VIPERS
| #04 | 007 / 006 | 1510 | Imperial-Botz
| #05 | 005 / 004 | 1509 | MinervaBots
|  *  | 002 / 002 | 1501 | Quantum-team
|  *  | 002 / 002 | 1501 | Trincabotz
|  *  | 002 / 002 | 1499 | UFFight
| #06 | 003 / 004 | 1491 | RioBotz
|  *  | 000 / 002 | 1480 | RobotBulls
|  *  | 000 / 002 | 1480 | OVERLOAD
|  *  | 000 / 002 | 1480 | Uai!rrior
| #07 | 008 / 011 | 1480 | Phoenix
| #08 | 002 / 005 | 1473 | DragonBotz
|  *  | 000 / 004 | 1461 | Bodetronic
| #09 | 002 / 008 | 1452 | ESC-Escola-de-Robótica-São-Caetano
| #10 | 007 / 017 | 1451 | OMEGABOTZ
</details>

<details>
<summary>2017</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 007 / 002 | 1552 | KIMAUÁNISSO
| #02 | 011 / 006 | 1541 | ThundeRatz
| #03 | 006 / 002 | 1539 | UFFight
| #04 | 013 / 009 | 1530 | Imperial-Botz
| #05 | 005 / 004 | 1509 | Phoenix
|  *  | 002 / 002 | 1502 | Trincabotz
|  *  | 002 / 002 | 1500 | MinervaBots
|  *  | 001 / 002 | 1491 | Expert-Robots
|  *  | 001 / 002 | 1490 | RioBotz
|  *  | 001 / 003 | 1484 | SALVADOR-VIPERS
|  *  | 000 / 002 | 1481 | Bodetronic
|  *  | 000 / 002 | 1480 | GER
|  *  | 000 / 002 | 1480 | BrBots
|  *  | 000 / 004 | 1462 | Haka
| #06 | 001 / 006 | 1459 | OMEGABOTZ
</details>



## Ranking Robôs Sumô 3kg Rádio-Controlado

<details>
<summary>Ranking Geral 2017-2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 064 / 012 | 1768 | Eleven-RC
| #02 | 049 / 006 | 1754 | Paçoca-RC
| #03 | 038 / 012 | 1668 | Frank-RC
| #04 | 042 / 013 | 1666 | Stonehenge
| #05 | 039 / 024 | 1619 | Galena-RC
| #06 | 023 / 013 | 1607 | Coelho-Escovado
| #07 | 020 / 009 | 1599 | Charizard-RC
|  *  | 005 / 000 | 1568 | Scar-MX
| #08 | 010 / 005 | 1554 | Dolgorsuren-Dagvadorj
| #09 | 007 / 002 | 1551 | Banguela-RC
| #10 | 022 / 018 | 1551 | Raijū-RC
| #11 | 010 / 006 | 1544 | Bullbasauro-Controlado
| #12 | 033 / 026 | 1539 | Kuro-Usagi
| #13 | 008 / 004 | 1536 | Mr.PIG
|  *  | 004 / 001 | 1534 | Thorkell
| #14 | 048 / 042 | 1534 | Moai-RC
|  *  | 005 / 002 | 1532 | CaiPiloto
|  *  | 003 / 000 | 1532 | Gyarados-RC
| #15 | 010 / 006 | 1530 | Paladino
| #16 | 008 / 005 | 1526 | Harry-Porco
| #17 | 021 / 025 | 1516 | Bullbasaur-Controlado
| #18 | 007 / 005 | 1514 | PitBull-Controlado
|  *  | 002 / 001 | 1512 | Autistônomo
| #19 | 007 / 007 | 1508 | Kamex
|  *  | 002 / 002 | 1507 | Tanos
| #20 | 018 / 020 | 1507 | Atena
| #21 | 014 / 016 | 1505 | Aldebaran
| #22 | 012 / 013 | 1505 | Shiryu
| #23 | 007 / 007 | 1505 | Itiban
| #24 | 008 / 008 | 1504 | Roberto
| #25 | 006 / 006 | 1503 | Môzóvs
|  *  | 001 / 001 | 1503 | Zabullza
|  *  | 001 / 001 | 1501 | Areki
|  *  | 002 / 002 | 1501 | Gordox
|  *  | 002 / 002 | 1501 | Morgana
|  *  | 002 / 002 | 1500 | Seppuku
|  *  | 002 / 002 | 1499 | MiniZord
| #26 | 011 / 015 | 1499 | Mooncake
|  *  | 002 / 002 | 1497 | O-Agonia
| #27 | 025 / 029 | 1496 | Ronda
|  *  | 001 / 002 | 1495 | Gorax-2.0
|  *  | 003 / 004 | 1495 | Shenbong-RC
|  *  | 000 / 001 | 1493 | Phoenix
|  *  | 001 / 002 | 1493 | MadimBull
|  *  | 001 / 002 | 1493 | RalaCoxa
|  *  | 000 / 001 | 1493 | Utopia
|  *  | 001 / 002 | 1492 | Poko-Loko
|  *  | 001 / 002 | 1491 | SIRE-RC-UB
|  *  | 000 / 001 | 1491 | Adubinho
|  *  | 001 / 002 | 1491 | Grigio
|  *  | 001 / 002 | 1491 | Titan
|  *  | 001 / 002 | 1491 | Odyssay
|  *  | 000 / 001 | 1491 | Ninjai
|  *  | 001 / 002 | 1490 | Mareta
|  *  | 001 / 002 | 1490 | Rato
| #28 | 006 / 008 | 1490 | Dinamite
| #29 | 004 / 007 | 1488 | Zoio
|  *  | 001 / 002 | 1488 | Leia
|  *  | 000 / 002 | 1486 | Moto-Moto-RC
|  *  | 000 / 002 | 1485 | Topotoropo-RC
|  *  | 002 / 004 | 1485 | Fanático
|  *  | 000 / 002 | 1485 | Bot-Lee-RC
| #30 | 003 / 005 | 1484 | Traga-Vasilha
|  *  | 000 / 002 | 1484 | The-Arsonist
|  *  | 000 / 002 | 1483 | Sindrome-RC
|  *  | 000 / 002 | 1482 | Trator
|  *  | 000 / 002 | 1482 | Batata
|  *  | 000 / 002 | 1482 | Ganon
| #31 | 004 / 006 | 1482 | C3
|  *  | 000 / 002 | 1482 | Vader-2
| #32 | 004 / 006 | 1482 | Porco-Aranha
|  *  | 000 / 002 | 1481 | Supra-Sumo
|  *  | 000 / 002 | 1481 | Killer
|  *  | 000 / 002 | 1481 | Manivela
|  *  | 000 / 002 | 1481 | Faustinho
|  *  | 000 / 002 | 1481 | INTACTUZ V1.0
|  *  | 000 / 002 | 1481 | Poco-Loco
|  *  | 000 / 002 | 1481 | Coiote
|  *  | 000 / 002 | 1481 | Hulk-TSI
|  *  | 001 / 004 | 1481 | ExcaliBull
|  *  | 000 / 002 | 1481 | Bullbasaur-RC
|  *  | 000 / 002 | 1480 | Clayton
|  *  | 000 / 002 | 1480 | Anoobs-II
|  *  | 000 / 002 | 1480 | HAKA-B
|  *  | 000 / 002 | 1480 | HAKA-A
|  *  | 000 / 002 | 1480 | Calypso
|  *  | 000 / 002 | 1480 | Kaizen
|  *  | 000 / 002 | 1479 | Máquina-do-Mal
|  *  | 000 / 002 | 1479 | Bidê
|  *  | 000 / 002 | 1479 | Syrax-RC
| #33 | 010 / 016 | 1478 | Drakkar
|  *  | 001 / 004 | 1477 | PitBull-RC
|  *  | 001 / 004 | 1477 | Urutu
| #34 | 004 / 007 | 1476 | Blanka
|  *  | 001 / 004 | 1476 | Tractiana
| #35 | 028 / 033 | 1476 | Hariyama
| #36 | 002 / 006 | 1474 | Artemis-RC
|  *  | 001 / 004 | 1473 | Cleytompson
| #37 | 004 / 008 | 1473 | Se-Pega-no-Olho
|  *  | 002 / 005 | 1471 | EtecAP
| #38 | 002 / 006 | 1471 | Mooncake-RC
|  *  | 001 / 004 | 1469 | Totoro-RC
|  *  | 001 / 004 | 1469 | Pericão
|  *  | 000 / 004 | 1466 | Jotunheim
| #39 | 002 / 006 | 1466 | Auterna
|  *  | 000 / 004 | 1463 | Zé-Torquinho
|  *  | 000 / 004 | 1461 | HeavyBull
| #40 | 008 / 014 | 1458 | Golem
| #41 | 017 / 029 | 1457 | RiscaFaca
| #42 | 002 / 008 | 1453 | Zerum
|  *  | 000 / 006 | 1446 | JPLSM
|  *  | 000 / 006 | 1444 | Tomoe
| #43 | 001 / 010 | 1439 | Kurupira
| #44 | 018 / 027 | 1432 | Valeska
| #45 | 003 / 016 | 1401 | Bullvidoso-Controlado
| #46 | 000 / 012 | 1398 | Rampinha
</details>

<details>
<summary>2025</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
|  *  | 004 / 000 | 1539 | Charizard-RC
|  *  | 003 / 000 | 1530 | Gyarados-RC
| #01 | 004 / 002 | 1519 | Galena-RC
| #02 | 003 / 002 | 1509 | Dinamite
|  *  | 001 / 001 | 1500 | Zabullza
|  *  | 001 / 001 | 1500 | Bullbasauro-Controlado
|  *  | 001 / 002 | 1491 | ExcaliBull
|  *  | 001 / 002 | 1491 | Aldebaran
|  *  | 000 / 002 | 1480 | Syrax-RC
|  *  | 000 / 002 | 1480 | Ganon
|  *  | 000 / 002 | 1480 | Moai-RC
|  *  | 000 / 002 | 1480 | Artemis-RC

</details>

<details>
<summary>2024</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 010 / 002 | 1576 | Eleven-RC
| #02 | 009 / 002 | 1572 | Paçoca-RC
| #03 | 016 / 007 | 1569 | Galena-RC
| #04 | 009 / 002 | 1566 | Frank-RC
| #05 | 014 / 007 | 1557 | Coelho-Escovado
| #06 | 005 / 000 | 1551 | Scar-MX
| #07 | 009 / 005 | 1535 | Bullbasauro-Controlado
| #08 | 007 / 004 | 1529 | Charizard-RC
| #09 | 009 / 008 | 1516 | Moai-RC
| #10 | 007 / 006 | 1512 | Raijū-RC
| #11 | 005 / 004 | 1511 | Aldebaran
| #12 | 007 / 007 | 1502 | Kamex
|  *  | 002 / 002 | 1501 | Shenbong-RC
|  *  | 002 / 002 | 1501 | Tanos
|  *  | 002 / 002 | 1500 | Morgana
| #13 | 003 / 004 | 1490 | Hariyama
|  *  | 000 / 001 | 1490 | Ronda
|  *  | 001 / 002 | 1489 | Gorax-2.0
| #14 | 004 / 006 | 1488 | Atena
| #15 | 002 / 004 | 1484 | Artemis-RC
|  *  | 000 / 002 | 1483 | Kurupira
|  *  | 000 / 002 | 1482 | ExcaliBull
|  *  | 000 / 002 | 1482 | The-Arsonist
|  *  | 000 / 002 | 1481 | Sindrome-RC
|  *  | 000 / 002 | 1481 | Bot-Lee-RC
| #16 | 002 / 004 | 1481 | Dinamite
|  *  | 000 / 002 | 1481 | Topotoropo-RC
|  *  | 000 / 002 | 1480 | Manivela
|  *  | 000 / 002 | 1480 | PitBull-Controlado
|  *  | 000 / 002 | 1480 | Kuro-Usagi
|  *  | 000 / 002 | 1480 | HeavyBull
|  *  | 000 / 002 | 1480 | Bullbasaur-RC
|  *  | 000 / 002 | 1480 | Calypso
|  *  | 000 / 002 | 1480 | Kaizen
|  *  | 000 / 002 | 1480 | Moto-Moto-RC
|  *  | 000 / 002 | 1480 | Cleytompson
| #17 | 005 / 008 | 1473 | RiscaFaca
| #18 | 001 / 004 | 1471 | PitBull-RC
| #19 | 002 / 006 | 1465 | Mooncake-RC
|  *  | 000 / 004 | 1462 | Bullvidoso-Controlado

</details>

<details>
<summary>2023</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 007 / 002 | 1548 | Frank-RC
| #02 | 004 / 001 | 1531 | Paçoca-RC
| #03 | 008 / 004 | 1531 | Raijū-RC
|  *  | 003 / 000 | 1531 | Charizard-RC
| #04 | 004 / 001 | 1530 | Eleven-RC
| #05 | 007 / 004 | 1529 | Coelho-Escovado
| #06 | 003 / 002 | 1511 | Aldebaran
| #07 | 004 / 003 | 1509 | Galena-RC
| #08 | 004 / 004 | 1502 | Mooncake
|  *  | 002 / 002 | 1500 | Roberto
| #09 | 003 / 004 | 1491 | Atena
| #10 | 003 / 004 | 1490 | Kuro-Usagi
|  *  | 001 / 002 | 1490 | Kurupira
| #11 | 003 / 004 | 1489 | Hariyama
| #12 | 002 / 004 | 1482 | Moai-RC
| #13 | 002 / 004 | 1482 | Bullbasaur-Controlado
|  *  | 000 / 002 | 1480 | Bullvidoso-Controlado
|  *  | 000 / 002 | 1480 | Totoro-RC
|  *  | 000 / 002 | 1480 | Valeska
| #14 | 001 / 004 | 1472 | Ronda
| #15 | 001 / 004 | 1471 | RiscaFaca
| #16 | 001 / 004 | 1471 | Tractiana

</details>

<details>
<summary>2022</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 013 / 000 | 1615 | Paçoca-RC
| #02 | 014 / 002 | 1600 | Eleven-RC
| #03 | 014 / 008 | 1554 | Galena-RC
| #04 | 007 / 003 | 1539 | Frank-RC
| #05 | 005 / 001 | 1538 | Banguela-RC
| #06 | 007 / 004 | 1532 | Ronda
| #07 | 004 / 002 | 1522 | Charizard-RC
| #08 | 008 / 006 | 1521 | Kuro-Usagi
| #09 | 009 / 009 | 1510 | Bullbasaur-Controlado
| #10 | 005 / 004 | 1509 | Roberto
| #11 | 003 / 002 | 1507 | Shiryu
|  *  | 002 / 002 | 1500 | Aldebaran
| #12 | 006 / 006 | 1499 | Raijū-RC
| #13 | 004 / 004 | 1499 | Atena
|  *  | 002 / 002 | 1499 | Seppuku
| #14 | 002 / 003 | 1492 | Zoio
|  *  | 001 / 002 | 1490 | SIRE-RC-UB
|  *  | 001 / 002 | 1490 | Grigio
|  *  | 001 / 002 | 1490 | Urutu
|  *  | 001 / 002 | 1490 | Totoro-RC
|  *  | 001 / 002 | 1488 | Leia
| #15 | 006 / 007 | 1487 | Moai-RC
|  *  | 000 / 002 | 1482 | Batata
|  *  | 000 / 002 | 1479 | Vader-2
| #16 | 004 / 007 | 1476 | Hariyama
| #17 | 002 / 005 | 1474 | Mooncake
| #18 | 001 / 004 | 1472 | Se-Pega-no-Olho
| #19 | 007 / 011 | 1472 | RiscaFaca
| #20 | 001 / 004 | 1469 | Pericão
|  *  | 000 / 004 | 1463 | Jotunheim
| #21 | 002 / 006 | 1463 | Bullvidoso-Controlado
|  *  | 000 / 004 | 1461 | Kurupira
| #22 | 000 / 009 | 1420 | Valeska
</details>

<details>
<summary>2021</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 005 / 002 | 1531 | Moai-RC
|  *  | 003 / 000 | 1530 | Frank-RC
|  *  | 003 / 000 | 1530 | Eleven-RC
|  *  | 002 / 000 | 1520 | Paçoca-RC
| #02 | 006 / 004 | 1519 | Kuro-Usagi
|  *  | 002 / 001 | 1511 | Banguela-RC
| #03 | 004 / 004 | 1500 | Mooncake
|  *  | 001 / 001 | 1500 | Areki
| #04 | 004 / 004 | 1500 | RiscaFaca
|  *  | 002 / 002 | 1499 | Hariyama
|  *  | 001 / 002 | 1489 | Galena-RC
| #05 | 002 / 004 | 1481 | Ronda
| #06 | 002 / 004 | 1480 | Zoio
|  *  | 000 / 002 | 1480 | Charizard-RC
|  *  | 001 / 003 | 1479 | Shiryu
|  *  | 000 / 002 | 1479 | Traga-Vasilha
| #07 | 001 / 004 | 1471 | Bullvidoso-Controlado
</details>

<details>
<summary>2020</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 006 / 002 | 1540 | Hariyama
| #02 | 004 / 001 | 1530 | Thorkell
| #03 | 004 / 002 | 1519 | Stonehenge
|  *  | 002 / 002 | 1501 | Kuro-Usagi
|  *  | 002 / 002 | 1501 | Bullbasaur-Controlado
|  *  | 002 / 002 | 1501 | Se-Pega-no-Olho
|  *  | 002 / 002 | 1499 | Atena
|  *  | 001 / 001 | 1499 | PitBull-Controlado
|  *  | 001 / 002 | 1490 | Valeska
|  *  | 000 / 001 | 1490 | Auterna
|  *  | 001 / 002 | 1490 | Aldebaran
|  *  | 000 / 002 | 1481 | Zé-Torquinho
|  *  | 000 / 002 | 1480 | Moai-RC
|  *  | 000 / 002 | 1480 | Rampinha
</details>

<details>
<summary>2019</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 014 / 002 | 1619 | Eleven-RC
| #02 | 016 / 004 | 1600 | Stonehenge
| #03 | 010 / 003 | 1565 | Dolgorsuren-Dagvadorj
| #04 | 012 / 005 | 1553 | Moai-RC
| #05 | 014 / 008 | 1552 | Kuro-Usagi
| #06 | 006 / 002 | 1540 | PitBull-Controlado
|  *  | 004 / 000 | 1539 | Paçoca-RC
| #07 | 008 / 004 | 1535 | Frank-RC
| #08 | 010 / 008 | 1517 | Valeska
| #09 | 003 / 002 | 1511 | Môzóvs
| #10 | 005 / 004 | 1510 | Atena
| #11 | 008 / 008 | 1510 | Shiryu
| #12 | 006 / 005 | 1509 | Itiban
|  *  | 002 / 002 | 1501 | Paladino
|  *  | 002 / 002 | 1497 | O-Agonia
|  *  | 001 / 002 | 1492 | Raijū-RC
|  *  | 001 / 002 | 1492 | RalaCoxa
|  *  | 000 / 001 | 1491 | Adubinho
|  *  | 001 / 002 | 1490 | Rato
|  *  | 001 / 002 | 1490 | Se-Pega-no-Olho
|  *  | 001 / 002 | 1490 | MadimBull
|  *  | 001 / 002 | 1490 | Cleytompson
| #13 | 010 / 012 | 1489 | Drakkar
| #14 | 006 / 008 | 1488 | Hariyama
|  *  | 000 / 002 | 1483 | RiscaFaca
|  *  | 000 / 002 | 1481 | Trator
|  *  | 000 / 002 | 1481 | Faustinho
|  *  | 000 / 002 | 1480 | Aldebaran
|  *  | 000 / 002 | 1480 | Coiote
|  *  | 000 / 002 | 1480 | Zé-Torquinho
|  *  | 000 / 002 | 1479 | Máquina-do-Mal
|  *  | 000 / 002 | 1479 | Bidê
| #15 | 004 / 006 | 1479 | Golem
| #16 | 002 / 004 | 1478 | Blanka
| #17 | 005 / 008 | 1475 | Bullbasaur-Controlado
| #18 | 002 / 005 | 1473 | Auterna
| #19 | 002 / 005 | 1472 | EtecAP
|  *  | 000 / 003 | 1471 | Zerum
| #20 | 004 / 008 | 1465 | Ronda
| #21 | 000 / 006 | 1446 | JPLSM
| #22 | 000 / 008 | 1426 | Rampinha
</details>

<details>
<summary>2018</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 015 / 005 | 1585 | Stonehenge
| #02 | 012 / 003 | 1584 | Paçoca-RC
| #03 | 011 / 003 | 1573 | Eleven-RC
| #04 | 005 / 002 | 1530 | CaiPiloto
| #05 | 004 / 002 | 1518 | Mr.PIG
|  *  | 002 / 001 | 1511 | Autistônomo
| #06 | 003 / 002 | 1511 | Traga-Vasilha
| #07 | 007 / 006 | 1510 | Moai-RC
| #08 | 006 / 005 | 1510 | Ronda
| #09 | 003 / 002 | 1509 | Harry-Porco
| #10 | 005 / 004 | 1509 | Valeska
|  *  | 002 / 002 | 1500 | Hariyama
|  *  | 002 / 002 | 1500 | Gordox
|  *  | 002 / 002 | 1500 | Paladino
|  *  | 002 / 002 | 1499 | MiniZord
|  *  | 002 / 002 | 1499 | Môzóvs
| #11 | 002 / 003 | 1495 | Blanka
| #12 | 002 / 003 | 1493 | Zerum
|  *  | 000 / 001 | 1492 | Utopia
|  *  | 001 / 002 | 1492 | Poko-Loko
|  *  | 001 / 002 | 1491 | Itiban
|  *  | 001 / 002 | 1490 | Mareta
|  *  | 000 / 001 | 1490 | Ninjai
| #13 | 003 / 004 | 1489 | C3
| #14 | 002 / 004 | 1483 | Fanático
|  *  | 000 / 002 | 1481 | Supra-Sumo
|  *  | 000 / 002 | 1481 | Killer
|  *  | 000 / 002 | 1480 | Clayton
|  *  | 000 / 002 | 1480 | HeavyBull
|  *  | 000 / 002 | 1480 | Poco-Loco
|  *  | 000 / 002 | 1480 | Porco-Aranha
|  *  | 000 / 002 | 1480 | Rampinha
|  *  | 000 / 002 | 1480 | Dolgorsuren-Dagvadorj
|  *  | 000 / 004 | 1467 | Drakkar
| #15 | 002 / 006 | 1466 | Golem
|  *  | 000 / 004 | 1461 | Tomoe
</details>

<details>
<summary>2017</summary>

| Position  | Win/Losses  | Elo  | Team              |
|:---------: |:-----------:|:-----:|:----------------:|
| #01 | 007 / 002 | 1545 | Stonehenge
| #02 | 006 / 002 | 1537 | Paladino
| #03 | 005 / 002 | 1530 | Eleven-RC
|  *  | 002 / 000 | 1522 | Paçoca-RC
| #04 | 004 / 002 | 1521 | Mr.PIG
| #05 | 005 / 003 | 1518 | Harry-Porco
| #06 | 003 / 002 | 1510 | Ronda
| #07 | 004 / 004 | 1502 | Porco-Aranha
| #08 | 004 / 004 | 1501 | Moai-RC
|  *  | 002 / 002 | 1501 | Hariyama
|  *  | 002 / 002 | 1500 | Golem
|  *  | 002 / 002 | 1499 | Valeska
|  *  | 001 / 002 | 1492 | Môzóvs
|  *  | 001 / 002 | 1491 | Titan
|  *  | 001 / 002 | 1491 | Odyssay
|  *  | 000 / 001 | 1490 | Traga-Vasilha
|  *  | 001 / 002 | 1490 | C3
|  *  | 000 / 002 | 1481 | Zerum
|  *  | 000 / 002 | 1481 | Hulk-TSI
|  *  | 000 / 002 | 1480 | Urutu
|  *  | 000 / 002 | 1480 | Anoobs-II
|  *  | 000 / 002 | 1480 | Tomoe
|  *  | 000 / 002 | 1480 | HAKA-B
|  *  | 000 / 002 | 1480 | HAKA-A
</details>


