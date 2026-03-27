#!/bin/bash

mkdir -p customer-analytics/results

cp results/*.csv customer-analytics/results/
cp results/*.txt customer-analytics/results/
cp results/*.png customer-analytics/results/

docker stop my_container
docker rm my_container