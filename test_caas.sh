#!/bin/bash

HOST="localhost:5000"
URL="http://${HOST}/equals?x=${1}&y=${2}&op=${3}"
curl -X POST -H "Content-Type: text/plain" ${URL} 
