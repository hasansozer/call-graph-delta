@echo off
setlocal enabledelayedexpansion
set total=0

if "%~1"=="" (
    echo Usage: count_lines.bat "root_directory"
    exit /b 1
)

set "root_dir=%~1"

for /r "%root_dir%" %%G in (*.py) do (
    set /a count=0
    for /f %%A in ('findstr /R /N "^" "%%G" ^| find /c ":"') do set /a count=%%A
    set /a total+=count
    echo Checking "%%G" - Lines: !count!
)

echo Total Lines of Code: !total!
