@echo off
git rev-parse --short head > info.txt
set /p commit=<info.txt
git rev-parse --abbrev-ref head > info.txt
set /p branch=<info.txt
del info.txt
set prefix=%branch%-%commit%
rmdir /S /Q reader-mediacenterjs.wiki
git clone https://github.com/rohitkumar003/reader-mediacenterjs.wiki.git
cd reader-mediacenterjs.wiki
echo checking if %prefix%.zip already exists.
jar -cMf .\%prefix%.zip ..\build\debug
find /c "%prefix%.zip" testpage.md && ( echo File %prefix%.zip exists. && exit ) 
echo File %prefix%.zip does not exists.
@echo: >> testpage.md 
echo [%prefix%.zip](%prefix%.zip)>>testpage.md
git status -s
git add %prefix%.zip
git add testpage.md
git commit -m "Updating artifact"
git push
cd ..
