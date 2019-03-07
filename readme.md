![](https://images.weserv.nl?url=https://www.python.org/static/community_logos/python-logo-master-v3-TM.png&w=300)

# Galton Board (Python)

![](https://images.weserv.nl?url=mathworld.wolfram.com/images/eps-gif/GaltonBoard_1000.gif)

> The bean machine, also known as the Galton Board or quincunx, is a device invented
by Sir Francis Galton to demonstrate the central limit theorem, in particular that the normal
distribution is approximate to the binomial distribution. Among its applications, it afforded
insight into regression to the mean or "regression to mediocrity".

## Cucumber

![](https://images.weserv.nl/?url=cdn-images-1.medium.com/max/1200/1*oPCrD81z6KzgA20OhiTIQg.png&w=250)

Feature test is implemented using Cucumber.

## Explanation

The implementation of the`Galton Board` is proven te work by using a `test double`, which replaces the
unpredictable behavior of the dropping bullets, with a predefined path from which can be determined in which
tray the bullet will end.

## Result

Run `python src/Main.py`

```
00
00000000
00000000000000000000000
000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000
000000000000000000000
000
0
```

# Run tests

## Unit 

`python -m unittest tests.{file_name}`

## Feature

`behave`
