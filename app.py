{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from flask import Flask, Response \
import random \
app = Flask(__name__) \
\
@app.route('/random-word', methods=['GET']) \
def random_word(): \
	with open('words.txt', 'r')) as file: \
		words = file.read().splitlines() \
	word = random.choice(words) \
	return Response(word, mimetype='text/plain') \
\
if __name__ == '__main__': \
	app.run(host='0.0.0.0', port=5000)}