# shigma
*Shigma* is a Python package allowing for sigma (&Sigma;) and pi (&Pi;) notation. It is very easy to learn and works like you'd expect. You'll get the hang of it very fast.
## Installation
You must make sure, you're using the right version of Python. Run this command:
```commandline
python --version
```
This will give you the version of Python. It must be Python 3.8 or later.

Now that you know that you have th right version of Python, run this command:
```commandline
python -m pip --upgrade
```
There is a chance, you're using an outdated release of Pip. This command will update it.

Finally, run this command:
```commandline
python -m pip install shigma
```
This installs the package so you can use it.
## How to use
### Sigma
Envision yourself an expression with sigma notation. Like this: $\sum_{i=1}^{10} i^2$
This is how you write that in raw Python:
```python
arr = []

for i in range(1, 10 + 1):
  arr.append(i**2)

out = sum(arr)
```
This is how you write that with shigma.
```python
out = sigma_not(1, "i**2", 10)
```
Seems simple enough, right? If you are weird, or appreciate how unicode has become the standard encoding ¯\\\_(ツ)_/¯. Use the unicode symbol instead!
```python
out = Σ(1, "i**2", 10)
```
Yeah, unprofessional I know.
### Pi
You'll probably be using prodcut notation a lot too. To rewrite this:
$$\prod_{i=1}^{10} i^2$$
into Python with the shigma package, you write this
```python
out = pi_not(1, "i**2", 10)
```
*unless of course...*
```python
out = Π(1, "i**2", 10)
```
