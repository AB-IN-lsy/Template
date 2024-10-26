@echo off

:: Hexo deploy script
:: Powered by AB-IN
:: Last edit: 2024/6/22

:: Arguments:
:: %1: algoliaIndexingKey

:: Set descriptive variables
set "hexoPath=D:\Code\Hexo"
set "algoliaIndexingKey=%~1"

:: Navigate to Hexo directory
D:
cd "%hexoPath%"

:: Set Algolia indexing key
set HEXO_ALGOLIA_INDEXING_KEY=%algoliaIndexingKey%

:: Run Hexo commands
hexo clean & hexo g & hexo algolia & hexo deploy
