# FileSensor

**Dynamic file detection tool based on crawler**  
基于爬虫的动态敏感文件探测工具  

![banner](http://static.cdxy.me/Screenshot-banner-filesensor.png)

Feature
-------
* Generate the fuzzing vectors based on crawler results  
**(input)http://localhost/ -> (crawl)http://localhost/test.php -> (detect)http://localhost/.test.php.swp**  

* Scrapy framework  
Stable crawler and customizable HTTP requests.  

* Custom 404 filter  
Use a regular expression to filter out user-defined 404 pages(which status code is 200).  

Requirement
-----------
* Python 3.x
* pip

Install
-------
1. `git clone https://github.com/Xyntax/FileSensor`
2. `cd FileSensor`
3. `pip3 install -r requirements.txt`

* [Scrapy official installation guide](http://scrapy.readthedocs.io/en/latest/intro/install.html)

Usage
-----
```
FileSensor ver0.2 by <i@cdxy.me>
https://github.com/Xyntax/FileSensor

Usage:
  filesensor.py URL [--404 REGEX] [-o]
  filesensor.py (-h | --help)

Example:
  python3 filesensor.py https://www.cdxy.me --404 "404 File not Found!"

Options:
  -o           save results in ./output folder
  --404 REGEX  filter out custom 404 page with regex
  -h --help    show this help message

```


Links
-----

* [Bug tracking](https://github.com/Xyntax/FileSensor/issues)
* Contact <i@cdxy.me>
