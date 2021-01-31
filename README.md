# TIMSER

Public solution for [TIMESER](https://www.aicrowd.com/challenges/ai-blitz-5/problems/timser)

# Description 

Ability to predict the future can be really valuable.
But since we don’t have Doc and his DeLorean time machine from Back to the Future, 
we have to rely on other means to know the future. Using time-series prediction can you 
find the future of these synthetic stock prices. Given the prices of the stock for the past, 
predict its value in the future.

# Create a Local Environment 

```python
python3 -m virtualenv aicrowd_timser
source aicrowd_timser/bin/activate
pip install -r requirements.txt
```

# Training model

```python
sh scripts/train.sh
```

# Run prediction

```python
sh scripts/predict.sh
```