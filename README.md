# TweetGeneration


## Creating a Virtual Environment
- Install [Anaconda](https://www.anaconda.com/distribution/)
- Create a virtual-env - 
  - In Anaconda Command Prompt:
```
conda create -n nameOfEnv 
```
  - To activate:
```
conda.bat activate nameOfEnv
```
  - To deactivate:
```
conda.bat deactivate
```

## Package Installations

- Packages to be installed:
  - tweepy
  - twitter

- To install:
```
pip install packageName
```

## Code
- 
- twitterconnect.py
  - WOEID (Where On Earth Identifier) for India - 2282863
  - The trends list gets the trending topics present in the WOEID
  - A random trend is selected and sent to the function getTrending present in getTweetsInTreding.py
