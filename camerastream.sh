#!/bin/bash

raspivid -o - -t 0 -hf -vf -w 600 -h 400 -fps 20 |cvlc -v stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8554}' :demux=h264
