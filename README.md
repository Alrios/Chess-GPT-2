# Chess-GPT-2
Python Script to play a match of chess against a small size GPT-2 model.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This repository is a Bachelor's thesis project, where two GPT2 models were trained to play chess. The gpt2-300k model was trained with 300,000 chess games and gpt2-500k was trained with 500,000 chess games.

```bash
Chess-GPT-2/

├── chess-models/
│   ├── gpt2-300k/
│   │   ├── ...
│   ├── gpt2-500k/
│   │   ├── ...
│   ├── process.py
│   └── thread.py
└── .gitignore
└── README.md
└── chess-playing-script.py
```

The python script allows to play a match of chess against the models using [SAN language](https://www.chess.com/terms/chess-notation), one must define inside the script which model should be the opponent. 

## Technologies
Enviroment:
* conda 23.3.1

Python libraries:
* chess: 1.9.4
* transformers: 4.27.4

## Setup
To run this project, install first the [Transformer library from HuggingFace](https://huggingface.co/docs/transformers/installation). For the installation in anaconda/conda enviroment:

```
$ conda install -c huggingface transformers
```
Python [chess](https://pypi.org/project/chess/) library:
```
$ pip install chess
```

The language models need to be downloaded manually and put in the corresponding folder in chess-models/. [The two models can be downloaded here](https://drive.google.com/drive/folders/196nsUkekz_vfrIOixC4UpstOga1Busws?usp=sharing).

To run the script:
```
$ python chess-playing-script.py
```


