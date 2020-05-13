# Practice-Problem-Time-Series
Hackathon at https://datahack.analyticsvidhya.com/contest/practice-problem-time-series-2/

Participiated under nickname Rekmark. I have finished 87th of 735 participants.

# Problem Statement
Congratulations on your new job! This time you are helping out Unicorn Investors with your data hacking skills. They are considering making an investment in a new form of transportation - JetRail. JetRail uses Jet propulsion technology to run rails and move people at a high speed! While JetRail has mastered the technology and they hold the patent for their product, the investment would only make sense, if they can get more than 1 Million monthly users with in next 18 months.
 
You need to help Unicorn ventures with the decision. They usually invest in B2C start-ups less than 4 years old looking for pre-series A funding. In order to help Unicorn Ventures in their decision, you need to forecast the traffic on JetRail for the next 7 months.

# Solution
###### ARIMA, SARIMA
In data_analysis notebook you can find basic time series analysis. I found that ARIMA model should have order (1, 1, 1). Moreover data contains seasonality with weekly period. I tried transformation from hourly data to daily and then training SARIMA model but it yielded in RMSE around 250. I get stuck with hourly data, so period m = 168 (=1week). Unfortunately SARIMA model with such high period is too computationally expensive for my labtop. I decided to try periods of lower order. After that assumption I have tried m = [24,48,72]. Best result was RMSE ~ 195. 

###### Holt-Winters Method
After pretty bad results from previous models I have decided to try different model. H-W model is able to work reasonably fast with m = 168. After some optimalization and rewriting holtwinters.py it yielded in my final solution with RMSE = 160.167. Model is trained by train_model.py script.

Rewrited pieco of code in holtwinters.py (line 692):
```
if use_basinhopping:
                    # Take a deeper look in the local minimum we are in to find the best
                    # solution to parameters, maybe hop around to try escape the local
                    # minimum we may be in.
                    res = basinhopping(func, p[xi],
                                       minimizer_kwargs={'args': args, 'bounds': bounds[xi]},
                                       stepsize=0.01, niter=10000, niter_success=10)
```

