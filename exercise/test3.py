#!/usr/bin/env python
# coding=utf-8

# 'How are   you', 去除多余的空格

sentence = "How are   you"

sub_word = sentence.split()
print sub_word

sentence_changed = '#'.join(sub_word)
print sentence_changed

