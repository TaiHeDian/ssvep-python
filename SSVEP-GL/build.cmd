@echo off
cls

g++ -std=c++11 ssvep.cpp -o ssvep.exe -lGLEW -lglfw3 -lopengl32 -lgdi32 -lpthread

start /B ssvep.exe 50
start /B ssvep.exe 75
start /B ssvep.exe 100
start /B ssvep.exe 150

del ssvep.exe
