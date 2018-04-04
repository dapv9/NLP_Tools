# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import nltk


def tokenizer(text):
	tokenize = nltk.word_tokenize(text);
	return tokenize
# Create your views here.

def tagging(tokenizelist):
	tag = nltk.pos_tag(tokenize)
	return tag
