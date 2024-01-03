# shigma
*Shigma* is a Python package allowing for sigma (&Sigma;) and pi (&Pi;) notation. It is very easy to learn and works like you'd expect. You'l get the hang of it very fast.
## How to use
### Sigma
Envision yourself a sigma notation.
$$\sum_{i=1}^{10} i^2$$
is this it?
This is how you write that in raw Python:
```python
arr = []

for i in range(1, 10 + 1):
  arr.append(i**2)

out = sum(arr)
```
This is how you write that with shigma.
This is how you'd write that with shigma.
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
