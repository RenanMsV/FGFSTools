# FGFSTools | PYTHON 3 ONLY | WINDOWS ONLY


## How to:

### UfoExport2Stg.py 

Export Ufo Export content with tile separation.
Needs ufo-model-export.xml in the same path.

Exporta linhas de modelos do UFO com separação por tile.
Necessita de ufo-model-export.xml estar na mesma pasta.

By jam007 some changes by BR-RVD

### Dat2Gnet.py apt.dat KSFO

Export airport parking posisitions from WED apt.dat to 'ICAO_output' path.

Exporta posições de estacionamento do WED apt.dat para a pasta 'ICAO_output'.

By someone I do not remember. I'll put his name when I do.  Changes by BR-RVD.

### ORCAM.py

Runs ORCAM if you have it.
Put the ORCAM.py script in the bin folder of your FlightGear.
Example: D:\Flightgear 2017.1\bin\ORCAM.py
And run the file. It will ask you to enter an ICAO.
Then it asks if you have any custom scenery for this airport. If you have, enter the path for this scenario.
If you do not type enter without typing anything.

Coloque o script ORCAM.py na pasta bin do seu FlightGear. Exemplo : D:\Flightgear 2017.1\bin\ORCAM.py
E execute o arquivo. Ele irá lhe pedir para digitar um ICAO.
Depois ele pergunta se você possui algum cenário customizado para este aeroporto.
Caso tenha digite o caminho para este cenario.
Caso não tecle enter sem digitar nada

By BR-RVD

### LevelD2FixDat.py

Converts LevelD Airac Fixes to FG fix.dat format.

Converte Fixos do Airac LevelD para fixos do FG.

By BR-RVD

### LevelD2Procedures.py

Converts LevelD Airac Procedures to FG Aiports Procedures format.

Converte Airac da LevelD para procedimentos do FG.

By BR-RVD

### FGFS_ServerPing.py

Shows the best FG Server based on ping (latency).

Mostra o melhor servidor do FG baseado no ping (latencia).

By BR-RVD

### coordinatesFromTileIndex.py

Shows the bounding box coordinates from one tile index. Eg 2183314 outputs LB: -23.75 LT: -23.625 RT: -46.5 RB: -46.25 , -23.6875 -46.375

Mostra as coordenadas dos cantos de um 'tile'. Ex 2183314 outputs LB: -23.75 LT: -23.625 RT: -46.5 RB: -46.25 , -23.6875 -46.375

By someone I do not remember. I'll put his name when I do.  Changes by BR-RVD.

### get_fr24_planes_data.py

Gets a JSON with FlightRadar24 data. Data contains all planes in a bounding box area.
``` python
coords = get_coords_bounding_box(-22.907104,-47.063240, 20) # lat , lon , box distance in km
get_FR24_nearplanes(coords)
```
Mostra dados do FlightRadar24. Dados contém todas aéronaves em uma área.
``` python
coords = get_coords_bounding_box(-22.907104,-47.063240, 20) # lat , lon , distancia em km
get_FR24_nearplanes(coords)
```
