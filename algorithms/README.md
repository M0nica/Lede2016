# Algorithms Notes and Exercises

My own personal notes will live in this repository.
Projects and exercises completed for Algorithms course will live <a href="https://github.com/M0nica/algorithms">here</a> and will remain synced with the main branch.


Instructions for setting up repository that remains synced with the rest of the class:
#First time

```bash
git remote add upstream https://github.com/ledeprogram/algorithms.git
git fetch upstream
git checkout gh-pages
git merge upstream/gh-pages  
git push origin gh-pages
```
--

#Every time afterwards

```bash
git fetch upstream
git checkout gh-pages
git merge upstream/gh-pages  
git push origin gh-pages
```
