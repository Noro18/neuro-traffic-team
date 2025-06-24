# neuro-traffic-team

iha folder openCv nia laran iha file `cv.py` ne hanesan file teste ida atu teste funsionamento hus iopen cv nian lao ou lao uza droidcam

Iha file cv.py nian troka  ``.VideoCaputre(video_path)`` ba fali ``VideoCapture(0)`` para bele uza idaidak nia webcam sai source video.

## Oinsa Prepara atu bele halao Systema ida ne'e

App ida ne'e presiza:
1. Django
2. OpenCV
3. Ultralytics

tan ne'e atu bele install librarie sira ne'ebe presiza bele installa deit kedas ho commando tuir mai

``pip install -r requirements.txt`` se karik uza python <= 3.11

Maibe se quando uza versaun python ne'ebe boot > 3.11 entaun bele:
- installa tia lai python versaun foun
- no utiliza fali commando ``py -3.11 -m pip install -r requirements.txt``
- No se quando hanesan ne'e ona troka mos interpreter ne'ebe uza iha vs code ho commando ``Ctrl + Shift + p`` no search python interpreter no hili **python 3.11** ne'ebe installa ona
- Se quando run file iha terminal uza commando ``py -3.11 cv.py`` se wainhira ba ona directory ne'ebe mak loos.
