@echo off
setlocal enabledelayedexpansion

REM %1 package name
REM %2 source folder
REM %3 output file name

PATH C:\Users\hasans\AppData\Local\Programs\Python\Python311
PATH C:\Users\hasans\AppData\Local\Programs\Python\Python311\Scripts

set "fileList="

for /R "%2" %%F in (*.py) do (
    set "fileList=!fileList! "%%F""
)

pycg --package %1 %fileList% > %3

 


