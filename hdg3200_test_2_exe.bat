@ECHO OFF

CD ..
SET TEST_ROOT=%CD%
SET VIRTUALENV_ROOT=%TEST_ROOT%\env
SET SCRIPTS_ROOT=%VIRTUALENV_ROOT%\Scripts

REM ======== Active virtualenv ========
CD /D %~dp0
IF NOT EXIST %SCRIPTS_ROOT%\activate.bat (
    ECHO %SCRIPTS_ROOT%\activate.bat not exist, please check the virtual environment!
    goto complete
)
CALL %SCRIPTS_ROOT%\activate.bat
REM ECHO %PATH%

REM ======== Start service ========
%SCRIPTS_ROOT%\pyinstaller.exe --noconfirm --onefile --distpath=dist --paths=E:\mt7628SDK\生产测试\HDG3200_TEST_V2\env hdg3200_test.py

:COMPLETE
PAUSE
