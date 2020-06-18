## introduction
![malan_logo](https://github.com/malan-project/malan/blob/master/malan_svc/static/images/logo.png)
*malan* is a tool for malware analyzing. we provide analyzing tool based on machine learning and evaluation wiki site.

## how to start
First, configure docker environment on yout local machine. 
### install
Install the project to your local machine. Download and unzip the project or use
> git clone https://github.com/malan-project/malan

### run
In linux environment, use following command
> docker-compose up -d

**compose up** in vscode(extension Docker required) also works.

### use malanwiki(temporary)
> docker build --pull --rm -f "Dockerfile" -t wiki:latest "."

> docker run -d -p 7000:70 wiki:latest

## edit project
After editing project, you have to rebuild docker iamges
docker-compose build && docker-compose up -d

## pull request

 1. Notice your own development environment
 2. Merging to master is decided by discussion
 
## make issue

 1. Clarify the purpose(bug_fix, development, optimization, etc)
 2. Follow coding style
 
## coding convention rule
+ [python](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
+ [javascript](https://google.github.io/styleguide/jsguide.html)

## LICENSE
[license.txt](https://github.com/malan-project/malan/blob/master/LICENSE)
