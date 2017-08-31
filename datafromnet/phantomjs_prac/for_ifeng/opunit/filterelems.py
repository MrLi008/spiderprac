# coding=utf8
from bs4 import BeautifulSoup
import re


def getFormatURLFrom(response, parttern):
    bsobj = BeautifulSoup(response, 'html.parser')
    links = bsobj.findAll('a', href=re.compile(parttern))

    return links