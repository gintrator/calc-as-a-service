#!/bin/bash

URL="http://localhost:5000/caas?x=${1}&y=${2}&op=${3}"
curl -X POST -H "Content-Type: text/plain" ${URL} 
